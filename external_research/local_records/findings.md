# County/State Public Records Research — Data Center BLM Projects (NV/WY/AZ)

Research conducted 2026-09-09. Covers five tasks in priority order per assignment. All source URLs and dead-end queries are logged in the "Search Log" section at the end of each task and in the master log at the bottom.

---

## HEADLINE FINDINGS (real corporate parent names distinct from the BLM-filing LLC)

1. **"Copia GDC, LLC" (BLM applicant, Monarch Data Center, Sierra Front FO, NV) = "Copia Power DevCo, LLC" at the county level, itself the Nevada arm of "Copia Power," a Salt Lake City–based energy/data-center developer.** Copia Power is publicly reported as backed by global private-equity firm **Carlyle**. This is confirmed by a primary document: the Lyon County Planning Commission (July 14, 2026) and Board of County Commissioners (August 6, 2026) agenda packets for case **PLZ-2026-041**, both naming "Copia Power Devco, LLC" as applicant for the Monarch Data Center rezoning (APNs 014-201-07 and 014-201-30, 505.40 acres). Downloaded to `documents/lyon-county-monarch/`.
2. **The same "Copia Power" entity is also the applicant, under the name "Copia Power," for a Maricopa County, Arizona rezoning case for the "Belmont Energy Center"** — a planned 30,000-acre "digital and power infrastructure campus" in the Harquahala Valley west of Phoenix (~3,100 acres in the immediate rezoning request; ~2,860 ac solar, ~320 ac gas/BESS/data center). This is the same geographic area (Harquahala Valley) and the same corporate family as the BLM's "Copia Digital, LLC" filings for Frontier, Harquahala, and TAP Data Centers (Lower Sonoran FO). Exact 1:1 parcel correspondence between the Maricopa County case and the specific BLM ROW case boundaries was **not confirmed** from the sources reviewed — treat as strong circumstantial linkage, not a proven match.
3. **Wyoming Hyperscale White Box LLC's founder, Trenton Thornock, has rebranded/expanded the company as "Prometheus Hyperscale."** Multiple outlets (Data Center Dynamics, Data Center Frontier) describe Prometheus Hyperscale as the successor entity that "expands upon the footprint and the promise of the Wyoming Hyperscale White Box project." Prometheus Hyperscale is itself already in the project dataset as a separate applicant (WYWY106720454/455/456, filed 2025-02-18) — meaning two entries in the original BLM case list likely trace back to the same founder/company at different stages of growth.

An **unconfirmed, unverified lead** surfaced in a secondary (AI-generated) search summary — not corroborated against a primary source in the time available — claiming a company called "Skylar" amended a solar-facility BLM right-of-way into a data center with BLM approval "in June" without environmental review. This closely parallels the well-documented Townsite Data Center pattern (a different, confirmed applicant) and may be a conflation by the search tool rather than a fact about Skylar Opportunities LLC. **Flagging for the researcher to verify directly rather than citing as fact.**

---

## Task 1 — Nevada GOED data center tax-abatement board meetings

**Method:** Downloaded and full-text-searched (via `pdftotext -layout`, not just AI summarization) five GOED board agendas/minutes spanning the requested 2024–2026 window, plus GOED's public "Data Center Tax Abatements" fact sheets, saved to `documents/goed-board-meetings/`:
- `1.-Agenda-February-6-2025.pdf`
- `3.-GOED-Board-Meeting-Minutes-November-14-2024.pdf`
- `4.-GOED-Board-Meeting-Minutes-May-8-2025.pdf`
- `3.-GOED-Board-Meeting-Minutes-November-10-2025.pdf`
- `GOED-Board-Meeting-Minutes-February-5-2026-FINAL.pdf`
- `Data-Center-2025.pdf`, `Data-Center-2026.pdf`, `Tax-Abatements-Overview-MAR2024.pdf`

**Result: NONE of the eight target projects/entities appear in any GOED board agenda or minutes reviewed.** Grepping full extracted text for "Skylar," "Copia," "On The Mark," "Silver Springs," "Moorman," "Kimberly Mountain," "Dayton North," "Meadowlark," "Townsite," and "Sandy Valley" across all five board-meeting PDFs returned zero matches for any of the eight.

The only data center abatement applicants that DID appear before the GOED Board in this window were, in all cases, **in Storey County** (the Tahoe-Reno Industrial Center area near Reno) — unrelated to any of the eight target projects:
- **Vantage Data Centers NV12, LLC** — approved Nov. 14, 2024 (data center sales tax + personal property tax abatement)
- **CADC Reno 265, LLC** — on the Feb. 6, 2025 agenda (data center sales tax abatement)
- **PR TX 1, LLC** — approved Nov. 10, 2025 (100-MW data center, Storey County)
- **SV RNO** — approved Feb. 5, 2026 (200-MW data center, Storey County)

This negative finding is corroborated by independent reporting: The Nevada Independent's investigative piece ("Nevada is reviewing its data center tax breaks — but counties are out of the loop") states explicitly that **data center tax breaks have only ever affected local governments in three counties: Clark, Washoe, and Storey** — meaning Lyon County (Silver Springs/Dayton/Monarch cluster), White Pine/Elko County (Meadowlark), and the rest of the target list have **not** had a GOED data-center abatement application reach the Board, at least as of that article's reporting (accessed Sept. 2026). The same article and a companion Nevada Independent piece ("Nevadans get few details into data centers receiving tax breaks — and it might be illegal") document that GOED refuses to release audit data on prior abatement recipients, claiming they aren't public records — Nevada Independent's outside experts dispute this — and that 12 of Nevada's 17 counties say GOED never engaged them on the tax-break review, with Elko County Commissioner Rex Steninger quoted: "I don't think they've ever asked us."

**Separately (county-level, not GOED):** Lyon County itself is now in the middle of a live, high-profile zoning fight over the "Monarch Data Center," filed with Lyon County as applicant **"Copia Power DevCo, LLC"** (real estate/corporate name behind BLM applicant Copia GDC, LLC — see Headline Findings). Key facts, downloaded as primary documents to `documents/lyon-county-monarch/`:
- Case **PLZ-2026-041**: PUD zone change on 505.40 acres (APNs 014-201-07, 014-201-30), 4.6 million sq ft, 1,000 MW total (500 MW BESS + 500 MW gas backup), 8 buildings up to 95 ft.
- Lyon County Planning Commission recommended approval 4–3 on **July 14, 2026** (Commissioners Loomis, Irvin, and Allan dissenting).
- Lyon County Board of County Commissioners approved the rezone 3–1 on **August 6/7, 2026** (Commissioner Hockaday opposed; Commissioner Cassinelli abstained, citing a conflict of interest).
- Still required: final design approval, Nevada Division of Environmental Protection clearance, State Engineer (water rights) approval, and completion of land purchase.
- Walker River Paiute and Yerington Paiute tribes passed resolutions opposing the project.
- Amid public backlash over data centers generally, **Lyon County commissioners approved a moratorium on new data center, BESS, and commercial solar applications on July 23, 2026, running through January 22, 2027** (while the county drafts a dedicated data center ordinance) — this moratorium post-dates the Monarch approval and would not retroactively affect it, but would bar new applications for the Silver Springs cluster or Dayton North (Sierra Front FO, all still "Pending" per BLM records) during that window.
- Two Microsoft-affiliated NV Energy substations (Nighthawk, 32.59 ac; RNO18, 18.70 ac) received Lyon County conditional-use-permit approval March 5, 2026, north of US-50 in Silver Springs — these are described in press coverage as Microsoft-affiliated grid infrastructure in the same immediate area as the Silver Springs/Dayton BLM data-center cluster, though no source reviewed directly ties them to the specific Moorman Ridge/Silver Springs South/Kimberly Mountain Data BLM applicants by name.

**Documents downloaded:**
- `documents/lyon-county-monarch/planning-commission-2026-07-14-agenda.pdf` (full 289-page packet, ~80 MB)
- `documents/lyon-county-monarch/bocc-2026-08-06-agenda.pdf` (full packet with attachments, ~272 MB)
- `documents/lyon-county-monarch/pc_first15.txt`, `bocc_first20.txt` (text extracts confirming the Copia Power DevCo, LLC applicant name and case number, for quick reference without opening the full packets)
- `documents/goed-board-meetings/*.pdf` and matching `*.txt` extracts (all five board minutes/agenda + fact sheets)

---

## Task 2 — Wyoming Hyperscale White Box LLC build status

**Correction to task assumption:** the facility is **not** in Lincoln County — it sits southeast of **Evanston, in Uinta County, Wyoming** (near Aspen Mountain), though it is served administratively by BLM's Kemmerer Field Office, which covers a multi-county area including both Lincoln and Uinta counties. Separately, Lincoln County (Kemmerer) has recently amended its own zoning code to require future data center proposals to go before its Planning Commission and Board of Commissioners — but as of the most recent reporting found, **no data center project is currently proposed within Lincoln County itself.**

**Build status: strong evidence the original small-scale facility was built and reached at least an initial operating phase**, based on:
- Data Center Frontier (Nov. 2022): Wyoming Hyperscale White Box was "under construction" on 58 acres of Thornock family ranchland on Aspen Mountain, southeast of Evanston; fiber via the Union Pacific Railroad line; a 138 kV substation fed by the same switchgear as nearby renewable generation; a 30-MW first phase targeted to begin commissioning in 2023.
- The BLM access-road (9.5 ac) and water-facility (0.7 ac) ROW cases for Wyoming Hyperscale White Box LLC both closing "Case Closed" (not "without Action") on 2024-07-09 is consistent with normal completion of supporting-infrastructure permitting for an already-under-construction/newly-operating facility, rather than an abandonment.
- **Corporate continuity confirmed:** Wyoming Hyperscale White Box was rebranded by its founder/CEO Trenton Thornock into **Prometheus Hyperscale**, explicitly described by Data Center Dynamics as "the new corporate entity ... which expands upon the footprint and the promise of the Wyoming Hyperscale White Box project." Prometheus Hyperscale is a separate applicant already in the project dataset (three 2025 BLM filings — access road, telecom line, water pipeline — all in the Kemmerer/Rock Springs FO area).
- Prometheus Hyperscale's much larger successor project — a 506-acre, 1.25 GW (scaling to 5 GW) campus "east of Evanston" in Uinta County — received a unanimous Conditional Use Permit from the **Uinta County Board of Commissioners on June 16–18, 2026** (sources give both dates in different reports), following an industrial-subdivision rezone and unanimous Uinta County Planning & Zoning Commission recommendation on May 28, 2026. Fifteen conditions attached, including: construction must start within 5 years; annual water-consumption reporting for 10 years post-commissioning; CFD heat-dispersal analysis within 90 days of operation; DarkSky lighting compliance; road-maintenance responsibility for County Roads 180 and 181; 60 dB noise cap; sales-tax situs designation in Uinta County.
- A related workforce-housing "man camp" (Target Hospitality, up to 3,400 workers, ~150 acres of county land near Bear River State Park, ~8 miles from the data center site) received a Uinta County Planning & Zoning conditional-use permit and was headed to the county commission as of late July 2026 — separately, TerraPower's Natrium nuclear reactor construction in Kemmerer (Lincoln County) has its own, unrelated workforce-housing approval process.

No source reviewed stated in so many words "the facility is now operational" (i.e., no explicit "now running" confirmation was found), but the weight of the corporate/permitting timeline strongly supports the original hypothesis that the small-scale White Box facility was built.

---

## Task 3 — Meadowlark Data Center East & West closure reason

**Result: essentially no public trace of this project outside BLM's own MLRS case records.** No county filings, no news coverage, and no explanation for the 2025-03-05 closures were found.

- Confirmed the BLM Bristlecone Field Office (where these two cases were filed) is part of the **Ely District**, covering **White Pine County** (plus Lincoln and a small part of Nye County) — this matches the task's assumption.
- Downloaded and full-text-searched White Pine County's own official "Natural Resource and Public Land Issues Tracking List" (as of April 13, 2026), prepared by the county's Principal Resource Specialist — a document specifically meant to track BLM/public-land matters affecting the county. **"Meadowlark" does not appear anywhere in this document.** The only Bristlecone Field Office item tracked is an unrelated rPlus Energies/rPlus Hydro pumped-storage hydrogeologic evaluation ROW (White Pine Waterpower, LLC) — not a data center. Saved to `documents/meadowlark-white-pine/tracking_list.pdf` (+ `tracking_list.txt` extract).
- White Pine County did enact a 180-day data center moratorium (Resolution 2026-18, approved July 22, 2026) "to give local officials time to establish dedicated land-use regulations" — but coverage of that moratorium (Ely Times/elynews.com) does not name any specific project, applicant, or reference the earlier 2025 BLM closures.
- General web searches for "Meadowlark Renewables Center LLC," "Meadowlark" + White Pine/Elko County, and "Meadowlark" + BLM/Ely District all returned nothing relevant. A company called "Meadowlark Renewables" does exist publicly, but it is an unrelated landfill-gas-to-renewable-natural-gas joint venture (Greenview Energy + Sparq Renewables) operating in **Reno County, Kansas** — a different state, different business, and almost certainly a different (coincidentally-named) entity; this should not be read as connecting to the Nevada BLM applicant.
- BLM's own ePlanning project-search UI and the general blm.gov FOIA/press-release search returned nothing for "Meadowlark" in Nevada.

**Bottom line:** the "Case Closed" / "Case Closed without Action" disposition on the same day for these two large parcels (4,035 acres combined) remains unexplained from public records. As the original project summary suggested, a direct BLM FOIA/records request to the Bristlecone Field Office (Ely, NV) appears to be the only way to get the reason — nothing about it has surfaced in any county or news source found.

---

## Task 4 — Nevada water rights (Silver Springs / Dayton / Townsite cluster)

**Method:** Nevada Division of Water Resources hosts an ASP.NET "Permit Search" tool (`https://tools.water.nv.gov/PermitSearch.aspx`) that searches water-right records by owner name, application number, or certificate number, plus an "Advanced/Hydrographic Abstract" tool for basin-level queries (`https://tools.water.nv.gov/Hydrographic.aspx`) and a groundwater-basin summary tool (`https://tools.water.nv.gov/UndergroundActive.aspx`).

I scripted owner-name searches (via direct HTTP POST replicating the form's ASP.NET postback, since the site returns 404/blocked content to normal fetch tools) for: Skylar Opportunities, Copia (and Copia alone), Moorman Ridge, Kimberly Mountain, Silver Springs South, Dayton North, On The Mark, Meadowlark, Prometheus Hyperscale, Rhea Data, Leo Data, Valar Atomics, and Townsite Solar. **Every query returned "0 items."**

**However, this negative result should be treated as inconclusive, not a confirmed absence of water-right filings.** When I ran the same script against well-known real entities that should plausibly appear (e.g., "Silver Springs Mutual Water Company," a real, long-established local water utility; single letters like "a" or "e" which should match large numbers of records if substring search were functioning) — those also returned "0 items." That strongly suggests my scripted form submission is not actually triggering the site's server-side search (the "0 items" Telerik grid appears to be the tool's default/unqueried state, not a true empty-result state), rather than proving zero real records exist. I was unable to fully reverse-engineer the site's AJAX/UpdatePanel postback mechanism in the time available.

**Recommendation:** a human researcher should manually run these searches directly in a browser at `https://tools.water.nv.gov/PermitSearch.aspx` (owner-name field) and `https://tools.water.nv.gov/Hydrographic.aspx` (by hydrographic basin — Dayton Valley and Churchill Valley/Carson Desert basins cover the Silver Springs/Dayton area) for the entity names above. This task could not be completed with confidence via automation and should be flagged as **not reliably answered** rather than answered negatively.

No independent news coverage was found discussing water-right applications specifically tied to these entity names, though general regional coverage (Nevada Current, "Data center water/power needs, regulatory challenges strain rural communities," Feb. 2026) discusses water stress in the broader Lyon County area without naming specific applicants, and the Monarch Data Center's Lyon County approval explicitly still requires future State Engineer (water rights) approval as an outstanding condition — confirming no water right has been granted to that project yet, at minimum.

---

## Task 5 — Arizona county entitlements (Lower Sonoran FO cluster + Lake Havasu FO / Leo Data Center)

- **Maricopa County**: Adopted new zoning rules in early December 2025 that, for the first time, formally define "data center" in the county code and restrict construction to designated industrial zones in unincorporated areas only (cities like Phoenix/Chandler have separate zoning authority). The article covering this (KJZZ) does not name Copia Power, Belmont Energy Center, Harquahala Valley, or any specific pending case.
- Separately, **Copia Power** (the Salt Lake City parent behind Copia Digital/Copia GDC — see Headline Findings) has filed a Maricopa County rezoning request for the **"Belmont Energy Center,"** described as part of a planned 30,000-acre "digital and power infrastructure campus" in the **Harquahala Valley**, about an hour west of Phoenix, near Tonopah. The immediate rezoning request covers ~3,100 acres (~2,860 ac utility-scale solar; ~320 ac gas generation/BESS/data centers). This is the same broad geography and same corporate family as the BLM's Frontier (798 ac), Harquahala (355 ac), and TAP (999 ac) Data Center filings by Copia Digital, LLC (Lower Sonoran FO, filed 2025-11-13) — but I could not confirm from sources reviewed whether "Belmont Energy Center" is the same specific parcel(s) as one, some, or none of the three named BLM cases, or a wholly separate, adjacent parcel within the same larger campus concept. No specific Maricopa County case number was found for this rezoning in the time available.
- **Mohave County**: Adopted new data-center zoning regulations (Board of Supervisors, unanimous vote Dec. 1 — year not fully confirmed from the source snippet, but context places it in the same Nov.–Dec. 2025 wave as Maricopa's) requiring public hearings and added scrutiny of water/power use before any data center can be approved. No source found ties this specifically to Leo Data LLC or names the Leo Data Center project.
- A BLM solar-energy program page referenced a **"Leo Solar"** project as one of several public solar-variance-area applications under review in Mohave County — this may or may not be related to (or a predecessor/companion filing to) the "Leo Data Center" BLM ROW case (AZAZ106782092, Leo Data LLC, Lake Havasu FO, filed 2026-01-30); I could not access the BLM solar-permitting page directly (403 error) to confirm applicant identity, acreage, or whether it's the same footprint. This is a lead worth following up directly at `https://blmsolar.anl.gov/news/arizona/`.
- No county planning-commission agenda, staff report, or news coverage was found that names Frontier Data Center, Harquahala Data Center, TAP Data Center, or Leo Data Center by their exact BLM case names at the county level. Given that Boulder City/Townsite Data Center reporting (see adjacent finding below) shows developers explicitly shifting projects from city/county-zoned land onto BLM land specifically to avoid municipal zoning review, it's plausible some or all of these Arizona BLM parcels are wholly within federal land not subject to county zoning jurisdiction at all — which would explain the absence of county-level case records, as opposed to those records simply not having been found.

**Adjacent finding, not part of the original 8-project list but relevant context on the "BLM land as end-run around local zoning" dynamic:** Townsite Solar 2, LLC withdrew its separate application to the City of Boulder City for essentially the same data center project, instead expanding onto the adjacent, already-approved federal BLM parcel — reported by Nevada Current, 8NewsNow, and others (July 2026) as the developer moving from city-owned to federal land specifically because BLM approved the ROW amendment without new environmental review, while the city had been resisting. A federal appeals board (IBLA) reportedly halted the BLM approval on Sept. 1, 2026, finding BLM likely violated NEPA by relying on a review of a "previously approved but materially different project." This is documented in existing project files elsewhere in this repo (`documents/townsite-data-center/`) and is noted here only because it directly illustrates the same BLM-vs-county jurisdictional dynamic relevant to interpreting the AZ cluster's lack of county records.

---

## Master Search Log (all queries and URLs, including dead ends)

### WebSearch queries run
1. `Nevada GOED Board of Economic Development data center abatement 2025 agenda`
2. `goed.nv.gov board meeting minutes data center tax abatement`
3. `Nevada Governor's Office of Economic Development Lyon County data center abatement`
4. `Lyon County Nevada Planning Commission Monarch Data Center zoning agenda July 2026`
5. `"Copia Power DevCo" Nevada`
6. `Lyon County Nevada data center moratorium Silver Springs Dayton North planning commission`
7. `"Skylar Opportunities" Nevada GOED tax abatement OR "data center"` — no results
8. `"Copia GDC" OR "Copia Digital" OR "Copia Power" GOED Nevada tax abatement board` — no direct results
9. `"On The Mark Data Center" Nevada GOED OR abatement OR Lyon County` — no results
10. `"Meadowlark" data center Nevada White Pine OR Elko county` — no results (multiple follow-on auto-searches by the tool also came back empty)
11. `GOED board meeting agenda 2026 data center abatement Storey Clark Lyon`
12. `Nevada Division of Water Resources water rights application Silver Springs Dayton data center 2025` — no direct hits
13. `"Copia" OR "Moorman Ridge" OR "Kimberly Mountain" OR "Silver Springs South" water right application Nevada state engineer` — no direct hits
14. `Maricopa County OR La Paz County Arizona zoning data center Frontier Harquahala TAP Copia Digital`
15. `Mohave County Arizona Leo Data Center zoning Lake Havasu BLM` — no direct hits on Leo Data Center
16. `"Wyoming Hyperscale" data center Kemmerer Lincoln County built operational`
17. `"White Box" data center Wyoming Kemmerer`
18. `Lincoln County Wyoming planning commission data center permit Kemmerer`
19. `"Aspen Mountain" hyperscale data center Evanston Uinta County Wyoming permit built`
20. `Uinta County Wyoming planning commission Wyoming Hyperscale White Box permit`
21. `Trenton Thornock Wyoming Hyperscale White Box operational 2023 2024 data center running`
22. `"Frontier Data Center" OR "Harquahala Data Center" OR "TAP Data Center" Copia Digital Arizona BLM`
23. `"Leo Data Center" Arizona Mohave OR La Paz county BLM` — no direct hits (found "Leo Solar" instead)
24. `BLM "Leo Solar" Mohave County Arizona variance area data center public comment` — **blocked: session WebSearch budget (200/200) exhausted mid-query; no results returned**

### WebFetch URLs visited (including failures)
- `https://goed.nv.gov/notices-and-agendas/goed-board-meeting/` — fetched but unreadable via AI summarizer (binary-heavy); re-fetched via curl instead (below)
- `https://thenevadaindependent.com/article/nevadans-get-few-details-into-data-centers-receiving-tax-breaks-and-it-might-be-illegal` — read successfully
- `https://lasvegassun.com/news/2026/aug/07/nine-companies-secure-tax-breaks-while-promising-m/` — **HTTP 402 Payment Required**, could not read
- `https://www.carsonnow.org/07/10/2026/lyon-county-leaders-face-public-pushback-amid-surge-in-data-center-and-energy-development` — read successfully (key source)
- `https://goed.nv.gov/wp-content/uploads/2025/08/4.-GOED-Board-Meeting-Minutes-May-8-2025.pdf` (and 3 sibling minutes PDFs, and 2 fact-sheet PDFs) — fetched via WebFetch first (unreadable, binary PDF stream), then downloaded + `pdftotext`'d directly (successful, see documents folder)
- `https://thenevadaindependent.com/article/a-massive-data-center-in-rural-nevada-is-one-step-closer-to-being-built` — read successfully
- `https://nevadacurrent.com/2026/02/09/data-center-water-power-needs-regulatory-challenges-strain-rural-communities/` — **HTTP 403 Forbidden**, could not read
- `https://thenevadaindependent.com/article/nevada-is-reviewing-its-data-center-tax-breaks-but-counties-are-out-of-the-loop` — read successfully (key source: 3-county limitation quote)
- `https://eplanning.blm.gov/eplanning-ui/search?keyword=Meadowlark&type=project` — 404
- `https://eplanning.blm.gov/eplanning-ui/project/search?keyword=Meadowlark` — 404
- `https://elynews.com/2026/07/30/joint-white-pine-county-commission-road-commission-and-liquor-board-meeting/` — read successfully
- `https://www.whitepinecounty.net/DocumentCenter/View/13451/8f` (Natural Resource and Public Land Issues Tracking List) — downloaded and text-extracted directly
- `https://www.datacenterfrontier.com/hyperscale/article/21437203/wyoming-hyperscale-the-future-of-the-data-center` — read successfully
- `https://www.datacenterdynamics.com/en/news/wyoming-hyperscale-becomes-prometheus-hyperscale-reveals-pipeline-of-four-additional-sites/` — **HTTP 403 Forbidden**, could not read directly (summary obtained only via WebSearch snippet)
- `https://wyofile.com/uinta-county-data-center-moves-forward/` — read successfully
- `https://cowboystatedaily.com/2026/07/28/nuclear-and-data-center-man-camps-in-neighboring-counties-take-next-steps/` — read successfully
- `https://water.nv.gov/index.php/water-rights` — read successfully (identified the three search tool URLs)
- `https://www.abc15.com/news/business/copia-power-seeks-rezoning-for-3-100-acre-solar-and-data-center-project-near-phoenix` — read successfully (key source: Belmont Energy Center)
- `https://www.landdesk.org/p/the-big-data-center-buildup-comes` — paywalled, only headline/byline/caption accessible
- `https://blmsolar.anl.gov/news/arizona/` — **HTTP 403 Forbidden**, could not read
- `https://www.kjzz.org/business/2025-12-11/maricopa-county-is-the-latest-arizona-government-to-set-up-data-center-zoning-rules` — read successfully
- `https://www.mohavecounty.us/ContentPage.aspx?id=95&cid=1553` — **HTTP 403 Forbidden**
- `https://www.maricopa.gov/3735/Zoning-Ordinance` — **HTTP 404 Not Found**
- `https://pizenswitchtimes.com/2025/11/25/december-4-2025-lyon-planning-commission-to-address-monarch-data-center-request-for-mason-valley-rezoning/` — read successfully (agenda links extracted)
- `https://www.lyon-county.org/AgendaCenter` — read successfully twice (agenda-date listing, then targeted link extraction)
- `https://www.blm.gov/foia` — 404
- `https://eplanning.blm.gov/eplanning-ui/search` — 404

### Direct downloads via curl + pdftotext (bypassing WebFetch's binary-PDF limitation)
- All GOED board agenda/minutes/fact-sheet PDFs (8 files) → `documents/goed-board-meetings/`
- White Pine County land-issues tracking list → `documents/meadowlark-white-pine/`
- Lyon County Planning Commission (7/14/26) and BOCC (8/6/26) full agenda packets → `documents/lyon-county-monarch/`

### Nevada water-rights database scripted search (see Task 4 for full caveat)
- Tool: `https://tools.water.nv.gov/PermitSearch.aspx` (ASP.NET/Telerik RadGrid, owner-name field)
- Queried names: Skylar Opportunities, Copia, Moorman Ridge, Kimberly Mountain, Silver Springs South, Dayton North, On The Mark, Meadowlark, Silver Springs, Silver Springs Mutual, Vantage Data Centers, Sandy Valley Mining, Prometheus Hyperscale, Rhea Data, Leo Data, Valar Atomics, Townsite Solar, Microsoft, NV Energy, Smith, Walker River, Data Center, Google, SILVER, COPIA, "a", "e" — **all returned "0 items"**, including well-known control entities, indicating the automated form submission likely never triggered a real server-side query (see Task 4 caveat). Manual browser-based follow-up recommended.

## Next steps

No CAPTCHAs specifically blocked this workstream, but several sources need a human either because automation genuinely can't drive them, or because they're paywalled/geofenced rather than bot-blocked:

1. **Nevada water rights (Task 4) — needs a human at a real browser, not more scripting.** Go to `https://tools.water.nv.gov/PermitSearch.aspx`, type each of these into the owner-name field by hand, and note any hits: Moorman Ridge Data, Silver Springs South, Kimberly Mountain Data, Dayton North, On The Mark Data Center, Skylar Opportunities, Copia (and Copia Power), Sandy Valley Mining Energy & Compute, Townsite Solar 2, Meadowlark Renewables Center. Also try the hydrographic-basin tool (`https://tools.water.nv.gov/Hydrographic.aspx`) for the Dayton Valley and Churchill Valley/Carson Desert basins. This is the single highest-value manual follow-up in this file — the automated attempt could not even confirm the search form was firing.
2. **`blmsolar.anl.gov/news/arizona/`** (403 to automated fetch) — a human visiting directly in a normal browser may get through; this is the only lead on whether "Leo Solar" is connected to Leo Data Center.
3. **`lasvegassun.com`** article on nine companies securing NV tax breaks — returned HTTP 402 Payment Required to automated fetch; a human with a Las Vegas Sun subscription (or via a library database) could check whether any of our target entities are named.
4. **`nevadacurrent.com`**'s Feb. 2026 water/power stress article — returned 403 to automated fetch; worth a manual re-check, since Nevada Current usually isn't paywalled and this may just be bot-blocking.
5. **Maricopa County exact case number for "Belmont Energy Center"** — not found via search; a call or records request to Maricopa County Planning & Development would confirm whether it overlaps the BLM Frontier/Harquahala/TAP parcels or is a separate, adjacent site.
6. **BLM Bristlecone Field Office (Ely, NV) FOIA request** for the Meadowlark Data Center East/West closure reason — remains the only path, per both this workstream and news/press.
