# Nevada Corporate Ownership Research — BLM Data Center ROW Applicants

**Research date:** 2026-09-09
**Researcher:** Claude (agent session), for Center for Western Priorities
**Scope:** 10 Nevada-registered LLCs that filed BLM right-of-way applications for data-center-related projects (see `PROJECT_SUMMARIES.md` and `data_center_row_cases.csv` for BLM case context).

---

## CRITICAL LIMITATION — READ FIRST

**The Nevada Secretary of State's entity-search systems (SilverFlume, at `nvsilverflume.gov`, and the underlying search portal at `esos.nv.gov/EntitySearch/OnlineEntitySearch`) were unavailable for the entire duration of this research.** Every direct attempt (multiple retries, at different times, via both direct browser navigation and WebFetch) returned the same "Nevada Secretary of State | Scheduled Maintenance" page.

A web search confirmed why: **the State of Nevada took SilverFlume and its replacement system, ORION, offline for a planned, multi-day cutover starting 5:00 PM Wednesday, September 9, 2026 (today), with ORION scheduled to come back online at 5:00 AM Monday, September 14, 2026.** Phase 2 of the ORION Business Portal (replacing SilverFlume entirely, including Business Licensing, Marks, and Notary services) was set to launch September 14, 2026. During the outage window, the state's own guidance was that filings could only be submitted via fax, email, mail, or in-person — i.e., there was no way to query the entity database at all, by any method, during this window.

**Practical consequence: none of the specific facts SilverFlume would normally provide — entity/NVID number, exact formation/registration date, registered agent name and address, manager/officer listing, principal business address, or current status — could be obtained for ANY of the 10 target entities.** I could not download any Articles of Organization or Annual List PDFs from SilverFlume for the same reason. This is a hard blocker caused by the state system being down, not a search failure — see the full search log below for every attempt made.

I also attempted several third-party alternatives, with the following results:
- **opengovus.com** — accepts a "company=" query parameter but the results returned were **not actually filtered** by the query (they returned generic/unrelated Nevada LLCs dated 2021 regardless of the search term). Not usable as a data source; discarded.
- **bizapedia.com** — blocked by a "Human Verification" CAPTCHA challenge on first navigation. I do not attempt to bypass CAPTCHAs, so this source was not pursued further.
- **opencorporates.com** — blocked by an "HAProxy Challenge" (CAPTCHA) on direct navigation. Same rule applied; not pursued. Indirect results via Google/WebSearch of opencorporates.com did not surface any of the 10 target entities.
- **nevada-register.com** — returned HTTP 503 ("no available server") on every attempt, both via browser and WebFetch.
- **Wayback Machine** — one snapshot of the SilverFlume search *form* exists (2026-08-29), but the entity search is a dynamic, session-based POST query; a cached snapshot of the blank form does not yield any entity-specific data, and I did not pursue it further since it could not answer the actual questions.

Given all of the above, this report is built from **public documents other than SilverFlume** — BLM/NDOW/GOED/Nevada Dept. of Taxation filings, news coverage, and industry trackers — that happened to name real people, parent companies, or related entities. Where a fact below is not sourced to SilverFlume, that is because SilverFlume could not be reached at all during this research window. **Every unresolved data point is marked "Not found" or "Could not access" rather than guessed.**

**Recommendation:** Re-run the SilverFlume/ORION entity search for all 10 names after September 14, 2026, 5:00 AM (when ORION is scheduled to be back online), to fill the gaps documented below.

---

## Summary — Key Questions

### 1. Do Moorman Ridge Data LLC, Silver Springs South LLC, and Kimberly Mountain Data LLC (same filing date 2025-02-03, same BLM field office — Sierra Front) share a registered agent, manager, or business address?

**Confidence: No evidence (not "no relationship" — simply unresolved).** SilverFlume, which is the only source that would show registered agent/manager/address, was inaccessible. No news source, GOED/NDOW filing, or other public document reached names any of these three LLCs directly. The only suggestive circumstantial evidence is (a) their shared filing date and field office, (b) contiguous acreage in the same "Silver Springs" cluster (see PROJECT_SUMMARIES.md), and (c) the fact that a major, well-documented data center developer — **Tract** (Tract Capital Management / Fleet Data Centers, founded by Grant van Rooyen) — is independently reported to have closed on ~1,060 acres near Silver Springs in Lyon County in 2026 following rezoning. That acreage figure is close to, but does not exactly match, any single one of the three BLM parcels (1,160 ac / 1,117 ac / 680 ac) or their ~2,957-acre combined total, and no news source found named "Moorman Ridge," "Silver Springs South," or "Kimberly Mountain Data" as Tract entities. **This is suggestive but NOT confirmed** — it should be treated as a lead to verify once SilverFlume is back online (check whether Tract or an affiliate is the organizer/manager on any of these three LLCs' Articles of Organization) and by pulling the Lyon County memorandum-of-option filings referenced in the Nevada Independent's "No land? No problem" explainer.

### 2. Does Dayton North LLC share a registered agent/address with the Silver Springs entities?

**Confidence: No evidence.** Same blocker as above — SilverFlume inaccessible, and no secondary source names Dayton North, LLC specifically. Its 0.0-acre "placeholder" filing (per PROJECT_SUMMARIES.md) on the same date/office as the other three is suggestive of a shared master project, but this is speculation, not a documented fact.

### 3. Is Copia GDC, LLC's registered agent/address the same as "Copia Digital, LLC"?

**Confidence: Suggestive (not confirmed via SilverFlume, but strongly corroborated independently).** SilverFlume could not be checked for a literal registered-agent match. However, independent news reporting (The Nevada Independent, Aug. 2026; Connect CRE; DataCenterDynamics; NVBEX) **directly and unambiguously ties "Copia GDC, LLC"'s BLM project ("Monarch Data Center," NVNV106758167) to Copia Power**, a data-center/energy developer founded in 2021, backed by the private equity firm **Carlyle**, that already operates roughly 750 MW of existing energy-generation assets mostly in the Western U.S. Separately, the Nevada Department of Wildlife's Energy Review Program applicant log (public PDF, saved in this research — see `_shared_reference/`) shows **"Copia Power" as the applicant of record** on at least five other Nevada energy projects (Sawtooth Clyde Solar, Sawtooth Tromso Solar, Vlahakis Energy Center Solar BESS, Bergen BESS, Reine BESS, 2023–2024), plus a related shell name **"Sawtooth DevCo LLC"** (Amphibole Solar, Amended Reine BESS). This establishes that "Copia" is an active, multi-entity corporate family in Nevada using project-specific LLC names — consistent with "Copia GDC, LLC" and "Copia Digital, LLC" (the AZ/ID/OR/WY filer) being sibling entities of the same parent, but no document was found that states this explicitly for the name "Copia Digital." Treat as suggestive/likely, not confirmed.

### 4. Sandy Valley Mining Energy & Compute LLC — mining company, crypto-mining operation, or data center developer?

**Confidence: No evidence — could not determine.** No SilverFlume record, no news coverage, no GOED/NDOW filing, and no web presence at all was found for "Sandy Valley Mining Energy & Compute LLC" beyond the BLM ROW case itself (NVNV106836647, access road to the Goodsprings mining district, filed 2026-05-20). The entity appears to have essentially no public footprint outside the BLM filing. The name itself is ambiguous exactly as flagged in PROJECT_SUMMARIES.md — "Mining Energy & Compute" could describe a co-located crypto-mining/compute operation, a conventional mining company that also does off-grid compute, or a data-center developer using deliberately vague naming. Nothing found here resolves that ambiguity either way. This is a strong candidate to re-check once SilverFlume is back up, since the entity's stated NRS business purpose (visible on the Articles of Organization) would likely settle the question.

---

## Entity-by-entity findings

### 1. Moorman Ridge Data, LLC
*(files BLM ROW as "Silver Springs North Data Center," case NVNV106717444, 1,160 ac, Sierra Front FO, filed 2025-02-03)*

- **SilverFlume record:** Could not access — see Critical Limitation above. No entity number/NVID, formation date, registered agent, manager, principal address, or status could be determined.
- **Documents:** None obtained. Folder created at `documents/moorman-ridge-data-llc/` but is empty — no Articles of Organization or Annual List could be downloaded.
- **Alternate sources checked:** WebSearch for `"Moorman Ridge Data, LLC" Nevada` returned only geographic references to the real "Moorman Ridge" landform in White Pine County (unrelated to the LLC) and the Shellback Wilderness. No corporate or news hits. opengovus.com's "Moorman Ridge Data" search page returned unrelated, unfiltered generic NV LLC listings (site's search does not actually filter by query — discarded as unreliable).
- **Possible connection to Tract Capital Management / Fleet Data Centers:** Tract is independently reported (Tract.com press release, DataCenterDynamics, Baxtel) to have closed on ~1,060 acres near Silver Springs, Lyon County, following rezoning, with total Greater Reno portfolio over 12,500 acres. No source names Moorman Ridge Data LLC as a Tract entity. **Not found / unconfirmed.**

### 2. Silver Springs South, LLC
*(BLM case NVNV106717439, 1,117 ac, Sierra Front FO, filed 2025-02-03)*

- **SilverFlume record:** Could not access. No NVID, formation date, agent, manager, address, or status obtained.
- **Documents:** None obtained; folder `documents/silver-springs-south-llc/` created but empty.
- **Alternate sources checked:** WebSearch for `"Silver Springs South, LLC" Nevada registered agent` surfaced only an unrelated Delaware-formed "Silver Springs 181 Venture, LLC" and generic registered-agent-service marketing pages — no match. Same Tract Capital Management circumstantial note as above applies (not confirmed).

### 3. Kimberly Mountain Data, LLC
*(files BLM ROW as "Silver Springs West Data Center," case NVNV106717442 main + NVNV106802346 geotech, Sierra Front FO, filed 2025-02-03 / 2026-05-06)*

- **SilverFlume record:** Could not access. No NVID, formation date, agent, manager, address, or status obtained.
- **Documents:** None obtained; folder `documents/kimberly-mountain-data-llc/` created but empty.
- **Alternate sources checked:** WebSearch returned only unrelated hits for the historic mining ghost towns "Kimberly, Nevada" and "Kimberly, Utah," plus generic OpenCorporates/knowledge-base pages with no entity match. No news coverage found under this name.

**Cross-entity note for #1–#3:** No source accessed in this session shows a shared registered agent, manager, or address among these three. This should be re-tested directly against SilverFlume once it is back online — that is the only source that would show this definitively.

### 4. Dayton North, LLC
*(BLM case NVNV106717443, filed 2025-02-03, Sierra Front FO, 0.0 acres on file)*

- **SilverFlume record:** Could not access. No NVID, formation date, agent, manager, address, or status obtained.
- **Documents:** None obtained; folder `documents/dayton-north-llc/` created but empty.
- **Alternate sources checked:** WebSearch for `"Dayton North Data Center" Nevada` and `"Dayton North, LLC" Nevada site:nevada-register.com OR site:bizapedia.com` returned only unrelated Dayton, NV businesses (Silver Dollar Records LLC, Mann Built Construction LLC, Dayton Valley Aquaponics LLC) — no match for the target entity. nevada-register.com itself was unreachable (HTTP 503) throughout.

### 5. On The Mark Data Center LLC
*(BLM cases NVNV106778200, 560 ac main + NVNV106802350, 4.05 ac geotech, Sierra Front FO)*

- **SilverFlume record:** Could not access. No NVID, formation date, agent, manager, address, or status obtained.
- **Documents:** None obtained; folder `documents/on-the-mark-data-center-llc/` created but empty.
- **Alternate sources checked:** WebSearch surfaced a **similarly-named but distinct California LLC, "ON THE MARK DATA LLC"** (no "Center" in the name), California entity number 202118811453, formed 2021-07-05, principal address 2108 N St Ste N, Sacramento, CA 95816, manager **Mark Freeman**, registered agent Northwest Registered Agent, Inc. **This is NOT confirmed to be the same entity or the same people as the Nevada "On The Mark Data Center LLC"** — the names differ (no "Center") and no document connects them. Flagging as a lead only, not a finding. Also found: industry tracker mentions of an "On the Mark Silver Springs Data Center" project with BLM-authorized geotechnical work June–August 2026, consistent with the BLM case data already in PROJECT_SUMMARIES.md, but no ownership detail beyond that.

### 6. Skylar Opportunities LLC
*(files BLM ROW as "Horizon Project (Data Center)" NVNV106774473 and "Skylar Opportunities Data Center & BESS" NVNV106360814 + geotech NVNV106714160, Las Vegas FO)*

- **SilverFlume record:** Could not access. No NVID, formation date, agent, manager, address, or status obtained.
- **Documents:** None obtained; folder `documents/skylar-opportunities-llc/` created but empty.
- **Corroborating public-record finding (source: NDOW Energy Review Program Application Summary, public PDF from ndow.org, saved at `documents/_shared_reference/NDOW_Energy_Review_Program_Application_Summary_2025-09.pdf`):** An entity named **"Skylar Opportinities LLC"** [sic — typo in the source table] is listed as the applicant for a "Skylar Opportunities BESS" project in Clark County, application received 10/18/2022. This confirms the entity (allowing for the typo) has an activity record with the state predating the BLM filings and is plausibly the same LLC.
- **Possible "Skylar" naming lineage (suggestive, not confirmed):** The same NDOW table shows an much earlier, clearly-related-by-name entity, **"Skylar Res[ources]. LP,"** as co-applicant (with KOWEPO America LLC) on the original 2013 "Townsite Solar Project" (180 MW, Clark County) — a **different and larger** solar project than "Townsite Solar 2, LLC" (see entity #9 below; do not confuse the two). Trade press (Solar Industry Magazine, PV-Tech, Switch/Capital Dynamics press release) confirms **Skylar Resources LP** acquired 100% of the development rights to the original 180 MW Townsite Solar project from KOWEPO America in 2015, developed it as "Skylar Townsite LLC," and sold the completed project to **Capital Dynamics** (a Swiss asset manager) in August 2019 as "the first acquisition of Rob Roy's Gigawatt Nevada." Skylar Resources LP does not appear to still control that original project. Whether "Skylar Opportunities LLC" (2022–present, our target entity) is organized/managed by the same principals as "Skylar Resources LP" / "Skylar Townsite LLC" (2013–2019) is **not established by any document found** — it is only a shared-naming-convention lead. **Confidence: no evidence of a direct corporate link, only a suggestive naming pattern.**

### 7. Copia GDC, LLC
*(files BLM ROW as "Monarch Data Center," case NVNV106758167, 120 ac, Sierra Front FO, filed 2025-10-22)*

- **SilverFlume record:** Could not access. No NVID, formation date, agent, manager, address, or status obtained.
- **Documents:** None obtained; folder `documents/copia-gdc-llc/` created but empty.
- **Strong independent confirmation of real developer:** Multiple news sources — The Nevada Independent ("A massive data center in rural Nevada is one step closer to being built," and "No land? No problem…"), DataCenterDynamics, Connect CRE, NVBEX, The Cool Down, Carson Now — all identify **Copia Power** as the developer of the "Monarch Data Center" project (505 acres core footprint per news reports vs. 120 ac recorded on the BLM ROW case — the news acreage describes the county-zoning footprint including private land, not the BLM parcel specifically; these are consistent with being the same overall project). Key facts from reporting:
  - Copia Power was founded in 2021, is backed by **Carlyle** (global private equity), and operates ~750 MW of existing energy-generation assets, mostly in the Western U.S.
  - The Monarch project is 4.6 million sq ft across 14 buildings, ~\$11 billion, 1,000 MW demand, in Mason Valley/Yerington, Lyon County. Copia holds an **option agreement** (not a purchase) on land owned by the Masini family, a local farming/ranching family — per Nevada Independent reporting, this is why there is "often a scant paper trail" on the underlying land, and no deed/ownership change would show up until the option is exercised.
  - Copia Power's projects at 150–155 Penrose Lane, Yerington, NV, per DataCenterMap listing.
  - The NDOW Energy Review Program applicant log (see `_shared_reference/`) independently shows "Copia Power" as applicant on five other NV projects (Sawtooth Clyde Solar, Sawtooth Tromso Solar, Vlahakis Energy Center Solar BESS, Bergen BESS, Reine BESS — 2023–2024) and a related shell, "Sawtooth DevCo LLC" (Amphibole Solar, Amended Reine BESS), confirming Copia's pattern of per-project entity naming in Nevada.
- **Relationship to "Copia Digital, LLC" (the AZ/ID/OR/WY filer):** Not confirmed via SilverFlume registered-agent match (inaccessible). Given the shared "Copia" brand and confirmed Copia Power / Carlyle backing behind Copia GDC's Nevada project, it is **plausible/likely** that Copia GDC, LLC and Copia Digital, LLC are sibling project-entities of the same Copia Power corporate family, consistent with the "one company, per-parcel shells" pattern flagged in PROJECT_SUMMARIES.md. **Confidence: suggestive, not confirmed** — the actual registered-agent/organizer match still needs to be pulled from SilverFlume directly.

### 8. Sandy Valley Mining Energy & Compute LLC
*(BLM case NVNV106836647, access road to Goodsprings mining district, 331.89 ac, Las Vegas FO, filed 2026-05-20)*

- **SilverFlume record:** Could not access. No NVID, formation date, agent, manager, address, or status obtained.
- **Documents:** None obtained; folder `documents/sandy-valley-mining-energy-compute-llc/` created but empty.
- **Business-purpose question:** **Could not determine.** No news coverage, GOED filing, NDOW filing, or web presence whatsoever was found for this entity beyond the BLM case itself. Multiple search variants (`"Sandy Valley Mining Energy & Compute"`, `"Sandy Valley Mining Energy and Compute"`, general "Sandy Valley Nevada mining crypto compute" searches) returned only unrelated historical mining-district content (Sandy Valley Mill, Goodsprings ghost town history). **This entity has essentially no public footprint outside its own BLM filing** — notably thinner even than the other nine entities in this dataset. This is worth flagging to the journalist as itself a data point: an entity this opaque, filing for a *mining district access road* under a name combining "Mining," "Energy," and "Compute," with zero public trace, is exactly the profile PROJECT_SUMMARIES.md already flagged as lower-confidence/ambiguous. Resolving whether it's crypto-mining, conventional mining, or data-center-adjacent will very likely require the SilverFlume Articles of Organization (which lists a stated business purpose under Nevada law) once the system is back online, or a BLM records request for the underlying ROW application narrative.

### 9. Townsite Solar 2, LLC
*(files BLM ROW as amendment to "Townsite Data Center," case NVNV105844791, amendment to ROW NVN-99875, 85 ac, Las Vegas FO; Authorized 2026-04-22)*

- **SilverFlume record:** Could not access. No NVID, formation date, registered agent, or current status confirmed via SilverFlume.
- **Ownership — confirmed via independent state document (Nevada Dept. of Taxation fiscal-impact note, public PDF, saved at `documents/townsite-solar-2-llc/NV_DOT_fiscal_impact_note_Townsite_Solar_2_LLC.pdf`, source: `energy.nv.gov/siteassets/content/programs/reta/Townsite_Solar_2_fiscal_note.pdf`):**
  > "The project, known as the Townsite Solar 2, LLC (TS2) is **wholly owned by William O. Perkins Revocable Trust with William O. Perkins III as Trustee**. The address is **5847 San Felipe, Suite 4450, Houston, TX 77057**."
  - Project detail from the same document: 35 MW solar PV + 167 MW BESS, 90,000 MWh/yr net production, expected commercial operation by April 30, 2026 (per this 2024 filing — note PROJECT_SUMMARIES.md records the BLM authorization for the *data-center repurposing* as issued 2026-04-22, i.e., after the original solar COD date, consistent with the project having been redirected from solar to data-center use before ever operating as solar).
  - Location: 166 acres total (APN 189-14-000-002 and 189-14-000-005, Clark County), 1.25 mi south of I-11/Route 93 interchange, on BLM land near the CTC BRQ quarry pit.
  - Local reporting (KUNC/Mountain West News Bureau / UPR, "This Nevada city rejected a data center, so the developer turned to federal land," 2026-07-22) independently confirms **Townsite Solar 2, LLC is Houston-based** and that Boulder City initially rejected the project when proposed within city limits — citing inadequate NEPA review, water-consumption concerns in a drought region, and the developer bypassing required consultation with the city (per Boulder City Attorney Brittany Walker) — after which "the developer subsequently moved the project to adjacent federal land," i.e., onto BLM land, to proceed without city approval. This corroborates and adds context to the BLM record.
- **Important disambiguation — do not confuse with the unrelated, larger "Townsite Solar" project:** A different, much larger (180 MW) "Townsite Solar" project in Boulder City was originally filed with NV PUCN in 2012 by KOWEPO America LLC (a subsidiary of Korea Western Power Co.), later acquired by **Skylar Resources LP** (as "Skylar Townsite LLC") in 2015, and ultimately sold to **Capital Dynamics** (Swiss asset manager) in August 2019 as the "first acquisition of Rob Roy's Gigawatt Nevada" (per Switch/Capital Dynamics press release, PV-Tech, Solar Industry Magazine). **This is a separate project with separate ownership from "Townsite Solar 2, LLC"** — the "2" in the name appears to denote an unrelated, later, smaller solar-plus-storage project on a different footprint, owned by the Perkins Revocable Trust, not by Skylar Resources/Capital Dynamics. Flagging this clearly because the naming similarity is a likely source of confusion given "Skylar Opportunities LLC" (entity #6 above) has its own separate "Skylar" naming coincidence.
- **Documents saved:** `documents/townsite-solar-2-llc/NV_DOT_fiscal_impact_note_Townsite_Solar_2_LLC.pdf` (24-page Nevada Dept. of Taxation renewable-energy partial-abatement fiscal note, dated 2024, includes the ownership statement above plus a 20-year property-tax abatement calculation). No SilverFlume Articles of Organization or Annual List could be obtained.

### 10. Meadowlark Renewables Center LLC
*(BLM cases NVNV106699494 "Meadowlark Data Center East," 3,026 ac, and NVNV106720896 "Meadowlark Data Center West," 1,009 ac, Bristlecone FO; both Closed 2025-03-05)*

- **SilverFlume record:** Could not access. No NVID, formation date, agent, manager, address, or status obtained.
- **Documents:** None obtained; folder `documents/meadowlark-renewables-center-llc/` created but empty.
- **Alternate sources checked:** Extensive WebSearch variants (`"Meadowlark Renewables Center LLC" Nevada`, `"Meadowlark Renewables" Bristlecone field office`, GOED/PUCN/energy.nv.gov site-restricted searches) found **no matches at all** for this specific entity. All hits were unrelated: "Meadowlark Solar, LLC" (an operating solar asset in the EIA database, different state), "Meadowlark Ecological Consulting, LLC" (Las Vegas federal contractor, ecological consulting — different business entirely), and "Meadowlark Renewables, LLC" (an unrelated landfill-methane project in Reno County, Kansas, with Greenview Energy/Sparq Renewables). **None of these appear to be the same entity as Nevada's "Meadowlark Renewables Center LLC."** This entity, like Sandy Valley Mining Energy & Compute LLC, appears to have essentially no public footprint beyond its own (now-closed) BLM filings — notable given both parcels were closed out administratively (one "Case Closed," one "Case Closed without Action," per PROJECT_SUMMARIES.md) without any public explanation found.

---

## Full search/access log (for retracing steps)

All within a single research session on 2026-09-09. "Browser" = interactive browser tool (renders JS); "WebFetch" = non-interactive fetch (no JS); "WebSearch" = search-engine query tool.

| # | Method | Query / URL | Result |
|---|--------|-------------|--------|
| 1 | Browser navigate | `https://esos.nv.gov/EntitySearch/OnlineEntitySearch` | "Nevada Secretary of State \| Scheduled Maintenance" page |
| 2 | Browser navigate | `https://www.nvsilverflume.gov/home` | Same maintenance page |
| 3 | Browser navigate | `https://esos.nv.gov/` (root) | Same maintenance page |
| 4 | Browser navigate | `https://esos.nv.gov/EntitySearch/OnlineEntitySearch` (retry) | Same maintenance page (confirms not a one-off glitch) |
| 5 | Browser navigate | `https://www.nvsos.gov` | Loads normally (main SOS site, not affected) |
| 6 | Browser find | "business search" link on nvsos.gov | Found link to `esos.nv.gov/EntitySearch/OnlineEntitySearch` (confirms that's the correct/only entry point, and it's down) |
| 7 | WebFetch | `https://esos.nv.gov/EntitySearch/OnlineEntitySearch` | Returned a bot-detection/JS-required notice (consistent with degraded/maintenance state) |
| 8 | WebSearch | `Nevada Secretary of State SilverFlume esos.nv.gov maintenance outage September 2026` | Confirmed planned outage: SilverFlume/ORION down 9/9/2026 5PM–9/14/2026 5AM for ORION Phase 2 cutover |
| 9 | WebSearch | `"Moorman Ridge Data, LLC" Nevada` | No entity match; only geographic/topo references |
| 10 | WebSearch | `"Silver Springs South, LLC" Nevada registered agent` | No match; unrelated Delaware LLC and generic RA marketing pages |
| 11 | Browser navigate | `https://opengovus.com/nevada-corporation?company=Moorman+Ridge+Data` | Loaded but returned unfiltered/generic 2021-dated NV LLC listings — search param not functioning; discarded as unreliable |
| 12 | WebSearch | `"Kimberly Mountain Data" LLC Nevada opengovus OR opencorporates` | No match; unrelated Kimberly, NV/UT ghost-town hits |
| 13 | WebSearch | `"Copia GDC" LLC Nevada opengovus OR opencorporates` | No direct entity match |
| 14 | WebSearch | `"On The Mark Data Center LLC" Nevada` | Surfaced unrelated CA entity "ON THE MARK DATA LLC" (b2bhint.com) and general Nevada data-center industry sites |
| 15 | Browser navigate | `https://bizapedia.com/company-search.aspx?q=Moorman+Ridge+Data` | Blocked by "Human Verification" CAPTCHA — not bypassed per operating rules |
| 16 | WebSearch | `opencorporates "Silver Springs South" Nevada LLC` | No match |
| 17 | WebSearch | `"Sandy Valley Mining Energy" Compute LLC Nevada` | No match; only historical Sandy Valley mining-district content |
| 18 | WebSearch | `"Townsite Solar 2, LLC" Nevada registered agent` | Surfaced NV Dept. of Taxation fiscal note naming Perkins Revocable Trust as owner (entity #9) |
| 19 | WebFetch | `energy.nv.gov/.../Townsite_Solar_2_fiscal_note.pdf` | Retrieved as binary PDF; read directly (24 pages) — full ownership/project detail extracted |
| 20 | WebFetch | `https://townsitesolar2.com/` | Company splash page; no ownership info, only "55MW Solar + 150MW BESS, Boulder City, July 2026" |
| 21 | Browser navigate | `https://nevada-register.com/search?q=Skylar+Opportunities` and homepage | HTTP 503 "no available server" both times |
| 22 | WebFetch | `https://www.nevada-register.com/1004837-skylar-consulting-llc` | HTTP 503 |
| 23 | WebSearch | `"Dayton North, LLC" Nevada site:nevada-register.com OR site:bizapedia.com` | No match |
| 24 | WebSearch | `"Copia GDC, LLC" nevada-register.com OR bizapedia.com OR nvsos` | No direct match; generic NV business-search marketing pages |
| 25 | Browser navigate | `https://bizapedia.com/...` (2nd attempt via search URL) | Same CAPTCHA block |
| 26-28 | WebSearch | repeat of #16-18 confirming consistency | Same results |
| 29 | WebSearch | `"Kimberly Mountain Data" LLC Nevada site:energy.nv.gov OR site:goed.nv.gov` | No match |
| 30 | WebSearch | `"Moorman Ridge Data" OR "Silver Springs South" OR "Kimberly Mountain Data" site:energy.nv.gov OR site:goed.nv.gov OR site:tax.nv.gov` | No match |
| 31 | WebSearch | `"Copia GDC" OR "Copia Digital" Nevada data center developer news` | Found extensive Copia Power / Monarch Data Center coverage |
| 32 | WebSearch | `Silver Springs Nevada data center Moorman Ridge Kimberly Mountain developer news` | Found Tract Capital Management's Silver Springs land acquisition (~1,060 ac) — no direct name match |
| 33 | WebFetch | `thenevadaindependent.com/.../no-land-no-problem...` | Article about Monarch/Copia Power's option-agreement land strategy; no target-LLC names found |
| 34 | WebFetch | `tract.com/news/tract-expands-its-greater-reno-portfolio...` | No LLC/subsidiary names given for land-holding entity |
| 35 | Browser navigate + get_page_text | Same Nevada Independent article (full manual read, double-checking WebFetch) | Confirmed: no target-LLC names present anywhere in full article |
| 36 | Browser navigate | `https://opencorporates.com/companies/us_nv?q=Moorman+Ridge+Data...` | Blocked by "HAProxy Challenge" CAPTCHA — not bypassed |
| 37 | Browser navigate | `https://esos.nv.gov/EntitySearch/OnlineEntitySearch` (3rd retry, later in session) | Still "Scheduled Maintenance" |
| 38 | WebFetch | `corporationwiki.com/search/results?q=Moorman+Ridge+Data+LLC` | Redirected to `corp.wiki`; not pursued further |
| 39 | WebSearch | `"On The Mark Data Center" LLC Nevada developer news Silver Springs` | Found "On the Mark Silver Springs Data Center" BLM geotech timeline; no ownership |
| 40 | WebSearch | `"Dayton North Data Center" Nevada` | No match |
| 41 | WebSearch | `"Meadowlark Data Center" Bristlecone Nevada developer` | Found unrelated Townsite Solar 2 and Sierra Nevada Ally articles |
| 42 | WebFetch | `upr.org/mountain-west-news-bureau/.../nevada-data-center-federal-land-blm` | Confirmed Townsite Solar 2, LLC Boulder City rejection/BLM-relocation narrative (entity #9) |
| 43 | WebFetch | `sierranevadaally.org/.../data-centers-nevadas-new-boom/` | HTTP 403 via WebFetch |
| 44 | Browser navigate + get_page_text | Same Sierra Nevada Ally URL | Loaded successfully; full article read — general context only, no target-LLC names |
| 45 | WebFetch | `archive.org/wayback/available?url=esos.nv.gov/EntitySearch/OnlineEntitySearch` | One snapshot exists (2026-08-29) of the search form; not pursued (dynamic search, no cached results possible) |
| 46 | WebSearch | `"Meadowlark Renewables Center" LLC Bristlecone solar wind 2024 2025 GOED OR PUCN` | No match; only unrelated Meadowlark Solar/Ecological Consulting/Kansas-methane hits |
| 47 | WebSearch | `"Sandy Valley Mining Energy & Compute" OR "Sandy Valley Mining Energy and Compute"` | No match at all |
| 48 | WebSearch | `"Skylar Opportunities" LLC GOED tax abatement application manager officer Nevada` | No direct match |
| 49 | WebSearch | `"ON THE MARK DATA LLC" California 202118811453 officers` | Confirmed CA entity details (Mark Freeman, Sacramento) — flagged as unconfirmed/likely-unrelated to NV entity |
| 50 | WebSearch | `"Copia GDC" LLC Nevada Secretary of State manager registered agent Reno` | No direct match; generic NVSOS how-to pages |
| 51 | WebSearch | `Skylar Resources LP KOWEPO America Townsite Solar Boulder City owner` | Found full Skylar Resources → Capital Dynamics acquisition history for the *original*, unrelated 180MW Townsite Solar project (entity #9 disambiguation) |
| 52 | WebFetch | `goed.nv.gov/wp-content/uploads/2026/04/30-Day-Notice-May-14-2026.pdf` | Retrieved and read (4 pages) — GOED board meeting notice; none of the 10 target entities listed |
| 53 | WebFetch | `ndow.org/wp-content/uploads/2025/09/AB307-Public-Summary-Table.pdf` | Retrieved and read (8 pages) — NDOW Energy Review Program applicant table; found "Skylar Opportinities LLC" [sic] and multiple "Copia Power"/"Sawtooth DevCo LLC" entries (entities #6, #7). Saved to `documents/_shared_reference/`. |

---

## Documents saved

- `documents/townsite-solar-2-llc/NV_DOT_fiscal_impact_note_Townsite_Solar_2_LLC.pdf` — Nevada Dept. of Taxation renewable-energy partial property-tax abatement fiscal note for Townsite Solar 2, LLC (2024), names the Perkins Revocable Trust as sole owner.
- `documents/_shared_reference/NDOW_Energy_Review_Program_Application_Summary_2025-09.pdf` — Nevada Department of Wildlife's public log of energy-project applicants statewide (2012–2025); referenced for Skylar Opportunities LLC and Copia Power cross-checks.
- All other entity subfolders (`moorman-ridge-data-llc/`, `silver-springs-south-llc/`, `kimberly-mountain-data-llc/`, `dayton-north-llc/`, `on-the-mark-data-center-llc/`, `skylar-opportunities-llc/`, `copia-gdc-llc/`, `sandy-valley-mining-energy-compute-llc/`, `meadowlark-renewables-center-llc/`) were created per the task instructions but **remain empty** — no Articles of Organization or Annual List documents could be obtained for these nine entities due to the SilverFlume/ORION outage.

## Next steps

### No human help needed (system outage should have cleared)
1. **Re-run this entire research task now that Nevada's ORION Business Portal cutover (2026-09-09 through 2026-09-14) has passed.** Search all 10 entity names directly at `https://esos.nv.gov/EntitySearch/OnlineEntitySearch` (or its ORION successor if the URL changed) and download the Articles of Organization / Annual List for each. This should resolve the majority of "Not found / Could not access" items above, especially the registered-agent/address cross-checks for entities #1–#4 (the Silver Springs cluster) and whether Copia GDC's registered agent matches Copia Digital's.

### Needs a human to solve a CAPTCHA (agents are instructed not to bypass these)
2. **bizapedia.com** — blocked by a "Human Verification" challenge on every entity search attempted (Moorman Ridge Data, and others). If you have a spare minute: go to `https://bizapedia.com/nv/`, solve the CAPTCHA, and search each of the 10 entity names in turn — Bizapedia often mirrors state registry data (registered agent, officers) even when the state site itself is unreachable.
3. **opencorporates.com** — blocked by an "HAProxy Challenge." Same ask: solve it once, then search each of the 10 names at `https://opencorporates.com/companies/us_nv` — OpenCorporates sometimes has historical filing data even for entities whose current SilverFlume record is thin.

### Needs a manual (non-CAPTCHA) records pull
4. **Sandy Valley Mining Energy & Compute LLC** and **Meadowlark Renewables Center LLC** have essentially zero public footprint beyond their own BLM filings. A BLM records/FOIA request for the underlying ROW application narratives (which typically include a project description and applicant contact) may be faster than SilverFlume, and would also help explain why both Meadowlark parcels were closed without public explanation.
5. **Silver Springs cluster (Moorman Ridge, Silver Springs South, Kimberly Mountain)** — a Lyon County Assessor/Recorder search for memoranda of option or deed records referencing these parcel names could name the actual developer even before/instead of SilverFlume, per the Nevada Independent's reporting on how option agreements work in this market.
6. **Copia GDC, LLC** — Lyon County's "Monarch Data Center Specific Plan" zoning-application file (already partially pulled by the local-records workstream, see `external_research/local_records/findings.md`) is public and may have additional detail on Copia GDC's corporate address not yet extracted.
