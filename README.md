# mWater Asset Standards

Water and sanitation utilities collect asset data in whatever shape their software
imposes. Two utilities in the same country often cannot combine their pump
inventories, because one records a pump's rating in kilowatts and the other in
horsepower, under different field names, with different lists of pump types. That
gap blocks national reporting, blocks benchmarking between service providers, and
forces every new monitoring program to redesign a data model that already exists.

This repository holds two open standards that close that gap, published by mWater
Foundation, Inc. as machine-readable data:

| Standard | Version | Issued | Asset types | Attributes |
|---|---|---|---|---|
| [Water System Management Standard, Part 1: Asset Management](water/) | 1.0 | 2022-04-07 | 29 | 178 |
| [Sanitation System Management Standard, Part 1: Asset Management](sanitation/) | 1.0 | 2026-08-21 | 27 | 211 |

Each standard defines a set of asset classes and asset types, a numbered attribute
for every property those assets can carry, the data type and units of each
attribute, and the permitted values of every choice attribute. Every attribute has
a permanent five-digit code, so two systems can agree on what a field means without
agreeing on what to call it.

The two standards share a code grammar and use identical field definitions for
infrastructure that appears in both domains, such as pumps, pipes, tanks and meters.
An organization that implements one can implement the other with the same tooling.

## What is in this repository

The CSV tables are the source of truth. The JSON files and JSON Schemas are
generated from them by the scripts in `tools/`, and both are committed so that
consumers who prefer JSON never need to run anything.

```
water/                      Water standard, version 1.0
sanitation/                 Sanitation standard, version 1.0
  asset-types.csv             asset classes and types
  attributes.csv              every attribute: code, name, data type, units, group
  choices.csv                 permitted values for every choice attribute
  units.csv                   physical quantities, SI base units, conversion factors
  *-asset-standard.json       the four tables above as one JSON document
  EXTRACTION-NOTES.md         how the tables were derived, and every known defect
schema/                     JSON Schema (draft 2020-12) for validating asset records
crosswalk/                  non-normative mapping to mWater platform column ids
tools/                      build and validation scripts
tests/                      fixtures and a regression suite
docs/                       the published specification documents
```

## Using the standards

An implementer needs three things from this repository: the list of asset types to
support, the attributes that apply to each type, and the permitted values for the
choice attributes. All three come from the CSV files, and no mWater software is
required to read them.

Load `attributes.csv` to build a data model. Attributes with `scope` set to
`general` apply to every asset type. Attributes with `scope` set to `type_specific`
apply only to the asset type named in `asset_type`. The `applicability` column
records any further condition stated in the standard, such as an attribute that
appears only when a pump is electrically driven.

Store measurements as a magnitude and a unit, not as a bare number. The `units.csv`
table gives the SI base unit for each physical quantity and a conversion factor for
every alternate unit the standard recognizes. Recording magnitude and unit together
is what makes data from different countries comparable.

Values may be left blank. Section 6.2 of each standard states that an unknown or
not-applicable value shall be left blank, so blank does not mean zero and does not
mean false.

## Validating data

The repository ships a JSON Schema for each standard and a small command-line
validator. An asset record is a JSON object keyed by five-digit attribute codes.

```bash
pip install jsonschema
python3 tools/validate.py water tests/fixtures/valid/water-pump.json
python3 tools/validate.py sanitation my-export.ndjson
```

The schema enforces the data type of every attribute, the permitted values of every
choice attribute, and the rule that a type-specific attribute may appear only on its
own asset type. It accepts a single JSON object, an array of objects, or
newline-delimited JSON.

Run the full regression suite with `bash tests/run-tests.sh`. It checks the
fixtures, rebuilds the generated files and confirms they match what is committed,
and runs referential-integrity checks across the CSV tables.

## Relationship to the mWater platform

mWater implements both standards in its own platform, and the published data
dictionaries for the water and sanitation asset tables are open to anyone at
[portal.mwater.co](https://portal.mwater.co/#/data-dictionary/site-types/water_asset)
and
[portal.mwater.co](https://portal.mwater.co/#/data-dictionary/site-types/sanitation_asset).
The `crosswalk/` directory maps each attribute code to the matching platform column
id, which lets an organization move data between the two without re-reading either
specification.

That crosswalk is a convenience, not part of the standard. Where the platform and
the standard disagree, the standard governs. The crosswalk records how each row was
matched and leaves unmatched attributes visible rather than hiding them.

## Known defects

Both standards contain defects that this repository records rather than silently
repairs. The water standard states 28 asset types in its introduction and lists 29
in Table 4. Several attribute codes do not follow the code grammar the standards
themselves define. A handful of applicability conditions name attributes or choices
that do not exist. Some flow-rate conversion factors look mis-scaled.

Every one of these is listed in the `EXTRACTION-NOTES.md` file of the standard it
affects, with the source text quoted. Corrections belong in version 1.1 of each
standard, through the process in [GOVERNANCE.md](GOVERNANCE.md), not in an
undocumented edit to these tables.

The flow-rate and acre-ft conversion factors deserve particular caution. Both
standards publish factors that contradict their own stated conversion rule, and the
two standards contradict each other on gallons per minute and gallons per day. The
tables reproduce what was published. `DATA-DICTIONARY.md` explains the problem in
full.

Before publication, an independent audit compared every row of all eight tables
against the source documents, cell by cell rather than by sampling. It found no
transcription errors and 24 defects in the standards themselves.
[VERIFICATION-REPORT.md](VERIFICATION-REPORT.md) records the method and every
finding.

## License

Both standards and this repository are licensed under the Creative Commons
Attribution-ShareAlike 4.0 International License, CC BY-SA 4.0. The full text is in
[LICENSE](LICENSE), and the canonical text is at
https://creativecommons.org/licenses/by-sa/4.0/legalcode.

Anyone may share and adapt this material, including commercially, provided they give
attribution to mWater Foundation, Inc., indicate any changes, and license
derivatives under the same terms. See [NOTICE](NOTICE) for the attribution text and
[CITATION.cff](CITATION.cff) for the citation format.

## Contact

Questions about the standards, and offers of sanitation or water asset data for
validating version 1.0, go to info@mwater.co. Defects and change proposals belong in
the repository issue tracker, as described in
[CONTRIBUTING.md](CONTRIBUTING.md).
