# Data dictionary

This document describes every file a consumer of the mWater Asset Standards will
read, field by field, together with the metadata a data repository or catalog needs
to index the release. It covers the shape of the data. It does not restate the
standards themselves, which are in `docs/`.

## Dataset metadata

The table below gives the dataset-level metadata for this release, using the fields
that data repositories commonly ask for.

| Field | Value |
|---|---|
| Creator | mWater Foundation, Inc., Denver, Colorado, United States |
| Identifier | https://github.com/mWater/asset-standards |
| Subject | Water supply and sanitation asset management; data standards; WASH monitoring |
| Funders | United States Agency for International Development, for the water standard and for initial development of the sanitation standard under IUWASH Tangguh. mWater Foundation, Inc. funded completion of the sanitation standard. |
| Rights | CC BY-SA 4.0. No third-party rights are embedded in these tables. |
| Access information | Public. Direct download or `git clone`, no account, no API key, no rate limit. |
| Language | English |
| Dates | Water standard issued 2022-04-07. Sanitation standard issued 2026-08-21. Repository first published 2026-09. |
| File formats | CSV (RFC 4180, UTF-8, LF), JSON, JSON Schema draft 2020-12, Markdown, PDF |
| File structure | One directory per standard, each holding four related CSV tables joined on attribute code and asset type id |
| Variable list | This document, sections below |
| Code lists | `choices.csv` for choice attributes, `units.csv` for units, `asset-types.csv` for asset types |
| Versions | Git tags `water-v1.0` and `sanitation-v1.0`. Changes are recorded in CHANGELOG.md |
| Checksums | `SHA256SUMS` at the repository root, regenerated on each release |

## File encoding conventions

All CSV files follow RFC 4180. They are UTF-8 encoded without a byte order mark,
use LF line endings, quote any field containing a comma, quotation mark or newline,
and carry a header row. Attribute codes are five-digit strings and must be read as
text, because leading zeros are significant. A spreadsheet program that imports
`00003` as the number 3 has corrupted the data.

Empty means unknown or not applicable, in the tables and in conforming asset
records. Section 6.2 of each standard is explicit on this point. No file uses a
sentinel value such as `NULL`, `N/A` or `-1`.

## asset-types.csv

Each row is one asset type defined by the standard. Asset types are grouped into
asset classes, and the class controls how the asset behaves in a hierarchy.

| Column | Type | Description |
|---|---|---|
| `type_code` | string | The two-digit type number the standard assigns within its class. Unique within a class, not across the file. |
| `asset_class` | string | The class the type belongs to: System, Facility, Vertical, Horizontal, or Natural. The Natural class appears in the water standard only. |
| `type_id` | string | A lower_snake_case machine identifier for the type. Derived mechanically from `type_name` for this publication; it is not assigned by the standard document. |
| `type_name` | string | The name of the asset type, exactly as the standard gives it. |
| `description` | string | The definition of the asset type, quoted from the standard. |
| `allowed_parent_classes` | string | Empty throughout. Neither standard restricts which class may parent which, so the column is present for future use and carries no data today. |

## attributes.csv

Each row is one attribute. Both standards use the same header, so a consumer can
read either file with one parser.

| Column | Type | Description |
|---|---|---|
| `code` | string | The five-digit attribute code, permanent and unique within a standard. This is the identifier to store and exchange. |
| `name` | string | The standardized attribute name from the standard. |
| `scope` | enum | `general` for attributes that apply to every asset type, `type_specific` for attributes that apply to one type only. |
| `asset_class` | string | The class of the owning asset type, where the standard states one. Empty throughout the sanitation table, which does not scope attributes by class. |
| `asset_type` | string | The asset type name for type-specific attributes. Empty for general attributes. Joins to `asset-types.csv.type_name`. |
| `asset_type_id` | string | The machine identifier of the same type. Joins to `asset-types.csv.type_id`. Derived, not from the standard document. |
| `data_type` | enum | One of Text, Choice, Number, Date, Geometry, Checkbox, Image, Unit, or Asset ID. See the note below on Asset ID. |
| `unit_quantity` | string | For Unit attributes, the physical quantity measured, such as Length or Power. Joins to `units.csv.quantity`. |
| `si_unit` | string | The SI base unit for `unit_quantity`, looked up from the standard's units table. Populated in the sanitation table only. Water consumers should join to `units.csv` on `quantity` instead. |
| `description` | string | The definition of the attribute, quoted from the standard. |
| `applicability` | string | Any condition under which the attribute applies, quoted from the standard. See the note below on group conditions. |
| `required` | boolean | `TRUE` only where the standard uses "shall". Set on the water standard's Asset ID attribute and nowhere else. |
| `attribute_group` | string | The heading the attribute sits under, such as Basic info, Location, Hydraulic, or Points of contact. |

Section 4.1 of each standard defines eight data types. Both standards then use a
ninth value, `Asset ID`, on the attributes that reference another asset. These
tables record `Asset ID` as written rather than reclassifying it as Text, and the
discrepancy is logged in each standard's extraction notes. Consumers should treat an
`Asset ID` value as a string that refers to the Asset ID of another asset.

The `applicability` column holds one condition per attribute. Both standards also
apply conditions at the attribute-group level, and a handful of attributes carry
both. Where that happens, this column shows the narrower condition on the attribute
itself, and the extraction notes list every affected code so a consumer can combine
the two.

## choices.csv

Each row is one permitted value of one choice attribute. Attributes whose data type
is Choice must draw their value from this list.

| Column | Type | Description |
|---|---|---|
| `attribute_code` | string | The attribute the choice belongs to. Joins to `attributes.csv.code`. |
| `choice_id` | string | A lower_snake_case machine identifier, unique within the attribute. Derived mechanically from `choice_name`; it is not assigned by the standard document. |
| `choice_name` | string | The name of the choice, exactly as the standard gives it. |
| `description` | string | The definition of the choice, where the standard gives one. |

The `Type` attribute, code `00001`, is a choice attribute whose permitted values are
the asset types themselves. Neither standard restates them as a choice list, so
neither appears in this file. Consumers should take the values of `00001` from
`asset-types.csv`.

## units.csv

Each row is one unit that the standard recognizes for one physical quantity,
together with the factor that converts it to the SI base unit.

| Column | Type | Description |
|---|---|---|
| `quantity` | string | The physical quantity, such as Length, Pressure, or Flow rate. |
| `si_base_unit` | string | The SI base unit for that quantity. |
| `alternate_unit` | string | The unit this row describes. One row per quantity repeats the SI base unit itself, with a factor of 1. |
| `conversion_factor_to_si` | string | Multiply a magnitude in `alternate_unit` by this factor to obtain the SI base unit. Held as a string because two temperature rows hold a formula rather than a factor. |
| `notes` | string | The full unit name and the measurement system it belongs to. |

Temperature cannot be converted by a single factor, so the two temperature rows
carry the formula from the standard's own footnote instead. A numeric parser applied
blindly to this column will fail on those rows.

Several flow-rate conversion factors in the sanitation standard appear to be
reciprocals or to be mis-scaled against the rule the same standard states. They are
published here exactly as the standard gives them, and the discrepancy is listed in
`sanitation/EXTRACTION-NOTES.md`. A correction belongs in version 1.1.

## Columns that differ between the two standards

Three columns are populated in one standard and empty in the other, because the two
documents state different things. This is a property of the sources, not an error in
the tables.

`si_unit` is populated in the sanitation table and empty in the water table. Join to
`units.csv` on `unit_quantity` to obtain the same information for water.

`asset_class` is populated in the water table and empty in the sanitation table. The
sanitation standard does not scope attributes by class. To obtain the class of a
type-specific sanitation attribute, join to `asset-types.csv` on `asset_type_id`.

`required` is set on one attribute in the whole repository, the water standard's
Asset ID, code `00003`. Neither document has a required column. The flag was set from
the one place a standard uses "shall" about an attribute value. Treat every other
attribute as optional.

## A warning about the unit tables

Both standards publish flow-rate conversion factors that contradict the conversion
rule the same standards state in section 4.2, and both publish acre-ft as 1223.489
where one acre-foot is 1233.48 cubic metres. The two standards also contradict each
other: the water standard gives gallons per minute as 6.30902 x 10-5 and gallons per
day as 4.38126 x 10-8, while the sanitation standard gives the same mantissas with
positive exponents.

Every factor in `units.csv` is exactly as published. None was corrected. Anyone
converting flow rates or volumes should verify the factor against SI definitions
before use, and should expect corrections in the next version of both standards.

## Generated files

Two artifacts are generated from the CSV tables and committed alongside them, so
that a consumer who prefers JSON does not need to run any code.

`water/water-asset-standard.json` and `sanitation/sanitation-asset-standard.json`
hold the four tables of a standard as one document, with choices nested inside their
attribute and units grouped by quantity. Each carries a `counts` object that states
how many types, attributes and choices the release contains.

`schema/water-asset.schema.json` and `schema/sanitation-asset.schema.json` are JSON
Schemas, draft 2020-12, that validate a single asset record. A record is a JSON
object keyed by attribute code. The schema checks the data type of each value,
restricts choice attributes to their permitted values, requires a measurement to
carry both a magnitude and a recognized unit, and blocks a type-specific attribute
from appearing on the wrong asset type.

Run `python3 tools/build_json.py` and `python3 tools/build_schema.py` to regenerate
both after any change to a CSV table. The regression suite fails if the committed
files no longer match their sources.

## Crosswalk files

The `crosswalk/` directory maps attribute codes to the column ids of mWater's
published data dictionaries. Its own README documents the columns and the matching
method. Nothing in that directory is normative.
