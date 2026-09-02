# Changelog

This file records changes to the published standards and to the repository that
carries them. The two standards version independently. [GOVERNANCE.md](GOVERNANCE.md)
says who decides on changes.

## Repository

### 2026-09-01, first publication

mWater published both standards as machine-readable data for the first time. The
specification documents were already public. This release adds the tables, the
schema and the tooling that make the standards usable without reading a PDF.

Added the water standard as `asset-types.csv`, `attributes.csv`, `choices.csv` and
`units.csv`, transcribed from version 1.0 of the specification. Added the same four
tables for the sanitation standard. Added a generated JSON serialization of each
standard, a JSON Schema for validating asset records against each standard, a
command-line validator, and a regression suite. Added a non-normative crosswalk from
each standard to the column identifiers of mWater's published data dictionaries.
Added governance, contribution, privacy and SDG documentation.

Recorded every known defect in the two standards in an `EXTRACTION-NOTES.md` file
per standard, rather than correcting them silently. None of the defects has been
changed. Corrections belong in the next version of each standard.

## Water System Management Standard, Part 1: Asset Management

### 1.0, 2022-04-07

First release. Defines 5 asset classes, 29 asset types and 178 attributes, with 269
choice options and 9 physical quantities. Developed by mWater Foundation, Inc. with
funding support from the United States Agency for International Development.

Known defects in this version are listed in `water/EXTRACTION-NOTES.md`. The most
significant are a disagreement between the introduction, which states 28 asset
types, and Table 4, which lists 29; attribute codes on the Water system type that do
not follow the standard's own code grammar; four applicability conditions that name
attributes or choices that do not exist; and the use of a ninth data type, Asset ID,
that section 4.1 does not define.

## Sanitation System Management Standard, Part 1: Asset Management

### 1.0, 2026-08-21

First release. Defines 4 asset classes, 27 asset types and 211 attributes, with 445
choice options and 11 physical quantities. Covers sewered and on-site sanitation
across the whole service chain. Field definitions match the water standard wherever
an asset appears in both, including pumps, pipes, tanks, meters and valves.

Initial development was supported by the USAID IUWASH Tangguh project in Indonesia
during 2024. Work paused when that funding ended in early 2025. mWater funded
completion of version 1.0 in 2026.

Known defects in this version are listed in `sanitation/EXTRACTION-NOTES.md`. The
most significant are attribute codes on the Sanitation system that carry the
Subsystem type code; eleven general attributes that do not follow the code grammar
the same document defines; several flow-rate conversion factors that appear
reciprocal or mis-scaled; and one applicability condition that names four treatment
choices that do not exist.
