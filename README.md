# BLM Data Center Tracker

A Center for Western Priorities project that tracks right-of-way (ROW) cases on federal public lands, managed by the Bureau of Land Management (BLM), that appear to be tied to data center and AI-compute development, including nuclear-powered "gigasite" proposals. It combines a systematic search of BLM's public land-records database with corporate, news, and local-records research, and publishes the result as an interactive map.

**Live map:** https://blm-data-centers.netlify.app

## What's in the repo

| Path | What it is |
|---|---|
| `data_center_row_cases.csv` / `.geojson` | The core dataset: one row per confirmed or flagged case, with BLM attributes, polygon geometry, and centroids |
| `candidates_raw.csv` | Every raw search hit reviewed, including the false positives that were rejected |
| `map.html` → `site/index.html` | The interactive Leaflet map (`map.html` is the source; `site/` is what gets deployed) |
| `SUMMARY.md` | Running dataset summary and a dated log of every refresh |
| `PROJECT_SUMMARIES.md` | Per-project/developer write-ups with corporate and press research |
| `MLRS_API_HOWTO.md` | Step-by-step guide to querying BLM's MLRS ArcGIS REST service, so the search can be reproduced |
| `estimated_locations.json` | Hand-estimated locations for cases BLM has no geometry for (currently Project Beehive) |
| `external_research/` | Supporting research by source type (corporate filings, SEC EDGAR, news, local records, utility interconnection), each with a `findings.md` and archived source documents |
| `add_geometry.py`, `add_legal_land_desc.py`, `restore_manual_geometry.py`, `build_map_data.py` | The geometry and map-build pipeline (see below) |

## Methodology

### 1. Data source

All case data comes from BLM's Mineral & Land Records System (MLRS), via its public ArcGIS REST service (`Land_Use_Authorizations/Rights_of_Way_Case_Disp`). No login or API key is needed. The service exposes four case-disposition layers: **Pending**, **Authorized**, **Interim**, and **Closed**. We query all four. `MLRS_API_HOWTO.md` documents the endpoints, field names, and query patterns in full.

### 2. Finding candidate cases

BLM's ROW records have no "data center" category, so cases must be found by searching names. We use two independent passes:

1. **Topic-keyword pass.** Matches the case's geographic name (`CSE_NAME`) or applicant (`CUST_NM_SEC`) against terms such as `DATA`, `HYPERSCALE`, `GIGASITE`, `STARGATE`, `COMPUTE`, `SMR`, `MODULAR REACTOR`, `COLOCATION`, and similar.
2. **Known-developer pass.** Matches applicant names directly against developers already confirmed, through corporate, SEC, or press research, to be active in this space (for example Copia, Valar, Prometheus, Skylar, Meadowlark, Arevia, Tract, Fleet), plus a watch list of other sector players.

The second pass exists because the first has a structural blind spot. Early-stage BLM cases are often filed with no case name at all, and applicant LLC names (e.g. "Copia GDC, LLC") frequently contain no topic keyword. We found this gap on 2026-09-18, when a direct developer-name query surfaced a case, and eight others, that keyword search could never have found.

### 3. Manual review

Raw hits are noisy: the combined passes return roughly 300 rows per run, and most are false positives. Every hit is reviewed by hand against corporate records, press coverage, and the case's own details, and sorted into confirmed, flagged-ambiguous, or rejected. Rejected hits stay logged in `candidates_raw.csv`. Recurring false-positive families include legacy radio and telecom ("SMR" meaning Specialized Mobile Radio), place and company names containing "cloud" or "fleet," cell-tower "co-location" cases, uranium mining companies, "Digital 395" broadband fiber, and renewable-only projects by developers who also build data centers.

A case is "confirmed" only when its name, applicant, or surrounding research ties it to a data center or compute campus. Solar, transmission, or geotechnical cases from developers on the watch list are included when they appear to support a campus, and are flagged as ambiguous when that link is unconfirmed.

### 4. Geometry

Geometry is recovered in order of reliability:

1. **BLM's own polygon** from the ROW layer (`add_geometry.py`), reprojected to WGS84, with an area-weighted centroid.
2. **PLSS legal-land-description fallback** (`add_legal_land_desc.py`). When the ROW layer has no shape, we join BLM's `Case_Lands` service by case number and union the geocoded Township/Range/Section parcels.
3. **Manual recovery** (`restore_manual_geometry.py`) for one-off cases where both automated routes fail. Currently this is the Jacqueline Data Center Project, rebuilt from BLM's national PLSS reference service.
4. **Estimated location** (`estimated_locations.json`) for cases with no geometry at all. These show on the map as an approximate marker, clearly labeled as an estimate with its uncertainty and source. Only Project Beehive qualifies so far, hand-placed from NPR's locator map (about ±1 mile).

Cases that still have no location appear in the "Not yet mappable" list in the sidebar.

### 5. Refresh process

Each refresh re-runs both search passes, then re-queries every tracked case number directly to catch status changes, acreage changes, renames, and removals. Results are logged by date in `SUMMARY.md`. BLM changes records without notice (cases are renamed, closed, or have acreage rewritten), so changes are treated as provisional until corroborated.

Pipeline order after the search passes:

```bash
.venv/bin/python add_geometry.py
.venv/bin/python add_legal_land_desc.py
.venv/bin/python restore_manual_geometry.py   # must run after the two above, which rewrite the CSV/geojson wholesale
.venv/bin/python build_map_data.py            # embeds data in map.html, copies to site/, stamps "Last updated", deploys to Netlify
```

Pass `--no-deploy` to `build_map_data.py` to rebuild without deploying. Python dependencies are in `requirements.txt`.

## Reading the map

- **Disposition** is BLM's case status. *Pending* means an application is under review. *Authorized* means a land-use authorization has been issued. *Interim* is a BLM status between pending and final; in this dataset it includes some withdrawn applications and cases BLM moved out of Pending without a final decision. *Closed* means the case ended, usually without action. The map opens with Closed hidden; the checkbox turns it on.
- **The overview numbers** (cases, acres, states) follow whichever dispositions are checked.
- **Acres** are BLM's recorded acreage, summed across cases, plus acreage reported by the press for cases BLM has not yet recorded (currently Project Beehive's "more than 9,000 acres," per NPR). The total is shown as "at least" and rounded down to the nearest 500 acres.

## Limitations

- **Discovery is name-based and may miss cases.** A case with no name and an applicant we haven't identified will not be found. The developer watch list is extended whenever new players are confirmed.
- **Acreage is not always reliable.** BLM sometimes records 0 acres for early-stage and linear cases, and has rewritten recorded acreage on existing cases without explanation. Some tracked cases have no geometry yet.
- **A BLM case is not a project approval.** A ROW application is a request to use federal land. Pending cases may be withdrawn, denied, or never built, and one project can span several cases filed under different LLCs.
- **Multi-case campuses.** Some campuses are split across shell LLCs or supporting-infrastructure cases (roads, pipelines, transmission, geotechnical work), so case counts overstate the number of distinct projects.
- **Estimated locations** are approximations from published maps, not BLM data.
- **BLM's NEPA register** (eplanning.blm.gov) has no open API and is checked manually. It is not part of the automated search.

## Credits and license

A project of the [Center for Western Priorities](https://westernpriorities.org). Land-records data is from the Bureau of Land Management; corporate and press sources are cited in `PROJECT_SUMMARIES.md` and under `external_research/`. Released under the MIT License (see `LICENSE`).
