"""
Reapplies geometry that was recovered once, by hand, for cases where
the automated pipeline (add_geometry.py, then add_legal_land_desc.py)
can't produce it - because BLM has no digitized Shape for the case in
the ROW case-disposition layer *and* the Case_Lands legal-description
join also fails for it (as opposed to simply lacking a record yet).

Run this LAST, after add_geometry.py and add_legal_land_desc.py, on
every refresh. Both of those scripts rewrite the whole CSV/geojson
from scratch each time they run, so any one-off manual recovery is
silently wiped unless it's re-applied as a final patch step - this
script is that step.

Each entry in MANUAL_RECOVERIES is a one-time reconstruction; see the
docstring next to it (and SUMMARY.md's "Geometry / mapping" section)
for exactly how it was derived. If a future BLM data update gives one
of these cases real geometry via either upstream script, this script
detects that (the row already has a polygon_wkt) and leaves it alone.
"""
import csv
import json

from add_geometry import rings_to_geojson_geometry

CSV_PATH = "data_center_row_cases.csv"
GEOJSON_PATH = "data_center_row_cases.geojson"

MANUAL_RECOVERIES = {
    "WYWY106759247": {
        # Jacqueline Data Center Project (Copia Digital, LLC; WY,
        # Rock Springs FO; Interim/Application Withdrawn).
        #
        # BLM's Case_Lands join fails for this case (QLTY: "TOWNSHIP
        # NOT FOUND") even though it has a legal land description on
        # file (5 MTRS segments, WY Meridian 06, T20N/T21N R100-101W -
        # see its legal_land_description column). Recovered 2026-09-18
        # by querying BLM's separate, canonical national PLSS
        # reference service directly -
        # https://gis.blm.gov/arcgis/rest/services/Cadastral/BLM_Natl_PLSS_CadNSDI/MapServer,
        # layer 3 "PLSS Intersected" - for each cited aliquot/lot
        # (Sec 2: SW + Lots 3-4; Sec 10: N2NE + N2NW; Sec 32: entire
        # section, since its N2 + N2SW + N2SE + Lots 1-4 exhaustively
        # cover it) and unioning the parts into one polygon. Lands
        # next to the Jim Bridger power plant near Rock Springs, WY.
        "centroid_lat": "41.744404",
        "centroid_lon": "-108.761041",
        "polygon_wkt": (
            "MULTIPOLYGON(((-108.76332667550783 41.736389618168815, -108.76814489014552 41.73640067872533, "
            "-108.76811993045536 41.74001161801081, -108.76330530099396 41.739996362673786, "
            "-108.76332667550783 41.736389618168815)), "
            "((-108.76814489014552 41.73640067872533, -108.77296313352929 41.73641157236616, "
            "-108.77293456171337 41.74002665080496, -108.76811993045536 41.74001161801081, "
            "-108.76814489014552 41.73640067872533)), "
            "((-108.76332667550783 41.736389618168815, -108.76334805181833 41.732782873558776, "
            "-108.76816987768346 41.73278965640721, -108.76814489014552 41.73640067872533, "
            "-108.76332667550783 41.736389618168815)), "
            "((-108.76816987768346 41.73278965640721, -108.77299167839575 41.73279646808104, "
            "-108.77296313352929 41.73641157236616, -108.76814489014552 41.73640067872533, "
            "-108.76816987768346 41.73278965640721)), "
            "((-108.76330530099396 41.739996362673786, -108.76811993045536 41.74001161801081, "
            "-108.76809113495892 41.74318500122942, -108.76735019912267 41.74318713535594, "
            "-108.76328630971054 41.74319996893519, -108.76330530099396 41.739996362673786)), "
            "((-108.76811993045536 41.74001161801081, -108.77293456171337 41.74002665080496, "
            "-108.7728959602073 41.743173589951674, -108.7721852194427 41.74317205705327, "
            "-108.76809113495892 41.74318500122942, -108.76811993045536 41.74001161801081)), "
            "((-108.78745864719453 41.72919557216954, -108.79227844556206 41.72920366068858, "
            "-108.79224564986767 41.73281954370167, -108.78743215677511 41.73281376105463, "
            "-108.78745864719453 41.72919557216954)), "
            "((-108.7778141869805 41.729178951315625, -108.78263887577646 41.72918726040229, "
            "-108.78261866458088 41.73280800522198, -108.77780517059 41.7328022225739, "
            "-108.7778141869805 41.729178951315625)), "
            "((-108.78745864719453 41.72919557216954, -108.78743215677511 41.73281376172498, "
            "-108.78261866458088 41.73280800589237, -108.78263887577646 41.72918726040229, "
            "-108.78745864719453 41.72919557216954)), "
            "((-108.77298947033678 41.72917041831021, -108.7778141869805 41.729178951315625, "
            "-108.77780517059 41.7328022225739, -108.77299167839575 41.73279646808104, "
            "-108.77298947033678 41.72917041831021)), "
            "((-108.74808638930178 41.75724386654543, -108.74325197534459 41.75724626892238, "
            "-108.74324320149921 41.75362482377918, -108.74807691926208 41.75362250570643, "
            "-108.74808638930178 41.75724386654543)), "
            "((-108.76258953235873 41.75723664735187, -108.75775515343581 41.757239032976116, "
            "-108.75774176763979 41.75361747751881, -108.76257292340743 41.75361476003226, "
            "-108.76258953235873 41.75723664735187)), "
            "((-108.74321880056115 41.74638191163141, -108.74805440748105 41.746378594650636, "
            "-108.74806747886674 41.75000103369757, -108.7432344267555 41.75000337803869, "
            "-108.74321880056115 41.74638191163141)), "
            "((-108.75290049953695 41.7499985017018, -108.75772840699655 41.74999581086978, "
            "-108.75774176763979 41.75361747751881, -108.75291063702493 41.75361997385351, "
            "-108.75290049953695 41.7499985017018)), "
            "((-108.74805440748105 41.746378594650636, -108.7528903746254 41.74637506185474, "
            "-108.75290049953695 41.7499985017018, -108.74806747886674 41.75000103369757, "
            "-108.74805440748105 41.746378594650636)), "
            "((-108.75771236578052 41.74637320464024, -108.76253463541342 41.74637115439867, "
            "-108.76255631625278 41.74999287206561, -108.75772840699655 41.74999581086978, "
            "-108.75771236578052 41.74637320464024)), "
            "((-108.76255631625278 41.74999287072521, -108.76257292340743 41.75361476003226, "
            "-108.75774176763979 41.75361747751881, -108.75772840699655 41.74999581086978, "
            "-108.76255631625278 41.74999287072521)), "
            "((-108.74807691926208 41.75362250570643, -108.74324320149921 41.75362482377918, "
            "-108.7432344267555 41.75000337803869, -108.74806747886674 41.75000103369757, "
            "-108.74807691926208 41.75362250570643)), "
            "((-108.74806747886674 41.75000103369757, -108.75290049953695 41.7499985017018, "
            "-108.75291063702493 41.75361997385351, -108.74807691926208 41.75362250570643, "
            "-108.74806747886674 41.75000103369757)), "
            "((-108.75290049953695 41.7499985017018, -108.7528903746254 41.74637506185474, "
            "-108.75771236578052 41.74637320464024, -108.75772840699655 41.74999581086978, "
            "-108.75290049953695 41.7499985017018)), "
            "((-108.74807691926208 41.75362250570643, -108.75291063702493 41.75361997385351, "
            "-108.7529207736146 41.75724144607517, -108.74808638930178 41.75724386654543, "
            "-108.74807691926208 41.75362250570643)), "
            "((-108.75291063702493 41.75361997385351, -108.75774176763979 41.75361747751881, "
            "-108.75775515343581 41.757239032976116, -108.7529207736146 41.75724144607517, "
            "-108.75291063702493 41.75361997385351)), "
            "((-108.74320420293779 41.74315883337358, -108.74401886530602 41.74316055863865, "
            "-108.74804281202735 41.74316812594296, -108.74805440748105 41.746378594650636, "
            "-108.74321880056115 41.74638191163141, -108.74320420293779 41.74315883337358)), "
            "((-108.75288144447315 41.74317739974351, -108.7536767724015 41.743179432660156, "
            "-108.75769829816316 41.743189765479165, -108.75771236578052 41.74637320464024, "
            "-108.7528903746254 41.74637506185474, -108.75288144447315 41.74317739974351)), "
            "((-108.75769829816316 41.743189765479165, -108.75848154105604 41.743191826546564, "
            "-108.76251515095488 41.74320218684444, -108.76253463541342 41.74637115439867, "
            "-108.75771236578052 41.74637320464024, -108.75769829816316 41.743189765479165)), "
            "((-108.75288144447315 41.74317739974351, -108.7528903746254 41.74637506185474, "
            "-108.74805440748105 41.746378594650636, -108.74804281202735 41.74316812594296, "
            "-108.74884783367597 41.743169823726845, -108.75288144447315 41.74317739974351)))"
        ),
    },
}


def wkt_to_rings(wkt):
    """Inverse of add_geometry.rings_to_wkt: 'MULTIPOLYGON(((...)), (...))' -> [[[x, y], ...], ...]"""
    inner = wkt[len("MULTIPOLYGON(("):-2]
    rings = []
    for ring_str in inner.split("), ("):
        ring_str = ring_str.strip("()")
        pts = [[float(v) for v in pair.split()] for pair in ring_str.split(", ")]
        rings.append(pts)
    return rings


def main():
    with open(CSV_PATH, newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    with open(GEOJSON_PATH) as f:
        geojson = json.load(f)
    already_mapped = {feat["properties"]["case_number"] for feat in geojson["features"]}

    restored = []
    for row in rows:
        recovery = MANUAL_RECOVERIES.get(row["case_number"])
        if not recovery or row.get("polygon_wkt"):
            continue

        row["centroid_lat"] = recovery["centroid_lat"]
        row["centroid_lon"] = recovery["centroid_lon"]
        row["polygon_wkt"] = recovery["polygon_wkt"]
        restored.append(row["case_number"])

        if row["case_number"] not in already_mapped:
            rings = wkt_to_rings(recovery["polygon_wkt"])
            geojson["features"].append({
                "type": "Feature",
                "geometry": rings_to_geojson_geometry(rings),
                "properties": {k: v for k, v in row.items() if k != "polygon_wkt"},
            })

    if not restored:
        print("Nothing to restore (every manually-recovered case already has geometry).")
        return

    with open(CSV_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    with open(GEOJSON_PATH, "w") as f:
        json.dump(geojson, f, indent=2)

    print(f"Restored manually-recovered geometry for: {restored}")


if __name__ == "__main__":
    main()
