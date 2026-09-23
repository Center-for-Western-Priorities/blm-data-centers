# BLM MLRS Data Center ROW Cases — Summary

Source: BLM MLRS public ArcGIS REST service (`Land_Use_Authorizations/Rights_of_Way_Case_Disp`), all four case-disposition layers (Authorized, Pending, Interim, Closed). Two search passes are now used (see `MLRS_API_HOWTO.md` §7 for the methodology change and why it was added):

1. **Topic-keyword pass** (original method): `CSE_NAME`/`CUST_NM_SEC` matched against `DATA`, `HYPERSCALE`, `SERVER`, `COMPUTE`, `GIGASITE`, `STARGATE`, `CLOUD`, `SMR`, `AI`, `ARTIFICIAL INTELLIGENCE`, `COLOCATION`, `CO-LOCATION`, `NUCLEAR`, `MODULAR REACTOR`, `DIGITAL`. 128 raw hits from the original 14-keyword list.
2. **Known-developer pass** (added 2026-09-18): `CUST_NM_SEC` matched directly against the names of developers already confirmed (via corporate/SEC/news research) to be active in this space — `COPIA`, `VALAR`, `PROMETHEUS`, `SKYLAR`, `MEADOWLARK`, `AREVIA`, `TRACT`, `FLEET` — run independently of whether the case has a descriptive name at all. This pass exists because BLM case records are often filed with **no `CSE_NAME`** (null) in their early-Pending state, and applicant LLC names (e.g. "Copia GDC, LLC") frequently don't contain any topic keyword — so a topic-keyword-only search structurally cannot find them. See "Methodology gap found 2026-09-18" below.

Combined: 137 raw hits, manually reviewed down to 36 confirmed + 3 flagged-ambiguous cases. Full raw list: `candidates_raw.csv`. Filtered list: `data_center_row_cases.csv`.

## Refresh, 2026-09-23

Re-ran both search passes (topic-keyword + developer-name, the latter expanded with the sector-scan watch list from §7 of `MLRS_API_HOWTO.md`: `TERRAPOWER`, `NATRIUM`, `SABEY`, `CRUSOE`, `KAIROS`, `DEEP ATOMIC`, `OLEARY`, `STRATOS`) and separately re-queried all 39 previously-tracked case numbers directly to catch drift. Net result: **2 new confirmed cases, 2 status/acreage updates, 0 renames, 0 removals.**

**New cases:**
- **Leo Energy Geotech** (AZAZ106849711, Kingman FO, 39.53 ac, Pending, filed 2026-09-17) — Leo Data LLC, a geotech sub-case for the existing Leo Data Center (AZAZ106782092), same pattern as the geotech sub-cases already tracked for Silver Springs West, Skylar, and On The Mark.
- **Powerline to Prometheus facility** (WYWY105862062, Kemmerer FO, 13.23 ac, Pending, filed 2022-08-01) — applicant PacifiCorp (65% interest), explicitly named for Prometheus Hyperscale in BLM's own case name; a fourth Prometheus-linked supporting-infrastructure case (alongside the access road, water pipeline, and telecom line already tracked), and the oldest-filed case in this whole dataset by a wide margin — it predates every other Prometheus/Wyoming Hyperscale case here by over two years, suggesting this interconnection ROW has been in the pipeline since near the start of the Evanston build-out.

**Status/acreage drift on existing cases:**
- **NVNV106802346** (Silver Springs West Data Center Geotech) — Pending → **Authorized** (Land Use Authorization Issued, 2026-09-18).
- **NVNV106802350** (On The Mark Data Center Geotech) — Pending → **Authorized** (Land Use Authorization Issued, 2026-09-18); recorded acreage also jumped **4.05 → 560.0** acres in the same update — the geotech case now carries the same acreage as its parent On The Mark main site (NVNV106778200, 560 ac), which reads as BLM consolidating the geotech authorization's recorded footprint onto the main site rather than a real change in the geotech work itself. Flagged as provisional, same caveat as prior acreage-drift findings (Charleston, Rhea Data) — not independently confirmed.

**Broader keyword sweep, no other hits confirmed:** the wider raw pull (298 merged rows vs. 137 previously) was almost entirely noise from broadening `TRACT`/`FLEET`/`DIGITAL` further and adding the sector-scan names — same false-positive patterns already documented (DigitalPath Inc./California Broadband Coop, Arevia Power's renewable-only portfolio [Pink Sky Solar, Newark Valley, Silver Peak, Pony Express Wind, Libra Solar, San Emidio Solar I, Scorpio Energy Center — all already-known Arevia renewables, not data-center-linked], "Skylar Verano Solar" [Skylar Opportunities LLC's already-documented unrelated Riverside, CA solar lease], Norfleet/Northfleet Land Services, FirstDigital Telecom, and generic "CONTRACT/CONTRACTOR/TRACTOR" matches). No new developer names or sector players surfaced.

Geometry was refreshed for all 41 rows via `add_geometry.py` + `add_legal_land_desc.py`; **33/41 now have geometry** (up from 31/39 — both new cases lack a digitized Shape and Leo Energy Geotech has no Case_Lands record either, consistent with being a brand-new Pending filing). The manually-recovered Jacqueline Data Center Project polygon (see the "Geometry / mapping" section below) isn't reproducible by either script, and both of them overwrite the full CSV/geojson on every run, so it was getting silently wiped on each refresh. **Fixed 2026-09-23** by adding `restore_manual_geometry.py`, a third pipeline step that re-applies a small hardcoded table of one-off manual recoveries (currently just Jacqueline) after the other two scripts run — see its docstring for the exact provenance. **Run order going forward: `add_geometry.py` → `add_legal_land_desc.py` → `restore_manual_geometry.py`.**

**Excluded as false positives:** legacy telecom infrastructure using "SMR" (Specialized Mobile Radio, not Small Modular Reactor), company/place names containing "cloud" (St Cloud Mining, White Cloud Communications, McCloud, Cloud Peak Energy, etc.), cell-tower "co-location" cases (T-Mobile, BOR antenna sites), uranium/nuclear-fuel mining companies (Energy Fuels Nuclear, Western Nuclear, United Nuclear), federal facilities (NOAA data center, DOD comm sites, Nuclear Security Administration), generic "data collection" survey/monitoring permits, DigitalPath Inc./California Broadband Coop (rural broadband tower sites matched by "DIGITAL," unrelated), and Arevia Power's non-data-center wind/solar portfolio (Taurus Wind, Snake River Energy, Pink Sky Solar, Silver Peak, San Emidio Solar, Newark Valley, Scorpio Energy Center — all confirmed Arevia Power renewable-energy filings with no data-center connection).

## Methodology gap found 2026-09-18

The Washington Sun's Sept. 18, 2026 story ["Trump Is Considering More Data Centers on Public Lands Than Previously Known"](https://www.washingtonsun.com/climate-environment/trump-administration-data-centers-public-lands-proposals) reported an Oregon Copia Power right-of-way application. Our existing Charleston Data Center and BESS case (OR, Baker FO) already covered the named Oregon Copia project — but checking prompted a direct `CUST_NM_SEC LIKE '%COPIA%'` query (rather than relying on topic keywords), which turned up a **second, previously invisible Oregon case**:

- **OROR106695593** — applicant `Copia GDC, LLC`, Baker Field Office (same office as Charleston), 26 acres, **`CSE_NAME` is null** — no geographic name was ever assigned — status Closed ("Case Closed without Action," 2026-07-06).

This case could not have been found by the original method: it has no name to match `DATA`/etc. against, and "Copia GDC, LLC" itself doesn't contain any topic keyword. The same direct-developer-name query surfaced 8 more previously-missed cases nationally (new Copia Digital/Copia GDC parcels in Las Vegas FO totaling ~2,880 more acres, a Copia solar/transmission pair in Arizona, a new Valar Atomics Utah case, and a closed Skylar Opportunities transmission case) — all added below. It also caught a **live rename**: Valar's `UTUT106801248` is no longer named "Raceway Gigasite Small Modular Reactor/Data Center" in BLM's system — it's now "Project Beehive Small Modular Reactor/Data Center" (same case number/acreage/date), corrected throughout this project's files. Going forward, the known-developer pass should be re-run periodically and its keyword list extended every time a new developer is corporate-confirmed.

**Sector scan, 2026-09-18:** researched the broader AI-data-center/nuclear-SMR industry for other major players to add to the developer watch list. Checked directly against MLRS: established colo/REIT operators (Vantage, QTS, Aligned, EdgeConneX, Novva, Switch, Digital Realty, Compass, Stack), the highest-profile 2026 nuclear-SMR pairings (TerraPower/Natrium + Sabey in Kemmerer WY, Kairos/Google, Deep Atomic at Idaho National Lab), Tract/Fleet Data Centers' large Nevada expansion, Kevin O'Leary's 9GW "Wonder Valley"/Stratos project in Utah, and the major hyperscalers themselves (Microsoft, Meta, Amazon, Google, Oklo, Nvidia, Crusoe). **None currently have BLM MLRS records** — all confirmed to sit on private, military, DOE, or state-trust land rather than BLM parcels. Full detail and a standing watch list (for periodic re-checking, since a private-land project can spin off a BLM supporting-infrastructure filing later) is in `MLRS_API_HOWTO.md` §7.

## By developer / project cluster

**Copia Digital, LLC / Copia GDC, LLC / Copia Power Sawtooth DevCo, LLC** — serial multi-state filer, now 16 identified site/infrastructure proposals (up from 7 — 9 added 2026-09-18 via the developer-name search pass), mostly filed Oct 2025–early 2026:
- Frontier Data Center (AZ, Lower Sonoran FO, 798 ac, Pending)
- Harquahala Data Center (AZ, Lower Sonoran FO, 355 ac, Pending)
- TAP Data Center (AZ, Lower Sonoran FO, 999 ac, Pending)
- Harquahala to Hyder Transmission Line (AZ, Yuma FO, linear/no recorded acreage, Pending) — *new*, likely serves the Harquahala-cluster/Belmont Energy Center campus
- Stanley Solar (AZ, Hassayampa FO, 1,120 ac, Pending) — *new, flagged ambiguous*: solar-only filing, part of Copia Power's broader renewable portfolio; unconfirmed whether tied to a specific data-center campus
- Falcon Data Center (ID, Shoshone FO, 3,013 ac, Pending)
- Copia Power Sawtooth DevCo, LLC solar grant (ID, Four Rivers FO, no recorded acreage, Pending/contradictory "Case Closed" action) — *new, flagged ambiguous*: solar-only, different project name ("Sawtooth") than Falcon
- Monarch Data Center (NV, Sierra Front FO, 120 ac, Pending)
- (unnamed) Copia Digital, LLC — NV, Las Vegas FO, **2,519.57 ac**, Pending — *new*, no `CSE_NAME` assigned yet; largest single Copia parcel found, likely a major undisclosed Las Vegas-area site
- (unnamed) Copia GDC, LLC — NV, Las Vegas FO, 179.33 ac, Pending — *new*, no name
- (unnamed) Copia GDC, LLC — NV, Las Vegas FO, 183.29 ac, Pending — *new*, no name
- Charleston Data Center and BESS (OR, Baker FO, 106 ac [was 36 ac at our 2026-09-10 pull — BLM has since updated the acreage], Pending)
- (unnamed) Copia GDC, LLC — OR, Baker FO, 26 ac, Closed without Action 2026-07-06 — *new*: **the case our original search missed** (see "Methodology gap" above)
- Jacqueline Data Center Project (WY, Rock Springs FO, **Application Withdrawn**)

**Silver Springs cluster** (NV, Sierra Front FO, filed same day 2025-02-03) — appears to be one large multi-parcel campus split across shell LLCs:
- Silver Springs North — Moorman Ridge Data, LLC (1,160 ac)
- Silver Springs South — Silver Springs South, LLC (1,117 ac)
- Silver Springs West — Kimberly Mountain Data, LLC (680 ac) + geotech sub-case
- Dayton North Data Center — Dayton North, LLC (same field office/filing date, possibly related)

**Skylar Opportunities LLC** (NV, Las Vegas FO) — 4 related cases for one site: Horizon Project (Data Center), Skylar Opportunities Data Center & Bess, + geotech sub-case, + Eldorado GenTie (Skylar) transmission line (42 ac, Interim/Case Closed without Action 2026-08-28 — *new*, found via developer-name pass).

**On The Mark Data Center LLC** (NV, Sierra Front FO) — main site (560 ac, Pending) + geotech sub-case.

**Meadowlark Renewables Center LLC** (NV, Bristlecone FO) — East (3,026 ac) + West (1,009 ac), both **Closed 2025-03-05** — worth checking eplanning for why (denied/withdrawn vs. superseded).

**Valar Atomics** (UT, Price FO) — nuclear-powered compute campuses, all Pending:
- Green River Gigasite Small Modular Reactor/Data Center (10,271 ac)
- Project Beehive Small Modular Reactor/Data Center (renamed from "Raceway Gigasite Small Modular Reactor/Data Center" — same case # UTUT106801248, same filing date/acreage; BLM changed the name between our 2026-09-10 and 2026-09-18 pulls)
- (unnamed) distribution line / oil & gas pipeline case (0 ac recorded) — *new*, found via developer-name pass; likely supporting infrastructure for one of the two Gigasite sites

**Prometheus Hyperscale** (WY, Kemmerer FO) — 3 supporting infrastructure ROW cases (access road, water pipeline, telecom line) referencing "Data Center," all Pending; the main site case itself didn't surface under these keywords — worth a direct eplanning search for "Prometheus Hyperscale."

**Wyoming Hyperscale White Box LLC** (WY, Kemmerer FO) — access road + water facility, both **Closed 2024-07-09** — earliest-dated case in this set, likely an already-operational facility.

**Townsite Data Center** — Townsite Solar 2, LLC (NV, Las Vegas FO, 85 ac, **Authorized** 2026-04-22) — paired with a solar project.

**Rhea Data LLC** (ID, Four Rivers FO, 1 ac, Pending) — small early-stage case.

**Leo Data LLC** (AZ, Lake Havasu FO, 1,110 ac, Pending).

## Flagged for review (ambiguous)

- **Sandy Valley Mining Energy & Compute LLC** (NV, Las Vegas FO, 331.89 ac, Pending) — access road to the Goodsprings mining district; business name suggests a mining/crypto-compute operation rather than a conventional data center. Included for your judgment call.
- **Stanley Solar / Copia GDC, LLC** (AZ, Hassayampa FO, 1,120 ac, Pending) — *new*: a solar-only filing from a confirmed data-center developer; unconfirmed whether it's part of a specific data-center campus or Copia's separate 25GW solar/storage portfolio.
- **Copia Power Sawtooth DevCo, LLC solar grant** (ID, Four Rivers FO, no recorded acreage) — *new*: another solar-only Copia-affiliated filing, under a differently-named DevCo shell than Falcon Data Center; relationship to a specific data-center project unconfirmed.

## Status breakdown

(41 rows: 38 confirmed + 3 flagged ambiguous cases — updated 2026-09-23, see "Refresh" section above)

| Disposition | Count |
|---|---|
| Pending | 31 |
| Closed | 5 |
| Authorized | 3 |
| Interim | 2 |

## Geometry / mapping (added 2026-09-18)

`data_center_row_cases.csv` now includes `centroid_lat`, `centroid_lon`, and `polygon_wkt` columns, pulled directly from the same MLRS ArcGIS REST service (`returnGeometry=true`, `outSR=4326`) keyed by each case's disposition layer — see `add_geometry.py`. Centroids are computed with a proper area-weighted polygon-centroid formula (not a naive vertex average), so they land inside irregular parcel shapes correctly.

A standalone `data_center_row_cases.geojson` (FeatureCollection, full polygons + all case attributes) was also generated for direct import into QGIS, Google My Maps, kepler.gl, geojson.io, etc.

**30 of 39 cases got geometry from the ROW case-disposition layer; 9 did not** — BLM's system has no digitized Shape recorded for these yet in that layer (confirmed by checking all four dispositions directly, not a query bug). Most also have `0.0` recorded acreage — consistent with being early-stage filings BLM hasn't surveyed/digitized yet.

**Legal land descriptions / MTRS (added 2026-09-18, `add_legal_land_desc.py`):** a sibling ArcGIS service, `Case_Lands` (`https://gis.blm.gov/nlsdb/rest/services/Case_Lands/MapServer/0`), carries each case's Legal Land Description from BLM's LR2000 Case Recordation Database — Meridian/Township/Range/Section ("MTRS") strings, e.g. `AZ 14 0020S 0100W 032 Z W2NW,W2SW` (AZ, Meridian 14, T20S R100W, Sec 32, aliquot W½NW¼+W½SW¼) — independent of whether the ROW layer has a mapped Shape. Queried by `CSE_NR` and added as a new `legal_land_description` column (semicolon-joined per case, empty when BLM has no LLD on file yet). Where this service also had its own PLSS-derived geometry, it was unioned in to fill gaps in `polygon_wkt`/`centroid_lat`/`centroid_lon`.

Of the original 9 geometry-less cases, this recovered one more (10 → 29 missing... i.e. **31/39 now have geometry**):
- **`AZAZ106766456`** (Harquahala to Hyder Transmission Line) — full polygon + centroid recovered from `Case_Lands` (6 legal-description parcel segments).
- **`WYWY106759247`** (Jacqueline Data Center Project, withdrawn) — has an MTRS legal description (5 segments, WY Meridian 06) but BLM's own `Case_Lands` join failed for it (`QLTY: "TOWNSHIP NOT FOUND"`). **Recovered anyway, manually (2026-09-18):** the townships/sections it cites (T20N/T21N R100-101W, 6th PM) turned out to exist and be fully surveyed in BLM's *separate*, canonical national PLSS reference service (`https://gis.blm.gov/arcgis/rest/services/Cadastral/BLM_Natl_PLSS_CadNSDI/MapServer`, layer 3 "PLSS Intersected") — so the `Case_Lands` failure was a gap in BLM's internal case-to-land join, not an actual absence of surveyed land. Queried each cited aliquot/lot directly (Sec 2: SW¼ + Lots 3-4; Sec 10: N½NE¼ + N½NW¼; Sec 32: entire section, since its N½ + N½SW¼ + N½SE¼ + Lots 1-4 exhaustively cover it) and unioned the parts into one polygon. Lands right next to the Jim Bridger power plant near Rock Springs, WY — consistent with the site-selection logic of other cases in this set (grid interconnection already in place). Same recovery approach (per-case PLSS query, not a scripted pass) should work for any future geometry-less case whose `Case_Lands` join fails but that has a legal description on file.
- The remaining 7 (`NVNV106717443` Dayton North, `NVNV106774473` Horizon Project, `NVNV106758167` Monarch Data Center, `OROR106761793` Charleston Data Center and BESS, `UTUT106801248` Project Beehive, `UTUT106833224` and `IDID106725198`, both unnamed) have **no record at all** in `Case_Lands` either — BLM hasn't recorded a legal land description for these cases yet in any system checked so far, so there's nothing yet to query the national PLSS service with.

Worth re-running all three scripts periodically (`add_geometry.py`, `add_legal_land_desc.py`, `restore_manual_geometry.py` — see "Refresh, 2026-09-23" above), same as the acreage/rename drift noted above.

## Next step

Cross-reference each case (or the subset you care about) against eplanning.blm.gov's public project search to pull the full NEPA project description, documents, and comment-period status where one exists.
