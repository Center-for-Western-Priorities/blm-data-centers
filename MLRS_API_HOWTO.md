# How to Query BLM's MLRS Rights-of-Way Database via its ArcGIS REST API

This documents the exact method used in this project to search BLM's Mineral & Land Records System (MLRS) land-use-authorization / rights-of-way (ROW) data — without clicking through the map UI's attribute table. It's written so a human or another agent can reproduce every step.

**Scope note:** this covers the MLRS/GIS ROW database only. It does *not* cover BLM's separate NEPA project register (eplanning.blm.gov), which has no comparable open REST API and had to be driven through its web UI instead.

## 1. Background: what you're actually talking to

The map layer the public-facing MLRS "Land Map" shows (Land Use Authorizations → Rights-of-Way, with sub-categories for Pending/Authorized/Interim/Closed) is backed by a standard **Esri ArcGIS Server REST service**. It's public and requires no login, API key, or authentication — the same data the web map renders is available as JSON over plain HTTPS.

Base service URL for the national ROW case dataset:

```
https://gis.blm.gov/nlsdb/rest/services/Land_Use_Authorizations/Rights_of_Way_Case_Disp/MapServer
```

Anything under `gis.blm.gov/nlsdb/rest/services/` is this same kind of ArcGIS REST endpoint — other BLM datasets (e.g. mining claims, grazing allotments) live at sibling paths under the same host, following the same conventions described below.

## 2. Step 1 — Discover the service structure

Append `?f=json` to any ArcGIS REST endpoint to get its metadata as JSON instead of an HTML preview page.

```bash
curl -s "https://gis.blm.gov/nlsdb/rest/services/Land_Use_Authorizations/Rights_of_Way_Case_Disp/MapServer?f=json" | python3 -m json.tool | less
```

The response includes a `layers` array — this is how we learned the four ROW case-disposition types are exposed as separate **sub-layers**, each with its own numeric ID:

| Layer ID | Name |
|---|---|
| 0 | Authorized |
| 1 | Pending |
| 2 | Interim |
| 3 | Closed |

Every query below targets one specific layer ID via its own sub-URL: `.../MapServer/<layer_id>`.

## 3. Step 2 — Discover the field names

Query a specific layer (not the MapServer root) with `?f=json` to get its field list, including each field's internal name, human-readable alias, and type:

```bash
curl -s "https://gis.blm.gov/nlsdb/rest/services/Land_Use_Authorizations/Rights_of_Way_Case_Disp/MapServer/1?f=json"
```

This is the step that told us, for example, that "Geographic Name" (what you'd type into the map UI's attribute-table filter) is actually the field `CSE_NAME`, and "Business Account Name" is `CUST_NM_SEC` — the exact field names you need for the `where` clause in step 4. Full field reference:

| Field name | Alias (what the map UI calls it) | Type |
|---|---|---|
| `OBJECTID` | OBJECTID | esriFieldTypeOID |
| `ADMIN_STATE` | Administrative State | esriFieldTypeString |
| `GEO_STATE` | Geographic State | esriFieldTypeString |
| `BLM_PROD` | BLM Product | esriFieldTypeString |
| `CSE_DISP` | Case Disposition | esriFieldTypeString |
| `CSE_TYPE_NR` | BLM Product Code | esriFieldTypeString |
| `CSE_NR` | Case Serial Number | esriFieldTypeString |
| `LEG_CSE_NR` | Legacy Case Serial Number | esriFieldTypeString |
| `CSE_NAME` | **Geographic Name** | esriFieldTypeString |
| `CMMDTY` | Commodity | esriFieldTypeString |
| `CUST_NM_SEC` | **Business Account Name** | esriFieldTypeString |
| `PCT_INT_SEC` | Business Account Percent Interest | esriFieldTypeDouble |
| `INT_REL_SEC` | Business Account Interest Relationship | esriFieldTypeString |
| `CSE_DISP_DT` | Case Disposition Date | esriFieldTypeDate |
| `CSE_JURIS_CD` / `CSE_JURIS_DESC` | Case File Jurisdiction (code / description, i.e. the field office) | esriFieldTypeString |
| `CSE_WIDTH` / `CSE_LGTH` | Case Width / Length | esriFieldTypeString |
| `QLTY` | Data Quality (internal geocoding-confidence log — verbose, not analytically useful) | esriFieldTypeString |
| `CSE_META` | Case Metadata | esriFieldTypeString |
| `RCRD_ACRS` | Case Acres | esriFieldTypeDouble |
| `SF_ID` | Salesforce ID (BLM's internal case-management system ID) | esriFieldTypeString |
| `Shape` | Geometry | esriFieldTypeGeometry |
| `REC_TYPE_CSE_GRP` | Record Type – Case Group | esriFieldTypeString |
| `CSE_DISP_ACTION` | Case Disposition Action (e.g. "Application Withdrawn," "Land Use Authorization Issued") | esriFieldTypeString |

## 4. Step 3 — Run a query

The actual data lives at a `query` sub-endpoint of each layer:

```
https://gis.blm.gov/nlsdb/rest/services/Land_Use_Authorizations/Rights_of_Way_Case_Disp/MapServer/<layer_id>/query
```

It's a standard Esri REST query endpoint (GET or POST) accepting these key parameters:

| Parameter | Purpose | Example |
|---|---|---|
| `where` | SQL-style filter, evaluated server-side | `UPPER(CSE_NAME) LIKE '%DATA%'` |
| `outFields` | Comma-separated field list to return (`*` for all) | `CSE_NR,CSE_NAME,CUST_NM_SEC` |
| `returnGeometry` | Whether to include map geometry (set `false` — we never needed shapes) | `false` |
| `f` | Response format | `json` |
| `returnCountOnly` | Return just a count, no rows — fast way to check scope before pulling data | `true` |
| `returnDistinctValues` | Return only distinct values of the requested field(s) — combine with `orderByFields` | `true` |

### 4a. Cheapest possible check: just get a count

Before pulling any records, check how many would come back — this is a single lightweight request:

```bash
curl -s "https://gis.blm.gov/nlsdb/rest/services/Land_Use_Authorizations/Rights_of_Way_Case_Disp/MapServer/1/query" \
  --data-urlencode "where=UPPER(CSE_NAME) LIKE '%DATA%' OR UPPER(CUST_NM_SEC) LIKE '%DATA%'" \
  --data-urlencode "returnCountOnly=true" \
  --data-urlencode "f=json"
```

We used this to check all four dispositions before deciding it was safe to pull full records (51 total hits across Authorized/Pending/Interim/Closed for the literal word "data" — small enough to work with).

### 4b. Pulling actual records

```bash
curl -s "https://gis.blm.gov/nlsdb/rest/services/Land_Use_Authorizations/Rights_of_Way_Case_Disp/MapServer/1/query" \
  --data-urlencode "where=UPPER(CSE_NAME) LIKE '%DATA%' OR UPPER(CUST_NM_SEC) LIKE '%DATA%'" \
  --data-urlencode "outFields=CSE_NR,CSE_NAME,CUST_NM_SEC,GEO_STATE,CSE_DISP,CSE_DISP_DT,RCRD_ACRS,CMMDTY,BLM_PROD,SF_ID" \
  --data-urlencode "returnGeometry=false" \
  --data-urlencode "f=json"
```

Response shape is standard Esri JSON: a `features` array, each element with an `attributes` object keyed by the field names you asked for.

### 4c. Getting distinct values of a field (useful for scoping a search before committing to it)

```bash
curl -s "https://gis.blm.gov/nlsdb/rest/services/Land_Use_Authorizations/Rights_of_Way_Case_Disp/MapServer/1/query" \
  --data-urlencode "where=1=1" \
  --data-urlencode "outFields=CMMDTY" \
  --data-urlencode "returnDistinctValues=true" \
  --data-urlencode "orderByFields=CMMDTY" \
  --data-urlencode "returnGeometry=false" \
  --data-urlencode "f=json"
```

We used this to check what commodity codes (`CMMDTY`) data centers actually get classified under before trying to filter by category — it turned up that data centers use generic codes ("OTHER," "OTHER ENERGY FACILITIES," "NON-ENERGY FACILITIES") shared with thousands of unrelated ROW cases nationally, which is why filtering by commodity code alone was a dead end (126,591 hits — checked via `returnCountOnly` first, which is exactly why that cheap check in step 4a is worth doing before pulling anything).

## 5. Practical workflow we actually used, end to end

1. **Set up a Python virtualenv** with `requests` installed (per this workspace's convention — see the repo's own `CLAUDE.md` — write scripts to files rather than inline `python -c` one-liners):
   ```bash
   python3 -m venv .venv
   .venv/bin/pip install requests
   ```
2. **Cheap scoping query** — ran `returnCountOnly=true` with a broad keyword ("DATA") across all four disposition layers to confirm the result set was small enough to work with by hand (51 hits).
3. **Broadened the keyword list** once the user asked for a wider net: instead of one keyword, built a single `where` clause that ORs together many terms, each checked against both `CSE_NAME` and `CUST_NM_SEC`:
   ```python
   keywords = [
       "DATA", "HYPERSCALE", "SERVER", "COMPUTE", "GIGASITE", "STARGATE",
       "CLOUD", "SMR", " AI ", "AI-", "-AI", "ARTIFICIAL INTELLIGENCE",
       "COLOCATION", "CO-LOCATION", "NUCLEAR", "MODULAR REACTOR",
   ]
   where_clause = " OR ".join(
       f"UPPER(CSE_NAME) LIKE '%{kw}%' OR UPPER(CUST_NM_SEC) LIKE '%{kw}%'"
       for kw in keywords
   )
   ```
   *(Note: this string-concatenation approach is fine here because the keyword list is a fixed, developer-supplied constant — never build a `where` clause this way from untrusted/user-supplied input, since it's a straightforward SQL-injection vector against the ArcGIS query engine.)*
4. **Ran that combined query against all four layers**, requesting full attributes (`outFields=<explicit list>` — deliberately excluding the noisy `QLTY`/`CSE_META` geocoding-log fields, which contain embedded newlines that make CSV output unreadable), and merged results into one dict keyed by case number (`CSE_NR`) to de-duplicate.
5. **Wrote the merged results to CSV** (128 raw candidate rows) and manually reviewed every row for false positives (e.g. "SMR" matched decades-old Specialized Mobile Radio telecom companies, not Small Modular Reactor nuclear projects; "CLOUD" matched place names and mining companies with "Cloud" in them) before treating anything as a real data-center project.

## 6. Gotchas learned the hard way

- **`LIKE` matching is a blunt instrument.** A short, common keyword (e.g. "AI" without padding, or "SMR") will match unrelated substrings inside longer words/company names. Always manually review hits rather than trusting a keyword match as confirmation of relevance — see step 5's false-positive list above.
- **Don't filter by commodity/category code alone** — BLM's `CMMDTY` codes for ROW cases are broad, decades-old categories shared by thousands of unrelated authorizations (pipelines, roads, grazing fences, etc.), not a "data center" category. A `returnCountOnly` check before any real pull will catch this before you waste time.
- **`QLTY` and `CSE_META` are internal geocoding-quality logs**, not descriptive metadata — they contain multi-line, semi-structured debug text (e.g. "36 sections retrieved... 16 matching sections found...") that will break naive CSV export if included in `outFields`. Leave them out unless you specifically need geocoding-confidence detail.
- **This service is national in scope** — there's no need to guess at a per-state URL; a single `GEO_STATE` field lets you filter by state within one query if you want to, but the base URL above covers every BLM state office.
- **No pagination was needed for our use case** (max ~130 rows per query), but the standard Esri `resultOffset` / `resultRecordCount` parameters exist if a query you run returns more than the service's default max-record-count (commonly 1,000 or 2,000 depending on server config) — check the `maxRecordCount` field in the layer's `?f=json` metadata if you're unsure.

## 7. Methodology addition (2026-09-18): a second, developer-name-driven search pass is required

**The gap:** the topic-keyword method in §5 has a structural blind spot — it can only find a case if the case's `CSE_NAME` *or* `CUST_NM_SEC` contains one of the topic words. Two common BLM record-keeping patterns defeat this entirely:

1. **`CSE_NAME` is frequently null.** Many cases — especially recently-filed, early-stage "Pending" ones — have no geographic/project name assigned yet in MLRS. If the name field is empty, there's nothing for a `CSE_NAME LIKE '%DATA%'` clause to match, no matter how the keyword list is tuned.
2. **Applicant LLC names don't reliably contain a topic word.** "Copia GDC, LLC," "Copia Power Sawtooth DevCo, LLC," and generic per-parcel shells generally won't match `DATA`/`HYPERSCALE`/etc. even though corporate research has already confirmed exactly who they are.

Combine both (a null-named case filed by a shell LLC) and a real, currently-active data-center-related case becomes **completely invisible** to keyword search — not a matter of tuning the keyword list better, since there's no string to match against on either side of the `OR`.

**How it was found:** cross-checking this project's Oregon coverage against The Washington Sun's 2026-09-18 story on BLM data-center proposals. The Sun reported a Copia Power Oregon project; our dataset already had Charleston Data Center and BESS (OR, Baker FO). Rather than assume that was the whole Oregon picture, we ran `CUST_NM_SEC LIKE '%COPIA%'` directly (no topic keyword at all) across all four layers, which surfaced **OROR106695593** — a second, `CSE_NAME`-null, Closed Copia GDC case in the same field office. That one query, run for `COPIA` alone, also turned up 8 more previously-missed cases nationally.

**The fix — run a second pass keyed on known developers, independent of topic keywords:**

```bash
curl -s "https://gis.blm.gov/nlsdb/rest/services/Land_Use_Authorizations/Rights_of_Way_Case_Disp/MapServer/<layer_id>/query" \
  --data-urlencode "where=UPPER(CUST_NM_SEC) LIKE '%COPIA%'" \
  --data-urlencode "outFields=CSE_NR,CSE_NAME,CUST_NM_SEC,GEO_STATE,CSE_DISP,CSE_DISP_DT,RCRD_ACRS,CMMDTY,BLM_PROD,CSE_JURIS_DESC" \
  --data-urlencode "returnGeometry=false" \
  --data-urlencode "f=json"
```

Run once per known developer name/fragment, across all four layers, and merge into the existing candidate set by `CSE_NR`. The developer list should be **seeded from corporate research, not guessed** — every name below came from separate corporate and press research (see `external_research/`):

`COPIA` (Copia Digital / Copia GDC / Copia Power [DevCo variants]) · `VALAR` (Valar Atomics) · `PROMETHEUS` (Prometheus Hyperscale) · `SKYLAR` (Skylar Opportunities / Skylar Capital) · `MEADOWLARK` (Meadowlark Renewables Center) · `AREVIA` (Arevia Power — parent of Idaho's Rhea Data LLC per the Sun's reporting) · `TRACT` / `FLEET` (Tract Capital Management / Fleet Data Centers — unconfirmed Nevada lead)

**This list must grow every time corporate research confirms a new developer** — it's the whole point of the pass. It will *not* catch a brand-new developer nobody has identified yet; only the topic-keyword pass (§5) or outside reporting can do that. Run both passes together, not one instead of the other — each catches cases the other misses (topic-keyword catches new/unknown developers with descriptively-named cases; developer-name catches known developers with undescribed or non-obviously-named cases).

**Caution:** short developer-name fragments produce false positives too (e.g. `TRACT` alone matches "CONTRACTING," "CONTRACT," "TRACTOR" — see the results this actually returned). Always manually review hits exactly as in §5 step 5, and prefer the fuller name fragment (`AREVIA` not `REVIA`) to cut noise.

### Sector scan, 2026-09-18: checked a broader set of national players — none currently on BLM land

Prompted by the Oregon miss, we ran a wider industry-research pass (news search on the AI-data-center/nuclear-SMR sector) to find any other major developer that should be added to the watch list, then checked each candidate directly against MLRS. Two categories came back negative — worth recording so this isn't re-litigated on the next pass:

- **Established data-center REITs/colo operators** (Vantage Data Centers, QTS, Aligned Data Centers, EdgeConneX, Novva, Switch, Digital Realty, Compass Datacenters, Stack Infrastructure): zero BLM hits under any name variant tried. These companies build near-metro on private/grid-connected land; none of them appear to be pursuing remote BLM parcels the way Copia Power, Valar Atomics, or Skylar Capital are.
- **The most-reported 2026 nuclear-SMR-plus-data-center deals** (TerraPower/Natrium + Sabey Data Centers in Kemmerer, WY; Kairos Power/Google; Deep Atomic's proposal at Idaho National Laboratory; Fermi): zero BLM hits. Confirmed via reporting that these sit on private land (TerraPower's Kemmerer site is a former coal-plant parcel), DOE-administered land (INL, not BLM), or haven't reached a site-specific filing yet.
- **Tract / Fleet Data Centers**, previously an unconfirmed lead in the Silver Springs cluster writeup, checked directly: zero BLM hits despite Tract's large (~8,590-acre) and growing Storey County, NV footprint — that project is on private industrial land (Tahoe-Reno Industrial Center).
- **Kevin O'Leary's "Wonder Valley"/Stratos/O'Leary Digital** project in Box Elder County, UT (40,000 acres, up to 9GW): zero BLM hits — land is private, military (Hill AFB/Utah Test and Training Range), and Utah state trust (MIDA)-administered, not BLM. (Note: a literal `WONDER VALLEY` search does return 4 unrelated hits — a real place name in Barstow FO, California, decades old — don't mistake those for this project.)
- Also checked and clear: Microsoft, Meta Platforms, Amazon, Oklo, Nvidia, Crusoe Energy — no BLM hits under their own names (the one "GOOGLE" hit, `NVNV106750718`, is Google Fiber Nevada, LLC — a broadband ROW, unrelated to a data center).

**Why check companies with zero results at all:** several of these sit geographically close to BLM-administered checkerboard land in states we're already tracking (TerraPower/Sabey and Crusoe in Wyoming; O'Leary/Wonder Valley adjacent to Utah's West Desert BLM holdings), and this sector is moving fast enough that a private-land project today can spin off a BLM supporting-infrastructure ROW (access road, transmission, water) within months, the same way Prometheus Hyperscale's private Evanston campus did. **Add these to a standing watch list and re-run the check periodically** (e.g., alongside each future keyword-list refresh) rather than searching for them only once:

`TERRAPOWER` · `NATRIUM` · `SABEY` · `CRUSOE` · `KAIROS` · `DEEP ATOMIC` · `TRACT` / `FLEET DATA` · `O'LEARY DIGITAL` / `STRATOS` (note the apostrophe breaks the ArcGIS SQL parser — `where=UPPER(CUST_NM_SEC) LIKE '%O''LEARY%'` needs the doubled single-quote escape, or just search `OLEARY` and `STRATOS` separately)

**Also watch for silent data drift between pulls.** The same re-check found that Valar's `UTUT106801248` had been renamed in BLM's system (from "Raceway Gigasite..." to "Project Beehive...") and that Charleston Data Center's recorded acreage had grown from 36 to 106 acres — both since our original 2026-09-10 pull, with no announcement. `RCRD_ACRS` and `CSE_NAME` on Pending cases should be treated as provisional and worth periodically re-pulling for any case you're actively tracking or citing publicly.
