# Extraction notes — Water System Management Standard, Part 1: Asset Management

## 1. Source

| Field | Value |
|---|---|
| Title | *The Water System Management Standard: Part 1 -- Asset Management* |
| Publisher | mWater Foundation |
| Version | 1.0 |
| Date | April 7, 2022 |
| Licence | Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) |
| Google Drive file ID | `1VvorPMQIqoYjFIiQbzwNCDkiTUwC4Q4-gJgHw2ml6pk` |
| Drive mime type | `application/vnd.google-apps.document` |
| Drive `modifiedTime` at extraction | 2024-07-03T06:56:42.980Z |

**Note on version drift:** the Drive document is a *live* Google Doc whose `modifiedTime` is
2024-07-03, more than two years after the "Version 1.0 / April 7, 2022" printed on its title page.
The document body still self-identifies as Version 1.0. This extraction reflects the document as
retrieved on 2026-09-01; it may not be byte-identical to whatever was published on 2022-04-07.

### Method

1. `mcp__Google_Drive__get_file_metadata` — confirmed identity and mime type.
2. `mcp__Google_Drive__download_file_content` with
   `exportMimeType = application/vnd.openxmlformats-officedocument.wordprocessingml.document`
   (the plain `read_file_content` route was not used for the tables, because the `.docx` route
   preserves the bold/italic run formatting that the standard itself uses as the *only* signal
   distinguishing a group name from an attribute name from a choice name — see §6.3 quoted below).
3. Base64-decoded the export to `source.docx` with a short Python script.
4. Parsed with `python-docx` (`source.docx` was a working file and was removed after extraction; re-running `build.py` requires re-downloading it by the steps above). Document-order traversal of `body` (paragraphs interleaved with
   tables) was used to bind each attribute table to the section heading above it. Row
   classification used: *has a 5-digit code* → attribute; *no code and all runs bold* → group;
   *otherwise* → choice option of the attribute immediately above.
5. Build script kept alongside the outputs as `build.py`; the parse log is in `_meta.json`.

## 2. Coverage

| Item | Count | Standard's own stated total |
|---|---|---|
| Asset classes | 5 | 5 ("5 classes", Introduction) |
| Asset types | **29** | **28** ("28 types of assets", Introduction) — **mismatch, see A1** |
| General attributes (Table 5) | 63 | not stated |
| Type-specific attributes (Tables 6–24) | 115 | not stated |
| **Total attributes** | **178** | not stated |
| Choice options | 269 | not stated |
| Attribute groups (distinct headings) | 39 | not stated |
| Unit quantities | 9 | not stated |
| Unit rows (base + alternates) | 49 | not stated |
| Asset types with a type-specific attribute table | 19 of 29 | — |

Attribute counts by class: general 63; System 7; Facility 2; Vertical 102; Horizontal 4; Natural 0.

## 3. Per-table log

| Output file | Document table(s) read |
|---|---|
| `units.csv` | Table 2, "Units of measurement" (§4.2) — python-docx table index 1 |
| `asset-types.csv` | Table 4, "Asset types" (§5.5) — index 3. Class names/definitions cross-checked against Table 3, "Asset classes" (§5.4), index 2 |
| `attributes.csv` (scope=general) | Table 5, "General attributes for all assets" (§6.4) — index 4 |
| `attributes.csv` (scope=type_specific) | Tables 6–24 (§6.5.1.1 – §6.5.4.1) — indices 5–23, bound to types: 5→Water system, 6→Water facility, 7→Source, 8→Pump, 9→Tank, 10→Power, 11→Treatment, 12→Meter, 13→Electrical, 14→Valve, 15→Hydrant, 16→Junction, 17→Sampling point, 18→Sensor, 19→Analyzer, 20→Structure, 21→Water point, 22→Other vertical, 23→Pipe |
| `choices.csv` | Same tables as `attributes.csv` (choice rows) |
| Not extracted to CSV | Table 1, "Data types" (§4.1) — 8 data types + descriptions; reproduced in §6 below |

Document tables 1–24 are numbered in the text as "Table 1" … "Table 24"; python-docx indices are
0-based and therefore one lower. Figures 1 and 2 are **images** and were not machine-readable;
Figure 1 ("Asset classes and types") duplicates Table 4. It was rendered at 220 dpi and read during verification: it shows 28 types and omits "504 Spring". See VERIFICATION-REPORT.md, S1.

## 4. Ambiguities, gaps and judgement calls

### A1. The stated total of asset types (28) does not match Table 4 (29 rows)
The Introduction says "The standard currently recognizes 28 types of assets and 5 classes, as
shown in Figure 1." Table 4 lists **29** asset types. All 29 are recorded. Verification resolved this: Figure 1 shows 28 and omits "504 Spring", so Table 4 is normative and both the Introduction and Figure 1 are stale. Figure 1 is a raster
image and could not be counted to determine which of the two numbers is authoritative, or whether
one type was added after the introductory sentence was written.

### A2. `type_code`: the standard assigns a 3-digit "#", not a 2-digit type code
Table 4's column is headed `#` and contains 3-digit values (101, 201, 301 … 509). §"Standardized
names and definitions" states the composition grammar: *"attributes have a unique numerical ID
code that specifies the class (1-digit), type (2-digits), and attribute (2-digits)"*. `type_code`
in `asset-types.csv` therefore holds the **last two digits** of the "#" (mechanical decomposition
per the standard's own grammar), not the verbatim 3-digit value. Consequence: **`type_code` is
unique only within a class, not globally** — `01` is Water system, Water facility, Source, Pipe
and Reservoir. The verbatim 3-digit values are preserved in the mapping below.

| # | class | type | # | class | type | # | class | type |
|---|---|---|---|---|---|---|---|---|
| 101 | System | Water system | 307 | Vertical | Electrical | 399 | Vertical | Other vertical |
| 201 | Facility | Water facility | 308 | Vertical | Valve | 401 | Horizontal | Pipe |
| 301 | Vertical | Source | 309 | Vertical | Hydrant | 402 | Horizontal | Canal |
| 302 | Vertical | Pump | 310 | Vertical | Junction | 501 | Natural | Reservoir |
| 303 | Vertical | Tank | 311 | Vertical | Sampling point | 502 | Natural | River/stream |
| 304 | Vertical | Power | 312 | Vertical | Sensor | 503 | Natural | Aquifer |
| 305 | Vertical | Treatment | 313 | Vertical | Analyzer | 504 | Natural | Spring |
| 306 | Vertical | Meter | 314 | Vertical | Structure | 505 | Natural | Riparian zone |
| | | | 315 | Vertical | Water point | 506–509 | Natural | Infiltration basin, Forest, Wetland, Watershed |

### A3. Water system attribute codes contradict the Water system type code
Water system is type **101** in Table 4, but every attribute in Table 6 (Water system attributes)
is numbered **102**xx (10201–10207). Under the standard's own code grammar these decode to class 1,
type **02** — a type that does not exist. Every other type's attribute codes agree with its "#"
(Water facility 201→201xx, Source 301→301xx, …, Pipe 401→401xx). Recorded verbatim; **not
corrected**. This is the single most consequential defect found.

### A4. `Asset ID` is used as a data type but is not one of the eight data types
Table 1 (§4.1) defines exactly eight data types: Text, Choice, Number, Date, Geometry, Checkbox,
Image, Unit. Two attributes declare a ninth, undefined data type `Asset ID`:
`00006 Parent asset ID` and `00091 Upstream asset`. The brief asked that `data_type` be one of the
eight; fidelity to the source wins, so **`Asset ID` is recorded verbatim** in `attributes.csv`
rather than being silently coerced to `Text`. Downstream consumers should decide explicitly.

### A5. Attribute group `Hierarchy` is a ninth group
The brief listed eight groups. Table 5 also contains a bold group heading **`Hierarchy`**
(attributes 00031–00037), and it is the only group in the whole document that carries a
description in the Description column (quoted in §6). All 39 group names actually present are
carried in the `attribute_group` column verbatim, including the per-type `… info` / `… data`
groups (`Water system info`, `Well data`, `Pump curve`, `Tank dimensions`, etc.).

### A6. Group-level conditions: inherited into `applicability`, with loss where both exist
§6.3 states that a condition on a group row "applies to all attributes in the group". `applicability`
therefore holds: the attribute's own Conditions cell verbatim if non-empty; otherwise the group's
Conditions cell verbatim (41 attributes inherited this way). **Where an attribute has its own
condition *and* sits inside a conditioned group, only the attribute's own condition is in the CSV
and the group condition is lost.** The 11 affected attributes, with the full conjunction:

| code | name | group condition | own condition |
|---|---|---|---|
| 00092 | Nominal diameter | Type: Pump, Tank, Treatment, Meter, Valve, Hydrant, Junction, Sampling point, Water point, Pipe | Type: Meter, Valve, Junction, Pipe |
| 00093 | Pipe length | *(as above)* | Type: Pipe |
| 00094 | Material | *(as above)* | Type: Meter, Valve, Hydrant, Junction, Pipe |
| 00095 | Minor loss coefficient | *(as above)* | Type: Junction, valve, meter |
| 00096 | Roughness coefficient | *(as above)* | Type: Pipe |
| 10202 | Network type | Type: Water system | Type of system: Distribution |
| 30142 | Spring box length | Source type: Spring | Spring box present: True |
| 30143 | Spring box width | Source type: Spring | Spring box present: True |
| 30144 | Spring box depth | Source type: Spring | Spring box present: True |
| 30155 | Pump position | Source type: Borehole | Pump or lifting device: Submersible |
| 30422 | Generator apparent power | Power type: Generator | Type of current: Single phase AC, Three phase AC |

Note that in five of these the group condition is *wider* than the attribute condition (00092–00096),
so nothing is lost in practice; in the other six the two conditions are independent and the
conjunction genuinely matters.

Full list of group-level conditions as written:

| table | group | condition |
|---|---|---|
| 5 (general) | Hydraulic | Type: Pump, Tank, Treatment, Meter, Valve, Hydrant, Junction, Sampling point, Water point, Pipe |
| 5 (general) | Points of contact | Type: Water system, Water point |
| 6 (Water system) | Water system info | Type: Water system |
| 8 (Source) | Well data | Source type: Borehole, Dug well |
| 8 (Source) | Spring data | Source type: Spring |
| 8 (Source) | Borehole data | Source type: Borehole |
| 9 (Pump) | Pump motor data | Pump motor configuration: Integrated with pump |
| 11 (Power) | Generator data | Power type: Generator |
| 11 (Power) | Solar power data | Power type: Solar |
| 21 (Structure) | Perimeter data | Structure type: Perimeter |

### A7. Conditions that reference attribute or choice names that do not exist
The condition grammar in §6.3 requires "the name of the attribute, type, or class that the
condition depends on". Four conditions do not resolve against any name defined in the standard:

| code | condition as written | problem |
|---|---|---|
| 10202 | `Type of system: Distribution` | No attribute named "Type of system"; the intended attribute is presumably `10201 Water system type`, whose choice is named "Distribution **network**", not "Distribution". Two mismatches in one condition. |
| 30522 | `Chlorination type: Sodium hypochlorite (bleach), Calcium hypochlorite, Chloramine` | No attribute named "Chlorination type"; presumably `30521 Chlorine type`. ("Chlorination data" is the group name.) |
| 30155 | `Pump or lifting device: Submersible` | Attribute `30126 Pump or lifting device` exists, but its choice is named "Submersible **pump**", not "Submersible". |
| 30203, 30204 | `Pump type: NOT Hand pump` | Uses a negation operator `NOT`. §6.3 defines only a name-colon-value-list grammar with comma-separated alternatives; negation is undocumented. |

Also `20102`'s condition `Water facility type: Process area` is well-formed, but the referenced
attribute `20101 Water facility type` has an **empty description** (see A10).

### A8. Case inconsistency in condition value lists
Type names are inconsistently capitalised inside conditions, e.g. `Type: Meter, Water Point`
(00018, capital P), `Type: Water system, water facility` (00021, 00066, 00067, 00070, lowercase w),
`Type: Pump, tank, power, valve` (00071), `Type: Junction, valve, meter` (00095) versus
`Type: Meter, Valve, Junction, Pipe` (00092). Recorded verbatim; a case-sensitive resolver will
fail on these.

### A9. `Water facility info` group carries no `Type:` condition, unlike `Water system info`
Table 7's group heading has an empty Conditions cell, whereas the equivalent group in Table 6 has
`Type: Water system`. All other type-specific tables likewise omit a `Type:` condition on the group
row — applicability to the type is implied only by the section the table appears in. `Water system
info` is the lone exception. `asset_type` in `attributes.csv` records the binding for all of them.

### A10. Five attributes have an empty Description cell
`20101 Water facility type`, `30126 Pump or lifting device`, `31001 Junction type`,
`31201 Sensor type`, `31401 Structure type`. Left empty; not filled in.

### A11. Fifteen choice options have an empty Description cell
All five options (`Very low`, `Low`, `Moderate`, `High`, `Very high`) of each of
`00053 Probability of failure`, `00054 Consequence of failure`, `00055 Asset risk`. The scale is
undefined — the standard gives no thresholds or definitions for these risk bands. Left empty.

### A12. `00001 Type` is a Choice attribute with no choice list
Its description defers to §5.5 ("Type of asset, according to the definitions in Section 5.5"). No
choice rows appear beneath it, so `choices.csv` contains no rows for `00001`. The de facto choice
list is `asset-types.csv`.

### A13. Choice rows that are not italicised
§6.3 says choice names are "displayed indented and in italic font". Eleven rows break this: all
nine choices of `20101 Water facility type` and both choices of `30423 Engine cooling system` are
in normal (non-italic) font. They were classified as choices on the basis of having no code and no
bold, which is unambiguous, but a formatting-only parser would misread them.

### A14. Line-break hyphenation artifact in a data type
`30125 Groundwater temperature` has the data type cell `Unit: Temp-⏎erature` (hyphenated across a
line break inside the cell). Recorded as `unit_quantity = Temperature`. This is a de-hyphenation of
a typographic artifact, not a substantive change.

### A15. Attribute codes are non-contiguous
Within the general table, blocks run 00001–00006, 00011–00023, 00031–00037, 00041–00043,
00051–00057, 00061–00071, 00091–00096, then jump to 00171–00176 and 00181–00184. Codes
00097–00170 are unassigned. Type-specific tables likewise leave gaps (e.g. Source: 30101–30109,
30121–30128, 30141–30146, 30151–30156). No code is duplicated anywhere — the uniqueness check
passed with zero collisions across all 178 attributes.

### A16. Ten asset types have no attribute table
Canal (402) and all nine Natural types (501–509) have no type-specific attributes. §6.5.4.2 and
§6.5.5 both read only "This section is reserved." Recorded as asset types with zero attributes;
this is a deliberate gap in the source, not an extraction failure.

### A17. `allowed_parent_classes` is empty for every asset type
The standard states parent-child relationships exist (§5.3) but places **no** constraint on which
classes or types may parent which. Nothing was inferred; the column is empty throughout. Any
hierarchy implied by Figure 1 was read during verification; see VERIFICATION-REPORT.md, S1.

### A18. `required` is empty for every attribute except `00003 Asset ID`
No attribute table has a required/optional column. The only mandatory-value statement anywhere is
§5.2: "All assets **shall** be assigned an identification code, referred to as the Asset ID".
`00003` is therefore marked `required = TRUE`; every other row is empty. Note that §6.4's "The
following attributes shall be **available** for all assets" is a requirement on the *system*, not
on the *value* — it was not treated as making all 63 general attributes required.

### A19. `units.csv` shape decisions
- One row per unit. The base unit of each quantity appears as its own row with
  `alternate_unit = si_base_unit` and `conversion_factor_to_si = 1`.
- The document's `Symbol` column populates `si_base_unit`/`alternate_unit`; the `Name` and `System`
  columns are preserved in `notes` (`Name: …; System: …`) because the given header has no place for them.
- Conversion factors are verbatim, including Unicode scientific notation (`1 X 10⁻⁶`, `8.64 X 10⁴`).
  They are **not** normalised to floats.
- **Temperature has no conversion factor.** The document puts conversion *formulas* in that column
  (`tF = tC x 1.8 + 32` and `tC = (tF - 32) / 1.8`). These strings are carried verbatim in
  `conversion_factor_to_si` and flagged in `notes`. Anything parsing that column as a number will fail
  on these two rows.
- **The `System` column is wrong for several rows** as printed: `m H₂O`, `cm H₂O` and `mm Hg` are
  marked `SI` although they are conventional/legacy pressure units, and `kVA` is marked `SI` under
  Power. Recorded verbatim; not corrected.
- Quantity names carry footnote markers in the source (`Time*`, `Temperature**`). The markers are
  stripped from `quantity` and the footnote is flagged in `notes`; the footnote text is quoted in §6.

### A20. Derived-identifier rules (`type_id`, `choice_id`)
Purely mechanical: Unicode NFKD, strip combining marks, lowercase, replace every run of
non-`[a-z0-9]` with `_`, trim leading/trailing `_`. Consequences worth knowing:
`River/stream` → `river_stream`; `Sodium hypochlorite (bleach)` → `sodium_hypochlorite_bleach`;
`Uninterruptible power supply (UPS)` → `uninterruptible_power_supply_ups`; `pH` → `ph`;
`60 Hz` → `60_hz` and `50 Hz` → `50_hz` (**these begin with a digit** and are not valid identifiers
in most languages). `choice_id` is unique within its attribute but deliberately **not** globally
unique — `other`, `steel`, `pvc`, `plastic` etc. recur across attributes; the key is
(`attribute_code`, `choice_id`).

### A21. Document is a live Google Doc, not a frozen release artifact
See §1. There is no checksum, DOI or immutable published copy referenced in the document to verify
against.

## 5. Validation performed

- All 178 `code` values in `attributes.csv` are unique — **0 duplicates**.
- All 269 `attribute_code` values in `choices.csv` resolve to a row in `attributes.csv` — **0 orphans**.
- All `asset_type` values in `attributes.csv` resolve to a `type_name` in `asset-types.csv` — **0 unknown**.
- `choice_id` is unique within each `attribute_code` — **0 collisions**.
- Every Choice-typed attribute has at least one choice row except `00001 Type` (see A12).
- All four CSVs parse with `csv.DictReader`; row counts 29 / 178 / 269 / 49.
- `type_code` is *not* unique across `asset-types.csv` by design (see A2).

## 6. Content that does not fit the CSV shape — verbatim

> **§5.2 Unique identification of assets.** "All assets shall be assigned an identification code, referred to as the Asset ID (section 6.4), that is unique with respect to all other assets included in the asset register. Identification codes may be text strings, numerical codes, or mixtures of text and numbers. In order to facilitate the tracking of maintenance interventions and failures over time, the asset ID shall be immutable, meaning it shall never be changed, even when an asset is moved or updated, and it shall never be reused when an asset is replaced or removed from service."

> "Organizational data managers and software providers should consider developing procedures or algorithms to check for and resolve duplicate asset IDs, especially when assets are created offline and later uploaded to a central database."

> "An organization may choose to use a hierarchical coding system, in which parts of the asset ID refer to types, facilities, or other categories that assist in identifying the location or function of the asset. Organizations setting up hierarchical coding systems should take into consideration the following: Assets are often moved from one location to another; Names of administrative regions and facilities change from time to time; and The asset owner or managing organization might change for a facility."

> "The asset coding system and staff procedures shall be designed to maintain a unique and immutable Asset ID over the entire service life of the asset."

> **§5.3 Parent and child relationships.** "Any asset shall have an optional parent asset, which is defined by the value of the Parent ID attribute of the child asset. A child asset shall have only one parent asset, but parent assets may have an unlimited number of child assets."

> **§5.4 Asset classes.** "In this document, asset classes are not necessary to include when describing an asset because the asset types (next section) are unique and sufficient to define the required attributes. However, the asset class can be useful for organizing lists of asset types during data collection, searching, and analysis." … "The asset classes provided in the following table shall be accommodated in asset management systems."

> **§5.5 Asset types.** "The asset types described in the following tables shall be made available to include in the asset management system."

> **§6.2 Characteristics of attributes.** "Attributes and their usage shall conform to the following characteristics: Attributes whose values are unknown or not applicable shall be left blank. The standard does not distinguish between a missing value and an unknown value, but implementers may choose to track additional metadata about attributes that are not answered, such as when an inspector was unable to determine the value. Attributes with conditions shall only be assigned a value when the condition is satisfied. Some attributes are only applicable when another attribute has a certain value or when the asset has a specific class or type. These conditions, which may apply to individual attributes or to groups of attributes, are provided in the attribute tables."

> **§6.3 How to read and interpret attribute tables.** "Code: The 5-digit unique code assigned to each attribute. Group, Attribute, or Choice Name: The unique name used in the standard to refer to the attribute, group, or choice option. Note that the text formatting defines which of these three kinds of name is being defined: Group names are in bold font and do not have an associated attribute ID. Attribute names are in normal font and always have an attribute ID in the row where they appear. Choice names are the names of the answer choices available for the attribute immediately above them and are displayed indented and in italic font. Description: A brief phrase or sentence to further define the meaning or use of the attribute or answer choice. Data type: The data type and unit of measurement defined (see Section 4) to be used with this attribute. In cases where more than one data type is permitted, types are separated by commas (,). Conditions: The condition that must all be met in order for the group or attribute to be applicable. Conditions are formatted with the name of the attribute, type, or class that the condition depends on, followed by a colon (:) and the values or answer choices that satisfy the condition. In cases where multiple values could satisfy the condition, each value is separated by a comma (,). Note that when a condition appears on the same row as a Group name, it applies to all attributes in the group (meaning all attributes that appear below the group name)."

> **§6.4 General attributes.** "The following attributes shall be available for all assets."

> **§6.5 Type-specific attributes.** "The attributes defined in this section apply only to a specific asset type. Some asset types do not currently have type-specific attributes so they do not appear in this section."

> **Code-composition grammar (Introduction, "Standardized names and definitions").** "All types and attributes in this standard have unique names to improve clarity and interoperability in asset management systems. In addition, attributes have a unique numerical ID code that specifies the class (1-digit), type (2-digits), and attribute (2-digits). In cases where attributes have a fixed set of possible values, the choices are also given names and are further defined by descriptions. The descriptions and definitions in this document are based on industry standard terms and cross-referenced against the American Water Works Association Water Dictionary (McTigue et at. 2010) and relevant ISO standards. Implementers are free to substitute their own terms or translations for the types, attributes, and choices specified in this standard but they should ensure that they are traceable back to the standard term for the purposes of data exchange and publication."

> **Hierarchy (Introduction, "Organization of assets").** "Asset management systems typically use hierarchical classification schemes and parent-child relationships to help keep assets organized and help field staff to quickly identify or locate an asset. This standard accommodates up to 7 optional levels of hierarchical classification using attributes whose values are determined and enforced by the organization implementing the standard. In addition, any asset can be assigned a parent asset, creating a parent-child relationship between the two assets."

> **`Hierarchy` group description (Table 5).** "Hierarchy refers to a tiered set of names that help to locate or organize assets; the use of an asset hierarchy is optional and an organization may choose to use fewer levels than the 7 that are available in this standard"

> **Groups and conditions (Introduction, "Attributes").** "Groups are headings that organize data and keep similar attributes together. Every attribute in this standard has a group, even if there is only one attribute in the group. This is intended to provide consistency for programmers to design user interfaces that work the same way for any asset." … "Conditions are rules, based on the values of other attributes or the type of asset, that determine whether or not an attribute is applicable to a particular asset. For example, if the shape of a tank is cylindrical, then the diameter and height need to be recorded whereas a rectangular tank has a length and width but no diameter. Conditions may be applied to individual attributes or to groups of attributes."

> **§4.2 unit conversion rule.** "The conversion factors are expressed with reference to the base unit, such that within each physical quantity the conversion factor for the base unit is always equal to 1. This means that a conversion factor can be treated as the ratio of the current unit to the base unit, or the amount of the base unit that would be equal to one current unit. For example, the conversion factor for centimeters, 0.01, implies that 1 cm = 0.01 m." … "In the case of temperature, the conversion factor approach does not apply. Instead, follow the conversion formulas provided in Table 2."

> **§4.2 Unit-type naming convention.** "Attributes that have the data type of Unit (see Section 4.1) include the name of the physical quantity that is being measured. The name “Unit” is followed by a colon (“:”) and then the name of the physical quantity. For example, the physical quantity of Length would appear in the Data type column of the attribute tables as: “Unit: Length”."

> **Table 2 footnote \*.** "In this standard, time is used to refer to days, months, and years, where one year is defined using the average Gregorian year, defined as exactly 365.2425 days. Months are defined as 1/12 of a Gregorian year. This approximation is useful only for expressing approximate durations, such as intervals between scheduled maintenance activities, and is not intended to be used for calculating exact calendar dates."

> **Table 2 footnote \*\*.** "Temperature is a special case. Use the formula provided, where tF = temperature in degrees Fahrenheit and tC = temperature in degrees Celsius."

### Table 1 — Data types (§4.1), not extracted to CSV

| Data type | Description |
|---|---|
| Text | Any combination of letters, numbers, punctuation, and spaces (also known as Character in some programming languages) |
| Choice | Text field that has a fixed set of possible values (also known as an Enumeration or Factor) |
| Number | Any integer or decimal number, consisting of a whole number part and an optional decimal part, with either a fixed or variable number of digits after the decimal point |
| Date | Calendar date according to the Gregorian calendar that includes the 4-digit year, 2-digit month, and 2-digit day in that order, and optionally separated by a delimiting character Example: 2021.05.07 and 20210507 both specify the 7th day of May in the Year 2021 |
| Geometry | Location of a point, line, or polygon on the surface of the earth, according to the WGS84 geographic coordinate system (any common file format for geographical data may be used, including GeoJSON or ESRI Shape File) |
| Checkbox | Binary outcome that can only have values of TRUE or FALSE; checkbox questions default to FALSE unless the user changes the value to TRUE (also known as Boolean or Logical) |
| Image | Image file in any common format, such as JPG or PNG |
| Unit | Physical quantity that has both a magnitude (a number) and a unit of measurement |

### Table 3 — Asset classes (§5.4), incl. the Geometry column that has no home in `asset-types.csv`

| Asset class | Description | Geometry |
|---|---|---|
| System | Collection of assets that are managed in a similar manner to provide a service. | Point or polygon |
| Facility | Physical location where specific functions are performed. | Point or polygon |
| Vertical | Asset within a building or facility, or free-standing, often composed of multiple components; also known as an above ground asset (AWWA 2018). | Point |
| Horizontal | Asset which may be configured or networked for the purpose of moving materials or services from one place to another, such as pipes or conduits (AWWA 2018); also known as below ground assets, but may exist above or below ground. | Line |
| Natural | Strategically planned and managed natural lands, such as forests and wetlands, working landscapes, and other open places that provide associated benefits to human populations (Benedict and McMahon, 2006); also known as natural infrastructure. | Line or Polygon |

### §3 Terms and definitions, not extracted to CSV

> **3.0.1 asset ID** — "a code used to identify a particular asset that is unique within the asset register (see Section 5.2 for requirements regarding unique identification of assets)"
> **3.0.2 asset management system** — "the policies and procedures that an organization uses to manage assets"
> **3.0.3 asset portfolio** — "assets that are within the scope of the asset management system"
> **3.0.4 asset register** — "a complete listing of the asset information of an organization"
> **3.0.5 attribute ID** — "a unique 5-digit code used in this standard to refer to a specific attribute"
> **3.0.6 conduit** — "any artificial or natural duct, either open or closed, for conveying fluids"
> **3.0.7 unit of measurement** — "a definite magnitude of a physical quantity, defined by convention or law, that is used as a standard for measurement of the same kind of quantity"

### §1 Scope, §2 Normative references

> **§1** "This document provides guidance for managing and sharing data about a water supply and distribution system. This standard is applicable to any engineered or constructed works designed to deliver water for human use and consumption. Use of this standard does not require or depend on the use of a particular software application or database technology."

> **§2** "There are no normative references in this document."
