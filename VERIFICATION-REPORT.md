# Transcription verification report

**Scope.** Independent audit of `water/{asset-types,attributes,choices,units}.csv` and
`sanitation/{asset-types,attributes,choices,units}.csv` against the two published PDFs in
`docs/`, plus a check of the claims made in each `EXTRACTION-NOTES.md`.

**Date of audit:** 2026-09-01.
**Sources of truth:** `docs/Water-System-Management-Standard-v1.0.pdf` (52 pp, v1.0, 7 April 2022)
and `docs/Sanitation-System-Management-Standard-v1.0.pdf` (60 pp, v1.0, 21 August 2026).

All line references below are **1-based file line numbers including the header row**, so
`attributes.csv:65` is data row 64. Page references are PDF page numbers.

---

## 1. Method and sample sizes

The audit did not sample. Every row of all eight CSVs was compared against the PDFs by two
independent extraction paths, and the two paths were required to agree.

**Path A — structured table extraction.** `pdfplumber` `find_tables()` / `extract()` over every
page, with per-cell font inspection (`ArialMT` / `Arial-BoldMT` / `Arial-ItalicMT`) so that group
rows, attribute rows and choice rows could be classified by the same formatting rule the standards
state in §6.3, rather than by guessing from text. Rows split by pdfplumber across a page break or
an internal line break were re-joined before comparison. This produced an independent
reconstruction of every attribute table.

**Path B — flat text extraction.** `pdftotext -layout` for column-aligned reading and
`pdftotext -raw` for reading-order text. Every `name` and `description` string in both
`attributes.csv` and both `choices.csv` was tested for verbatim containment in the Path B text
(whitespace-insensitive). All 2 171 strings were found, except 15 that are interrupted by a page
break in the source; each of those 15 was inspected by hand and confirmed.

**Path C — figures.** `Figure 1` and `Figure 2` in both documents are embedded raster images and
carry no extractable text. Both pages were rendered at 220 dpi and read visually. This is how the
water standard's 28-vs-29 discrepancy was resolved (§3, finding S1) — the extraction notes report
it as unresolvable.

**Coverage achieved**

| Comparison | Water | Sanitation |
|---|---:|---:|
| Attribute rows compared on code, name, description, data_type, unit_quantity, attribute_group, applicability, scope, asset_type, asset_type_id | 178 / 178 | 211 / 211 |
| Choice rows compared on parent attribute, ordinal position, name, description | 269 / 269 | 445 / 445 |
| Unit rows compared on quantity, SI base unit, alternate unit, conversion factor, unit name, SI/US system | 49 / 49 | 58 / 58 |
| Asset type rows compared on class, number, name, description | 29 / 29 | 27 / 27 |
| Group heading rows reconciled | 39 / 39 | 42 / 42 |
| Discrete claims in `EXTRACTION-NOTES.md` tested against the PDF | 21 (A1–A21) + §5 | §2–§5.10 |

Derived columns (`type_id`, `choice_id`, `asset_type_id`, `si_unit`) were recomputed from the
documented rules and compared; the JSON products in each directory were diffed field-by-field
against the CSVs; `SHA256SUMS` verified; `tests/run-tests.sh` run.

---

## 2. Confirmed counts

Counted from the PDFs, not taken from the notes.

### Water System Management Standard

| Item | Counted from PDF | Where | CSV |
|---|---:|---|---:|
| Asset classes | 5 | Table 3, p13 | 5 distinct in `asset-types.csv` |
| Asset types | **29** | Table 4, pp14–15 | 29 rows |
| Asset types stated in the Introduction | **28** | p2 | — |
| Asset types shown in Figure 1 | **28** | p2 (image) | — |
| General attributes | 63 | Table 5, pp17–24 | 63 rows `scope=general` |
| Type-specific attributes | 115 | Tables 6–24, pp24–50 | 115 rows |
| **Total attributes** | **178** | — | 178 rows |
| Choice options | 269 | Tables 5–24 | 269 rows |
| Attribute groups | 39 | Tables 5–24 | 39 distinct |
| Unit quantities / unit rows | 9 / 49 | Table 2, pp10–11 | 9 / 49 |
| Asset types with no attribute table | 10 (Canal + 9 Natural) | §6.5.4.2, §6.5.5, pp50–51 | — |

An independent regex count of five-digit codes at line-start in the `-layout` text of pp17–52
returned exactly 178 codes, all distinct.

**The Introduction's "28" is confirmed** (p2: "The standard currently recognizes 28 types of assets
and 5 classes, as shown in Figure 1"), and **Table 4's 29 is confirmed**. See S1 for the resolution.

### Sanitation System Management Standard

| Item | Counted from PDF | Where | CSV |
|---|---:|---|---:|
| Asset classes | 4 | Table 3, p10 | 4 distinct |
| Asset types | 27 | Table 4, pp11–12 | 27 rows |
| Asset types stated in the Introduction | 27 | p2 | — |
| Asset types shown in Figure 1 | 27 | p2 (image) | — |
| General attributes | 76 | Table 5, pp13–22 | 76 rows |
| Type-specific attributes | 135 | Tables 6–31, pp23–56 | 135 rows |
| **Total attributes** | **211** | — | 211 rows |
| Choice options | 445 | Tables 5–31 | 445 rows |
| Attribute groups | **42** | Tables 5–31 | 42 distinct + 1 attribute with none |
| Unit quantities / unit rows | 11 / 58 | Table 2, pp7–9 | 11 / 58 |
| Asset types with no attribute table | 1 (Subsystem) | §6.5.1.2, p23 | — |

Independent five-digit-code count over pp13–60: exactly 211, all distinct.

**Confirmed:** the sanitation document states "27 types of assets and 4 classes" (p2), Table 4
lists 27, and Figure 1 depicts 27. The mWater-published figures of 27 types and 211 attributes are
both reproduced exactly. Unlike the water standard, the sanitation standard is internally
consistent on its counts.

**Refuted:** nothing in the count claims put to this audit was refuted. The one claim that could
not previously be settled — which of the water standard's two numbers is right — is settled in S1.

---

## 3. Findings

### 3.1 Transcription errors (CSV differs from PDF)

**None.** Across 178 + 211 attribute rows, 269 + 445 choice rows, 49 + 58 unit rows and
29 + 27 asset-type rows, no cell in any of the eight CSVs was found to differ from the published
PDF. Every attribute name, attribute description, choice name, choice description, data type, unit
quantity, attribute group, condition string, unit symbol and conversion factor matches the source
character-for-character once line-break hyphenation and page-break splits are resolved. No option
is missing from any choice list, no option was added, no list is out of order, and no attribute is
filed under the wrong asset type or the wrong scope.

Specific checks that could have exposed an error and did not:

- **Long choice lists.** The 12 longest lists in each standard were checked end-to-end, including
  `sanitation 30501 Treatment type` (35 options, pp48–51, the longest list in either document) and
  `water 31201 Sensor type` / `water 30501 Treatment type` (16 each). The final option of every list
  is present.
- **Table boundaries.** Pages carrying two tables were checked by hand: water p43
  (Table 16 Hydrant `30901` → Table 17 Junction `31001`), water p50 (Table 23 Other vertical `39901`
  → Table 24 Pipe `40101`), sanitation p33 (Table 14 Valve `30802` → Table 15 Flow control `32101`),
  sanitation p55 (Table 29 → Table 30). All split correctly.
- **General / type-specific boundary.** `water 00184 Import code` sits at the top of p24, above the
  §6.5 heading, and is correctly marked `general` (`water/attributes.csv:64`). `sanitation 00185`
  likewise (`sanitation/attributes.csv:77`). No general attribute is misfiled as type-specific or
  vice versa in either file.
- **Descriptions are quotations, not paraphrases.** Verified for all 173 + 211 non-empty attribute
  descriptions and all 254 + 430 non-empty choice descriptions, by exact string match on two
  independent extraction paths. Source-side oddities are preserved rather than tidied — for example
  `water/attributes.csv:82` keeps the duplicated word in "Maximum **Flow rate rate** that the source
  can accommodate" (p28) and `water/choices.csv:193` keeps the misspelling "or **visa versa**." (p41).
- **Rounding and notation.** Conversion factors are carried verbatim including Unicode superscripts
  (`1 X 10⁻⁶`, `8.64 X 10⁴`) and the two temperature *formulas*; nothing was normalised to a float.
  The sanitation temperature cells legitimately read `t_F` / `t_C` in the source (p9), not `tF`/`tC`
  as in the water source (p11), and each file reproduces its own source.

The derived JSON (`water/water-asset-standard.json`, `sanitation/sanitation-asset-standard.json`),
the JSON Schemas, `SHA256SUMS` and `tests/run-tests.sh` are all consistent with the CSVs.

### 3.2 Source defects (the PDF is wrong or inconsistent; the CSV faithfully reproduces it)

| # | Finding | Source | CSV location |
|---|---|---|---|
| **S1** | **The water standard's "28 types" and Table 4's 29 differ because Figure 1 omits the asset type `504 Spring`.** Figure 1 (p2) shows Water system; Water facility; 16 Vertical types; Pipe, Canal; and 8 Natural types (Reservoir, River or stream, Aquifer, Riparian zone, Infiltration zone, Forest, Wetland, Watershed) — 28 in total. Table 4 (pp14–15) additionally lists `504 Spring`. The Introduction's sentence agrees with the figure, not the table. Table 4 is the normative list ("The asset types described in the following tables **shall** be made available"), so 29 is right and Figure 1 plus the Introduction are stale. | water p2 vs pp14–15 | `water/asset-types.csv:25` (Spring) — correctly present |
| **S2** | Figure 1 also names three types differently from Table 4: "River or stream" vs `River/stream`, "Infiltration zone" vs `Infiltration basin`, "Other" vs `Other vertical`. | water p2 | `water/asset-types.csv:23,27,19` follow Table 4 |
| **S3** | Water system is type `101` in Table 4, but every attribute in Table 6 is numbered `102xx`, which decodes under the standard's own grammar (class 1, type 02) to a type that does not exist. | water p14 vs p24 | `water/attributes.csv:65–71` |
| **S4** | The same defect in sanitation, and worse: Sanitation system is `101` and **Subsystem is `102`**, so the nine `10201`–`10209` codes decode to Subsystem — a real, different type whose own section (§6.5.1.2, p23) says "This section is reserved." | san p11 vs p23 | `sanitation/attributes.csv:78–86` |
| **S5** | `Asset ID` is used as a data type although Table 1 of each standard defines exactly eight data types and `Asset ID` is not one of them. | water pp17,22; san pp13,19 | `water/attributes.csv:7,49`; `sanitation/attributes.csv:7,58,59` |
| **S6** | **Flow-rate conversion factors contradict §4.2's own rule.** §4.2 defines the factor as "the amount of the base unit that would be equal to one current unit". Against base `m³/s`: water publishes `m³/d = 8.64 X 10⁴` (should be 1.157 × 10⁻⁵), `L/d = 86.4` (1.157 × 10⁻⁸), `ML/d = 8.64 X 10⁷` (1.157 × 10⁻²). Sanitation repeats all three and adds `m³/hr = 3600` (2.778 × 10⁻⁴) and `L/min = 60` (1.667 × 10⁻⁵). `L/s = 0.001` and `Mgal/d = 0.0438126` in the same block do satisfy the rule, so the block is internally inconsistent, not merely using a different convention. | water p10; san p8 | `water/units.csv:23,25,26`; `sanitation/units.csv:24,25,27,28,29` |
| **S7** | **The two published unit tables disagree with each other.** Water gives `gal/min (gpm) = 6.30902 X 10⁻⁵` and `gal/d = 4.38126 X 10⁻⁸`; sanitation gives the same mantissas with **positive** exponents, `6.30902 X 10⁵` and `4.38126 X 10⁸`. The water values are correct; the sanitation values are wrong by 10¹⁰ and 10¹⁶. Each CSV reproduces its own source faithfully, so the two published CSVs now disagree by design. | water p10 vs san p8 | `water/units.csv:27,28` vs `sanitation/units.csv:30,31` |
| **S8** | `acre-ft = 1223.489` in both standards. One acre-foot is 1233.489 m³; this is a digit transposition. | water p11; san p9 | `water/units.csv:45`; `sanitation/units.csv:54` |
| **S9** | `Mgal = 3785` (exact value 3785.412, and `gal` in the same block is given to seven figures as 0.003785412). Inconsistent precision. | water p11; san p9 | `water/units.csv:44`; `sanitation/units.csv:53` |
| **S10** | `kVA` is listed under **Power** with factor 1000 and marked SI, although kVA measures apparent power, not the real power measured in watts. | water p11; san p9 | `water/units.csv:37`; `sanitation/units.csv:46` |
| **S11** | In the water Table 2 the `System` column marks `m H₂O`, `cm H₂O` and `mm Hg` as **SI**; they are conventional pressure units. | water p10 | `water/units.csv:17,18,19` (`notes` column) |
| **S12** | The sanitation Table 2 carries a footnote "\* Temperature is a special case…" but **no asterisk on the `Temperature` heading** — an orphan marker. It also has **no Time footnote at all**, although `mo = 30.436875` and `yr = 365.2425` presuppose the average-Gregorian-year definition that the water standard supplies in its Time footnote. | san p9 vs water p11 | `sanitation/units.csv:55–57` (Time), `:58–59` (Temperature) |
| **S13** | The sanitation standard defines `Temperature` as an 11th unit quantity but no attribute in the document uses `Unit: Temperature`. | san p9 | `sanitation/units.csv:58,59` (unreferenced) |
| **S14** | **`39901 Other vertical asset type` sits under no group heading** (Table 29, p55), contradicting the standard's own statement that "Every attribute in this standard has a group". The equivalent water table (Table 23, p49) does carry `Other vertical info`. | san p55 | `sanitation/attributes.csv:199` — `attribute_group` empty |
| **S15** | Five water attributes have an empty Description cell: `20101`, `30126`, `31001`, `31201`, `31401`. `20101 Water facility type` is also the referent of another attribute's condition. | water pp26,28,43,45,47 | `water/attributes.csv:72,88,158,160,162` |
| **S16** | In both standards the five-point scales of `00053`, `00054`, `00055` have no descriptions and no defined thresholds — 15 undefined choice options per standard. | water p20; san p16 | `water/choices.csv`, `sanitation/choices.csv` (15 rows each) |
| **S17** | `00001 Type` is a Choice attribute with no choice list in either standard; the value set is only implied by Table 4. | water p17; san p13 | no rows in either `choices.csv` |
| **S18** | Eleven water choice rows are **not italicised**, breaking §6.3's own formatting rule: all nine choices of `20101` (p26) and both choices of `30423` (p36). Confirmed by font inspection (`ArialMT`, not `Arial-ItalicMT`). | water pp26,36 | `water/choices.csv` rows for `20101`, `30423` |
| **S19** | Conditions that reference names which do not exist. Water: `10202` "Type of system: Distribution" (no such attribute; the choice is "Distribution network"); `30522` "Chlorination type: …" (no such attribute); `30155` "Pump or lifting device: Submersible" (the choice is "Submersible pump"). Sanitation: `30521` "Treatment type: Chlorination, Disinfection, Chemical feed, Coagulation or flocculation, Nutrient removal (nitrogen or phosphorus), Lime stabilization" — four of the six named values are **not** among the 35 published choices of `30501 Treatment type`. | water pp24,30,39; san p52 | `water/attributes.csv:66,101,147`; `sanitation/attributes.csv:193` |
| **S20** | Undocumented condition grammars. §6.3 defines only `Name: value, value`. Water also uses `Pump type: NOT Hand pump` (`30203`, `30204`). Sanitation uses three further forms: `All types except: …` (`00027`, `00071`), `Type is not Sanitation point` (`00041`), `Pump type is not Manual pump` (`30203`, `30204`). A conforming parser built to §6.3 will mis-handle all of them. | water p31; san pp14,17,44 | `water/attributes.csv:105,106`; `sanitation/attributes.csv:24,32,161,162` |
| **S21** | Case and spacing inconsistencies inside condition strings, reproduced verbatim: water `Type: Meter, Water Point` (`00018`) vs `Type: Water system, Water point` (`00043`); `Type: Water system, water facility` (`00021`, `00066`, `00067`, `00070`); `Type: Pump, tank, power, valve` (`00071`); `Type: Junction, valve, meter` (`00095`). Sanitation: `Type: Sanitation system,Subsystem, Facility, Sanitation point` (missing space after the first comma, Points of contact group, p22) and `All types except: Sanitation system, subsystem` (lower-case, `00027`). A case-sensitive resolver fails on these. | water pp18,20,22,23; san pp14,22 | as cited |
| **S22** | `water 30702 Electrical power device type` (p41) is the only long choice list in either standard with no `Other` option, and its `Transformer` description contains the misspelling "visa versa". | water p41 | `water/choices.csv:190–197`, esp. `:193` |
| **S23** | The sanitation Pipe table skips attribute code `40102` (`40101` → `40103`, p55). Codes are non-contiguous throughout both standards; this is normal, but noted because `40102 Pipe color` exists in the water standard. | san p55 | `sanitation/attributes.csv:200,201` |
| **S24** | Under `Current`, both standards list a single unit (`A`) with no alternates, so the quantity's table adds nothing beyond naming the base unit. | water p11; san p9 | `water/units.csv:38`; `sanitation/units.csv:47` |

### 3.3 Documentation gaps (correct, but under-explained or mis-explained)

| # | Finding | Location |
|---|---|---|
| **D1** | **`water/EXTRACTION-NOTES.md` A1 states that Figure 1 "is a raster image and could not be counted to determine which of the two numbers is authoritative".** It can be counted: rendering p2 at 220 dpi shows the figure plainly, it contains 28 types, and the missing type is `504 Spring`. A2 further says Figure 1 "appears to duplicate Table 4 but could not be verified" — it does not duplicate Table 4 (S1, S2). The single most consequential open question in the water notes was answerable from the published PDF. | `water/EXTRACTION-NOTES.md` §3, A1, A17 |
| **D2** | `sanitation/EXTRACTION-NOTES.md` §3 says Figure 1 and Figure 2 were "not machine-read" and that "no data is believed to be lost — but this is stated as an assumption, not a verified fact." Verified here: sanitation Figure 1 depicts exactly the 27 types of Table 4, and Figure 2 is a content-free schematic. The assumption holds and can be upgraded to a verified statement. | `sanitation/EXTRACTION-NOTES.md` §3 |
| **D3** | `sanitation/EXTRACTION-NOTES.md` §4 states "The document uses **43** distinct group names". The document uses **42**; the 43rd apparent value is the empty cell on `39901`. The notes nowhere record that one attribute has no group at all (S14), even though §7.5 of the same notes quotes the standard's claim that "Every attribute in this standard has a group". This is the one substantive omission in an otherwise accurate set of notes. | `sanitation/EXTRACTION-NOTES.md:108`; `sanitation/attributes.csv:199` |
| **D4** | `sanitation/EXTRACTION-NOTES.md` §5.9 gives the rule-implied value for `ML/d` as **11.574**. It is 1.1574 × 10⁻² (1 ML/d = 1000 m³/d = 0.011574 m³/s) — the notes are out by 10³. The other six rows of that table are arithmetically correct, as is the `acre-ft` figure of 1233.48. The error is in the commentary only; `units.csv` is unaffected. | `sanitation/EXTRACTION-NOTES.md` §5.9 |
| **D5** | `water/EXTRACTION-NOTES.md` A19 discusses Table 2 at length — the temperature formulas, the mislabelled `System` column, the footnotes — but **never flags the flow-rate factors (S6) or `acre-ft` (S8)**, both of which are present in the water table too. The sanitation notes flag both. A reader of the water package alone is not warned. | `water/EXTRACTION-NOTES.md` A19 |
| **D6** | **`si_unit` is empty in all 178 rows of `water/attributes.csv` but populated in all 56 Unit rows of `sanitation/attributes.csv`.** The water notes never mention the column. `DATA-DICTIONARY.md:71` explains it as "The SI base unit, where the standard states one **on the attribute row**. Populated in the sanitation table only" — but no attribute row in either standard states an SI unit; the sanitation values are a lookup of Table 2's base unit, exactly as `sanitation/EXTRACTION-NOTES.md` §4 says. Water's Table 2 defines the same base units for all nine of its quantities, so the column could be populated identically. The stated provenance is wrong and the asymmetry is unexplained. | `water/attributes.csv` (all rows); `DATA-DICTIONARY.md:71` |
| **D7** | **`asset_class` is populated in all 115 type-specific rows of `water/attributes.csv` and empty in all 211 rows of `sanitation/attributes.csv`.** The sanitation notes justify leaving it empty; the water notes never mention populating it. Both values are derived by joining `asset_type` to `asset-types.csv`, so both files could carry it. | `water/attributes.csv`; `sanitation/attributes.csv`; `DATA-DICTIONARY.md:66` |
| **D8** | **`required` is `TRUE` on `water/attributes.csv:4` (`00003 Asset ID`) and empty on all 211 sanitation rows,** including `sanitation/attributes.csv:4` (`00003 Unique ID`). Neither source document has a required/optional column; both contain the same §5.2 sentence "All assets **shall** be assigned an identification code". `DATA-DICTIONARY.md:74` states the rule as "TRUE only where the standard uses 'shall'", which does not account for the difference. The water value is a defensible editorial inference (disclosed in A18) but it is an assertion the PDF does not make in that column, and it is applied to only one of the two standards. | `water/attributes.csv:4`; `sanitation/attributes.csv:4`; `DATA-DICTIONARY.md:74` |
| **D9** | **Group-level conditions are silently narrowed.** Where an attribute has its own condition *and* sits in a conditioned group, only the attribute's own condition reaches `applicability`; the group predicate is dropped. This affects 11 water rows (`00092`–`00096`, `10202`, `30142`–`30144`, `30155`, `30422`) and 7 sanitation rows (`00092`–`00096`, `00098`, `00099`). Both notes disclose it precisely and correctly, but **nothing in the CSVs marks these rows**, so a consumer reading only the tables gets a predicate weaker than the standard's. In six of the water cases the two conditions are independent, so the conjunction genuinely matters. | `water/attributes.csv`; `sanitation/attributes.csv`; both notes §A6 / §5.3 |
| **D10** | Choice ordering is meaningful in the source (the "Other" option is last, scales run Very low → Very high) but is recorded only as physical row order in `choices.csv`. There is no ordinal column, so any consumer that sorts or re-keys the file loses it. | both `choices.csv` |
| **D11** | Neither package carries a note that the two standards' Table 2 disagree on `gal/min` and `gal/d` (S7). A consumer joining the two `units.csv` files on `alternate_unit` will find two different factors for the same unit and has nothing to tell them which is right. | both `units.csv`; both notes |

### 3.4 Extraction-notes claims verified as accurate

Tested against the PDF and confirmed exactly, so that reviewers need not re-check them:

- Water A2 (three-digit `#` decomposed to two-digit `type_code`; `01` recurs five times), A3, A4,
  A5 (39 groups; `Hierarchy` is the only group carrying a description — confirmed, it is the only
  one of 39 + 42 group rows in either document with non-empty Description), A6 (the full list of
  10 group conditions; **41** attributes inherit; **exactly the 11** listed carry both), A7, A8,
  A10 (exactly those five empty descriptions), A11 (exactly 15), A12, A13 (exactly 11 non-italic
  choice rows, confirmed by font), A14 (`Unit: Temp-⏎erature` on `30125`, p28), A15 (every code
  block boundary as listed), A16, A18, A19, A20, and all of §5 (0 duplicate codes, 0 orphan
  choices, 0 unresolved `asset_type`, 0 `choice_id` collisions).
- Sanitation §2 (all counts), §2.1, §3 (all 31 per-table attribute and choice counts match the CSV
  exactly), §4 (all derivation rules reproduce the published `type_id` / `choice_id` values),
  §5.1(a) and (b), §5.2, §5.3 (8 inherit, 7 carry both — exactly the rows listed), §5.4 (the four
  non-existent `Treatment type` values), §5.5, §5.6, §5.7, §5.8, §5.9 (every published factor
  quoted correctly; only the ML/d *implied* value is wrong — D4), §5.10, §6.
- No claim in either notes file was found to describe a defect that is in fact a transcription
  mistake. Every quoted defect is real and every quotation is accurate.

---

## 4. Assessment

**The tables are fit to publish.**

The transcription is exact. Two independent extraction paths over 100 % of the rows found no cell
in any of the eight CSVs that differs from the published PDFs — no dropped choice option, no
truncated or paraphrased description, no mis-keyed code, no misfiled attribute, no altered
conversion factor. Source-side errors, typos and formatting violations are carried through rather
than silently repaired, which is the correct behaviour for a machine-readable rendering of a
published standard, and the great majority of them are disclosed in the extraction notes.

Three things should be fixed before the tables are described as canonical. None of them requires
re-transcribing anything.

1. **Correct the two notes errors and close the Figure 1 question (D1, D3, D4).** The water
   standard's 28-vs-29 discrepancy is resolvable and is resolved in S1: Figure 1 omits `504 Spring`,
   and Table 4's 29 is authoritative. `water/EXTRACTION-NOTES.md` should say so rather than record
   the question as unanswerable. `sanitation/EXTRACTION-NOTES.md` should correct "43" to 42, record
   that `39901` has no group at all, and correct the ML/d arithmetic.
2. **Resolve the three cross-standard column asymmetries (D6, D7, D8).** `si_unit`, `asset_class`
   and `required` are populated in one file and empty in the other for no reason that survives
   inspection, and `DATA-DICTIONARY.md` mis-states the provenance of `si_unit`. Either populate
   both or empty both, and say which in the data dictionary. Of these, `si_unit` in the water table
   is the one a consumer will actually miss.
3. **Warn consumers about the unit tables (S6, S7, S8).** The flow-rate block violates the
   standards' own conversion rule, `acre-ft` is transposed in both, and the two published tables
   give contradictory values for `gal/min` and `gal/d`. These are defects of the standards, not of
   the transcription, but publishing them as the canonical machine-readable form without a
   prominent, symmetric warning in both directories invites silent numerical error downstream.
   mWater should be asked to issue an erratum.

Beyond that, the group-condition narrowing (D9) is the one structural loss in the data model. It is
correctly documented in both notes but invisible in the tables themselves; a `group_applicability`
column, or a flag on the 18 affected rows, would remove the trap without inventing any text.
