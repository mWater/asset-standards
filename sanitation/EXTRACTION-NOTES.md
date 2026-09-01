# Extraction notes — Sanitation System Management Standard: Part 1 — Asset Management

## 1. Source and method

| Field | Value |
| --- | --- |
| Document title | The Sanitation System Management Standard: Part 1 — Asset Management |
| Drive file name | Sanitation System Management Standard - Part 1 - Asset Management v1.docx |
| Google Drive file ID | `1o3EPYaCmgzGlk5ZrHiPnan4-BNpEum8R` |
| MIME type | application/vnd.openxmlformats-officedocument.wordprocessingml.document (native .docx, not a Google Doc) |
| Publisher | mWater Foundation |
| Version | 1.0 |
| Date | 21 August 2026 |
| Drive modifiedTime | 2026-08-21T20:12:49.992Z |
| File size | 262,558 bytes |
| Licence | Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) |
| Extraction date | 2026-09-01 |

**Licence statement, verbatim from the Foreword:**

> This document is distributed by mWater Foundation under the open source Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0). You are free to share (copy and redistribute in any medium or format) and to adapt (remix, transform, and build upon for any purpose, even commercially) the material in this document, but you must provide attribution to mWater Foundation, indicate if changes were made, and distribute your contributions under the same license (ShareAlike). You may not apply any additional restrictions, such as legal terms or technological measures, that legally restrict others from doing anything the license permits.

**Method.** `mcp__Google_Drive__get_file_metadata` confirmed the MIME type and title. `mcp__Google_Drive__download_file_content` (no `exportMimeType`, since the file is already .docx) returned the file as base64; a short Python script base64-decoded it to `source.docx` in this directory. All tables were parsed with `python-docx` (`pip install python-docx --break-system-packages`) reading the document body in document order, so that each table could be tied to the heading and caption that precede it. `read_file_content` was not needed.

**How rows were classified.** Section 6.3 of the standard states that within an attribute table, group names are bold, attribute names are in normal font and always carry a code, and choice names are italic and indented. The parser reads the run-level bold/italic properties of the second column of every table row and applies exactly that rule. It does not guess from text content. Every row of every attribute table was classified as header, group, attribute or choice, with zero unclassifiable rows.

## 2. Coverage

| Item | Count |
| --- | ---: |
| Asset classes | 4 |
| Asset types | 27 |
| General attributes (Table 5) | 76 |
| Type-specific attributes (Tables 6–31) | 135 |
| **Total attributes** | **211** |
| Choice options | 445 |
| Choice-typed attributes | 70 |
| Unit quantities (Table 2) | 11 |
| Individual units of measurement (Table 2) | 58 |
| Data types (Table 1) | 8 |

Asset types by class: System 2, Facility 1, Vertical 22, Horizontal 2.

Unit quantities present: Length, Pressure, Flow rate, Mass flow, Area, Voltage, Power, Current, Volume, Time, Temperature.

### 2.1 Comparison against mWater's published figures

mWater's public communications state that this standard has **27 asset types and 211 attributes**.

| Figure | Published | Extracted | Difference |
| --- | ---: | ---: | ---: |
| Asset types | 27 | 27 | +0 |
| Attributes | 211 | 211 | +0 |

**Both figures agree exactly.** The document itself also states in "Classification of assets": "The standard currently recognizes 27 types of assets and 4 classes, as shown in Figure 1." No adjustment of any kind was made to reach these numbers; they are the raw parse counts. Note that the 211 total counts attribute rows only — group heading rows and choice rows are not attributes and are excluded, consistent with section 6.3.

## 3. Per-table log

| Document table | Content | Output |
| --- | --- | --- |
| Table 1 | Data types | not exported as a CSV; used to validate the data_type column of attributes.csv and quoted in section 7 below |
| Table 2 | Units of measurement | units.csv |
| Table 3 | Asset classes | asset_class values in asset-types.csv (names and order); descriptions/geometry not exported (no column in the given headers) |
| Table 4 | Asset types | asset-types.csv |
| Table 5 | General attributes for all assets | attributes.csv (scope=general) + choices.csv |
| Table 6 | Sanitation system attributes | attributes.csv (asset_type=Sanitation system, 9 attributes) + choices.csv (19 choices) |
| Table 7 | Facility attributes | attributes.csv (asset_type=Facility, 3 attributes) + choices.csv (8 choices) |
| Table 8 | Sanitation point attributes | attributes.csv (asset_type=Sanitation point, 5 attributes) + choices.csv (19 choices) |
| Table 9 | Connection attributes | attributes.csv (asset_type=Connection, 5 attributes) + choices.csv (9 choices) |
| Table 10 | Containment attributes | attributes.csv (asset_type=Containment, 8 attributes) + choices.csv (23 choices) |
| Table 11 | Vehicle attributes | attributes.csv (asset_type=Vehicle, 4 attributes) + choices.csv (7 choices) |
| Table 12 | Manhole attributes | attributes.csv (asset_type=Manhole, 8 attributes) + choices.csv (21 choices) |
| Table 13 | Junction attributes | attributes.csv (asset_type=Junction, 1 attributes) + choices.csv (9 choices) |
| Table 14 | Valve attributes | attributes.csv (asset_type=Valve, 2 attributes) + choices.csv (7 choices) |
| Table 15 | Flow control attributes | attributes.csv (asset_type=Flow control, 2 attributes) + choices.csv (19 choices) |
| Table 16 | Structure attributes | attributes.csv (asset_type=Structure, 5 attributes) + choices.csv (12 choices) |
| Table 17 | Power attributes | attributes.csv (asset_type=Power, 13 attributes) + choices.csv (20 choices) |
| Table 18 | Electrical attributes | attributes.csv (asset_type=Electrical, 2 attributes) + choices.csv (15 choices) |
| Table 19 | Meter attributes | attributes.csv (asset_type=Meter, 5 attributes) + choices.csv (15 choices) |
| Table 20 | Sampling point attributes | attributes.csv (asset_type=Sampling point, 3 attributes) + choices.csv (7 choices) |
| Table 21 | Sensor attributes | attributes.csv (asset_type=Sensor, 3 attributes) + choices.csv (16 choices) |
| Table 22 | Analyzer attributes | attributes.csv (asset_type=Analyzer, 2 attributes) + choices.csv (15 choices) |
| Table 23 | Datalogger attributes | attributes.csv (asset_type=Datalogger, 1 attributes) + choices.csv (5 choices) |
| Table 24 | Pump attributes | attributes.csv (asset_type=Pump, 15 attributes) + choices.csv (14 choices) |
| Table 25 | Tank attributes | attributes.csv (asset_type=Tank, 12 attributes) + choices.csv (21 choices) |
| Table 26 | Treatment attributes | attributes.csv (asset_type=Treatment, 8 attributes) + choices.csv (62 choices) |
| Table 27 | Dispersal attributes | attributes.csv (asset_type=Dispersal, 1 attributes) + choices.csv (6 choices) |
| Table 28 | Outfall attributes | attributes.csv (asset_type=Outfall, 4 attributes) + choices.csv (10 choices) |
| Table 29 | Other vertical attributes | attributes.csv (asset_type=Other vertical, 1 attributes) + choices.csv (0 choices) |
| Table 30 | Pipe attributes | attributes.csv (asset_type=Pipe, 7 attributes) + choices.csv (14 choices) |
| Table 31 | Channel attributes | attributes.csv (asset_type=Channel, 6 attributes) + choices.csv (8 choices) |

Figure 1 ("Asset classes and types") and Figure 2 ("Illustration of general and type-specific attributes and groups of attributes") are embedded images. They were not machine-read; nothing in the CSVs derives from them. Figure 1 restates Table 4 and Figure 2 restates the narrative of section "Attributes", so no data is believed to be lost — but this is stated as an assumption, not a verified fact.

Section 6.5.1.2 (Subsystem) contains only the sentence "This section is reserved." and has no table. Subsystem therefore appears in asset-types.csv but has zero type-specific attributes. Section 6.5 states: "The attributes defined in this section apply only to a specific asset type. Some asset types do not currently have type-specific attributes so they do not appear in this section."

## 4. Derivation and column-population decisions

Only one derived value is permitted by the extraction brief (`type_id`). Everything else below records where a column in the requested header had no direct source in the document.

- **`asset-types.csv` / `type_code`** — Table 4 gives a 3-digit number in a column headed `#`, e.g. `101`, `315`, `402`. Per the code-composition rule (section "Standardized names and definitions") the first digit is the class and the remaining two are the type. `type_code` therefore holds the last two digits of the document value verbatim (`01`, `15`, `02`). **`type_code` is unique only within a class, not globally**: `01` is used by Sanitation system (101), Facility (201) and Pipe (401); `02` by Subsystem (102), Pump (302) and Channel (402). The full 3-digit document value is recoverable as class-digit + `type_code`.
- **`asset-types.csv` / `type_id`** — the one permitted derived value. Mechanically produced from `type_name` by lower-casing, replacing every run of non-alphanumeric characters with a single underscore, and trimming leading/trailing underscores. All 27 are unique.
- **`asset-types.csv` / `allowed_parent_classes`** — **left empty in all 27 rows.** The standard places no class or type restriction on parentage. Section 5.3 says only: "Any asset shall have an optional parent asset, which is defined by the value of the Parent ID attribute of the child asset. A child asset shall have only one parent asset, but parent assets may have an unlimited number of child assets." No table or figure in the document constrains which class may parent which. Populating this column would have required inventing a rule.
- **`attributes.csv` / `asset_class`** — **left empty in all 211 rows.** The standard scopes attributes as either general (all assets) or type-specific (one named type). It never scopes an attribute to a class. No condition string in the document uses a class-level predicate; every type predicate is written as `Type: ...`, `All types except: ...` or `Type is not ...`. The class of a type-specific attribute is recoverable by joining `asset_type` to asset-types.csv.
- **`attributes.csv` / `required`** — **left empty in all 211 rows.** The document has no required/optional column and marks no individual attribute as mandatory. Section 6.4 says only "The following attributes shall be available for all assets.", which is a requirement on the system to offer the field, not on the data collector to fill it. Section 6.2 point 1 states the opposite for values: "Attributes whose values are unknown or not applicable shall be left blank. The standard does not distinguish between a missing value and an unknown value, but implementers may choose to track additional metadata about attributes that are not answered, such as when an inspector was unable to determine the value."
- **`attributes.csv` / `data_type`, `unit_quantity`, `si_unit`** — where the document's Data type cell reads `Unit: <quantity>` (section 4.2 defines that notation), `data_type` is set to `Unit` and `unit_quantity` to the quantity name verbatim. `si_unit` is a lookup of that quantity's base unit — the first unit listed under the quantity in Table 2, which section 4.2 defines as the base unit with conversion factor 1. Where the Data type cell is a plain type it is copied verbatim.
- **`attributes.csv` / `applicability`** — the Conditions cell, verbatim. See section 5.3 below for the group-condition inheritance decision.
- **`attributes.csv` / `attribute_group`** — the bold group heading in force at that row, verbatim from the document. The document uses 42 distinct group names, not the 9-name list suggested in the brief; the document's own names were used. The 9 suggested names all occur (though the document writes "Basic Info", with a capital I, not "Basic info"), but each type-specific table adds its own group headings such as "Pump curve", "Solar power data", "Tank dimensions".
- **`choices.csv` / `choice_id`** — mechanical lower_snake_case of `choice_name` by the same rule as `type_id`. No collisions occur within any attribute, so `(attribute_code, choice_id)` is unique across all 445 rows.
- **`units.csv`** — one row per unit listed in Table 2, including the base unit itself (which appears with `alternate_unit` equal to `si_base_unit` and conversion factor `1`). The unit **name** and the SI/US **System** column have no column in the requested header, so they are preserved in `notes` as `Name: <name>; System: <SI|US>`. Superscript characters in symbols and factors (m³, µm, ⁻⁶, ₂) are preserved as Unicode.

## 5. Ambiguities, gaps and defects found in the source

Nothing below was corrected in the CSVs. All values are as published.

### 5.1 Code-composition rule and the codes that break it

The rule, verbatim from "Standardized names and definitions": "attributes have a unique numerical ID code that specifies the class (1-digit), type (2-digits), and attribute (2-digits)." Section 3.0.5 adds: "attribute ID — a unique 5-digit code used in this standard to refer to a specific attribute."

All 211 codes were checked against this rule (first digit = class digit of the owning type, digits 2–3 = the type's 2-digit code, digits 4–5 = the attribute serial). **All 211 are exactly 5 digits and all 211 are unique — there are no duplicates.** Twenty codes do not compose as the rule predicts:

**(a) Sanitation system attributes carry the Subsystem type code (9 attributes).** Table 4 assigns Sanitation system the number `101` and Subsystem `102`. But Table 6, headed "6.5.1.1 Sanitation system" / "Table 6. Sanitation system attributes", uses codes `10201`–`10209`, i.e. class 1 + type **02** = Subsystem. Under the composition rule these nine codes decode to Subsystem, not Sanitation system.

| Code | Name | Table 4 number for Sanitation system | Prefix implied by code |
| --- | --- | --- | --- |
| 10201 | Sanitation system type | 101 | 102 (Subsystem) |
| 10202 | Sewer network type | 101 | 102 (Subsystem) |
| 10203 | Management type | 101 | 102 (Subsystem) |
| 10204 | Number of households in service area | 101 | 102 (Subsystem) |
| 10205 | Number of households currently served | 101 | 102 (Subsystem) |
| 10206 | System or network diagram | 101 | 102 (Subsystem) |
| 10207 | Total treatment capacity | 101 | 102 (Subsystem) |
| 10208 | Sewer technology | 101 | 102 (Subsystem) |
| 10209 | Design capacity (population equivalent) | 101 | 102 (Subsystem) |

This is a genuine ambiguity with two mutually exclusive readings and no evidence in the document to settle it: either the nine codes are mistyped and should be `101xx`, or the section/caption headings are wrong and these are Subsystem attributes (which would contradict 6.5.1.2 "This section is reserved"). **In attributes.csv these nine rows carry `asset_type = Sanitation system`, following the section heading and table caption, with the code left verbatim as published.** The heading was preferred over the code because the attribute names themselves ("Sanitation system type", "Sewer network type", "Total treatment capacity") are plainly system-level, and because 6.5.1.2 explicitly reserves the Subsystem section. This is a judgement call and is the single largest interpretive risk in this extraction.

**(b) Eleven general attributes use a 3-digit attribute serial (11 attributes).** General attributes are numbered `00001`–`00099` (class 0, type 00, attribute 01–99), which fits the rule. But the "Points of contact" and "Metadata" groups are numbered `00171`–`00176` and `00181`–`00185`. Read under the rule these decompose as class 0 + type **01** + attribute 71/81, i.e. they claim a type code of `01` rather than `00`. Read the way they were evidently intended — a 3-digit serial 171–185 in a `00`-prefixed general block — they exceed the 2-digit attribute field. Either way the 5-digit composition rule does not hold for them.

| Code | Name | Group |
| --- | --- | --- |
| 00171 | Primary contact name | Points of contact |
| 00172 | Primary contact position | Points of contact |
| 00173 | Primary contact phone number | Points of contact |
| 00174 | Secondary contact name | Points of contact |
| 00175 | Secondary contact position | Points of contact |
| 00176 | Secondary contact phone number | Points of contact |
| 00181 | Date updated | Metadata |
| 00182 | Date inspected | Metadata |
| 00183 | Alternate ID | Metadata |
| 00184 | Import code | Metadata |
| 00185 | Permit or licence number | Metadata |

**(c) All other 191 codes compose correctly**, including `39901` (Other vertical, type 399) and `40101`–`40207` (Pipe 401, Channel 402).

### 5.2 A data type that is not one of the eight defined data types

Table 1 defines exactly eight data types: Text, Choice, Number, Date, Geometry, Checkbox, Image, Unit. Three attributes have a Data type cell reading **`Asset ID`**, which is not among them. `Asset ID` is defined as a term in section 3.0.1 and as a concept in section 5.2, but never as a data type.

| Code | Name | Table | Data type as published |
| --- | --- | --- | --- |
| 00006 | Parent asset | Table 5 (general) | Asset ID |
| 00091 | Upstream asset | Table 5 (general) | Asset ID |
| 00097 | Downstream asset | Table 5 (general) | Asset ID |

**These three rows keep `Asset ID` verbatim in `data_type`.** Mapping them to `Text` would have been an invention; section 5.2 states "Identification codes may be text strings, numerical codes, or mixtures of text and numbers", so even the obvious guess is not unambiguous.

### 5.3 Group-level conditions

Section 6.3 states: "Note that when a condition appears on the same row as a Group name, it applies to all attributes in the group (meaning all attributes that appear below the group name)." Two groups in Table 5 carry a condition on the group row:

- **Hydraulic** — `Type: Pump, Tank, Treatment, Meter, Valve, Flow control, Junction, Sampling point, Sanitation point, Containment, Manhole, Dispersal, Outfall, Pipe, Channel, Connection`
- **Points of contact** — `Type: Sanitation system,Subsystem, Facility, Sanitation point` (note the missing space after the first comma; reproduced verbatim)

The requested header has no column for a group-level condition. The rule applied, and the reason:

- Where an attribute's own Conditions cell is **blank** and its group carries a condition, `applicability` holds the **group's condition, verbatim**. This affects 8 attributes: `00091` Upstream asset, `00097` Downstream asset (Hydraulic), and `00171`–`00176` (Points of contact). Leaving these blank would have wrongly presented them as unconditional.
- Where an attribute has **its own** condition and its group also has one, `applicability` holds the **attribute's own condition, verbatim**, and the group condition is not represented in the CSV. This affects 7 attributes, all in the Hydraulic group: `00092` Nominal diameter, `00093` Pipe length, `00094` Material, `00095` Minor loss coefficient, `00096` Roughness coefficient, `00098` Conveyed content, `00099` Invert level. **For these 7 rows, both conditions apply in the standard; attributes.csv shows only the narrower one.** A consumer needing the full predicate must AND the Hydraulic group condition above onto these seven. No text was merged or rewritten, because concatenating two condition strings would have produced a string that appears nowhere in the source.

### 5.4 A condition that references choice values which do not exist

Attribute `30521` (Primary chemical used, Treatment) has the condition `Treatment type: Chlorination, Disinfection, Chemical feed, Coagulation or flocculation, Nutrient removal (nitrogen or phosphorus), Lime stabilization`. `Treatment type` is attribute `30501`, whose published choice list contains **Coagulation or flocculation** and **Lime stabilization** but does **not** contain **Chlorination**, **Disinfection**, **Chemical feed** or **Nutrient removal (nitrogen or phosphorus)**. The nearest published choices are "Chlorine contact tank", "UV or ozone disinfection unit" and "Chemical dosing system", but no mapping is stated. The condition is recorded verbatim; nothing was remapped. Every other attribute-value condition in the document (35 of the 36 in total) resolves cleanly to an existing attribute name and existing choice names.

### 5.5 A Choice attribute with no choice list

Attribute `00001` **Type** has data type `Choice` but no italic choice rows beneath it in Table 5. Its value set is evidently the 27 asset types of Table 4, but the document never says so. **No choice rows were generated for `00001`.** All other 69 Choice-typed attributes have at least one choice option.

### 5.6 Choice options with no description

15 choice rows have an empty Description cell. They are the five-point scales of three general Financial attributes, where the choice names (Very low / Low / Moderate / High / Very high) are presumably self-explanatory. The `description` field is left empty for these rows.

| Attribute | Name | Choices with no description |
| --- | --- | --- |
| 00053 | Probability of failure | Very low, Low, Moderate, High, Very high |
| 00054 | Consequence of failure | Very low, Low, Moderate, High, Very high |
| 00055 | Asset risk | Very low, Low, Moderate, High, Very high |

### 5.7 Naming inconsistencies between narrative and attribute tables

- Section 5.3 refers to "the value of the **Parent ID** attribute of the child asset". No attribute named "Parent ID" exists. The attribute that performs this role is `00006` **Parent asset** ("Asset ID of the asset that is a parent to this asset").
- Section 5.2 refers to "an identification code, referred to as the **Asset ID** (section 6.4)". No attribute named "Asset ID" exists in section 6.4. The attribute that performs this role is `00003` **Unique ID**. `Asset ID` is separately used as a *data type* label on three attributes (see 5.2 above), which compounds the ambiguity.
- Attribute `00027` Land occupancy has the condition `All types except: Sanitation system, subsystem` — "subsystem" is lower-case where every other type reference in the document is capitalised. Recorded verbatim.
- The Points of contact group condition reads `Type: Sanitation system,Subsystem, Facility, Sanitation point` with a missing space after the first comma. Recorded verbatim.
- The Table 5 group heading is "Basic Info" (capital I). The brief's suggested vocabulary uses "Basic info". The document's spelling is used.

### 5.8 Two condition grammars for negation

Section 6.3 documents only the `Name: value, value` form. The document actually uses four forms: `Type: ...` (most attributes), `All types except: ...` (`00027`, `00071`), `Type is not <value>` (`00041` Status), and `<Attribute> is not <value>` (`30203`, `30204`: "Pump type is not Manual pump"). The negative forms are undocumented in 6.3. All are recorded verbatim; no condition was normalised into a canonical grammar.

### 5.9 Table 2 conversion factors that appear internally inconsistent

Section 4.2 states the rule: "The conversion factors are expressed with reference to the base unit, such that within each physical quantity the conversion factor for the base unit is always equal to 1. This means that a conversion factor can be treated as the ratio of the current unit to the base unit, or the amount of the base unit that would be equal to one current unit. In the case of temperature, the conversion factor approach does not apply; instead, follow the conversion formulas provided in Table 2." Under that rule the factor should be the number of base units in one of the listed units. Several **Flow rate** factors do not satisfy it — they appear to be reciprocals or otherwise mis-scaled relative to the base unit m³/s:

| Unit | Published factor | Value implied by the stated rule |
| --- | --- | --- |
| m³/d | 8.64 X 10⁴ | 1.157 X 10⁻⁵ |
| m³/hr | 3600 | 2.778 X 10⁻⁴ |
| L/min | 60 | 1.667 X 10⁻⁵ |
| L/d | 86.4 | 1.157 X 10⁻⁸ |
| ML/d | 8.64 X 10⁷ | 1.1574 X 10⁻² |
| gal/min (gpm) | 6.30902 X 10⁵ | 6.30902 X 10⁻⁵ |
| gal/d | 4.38126 X 10⁸ | 4.38126 X 10⁻⁸ |

`L/s` (0.001) and `Mgal/d` (0.0438126) in the same block do satisfy the rule, so the block is internally inconsistent rather than uniformly using a different convention. Separately, **Volume / acre-ft is published as 1223.489**; 1 acre-foot is 1233.48 m³, so this looks like a digit transposition. **All factors in units.csv are exactly as published. None were corrected.** Consumers should treat the Flow rate block and acre-ft as needing confirmation from mWater before use. Verification compared the two standards directly and found a further contradiction: the water standard publishes gal/min as 6.30902 X 10⁻⁵ and gal/d as 4.38126 X 10⁻⁸, while the sanitation standard publishes the same mantissas with positive exponents. See VERIFICATION-REPORT.md, S7.

Two further observations on Table 2, offered without change: **kVA (kilovolt-amps)** is listed under **Power** with factor 1000, though kVA measures apparent power rather than the real power measured in watts; and **Temperature** is present in Table 2 as an 11th quantity, with formulas instead of factors, but no attribute in the standard has data type `Unit: Temperature` — so Temperature is defined but unused. The 10 quantities that are used are exactly the 10 named in the extraction brief.

### 5.10 Items checked and found clean

- No malformed, merged or ragged table rows anywhere in the document. Every attribute table has the same 5 columns and a correct header row.
- No duplicate attribute codes (211 codes, 211 distinct).
- No duplicate type names or type_ids; no duplicate choice_ids within an attribute.
- Every `attribute_code` in choices.csv exists in attributes.csv; every `asset_type` in attributes.csv exists in asset-types.csv.
- Section 6.3 allows multiple data types separated by commas ("In cases where more than one data type is permitted, types are separated by commas"). **No attribute in the document actually uses this**, so no multi-valued `data_type` cell had to be handled.
- No attribute has an empty Name or Description cell.

## 6. Validation performed

All four CSVs were re-read with Python's `csv` module after writing. RFC 4180, UTF-8, LF line endings, minimal quoting, one header row exactly as specified.

| File | Data rows | Checks |
| --- | ---: | --- |
| asset-types.csv | 27 | 27 unique type_ids; type_code unique within class (see 4); all 4 class names from Table 3 |
| attributes.csv | 211 | 211 unique codes, all 5 digits; all asset_type values resolve to asset-types.csv; data_type in the 8 defined types plus the 3 `Asset ID` exceptions of 5.2 |
| choices.csv | 445 | all attribute_codes resolve to attributes.csv; all parents are Choice-typed |
| units.csv | 58 | 11 quantities, each with exactly one base unit at factor 1 |

## 7. Narrative rules quoted verbatim

These are the rules of the standard that do not fit the CSV shape. All are exact quotations.

### 7.1 Code composition and standardized names ("Standardized names and definitions")

> All types and attributes in this standard have unique names to improve clarity and interoperability in asset management systems. In addition, attributes have a unique numerical ID code that specifies the class (1-digit), type (2-digits), and attribute (2-digits). In cases where attributes have a fixed set of possible values, the choices are also given names and are further defined by descriptions. The descriptions and definitions in this document are based on industry standard terms and cross-referenced against relevant standards and recognized sanitation-sector references. Implementers are free to substitute their own terms or translations for the types, attributes, and choices specified in this standard but they should ensure that they are traceable back to the standard term for the purposes of data exchange and publication.

Section 3.0.5, terms and definitions:

> **attribute ID** — a unique 5-digit code used in this standard to refer to a specific attribute

### 7.2 Classification into classes and types ("Classification of assets")

> This standard classifies assets using a two-tiered structure that consists of types of assets that are organized into classes. The asset types are unique and sufficient to describe an asset. Classes are not required to define a type, they are simply useful groupings that reflect common industry practices. The standard currently recognizes 27 types of assets and 4 classes, as shown in Figure 1.

Section 5.4:

> Asset classes are useful groupings of asset types that fulfill similar functions and tend to have a common asset management strategy (AWWA 2018). In this document, asset classes are not necessary to include when describing an asset because the asset types (next section) are unique and sufficient to define the required attributes. However, the asset class can be useful for organizing lists of asset types during data collection, searching, and analysis.

> The asset classes provided in the following table shall be accommodated in asset management systems.

Section 5.5:

> An asset type is a grouping of assets with common characteristics that distinguish them as a group (ISO 55000). In this document, asset types are used to determine which type-specific attributes can be added to that particular asset. The asset types described in the following tables shall be made available to include in the asset management system.

### 7.3 Hierarchy and parent–child rules

"Organization of assets":

> Asset management systems typically use hierarchical classification schemes and parent-child relationships to help keep assets organized and help field staff to quickly identify or locate an asset. This standard accommodates up to 7 optional levels of hierarchical classification using attributes whose values are determined and enforced by the organization implementing the standard. In addition, any asset can be assigned a parent asset, creating a parent-child relationship between the two assets.

Section 5.3, Parent and child relationships:

> Any asset shall have an optional parent asset, which is defined by the value of the Parent ID attribute of the child asset. A child asset shall have only one parent asset, but parent assets may have an unlimited number of child assets.

### 7.4 Uniqueness and immutability of the Asset ID (section 5.2)

> All assets shall be assigned an identification code, referred to as the Asset ID (section 6.4), that is unique with respect to all other assets included in the asset register. Identification codes may be text strings, numerical codes, or mixtures of text and numbers. In order to facilitate the tracking of maintenance interventions and failures over time, the asset ID shall be immutable, meaning it shall never be changed, even when an asset is moved or updated, and it shall never be reused when an asset is replaced or removed from service.

> Organizational data managers and software providers should consider developing procedures or algorithms to check for and resolve duplicate asset IDs, especially when assets are created offline and later uploaded to a central database.

> An organization may choose to use a hierarchical coding system, in which parts of the asset ID refer to types, facilities, or other categories that assist in identifying the location or function of the asset. Organizations setting up hierarchical coding systems should take into consideration the following:

> - Assets are often moved from one location to another;
> - Names of administrative regions and facilities change from time to time; and
> - The asset owner or managing organization might change for a facility.

> The asset coding system and staff procedures shall be designed to maintain a unique and immutable Asset ID over the entire service life of the asset.

### 7.5 General vs type-specific attributes, groups and conditions ("Attributes")

> The standard recognizes that there are some general attributes that apply to most or all assets and other type-specific attributes that only are relevant for certain kinds of assets. For example, most (but not all) types of equipment have a manufacturer, model, and serial number, but only containment structures have a storage volume.

> Distinguishing between general and type-specific attributes is helpful but not always sufficient to determine which kind of attribute applies to a certain asset, so the standard provides two additional concepts to help manage attributes:

> - Groups are headings that organize data and keep similar attributes together. Every attribute in this standard has a group, even if there is only one attribute in the group. This is intended to provide consistency for programmers to design user interfaces that work the same way for any asset.
> - Conditions are rules, based on the values of other attributes or the type of asset, that determine whether or not an attribute is applicable to a particular asset. For example, if the shape of a tank is cylindrical, then the diameter and height need to be recorded whereas a rectangular tank has a length and width but no diameter. Conditions may be applied to individual attributes or to groups of attributes.

### 7.6 Characteristics of attributes (section 6.2)

> Attributes and their usage shall conform to the following characteristics:

> 1. Attributes whose values are unknown or not applicable shall be left blank. The standard does not distinguish between a missing value and an unknown value, but implementers may choose to track additional metadata about attributes that are not answered, such as when an inspector was unable to determine the value.
> 2. Attributes with conditions shall only be assigned a value when the condition is satisfied. Some attributes are only applicable when another attribute has a certain value or when the asset has a specific class or type. These conditions, which may apply to individual attributes or groups of attributes, are provided in the attribute tables.

### 7.7 How to read and interpret attribute tables (section 6.3)

> All attributes defined in this standard are organized into tables that follow a consistent format with the following headings:

> - Code: The 5-digit unique code assigned to each attribute.
> - Group, Attribute, or Choice Name: The unique name used in the standard to refer to the attribute, group, or choice option. Note that the text formatting defines which of these three kinds of name is being defined:
>   - Group names are in bold font and do not have an associated attribute ID.
>   - Attribute names are in normal font and always have an attribute ID in the row where they appear.
>   - Choice names are the names of the answer choices available for the attribute immediately above them and are displayed indented and in italic font.
> - Description: A brief phrase or sentence to further define the meaning or use of the attribute or answer choice.
> - Data type: The data type and unit of measurement defined (see Section 4) to be used with this attribute. In cases where more than one data type is permitted, types are separated by commas (,).
> - Conditions: The condition that must all be met in order for the group or attribute to be applicable. Conditions are formatted with the name of the attribute, type, or class that the condition depends on, followed by a colon (:) and the values or answer choices that satisfy the condition. In cases where multiple values could satisfy the condition, each value is separated by a comma (,). Note that when a condition appears on the same row as a Group name, it applies to all attributes in the group (meaning all attributes that appear below the group name).

### 7.8 Scope of general and type-specific sections

> The following attributes shall be available for all assets. (section 6.4)

> The attributes defined in this section apply only to a specific asset type. Some asset types do not currently have type-specific attributes so they do not appear in this section. (section 6.5)

### 7.9 Units of measurement notation (section 4.2)

> Attributes that have the data type of Unit (see Section 4.1) include the name of the physical quantity that is being measured. The name "Unit" is followed by a colon (":") and then the name of the physical quantity. For example, the physical quantity of Length would appear in the Data type column of the attribute tables as: "Unit: Length".

> The units of measurement required to use this standard and their conversion factors are defined in Table 2. Each physical quantity has a base unit, which appears first in the table, and is defined by the International System of Units (SI). Conversion factors included in this section for SI units are derived from the SI Brochure (BIPM 2019).

> The conversion factors are expressed with reference to the base unit, such that within each physical quantity the conversion factor for the base unit is always equal to 1. This means that a conversion factor can be treated as the ratio of the current unit to the base unit, or the amount of the base unit that would be equal to one current unit. In the case of temperature, the conversion factor approach does not apply; instead, follow the conversion formulas provided in Table 2.

> \* Temperature is a special case. Use the formula provided, where t_F = temperature in degrees Fahrenheit and t_C = temperature in degrees Celsius. (Table 2 footnote)

### 7.10 Using the standard

> Organizations are encouraged to use this standard to design and develop infrastructure asset management systems that meet their unique needs, capabilities, and values. The standard is simple enough that it could be implemented using a spreadsheet or ledger, but organizations are encouraged to incorporate the standard into geographical information systems (GIS), online database systems, and mobile apps.

### 7.11 Definitions of an asset and an attribute

> An asset is an item, thing, or entity that has potential or actual value to an organization (ISO 55000). Sanitation systems generally consist of physical assets, which are engineered, manufactured, or constructed, spanning both sewered (network-based) and non-sewered (on-site) sanitation. For the purposes of database design, an asset consists of one single row in the table of assets. (section 5.1)

> An attribute is a piece of data that describes a quality or characteristic of an individual asset. (section 6.1)

