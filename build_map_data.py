"""
Final pipeline step: embed the refreshed geojson (plus the not-yet-mapped
CSV rows, as `unmapped`) into map.html's `const DATA = ...;` line and copy
the result to site/index.html.

Run order: add_geometry.py -> add_legal_land_desc.py ->
restore_manual_geometry.py -> build_map_data.py
"""
import csv
import json
import re
import os
import shutil
import subprocess

G = json.load(open("data_center_row_cases.geojson"))
mapped = {f["properties"]["case_number"] for f in G["features"]}
cols = [c for c in G["features"][0]["properties"].keys()]
unmapped = [
    {c: r[c] for c in cols}
    for r in csv.DictReader(open("data_center_row_cases.csv"))
    if r["case_number"] not in mapped
]
data = dict(G, unmapped=unmapped)
line = "const DATA = " + json.dumps(data, separators=(",", ":")) + ";"

html = open("map.html").read()
html, n = re.subn(r"^const DATA = .*;$", lambda m: line, html, flags=re.M)
assert n == 1
open("map.html", "w").write(html)
shutil.copyfile("map.html", "site/index.html")
os.remove("blm-data-center-tracker.zip") if os.path.exists("blm-data-center-tracker.zip") else None
subprocess.run(["zip", "-rq", "blm-data-center-tracker.zip", "site", "-x", "*.DS_Store"], check=True)
print(f"map.html + site/index.html: {len(G['features'])} mapped, {len(unmapped)} unmapped")
