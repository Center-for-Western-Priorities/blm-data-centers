"""
Enrich data_center_row_cases.csv with polygon geometry and centroids
pulled from the same BLM MLRS ArcGIS REST service documented in
MLRS_API_HOWTO.md.

For each case, queries the case's disposition-specific layer for its
geometry (WGS84 lon/lat), computes a proper area-weighted polygon
centroid (handles multi-ring/multi-part geometry and holes), and
writes:

  - data_center_row_cases.csv   (in place: adds centroid_lat,
    centroid_lon, polygon_wkt columns)
  - data_center_row_cases.geojson (standalone FeatureCollection with
    full polygon geometry + all case attributes, for direct import
    into QGIS / Google My Maps / kepler.gl / etc.)

A .bak copy of the original CSV is written before overwriting.
"""
import csv
import json
import shutil
import time

import requests

BASE = "https://nlsdbpubgis.blm.gov/arcgis/rest/services/Land_Use_Authorizations/Rights_of_Way_Case_Disp/MapServer"
LAYER_BY_DISPOSITION = {
    "Authorized": 0,
    "Pending": 1,
    "Interim": 2,
    "Closed": 3,
}
CSV_PATH = "data_center_row_cases.csv"
GEOJSON_PATH = "data_center_row_cases.geojson"


def fetch_geometry(case_number, layer_id, retries=5):
    """BLM's ArcGIS server intermittently returns a spurious
    {"error": {"code": 404, "message": "Layer not found"}} for a valid,
    existing layer (observed repeatedly, same layer/query succeeds on
    retry) -- retry before concluding geometry is genuinely absent."""
    url = f"{BASE}/{layer_id}/query"
    params = {
        "where": f"CSE_NR='{case_number}'",
        "outFields": "CSE_NR",
        "returnGeometry": "true",
        "outSR": "4326",
        "f": "json",
    }
    for attempt in range(retries):
        resp = requests.post(url, data=params, timeout=30)
        resp.raise_for_status()
        body = resp.json()
        if "error" in body:
            time.sleep(min(2 * (attempt + 1), 6))
            continue
        features = body.get("features") or []
        if not features:
            return None
        geom = features[0].get("geometry")
        if not geom or not geom.get("rings"):
            return None
        return geom["rings"]
    return None


def ring_signed_area_and_centroid(ring):
    """Shoelace-based signed area and centroid for one ring (list of [x,y])."""
    if ring[0] != ring[-1]:
        ring = ring + [ring[0]]
    a_sum = 0.0
    cx_sum = 0.0
    cy_sum = 0.0
    for (x0, y0), (x1, y1) in zip(ring, ring[1:]):
        cross = x0 * y1 - x1 * y0
        a_sum += cross
        cx_sum += (x0 + x1) * cross
        cy_sum += (y0 + y1) * cross
    area = a_sum / 2.0
    if area == 0:
        return 0.0, None, None
    cx = cx_sum / (6 * area)
    cy = cy_sum / (6 * area)
    return area, cx, cy


def polygon_centroid(rings):
    """Area-weighted centroid across all rings (handles holes/multi-part)."""
    total_area = 0.0
    wx = 0.0
    wy = 0.0
    all_points = []
    for ring in rings:
        all_points.extend(ring)
        area, cx, cy = ring_signed_area_and_centroid(ring)
        if cx is None:
            continue
        total_area += area
        wx += cx * area
        wy += cy * area
    if abs(total_area) > 1e-12:
        return wy / total_area, wx / total_area
    # degenerate (zero-area, e.g. a line-like sliver): fall back to
    # simple average of all vertices
    if not all_points:
        return None, None
    lon = sum(p[0] for p in all_points) / len(all_points)
    lat = sum(p[1] for p in all_points) / len(all_points)
    return lat, lon


def rings_to_wkt(rings):
    parts = []
    for ring in rings:
        coord_str = ", ".join(f"{x} {y}" for x, y in ring)
        parts.append(f"({coord_str})")
    return "MULTIPOLYGON((" + "), (".join(parts) + "))"


def main():
    with open(CSV_PATH, newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    shutil.copy(CSV_PATH, CSV_PATH + ".bak")

    new_cols = ["centroid_lat", "centroid_lon", "polygon_wkt"]
    for c in new_cols:
        if c not in fieldnames:
            fieldnames = fieldnames + [c]

    geojson_features = []
    missing = []

    for i, row in enumerate(rows):
        case_number = row["case_number"]
        disposition = row["disposition"]
        layer_id = LAYER_BY_DISPOSITION.get(disposition)
        if layer_id is None:
            print(f"  ! unknown disposition '{disposition}' for {case_number}, skipping")
            missing.append(case_number)
            row["centroid_lat"] = ""
            row["centroid_lon"] = ""
            row["polygon_wkt"] = ""
            continue

        rings = fetch_geometry(case_number, layer_id)
        if not rings:
            print(f"  ! no geometry returned for {case_number} ({row.get('geographic_name') or 'unnamed'})")
            missing.append(case_number)
            row["centroid_lat"] = ""
            row["centroid_lon"] = ""
            row["polygon_wkt"] = ""
            time.sleep(0.2)
            continue

        lat, lon = polygon_centroid(rings)
        row["centroid_lat"] = f"{lat:.6f}" if lat is not None else ""
        row["centroid_lon"] = f"{lon:.6f}" if lon is not None else ""
        row["polygon_wkt"] = rings_to_wkt(rings)

        geojson_features.append({
            "type": "Feature",
            "geometry": {"type": "Polygon", "coordinates": rings},
            "properties": {k: v for k, v in row.items() if k != "polygon_wkt"},
        })

        print(f"  [{i+1}/{len(rows)}] {case_number} -> ({lat:.5f}, {lon:.5f})" if lat is not None
              else f"  [{i+1}/{len(rows)}] {case_number} -> degenerate geometry, no centroid")
        time.sleep(0.2)

    with open(CSV_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    with open(GEOJSON_PATH, "w") as f:
        json.dump({"type": "FeatureCollection", "features": geojson_features}, f, indent=2)

    print(f"\nDone. {len(rows) - len(missing)}/{len(rows)} cases got geometry.")
    if missing:
        print("No geometry found for:", ", ".join(missing))
    print(f"Updated {CSV_PATH} (backup at {CSV_PATH}.bak)")
    print(f"Wrote {GEOJSON_PATH} with {len(geojson_features)} polygon features")


if __name__ == "__main__":
    main()
