# SEC EDGAR Search Findings — BLM Data Center / Hyperscale Compute Entities

Research conducted 2026-09-09 for Center for Western Priorities. Covers the entity names listed in
`PROJECT_SUMMARIES.md` (BLM ROW applicants and related project names in AZ, ID, NV, OR, UT, WY).

**Tools used:** SEC EDGAR full-text search (EFTS API, `https://efts.sec.gov/LATEST/search-index?q=...`,
which backs the public search UI at `https://www.sec.gov/edgar/search/`), and EDGAR company search
(`https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=...`). Full-text search covers
EDGAR filings from 2001 to present. All queries were run as exact quoted phrases. Raw JSON responses
for every query are saved in `../raw_json/` (sibling directory to this file) for reproducibility.

**Important scope caveat:** EDGAR full-text search indexes the *text* of filings, not a structured
company database. Common words/names (e.g., "Dayton," "North," "Rhea," "Leo") produce large numbers of
coincidental matches with zero connection to the entities we're investigating. Every hit below was
manually opened and read in context before being called "genuine" or "false positive." Company-name
lookups (browse-edgar) were also run for each entity to check whether it is itself a registered EDGAR
filer (has its own CIK) — this only returned a hit for Prometheus Hyperscale.

---

## MAJOR FINDING: Wyoming Hyperscale White Box LLC = Prometheus Hyperscale (same entity, renamed)

Oklo Inc. (NYSE: OKLO), a publicly traded advanced-nuclear/SMR company, discloses in its **Form 10-K
filed 2026-03-17** (accession 0001628280-26-018698, fiscal year 2025):

> "...we have signed non-binding letters of intent with Equinix, Inc. ("Equinix"), Diamondback E&P LLC
> ("Diamondback Energy"), and **Prometheus Hyperscale (formerly Wyoming Hyperscale White Box LLC)**
> ("Prometheus Hyperscale")..."

Direct URL: https://www.sec.gov/Archives/edgar/data/1849056/000162828026018698/oklo-20251231.htm
(saved to `documents/wyoming-hyperscale-white-box/oklo_10k_2026-03-17_full.htm`)

This confirms Wyoming Hyperscale White Box LLC (the Kemmerer/Rock Springs FO applicant, ROW cases
closed 2024-07-09 per MLRS) is the same operating business now called **Prometheus Hyperscale**, which
also has BLM cases in Wyoming under that later name (WYWY106720454/455/456, filed 2025-02-18).

A prior Oklo **8-K exhibit (EX-99.1, investor presentation, filed 2024-08-13)**, accession
0001104659-24-088946, states:

> "Partnered with computer networking company Wyoming Hyperscale to deliver 100 megawatts to its data
> centers over a 20-year power purchase agreement." ... "Oklo intends to supply 100 megawatts of power
> to Wyoming Hyperscale's data center campus." ... quote attributed to **"TRENTON THORNOCK, Founder and
> Managing Member of Wyoming Hyperscale."**

Direct URL: https://www.sec.gov/Archives/edgar/data/1849056/000110465924088946/tm2421217d1_ex99-1.htm
(saved to `documents/wyoming-hyperscale-white-box/oklo_8k_ex99-1_2024-08-13_investor-presentation.htm`)

This independently corroborates the Form D finding below: Trenton Thornock is listed as an "Executive
Officer, Director" of Prometheus Hyperscale in its September 2026 Form D.

---

## 1. Prometheus Hyperscale — GENUINE HIT (Form D)

**Search queries run:** `"Prometheus Hyperscale"` (efts full-text, 32 hits total — see below);
company-name lookup `company=prometheus+hyperscale` (1 registrant found).

**Filing:** Form D (Notice of Exempt Offering of Securities)
- **Filed:** 2026-09-09 (same day as this research — signature dated 2026-09-08)
- **CIK:** 0002145894
- **Accession number:** 0002145894-26-000002
- **EDGAR URL (filing index):** https://www.sec.gov/Archives/edgar/data/2145894/000214589426000002/0002145894-26-000002-index.htm
- **Primary document (XML):** https://www.sec.gov/Archives/edgar/data/2145894/000214589426000002/primary_doc.xml

**Filer/issuer name:** Prometheus Hyperscale (a Corporation, incorporated in Wyoming, 2024)

**Business address (per Form D issuer address):** 2550 North Loop West, Suite 240, Houston, TX 77092
(phone 713-670-6944)

**Mailing address on file with EDGAR (company record, may be registered-agent address):**
8936 County Road 180, Evanston, WY 82930

**Related persons (officers/directors) disclosed:**
| Name | Relationship(s) | Address |
|---|---|---|
| Trenton Thornock | Executive Officer, Director | 2550 North Loop West, Suite 240, Houston, TX 77092 |
| Trevor Neilson | Executive Officer, Director (signed the form as **President**) | same |
| Marc Chennault | Executive Officer | same |
| **Bernard Looney** | Executive Officer, Director | same |
| Matthew Wiener | Director | same |

Note: Bernard Looney is the former group CEO of BP plc (resigned 2023). The filing does not clarify
whether this is the same individual; the name match and the "Executive Officer, Director" role in an
energy-adjacent hyperscale/power venture warrants a manual identity check by the reporter before
publication.

**Offering details:**
- Total offering amount: **$34,846,637**
- Total amount sold: **$30,336,526**
- Total remaining: **$4,510,111**
- Number of investors already invested: **95** (all accredited; no non-accredited investors)
- Date of first sale: 2026-06-30
- Type of securities: Equity
- Exemption claimed: Rule 506(b) (item 06b)
- Minimum investment accepted: $0
- Sales commissions / finders' fees: $0

**Other 32 hits for "Prometheus Hyperscale" (full-text search, unquoted document text):** All but the
Form D above are the Oklo Inc. filings (10-Ks, 10-Qs, S-1s, 424Bs, etc., 2024–2026) that mention
Prometheus Hyperscale as a named customer/counterparty (see "Major Finding" section above for the two
most substantive ones). No other distinct filers.

**Documents saved:** `documents/prometheus-hyperscale/` — `primary_doc.xml` (raw structured Form D
data), `rendered_primary_doc.html` (EDGAR's human-readable XSLT rendering), `filing-index.htm`,
`company_filings_atom.xml` (full company filing history — confirms this is the *only* filing by this
CIK).

---

## 2. Wyoming Hyperscale White Box LLC / Wyoming Hyperscale

**Search queries run:** `"Wyoming Hyperscale White Box"` (6 hits), `"Wyoming Hyperscale"` (34 hits);
company-name lookup `company=wyoming+hyperscale` (0 registrants — this name itself has no EDGAR CIK).

**Result:** No filing was made *by* an entity named "Wyoming Hyperscale White Box LLC" or "Wyoming
Hyperscale" — it has no CIK of its own on EDGAR. All 34 full-text hits are Oklo Inc. filings (10-Ks,
10-Qs, 424Bs, S-1s, S-3s, ARS, one 2024 8-K) that mention "Wyoming Hyperscale" as a customer/PPA
counterparty. See the "Major Finding" section above for the two substantive ones (2026 10-K and 2024
8-K), which together establish: (a) Wyoming Hyperscale White Box LLC was renamed Prometheus Hyperscale,
and (b) Trenton Thornock is its founder/managing member, corroborating the Prometheus Hyperscale Form D
above.

**Conclusion:** No EDGAR filings under this exact entity name; genuine information is found only via
cross-references in Oklo Inc.'s filings, cataloged above and under Prometheus Hyperscale.

---

## 3. Valar Atomics

**Search queries run:** `"Valar Atomics"` (29 hits, full-text); company-name lookup
`company=valar+atomics` (7 registrants found, all SPV/feeder-fund series — see below).

**Result:** Valar Atomics itself (the operating SMR company referenced in the BLM filings for the
Green River and Raceway Gigasite projects) has **no EDGAR filings of its own** — it is not a reporting
company and has no Form D under its own name. However:

### 3a. Nine third-party investment-vehicle Form Ds reference "Valar Atomics" by name
These are **not filings by Valar Atomics** — they are Form Ds filed by special-purpose "series LLC"
investment vehicles (SPVs) that pool outside investor money to buy into Valar Atomics. All nine share
Delaware entity type and were signed either by "Sydecar LLC" (a fund-administration platform) as
Manager, or by "Alumni Funds" (AngelList-affiliated) as Sole Manager. None disclose Valar Atomics' own
officers — only the SPV administrator's signing officer.

| Entity name (as filed) | CIK | Accession | Filed | Total offering | Investors | Signer |
|---|---|---|---|---|---|---|
| Valar Atomics Jul 2025 a Series of CGF2021 LLC | 0002084125 | 0002084125-25-000001 | 2025-09-05 | $1,077,000 | 32 | Brett Sagan (Sydecar LLC GM) |
| Valar Atomics Aug 2025 a Series of CGF2021 LLC | 0002084317 | 0002084317-25-000002 | 2025-09-08 | $363,800 | 19 | Brett Sagan (Sydecar LLC GM) |
| AVSF - Valar Atomics 2025, LLC | 0002085342 | 0002085342-25-000001 | 2025-10-10 | $836,800 | 39 | Hilary Ncala (Alumni Funds Sr. VP) |
| VALAR ATOMICS B311 Feb 2026 a Series of CGF2021 LLC | 0002118792 | 0002118792-26-000001 | 2026-03-17 | $650,000 | 7 | Alexandra Nieland (Sydecar LLC GM) |
| VALAR ATOMICS 2 Feb 2026 a Series of CGF2021 LLC | 0002118844 | 0002118844-26-000001 | 2026-03-17 | $2,151,136 | 20 | Alexandra Nieland (Sydecar LLC GM) |
| VALAR ATOMICS 3 Feb 2026 a Series of CGF2021 LLC | 0002118841 | 0002118841-26-000001 | 2026-03-24 | $1,186,630 | 1 | Alexandra Nieland (Sydecar LLC GM) |
| Blackwing Valar Atomics Mar 2026 a Series of CGF2021 LLC | 0002118809 | 0002118809-26-000001 | 2026-03-13 | $1,116,530 | 20 | Alexandra Nieland (Sydecar LLC GM) |
| Valar Atomics Mar 2026 a Series of CGF2021 LLC | 0002122841 | 0002122841-26-000001 | 2026-03-23 | $388,915 | 7 | Brett Sagan (Sydecar LLC GM) |
| VALAR ATOMICS 4 Apr 2026 a Series of CGF2021 LLC | 0002130252 | 0002130252-26-000001 | 2026-04-22/23 | $369,415 | 26 | Brett Sagan (Sydecar LLC GM) |

Combined, these nine vehicles raised **≈$8.14 million** from a combined ~171 investor slots (some
investors may recur across vehicles) to invest into Valar Atomics between July 2025 and April 2026 —
consistent with a fast-growing, well-capitalized startup during the period it was filing its Utah BLM
ROW applications (Green River, filed 2026-02-13; Raceway, filed 2026-04-13).

EDGAR URLs (filing index pattern): `https://www.sec.gov/Archives/edgar/data/<CIK-no-leading-zeros>/<accession-no-dashes>/primary_doc.xml`
— raw XML for all nine saved to `documents/valar-atomics/cik_<CIK>/primary_doc.xml`.

### 3b. Deep Fission, Inc. S-1 (2026-05-20) names "Valar Atomics Inc."
Deep Fission, Inc. (another advanced-nuclear company, ticker FISN) states in its S-1
(accession 0001104659-26-064074):

> "In April 2025, we joined as a plaintiff, together with the State of Texas, State of Utah, State of
> Louisiana, State of Florida, the Arizona State Legislature..., Last Energy, Inc., and **Valar Atomics
> Inc.**, in a federal lawsuit filed in the U.S. District Court for the Eastern District of Texas
> against the NRC, captioned State of Texas et al. v. U.S. Nuclear Regulatory Commission (Case No.
> 6:24-cv-00507). The lawsuit challenges the NRC's interpretation and application of..."

This confirms "Valar Atomics Inc." as the operating company's formal legal name (a Delaware or similar
corporation, not disclosed further here) and places it as a co-plaintiff in ongoing NRC litigation —
useful corroborating context but not a direct SEC disclosure by Valar Atomics itself.
Direct URL: https://www.sec.gov/Archives/edgar/data/1918102/000110465926064074/tmb-20260331xs1.htm
(saved to `documents/valar-atomics/deep_fission_s1_2026-05-20_full.htm`)

---

## 4. Skylar Opportunities LLC / Skylar Opportunities — GENUINE HIT

**Search queries run:** `"Skylar Opportunities LLC"` (9 hits), `"Skylar Opportunities"` (9 hits,
identical result set); company-name lookup `company=skylar+opportunities` (0 registrants — not itself
an EDGAR filer).

**Result:** All 9 full-text hits are the same underlying mutual-fund registration document — Exchange
Listed Funds Trust's **Form 485BPOS / 485APOS** filings (post-effective amendments to a registered
investment company's registration statement), filed repeatedly between 2026-06-22 and 2026-09-09 as the
trust adds/updates individual fund series. Each contains, in Part C (Statement of Additional
Information exhibit on "other business affiliations" of portfolio managers), the same disclosure table
for the "Skylar" fund series:

> "**William O. Perkins, III**, CIO and President of Skylar Capital Management GP LLC ("SCMGP"), the
> General Partner of Skylar Capital Management LP ("SCM") ... [is also] President of its General
> Partner, SCMGP [for] Skylar Capital Advisers, LP ("SCA") ... President of its General Partner, SCA
> [for] Skylar Capital Energy Global Master Fund LP ("SCEGMF") ... President [of] Skylar Capital Energy
> Fund LP ... Director [of] Skylar Capital Energy Global Ltd ... President [of] Skylar Clearing LLC ...
> **President [of] Skylar Opportunities LLC** ... **President [of] Townsite Solar 2 LLC**."

A second individual, **Paul A. Queneau** (CFO, Executive VP & Secretary of SCMGP; former KPMG tax
partner 2016–2025, "KPMG is the audit and tax provider for all Skylar entities"), holds parallel
Executive VP & Secretary roles across the same corporate family, per the same table.

**Most recent filing (of the 9 identical hits):**
- Form: 485BPOS
- Filed: 2026-09-09
- Filer: Exchange Listed Funds Trust, CIK 0001547950
- Accession: 0001213900-26-098130
- EDGAR URL: https://www.sec.gov/Archives/edgar/data/1547950/000121390026098130/ea0304661-01_485bpos.htm

Full list of the 9 filings (all same disclosure content, filed as the trust's registration statement
was amended repeatedly through the year): 2026-06-22 (0001213900-26-070537), 2026-06-26
(0001213900-26-072157 and 0001213900-26-072523), 2026-06-29 (0001213900-26-073179), 2026-07-14
(0001213900-26-077675), 2026-08-10 (0001213900-26-087207), 2026-08-19 (0001213900-26-091338),
2026-08-27 (0001213900-26-094410), 2026-09-09 (0001213900-26-098130).

**Significance:** This directly ties **Skylar Opportunities LLC** (BLM applicant for the Horizon
Project / Skylar Opportunities Data Center & BESS, Las Vegas FO, NV) to **Skylar Capital Management** —
an SEC-registered-adviser-affiliated energy investment fund family headed by William O. Perkins III —
and, via the same disclosure, to **Townsite Solar 2 LLC** (the Nevada Townsite Data Center applicant,
the one BLM case in this dataset with full NEPA documentation). This is documentary evidence of common
ownership/control between these two BLM applicants, which MLRS records alone do not show.

**Document saved:** `documents/skylar-opportunities/exchange_listed_funds_trust_485bpos_2026-09-09_full.htm`
(full 485BPOS as filed; ~976 KB; the relevant table is in the Part C/SAI section under the heading
"Skylar").

---

## 5. Townsite Solar 2 LLC / Townsite Solar — GENUINE HIT (same filing as #4)

**Search queries run:** `"Townsite Solar 2"` (9 hits), `"Townsite Solar"` (9 hits, identical result
set); company-name lookup `company=townsite+solar` (0 registrants).

**Result:** Same Exchange Listed Funds Trust 485BPOS/485APOS filings as Skylar Opportunities LLC above
— see full detail in section 4. William O. Perkins III is disclosed as **President of Townsite Solar 2
LLC**, the applicant of record for the Townsite Data Center ROW (NVNV105844791, the only project in
this entire dataset with completed NEPA documentation, DOI-BLM-NV-S010-2026-0080-DNA).

**Document saved:** `documents/townsite-solar-2/exchange_listed_funds_trust_485bpos_2026-09-09_full.htm`
(identical copy of the same filing, saved under this entity's folder for convenience).

---

## 6. Copia Digital LLC / Copia Digital / Copia GDC — NO EDGAR FILINGS FOUND

**Search queries run:** `"Copia Digital LLC"` (0 hits), `"Copia Digital"` (3 hits, all false
positives), `"Copia GDC"` (0 hits); company-name lookups `company=copia+digital` and
`company=copia+gdc` (0 registrants each).

The 3 hits for the unquoted "Copia Digital" phrase are all unrelated: they come from Spanish-language
exhibits in filings by Vesta Real Estate Corporation (Mexico City-based REIT, 20-F, 2024-04-19),
Establishment Labs Holdings Inc. (Costa Rica-incorporated, S-1/A, 2018-07-13), and Petaquilla Minerals
Ltd (Panama-based miner, 6-K, 2011-05-09) — in each, "copia digital" is ordinary Spanish for "digital
copy," appearing in unrelated legal/contract boilerplate, not a reference to any company named "Copia
Digital."

**Conclusion: No EDGAR filings found for Copia Digital LLC, Copia Digital, or Copia GDC under any
variant searched.**

---

## 7. Leo Data LLC / Leo Data — NO EDGAR FILINGS FOUND

**Search queries run:** `"Leo Data LLC"` (0 hits), `"Leo Data"` (13 hits, all appear to be
coincidental); company-name lookup `company=leo+data` (0 registrants).

The 13 hits for unquoted "Leo Data" are spread across unrelated filers with no evident connection to a
BLM data-center applicant: Remote Knowledge Inc. (Houston, TX, 10-KSB/10-QSBs, 2007), Warner Chilcott
entities (S-4/A, 2006), bwin Interactive Entertainment AG / PartyGaming Plc (Form CB filings, 2010–2011,
online gambling), IQ Power AG (20-F, 2006, Switzerland), and Sidus Space Inc. (S-1/S-1A/424B4, 2023,
satellite manufacturing). One hit was directly checked in the Sidus Space filing and the words "Leo" and
"Data" did not appear in close proximity in the extracted text, consistent with a coincidental full-text
match; the remainder were not individually opened given the diversity of unrelated industries and eras
represented, but none show any Nevada/Arizona real-estate, power, or data-center subject matter.

**Conclusion: No EDGAR filings found for Leo Data LLC or Leo Data.**

---

## 8. Rhea Data LLC / Rhea Data — NO EDGAR FILINGS FOUND

**Search queries run:** `"Rhea Data LLC"` (0 hits), `"Rhea Data"` (1 hit, false positive); company-name
lookup `company=rhea+data` (0 registrants).

The single hit is Tarsus Pharmaceuticals, Inc.'s 10-Q (filed 2024-11-13, accession
0001819790-24-000129). Checked in context: "Rhea" there refers to the **"Rhea clinical trial"** for the
drug XDEMVY (Demodex blepharitis treatment) — a coincidental match of the word "Rhea" followed later in
the same document by the unrelated word "data," with no connection to any entity named Rhea Data LLC.

**Conclusion: No EDGAR filings found for Rhea Data LLC or Rhea Data.**

---

## 9. Moorman Ridge Data LLC — NO EDGAR FILINGS FOUND

**Search queries run:** `"Moorman Ridge Data"` (0 hits); company-name lookup `company=moorman+ridge`
(0 registrants).

**Conclusion: No EDGAR filings found for Moorman Ridge Data LLC.**

---

## 10. Silver Springs South LLC / Kimberly Mountain Data LLC / Dayton North LLC — NO EDGAR FILINGS FOUND

**Search queries run:** `"Silver Springs South"` (0 hits), `"Kimberly Mountain Data"` (0 hits),
`"Dayton North"` (216 hits, all false positives — see below); company-name lookups
`company=silver+springs+south`, `company=kimberly+mountain`, `company=dayton+north` (0 registrants
each).

The 216 hits for the unquoted, generic phrase "Dayton North" are overwhelmingly commercial-mortgage
securitization filings (Free Writing Prospectuses and 8-Ks from Barclays, Goldman Sachs, JPMorgan,
Wachovia, UBS mortgage trusts referencing loans against properties near "Dayton" combined with
directional/address text like "North..."), plus unrelated corporate subsidiary-list exhibits (Marriott
International EX-21 filings, Tenet Healthcare EX-21 filings) where "Dayton" (Ohio) and "North" (as in
"North Carolina" or a subsidiary name) appear adjacent by coincidence. None reference a Nevada shell LLC
or a data-center project. No further individual review of all 216 was performed beyond confirming this
pattern across the sample examined, given the entity itself has no EDGAR company record at all.

**Conclusion: No EDGAR filings found for Silver Springs South LLC, Kimberly Mountain Data LLC, or
Dayton North LLC under any name searched.**

---

## 11. On The Mark Data Center LLC — NO EDGAR FILINGS FOUND

**Search queries run:** `"On The Mark Data Center"` (0 hits); company-name lookup
`company=on+the+mark` (0 registrants).

**Conclusion: No EDGAR filings found for On The Mark Data Center LLC.**

---

## 12. Sandy Valley Mining Energy & Compute LLC — NO EDGAR FILINGS FOUND

**Search queries run:** `"Sandy Valley Mining Energy"` (0 hits); company-name lookup
`company=sandy+valley` (0 registrants).

**Conclusion: No EDGAR filings found for Sandy Valley Mining Energy & Compute LLC.**

---

## 13. Meadowlark Renewables Center LLC — NO EDGAR FILINGS FOUND

**Search queries run:** `"Meadowlark Renewables Center"` (0 hits); company-name lookup
`company=meadowlark+renewables` (0 registrants).

**Conclusion: No EDGAR filings found for Meadowlark Renewables Center LLC.**

---

## Summary table

| Entity | EDGAR hits? | Filing type found | Key takeaway |
|---|---|---|---|
| Copia Digital LLC / Copia Digital / Copia GDC | No | — | 3 unrelated Spanish-language false positives |
| Leo Data LLC / Leo Data | No | — | 13 unrelated false positives |
| Rhea Data LLC / Rhea Data | No | — | 1 unrelated false positive (drug trial name) |
| Valar Atomics | Indirect only | 9 Form Ds (3rd-party SPVs) + 1 S-1 mention | ~$8.14M raised via SPVs into Valar Atomics 2025-2026; named as NRC co-plaintiff in Deep Fission S-1 |
| Prometheus Hyperscale | Yes | Form D, filed 2026-09-09 | $34.8M offering; officers incl. Trenton Thornock, Trevor Neilson (President), Marc Chennault, Bernard Looney, Matthew Wiener; Houston, TX / Evanston, WY addresses |
| Wyoming Hyperscale White Box LLC / Wyoming Hyperscale | Indirect only | Oklo Inc. 10-K + 8-K | Confirmed renamed to Prometheus Hyperscale; Trenton Thornock named founder/managing member |
| Skylar Opportunities LLC | Yes | Fund SAI/Part C disclosure (9 near-duplicate 485BPOS/APOS filings) | William O. Perkins III (Skylar Capital Management) disclosed as President |
| Moorman Ridge Data LLC | No | — | — |
| Silver Springs South LLC | No | — | — |
| Kimberly Mountain Data LLC | No | — | — |
| Dayton North LLC | No | — | 216 unrelated false positives on generic phrase |
| On The Mark Data Center LLC | No | — | — |
| Sandy Valley Mining Energy & Compute LLC | No | — | — |
| Townsite Solar 2 LLC / Townsite Solar | Yes | Same fund SAI/Part C disclosure as Skylar Opportunities | William O. Perkins III disclosed as President - same corporate family as Skylar Opportunities LLC |
| Meadowlark Renewables Center LLC | No | — | — |

## Verbatim query log

```
efts.sec.gov/LATEST/search-index?q="Copia Digital LLC"
efts.sec.gov/LATEST/search-index?q="Copia Digital"
efts.sec.gov/LATEST/search-index?q="Copia GDC"
efts.sec.gov/LATEST/search-index?q="Leo Data LLC"
efts.sec.gov/LATEST/search-index?q="Leo Data"
efts.sec.gov/LATEST/search-index?q="Rhea Data LLC"
efts.sec.gov/LATEST/search-index?q="Rhea Data"
efts.sec.gov/LATEST/search-index?q="Valar Atomics"
efts.sec.gov/LATEST/search-index?q="Prometheus Hyperscale"
efts.sec.gov/LATEST/search-index?q="Wyoming Hyperscale White Box"
efts.sec.gov/LATEST/search-index?q="Wyoming Hyperscale"
efts.sec.gov/LATEST/search-index?q="Skylar Opportunities LLC"
efts.sec.gov/LATEST/search-index?q="Skylar Opportunities"
efts.sec.gov/LATEST/search-index?q="Moorman Ridge Data"
efts.sec.gov/LATEST/search-index?q="Silver Springs South"
efts.sec.gov/LATEST/search-index?q="Kimberly Mountain Data"
efts.sec.gov/LATEST/search-index?q="Dayton North"
efts.sec.gov/LATEST/search-index?q="On The Mark Data Center"
efts.sec.gov/LATEST/search-index?q="Sandy Valley Mining Energy"
efts.sec.gov/LATEST/search-index?q="Townsite Solar 2"
efts.sec.gov/LATEST/search-index?q="Townsite Solar"
efts.sec.gov/LATEST/search-index?q="Meadowlark Renewables Center"

https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=copia+digital&type=&dateb=&owner=include&count=100&output=atom
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=copia+gdc&type=&dateb=&owner=include&count=100&output=atom
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=leo+data&type=&dateb=&owner=include&count=100&output=atom
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=rhea+data&type=&dateb=&owner=include&count=100&output=atom
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=valar+atomics&type=&dateb=&owner=include&count=100&output=atom
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=prometheus+hyperscale&type=&dateb=&owner=include&count=100&output=atom
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=wyoming+hyperscale&type=&dateb=&owner=include&count=100&output=atom
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=skylar+opportunities&type=&dateb=&owner=include&count=100&output=atom
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=moorman+ridge&type=&dateb=&owner=include&count=100&output=atom
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=silver+springs+south&type=&dateb=&owner=include&count=100&output=atom
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=kimberly+mountain&type=&dateb=&owner=include&count=100&output=atom
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=dayton+north&type=&dateb=&owner=include&count=100&output=atom
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=on+the+mark&type=&dateb=&owner=include&count=100&output=atom
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=sandy+valley&type=&dateb=&owner=include&count=100&output=atom
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=townsite+solar&type=&dateb=&owner=include&count=100&output=atom
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=meadowlark+renewables&type=&dateb=&owner=include&count=100&output=atom
```

All raw JSON responses from the efts.sec.gov queries above are saved under
`external_research/sec_edgar/raw_json/efts_<slug>.json`.

## Next steps

No CAPTCHAs blocked this workstream — EDGAR is fully open. Two items still need human judgment rather than more searching:

1. **Verify the "Bernard Looney" identity match manually before publication.** The Prometheus Hyperscale Form D lists a Bernard Looney as Executive Officer/Director. This is very likely the former BP plc CEO (the corporate-other-states workstream independently found the same name in Wyoming's corporate filing for the same company, with a stated title of Chairman/CEO since April 1, 2026), but no filing in this search explicitly cross-confirms the two are the same person (e.g., no shared prior address, no biographical note). A quick search for a press release or LinkedIn profile confirming Bernard Looney's post-BP role would close this gap.
2. **Re-run the EDGAR full-text search periodically** for "Copia Digital," "Leo Data," and the Silver Springs-cluster LLC names — none currently have EDGAR filings, but Form Ds get filed on a rolling basis (Prometheus Hyperscale's own Form D was filed the same day this research was conducted), so a project that raises capital after this date could show up later.
