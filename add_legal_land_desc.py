"""
Fallback/supplement to add_geometry.py.

Queries BLM's sibling `Case_Lands` ArcGIS REST service (derived from the
LR2000 Case Recordation Database's Legal Land Descriptions, geocoded via
PLSS - i.e. Meridian/Township/Range/Section "MTRS"), keyed by CSE_NR:

  https://nlsdbpubgis.blm.gov/arcgis/rest/services/Case_Lands/MapServer/0

This is a different dataset than Rights_of_Way_Case_Disp (the one
add_geometry.py uses) and sometimes has records - including mapped
PLSS polygon geometry - for cases where the ROW case-disposition
layer's own Shape is null.

For every row in data_center_row_cases.csv:
  - adds a `legal_land_description` column: semicolon-joined MTRS
    strings from CSE_LND_META (e.g. "AZ 14 0020S 0100W 032 Z W2NW,W2SW"
    = AZ, Meridian 14, T20S, R100W, Sec 32, aliquot W2NW+W2SW), when
    Case_Lands has any record for that case - independent of whether
    geometry was recoverable.
  - for rows that are STILL missing centroid/polygon_wkt after
    add_geometry.py, tries to recover geometry by unioning all of that
    case's Case_Lands parcel-part rings and recomputing the centroid.

Run add_geometry.py first, and run restore_manual_geometry.py after this
script - it reapplies any one-off manual geometry recoveries that neither
this script nor add_geometry.py can reproduce, since both overwrite the
CSV/geojson wholesale on every run.
"""
import csv
import json
import shutil
import time

import requests

CL_URL = "https://nlsdbpubgis.blm.gov/arcgis/rest/services/Case_Lands/MapServer/0/query"
CSV_PATH = "data_center_row_cases.csv"
GEOJSON_PATH = "data_center_row_cases.geojson"

# reuse the same centroid math as add_geometry.py
from add_geometry import polygon_centroid, rings_to_wkt


def fetch_case_lands(case_number):
    params = {
        "where": f"CSE_NR='{case_number}'",
        "outFields": "CSE_LND_META,QLTY",
        "returnGeometry": "true",
        "outSR": "4326",
        "f": "json",
    }
    # Case_Lands is sometimes very slow (30s+ per query), so use a long
    # timeout and retry rather than dying mid-run.
    for attempt in range(4):
        try:
            resp = requests.post(CL_URL, data=params, timeout=120)
            resp.raise_for_status()
            return (resp.json().get("features") or [])
        except requests.exceptions.RequestException:
            if attempt == 3:
                raise
            time.sleep(5)


def main():
    with open(CSV_PATH, newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    shutil.copy(CSV_PATH, CSV_PATH + ".bak2")

    if "legal_land_description" not in fieldnames:
        fieldnames = fieldnames + ["legal_land_description"]

    with open(GEOJSON_PATH) as f:
        geojson = json.load(f)
    features_by_case = {
        feat["properties"]["case_number"]: feat for feat in geojson["features"]
    }

    recovered = []
    lld_found = []

    for row in rows:
        case_number = row["case_number"]
        feats = fetch_case_lands(case_number)
        if not feats:
            row["legal_land_description"] = ""
            continue

        lld_strings = sorted({
            feat["attributes"].get("CSE_LND_META") or ""
            for feat in feats
            if feat["attributes"].get("CSE_LND_META")
        })
        row["legal_land_description"] = "; ".join(lld_strings)
        lld_found.append(case_number)

        already_has_geometry = bool(row.get("polygon_wkt"))
        if already_has_geometry:
            continue

        all_rings = []
        for feat in feats:
            geom = feat.get("geometry")
            if geom and geom.get("rings"):
                all_rings.extend(geom["rings"])

        if not all_rings:
            continue

        lat, lon = polygon_centroid(all_rings)
        row["centroid_lat"] = f"{lat:.6f}" if lat is not None else ""
        row["centroid_lon"] = f"{lon:.6f}" if lon is not None else ""
        row["polygon_wkt"] = rings_to_wkt(all_rings)
        recovered.append(case_number)

        geojson["features"].append({
            "type": "Feature",
            "geometry": {"type": "MultiPolygon", "coordinates": [[r] for r in all_rings]},
            "properties": {k: v for k, v in row.items() if k != "polygon_wkt"},
        })

        print(f"  recovered geometry for {case_number} ({row.get('geographic_name') or 'unnamed'}) "
              f"via Case_Lands -> ({lat:.5f}, {lon:.5f})")

    with open(CSV_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    with open(GEOJSON_PATH, "w") as f:
        json.dump(geojson, f, indent=2)

    print(f"\nlegal_land_description found for {len(lld_found)}/{len(rows)} cases")
    print(f"Recovered geometry for {len(recovered)} previously-missing cases: {recovered}")
    print(f"Updated {CSV_PATH} (2nd backup at {CSV_PATH}.bak2) and {GEOJSON_PATH}")


if __name__ == "__main__":
    main()
