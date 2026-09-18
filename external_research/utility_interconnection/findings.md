# Utility Interconnection Research — Findings

**Note on provenance:** this file was written by the orchestrating session from the research subagent's final report, because the subagent's Write tool refused to create a file literally named `findings.md` (it appears to pattern-match that filename as an internal report file rather than a task deliverable). The subagent's detailed per-project match tables and full query-by-query log were not transferred with the final report and are not reproducible after the fact — only the headline findings and the verified downloaded documents below are preserved. If a full re-derivation of the search log is needed, this workstream should be re-run.

## Headline finding: Prometheus Hyperscale's main site is on private land, not BLM land

The flagship Prometheus Hyperscale campus (506 + 640 acres, near Evanston, Uinta County, WY, T15N R118W Sec 13) sits on **private land** — the Thornock family ranch — which is why no BLM "main site" ROW case exists. BLM's involvement is limited to the three infrastructure ROWs already in our MLRS dataset (access road, water pipeline, telecom line).

Confirmed scale, per Uinta County Conditional Use Permit approval, PR Newswire, and Cowboy State Daily coverage: **1.25 GW initial phase, development path to 5 GW**, roughly **$10 billion** in planned investment.

Critically, the company states this campus is a deliberately **islanded microgrid** — on-site natural gas generation plus carbon capture, with a future Oklo small modular reactor — built explicitly to have "no draw on the public utility grid, eliminating interconnection queue exposure." This explains why no PacifiCorp/Rocky Mountain Power interconnection filing exists for it: by design, there isn't one to find.

A separate, smaller, already-built predecessor at the same site — "Wyoming Hyperscale White Box" (the two BLM cases that closed 2024-07-09) — does appear, per trade press, to have an actual **120 MW Rocky Mountain Power contract**, distinct from the islanded flagship campus.

## Capacity figures found for other large projects

- **Valar Atomics (UT)** — no MW figure could be confirmed under the "Green River Gigasite" or "Raceway Gigasite" names specifically. Valar's own model is explicitly grid-independent (paired SMR). A real, unresolved discrepancy surfaced: most Green River-area nuclear/data-center news coverage actually names **Blue Castle Holdings / Fulcrum Point** (proposing 600–1,200 MW via Holtec SMRs) rather than Valar Atomics. This needs direct verification — it's possible these are two distinct, unrelated proposals in the same area, or that press coverage has conflated them.
- **Silver Springs cluster (NV)** — no utility-sourced MW figure. The closest match is for a likely-related-but-distinct "Monarch Data Center Campus" project in Yerington, reported in trade press at 150 MW (phase 1), gen-tied to NV Energy's Walker River Substation.
- **Townsite Data Center (NV)** — the strongest independent corroboration of any project in this dataset: multiple outlets cite **~150–170 MW**.

## Why utility queues mostly didn't help directly

NV Energy, PacifiCorp, Idaho Power, and the Arizona utilities (APS, Mohave Electric, UNS/AEPCO) **do not publish public, name-level large-load/data-center interconnection queues**. All four handle large-load requests through confidential bilateral/special-contract processes, disclosed publicly only in aggregate (e.g., in Integrated Resource Plan filings) or later, if and when a signed contract is docketed at a state PUC/PSC/ACC. Their FERC OASIS generator-interconnection queues are for power *generators*, not data-center *loads*, and returned no relevant matches. As a result, most project-level matches in this research came from trade press and third-party data-center trackers rather than utility documents themselves — labeled "possible/plausible," not "confirmed," throughout.

## No matches found at all for:

Dayton North Data Center, Meadowlark Data Center East & West, Sandy Valley Mining Energy & Compute, Jacqueline Data Center Project (WY), all four Arizona projects (Frontier, Harquahala, TAP, Leo Data Center), Falcon Data Center (ID), and Rhea Data LLC (ID).

## Documents downloaded (verified on disk)

- `documents/nv-energy/irp-2026-volume2.pdf` (+ `.txt` extract) — NV Energy 2026 Joint Integrated Resource Plan, Volume 2
- `documents/pacificorp/utah_psc_docket_2603505_application_2026-02-10.pdf` — Utah PSC docket application
- `documents/pacificorp/utah_psc_docket_2603505_redacted_testimony_pernichele_2026-03-03.pdf` — redacted testimony
- `documents/pacificorp/rmp_2025_irp_update_coverletter_2026-03-31.pdf` — Rocky Mountain Power 2025 IRP update cover letter
- `documents/pacificorp/wra_2025_datacenter_factsheet_ut.pdf` — Western Resource Advocates data center fact sheet (Utah)
- `documents/idaho-power/idahopower_LGIP_page_2026-09-09.html` — Idaho Power Large Generator Interconnection Procedures page
- `documents/idaho-power/idahopower_generator_interconnection_main_2026-09-09.html` — Idaho Power interconnection main page
- `documents/idaho-power/ipuc_open_electric_cases_2026-09-09.html` — Idaho PUC open electric case list
- `documents/aps/azcc_statewide_electric_utility_territory_map_2013-01-01_fetched_2026-09-09.pdf` — Arizona Corporation Commission utility territory map
- `documents/aps/interconnection_fyi_aps_queue_notes_2026-09-09.txt` — APS queue research notes
- `documents/mohave-electric-uns-aepco/azcc_docket_notes_2026-09-09.txt` — Arizona co-op docket research notes

## Next steps

No CAPTCHAs blocked this workstream — the barrier here was that utilities simply don't publish the data (confidential bilateral contracts), not that a search engine blocked access. Three follow-ups, none requiring CAPTCHA-solving:

1. **Verify whether "Green River Gigasite" (Valar Atomics, per BLM/MLRS) and the Blue Castle Holdings/Fulcrum Point Green River nuclear-SMR proposal are the same project, related projects, or an unrelated coincidence of location.** This same ambiguity was independently flagged by the news/press workstream — two separate research passes hit the same wall, which makes it a good candidate for a direct call to Green River, Utah's city government or Emery County planning office, who would know which (or both) projects are actually real and active locally.
2. **Confirm the Wyoming Hyperscale/Prometheus 120 MW Rocky Mountain Power contract** directly against a Utah/Wyoming PSC filing or PacifiCorp's own disclosures, rather than relying on trade press alone.
3. **Re-run this workstream's per-utility search with a fresh session** if a fully retraceable, line-by-line query log is required for publication-grade sourcing — the original subagent's exhaustive log did not survive being transferred into this file (see provenance note at the top).
