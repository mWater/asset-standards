# Crosswalk to the mWater data dictionary

mWater implements both standards in its own platform and publishes the resulting
data dictionaries openly. This directory maps each attribute code in a standard to
the matching column identifier in the platform, so that an organization moving data
in either direction does not have to read both specifications side by side.

Nothing here is part of either standard. Where the platform and the standard
disagree, the standard governs.

## Source

The platform column lists were retrieved from mWater's schema service in September
2026. The same information is browsable at
https://portal.mwater.co/#/data-dictionary/site-types/water_asset and
https://portal.mwater.co/#/data-dictionary/site-types/sanitation_asset.

`SCHEMA-NOTES.md` records the retrieval method, the exact counts, and the defects
found in the platform dictionaries themselves.

## Files

| File | Contents |
|---|---|
| `water-to-mwater.csv` | Water standard attribute codes mapped to `entities.water_asset` columns |
| `sanitation-to-mwater.csv` | Sanitation standard attribute codes mapped to `entities.sanitation_asset` columns |
| `water_asset_columns.csv` | All 617 columns of the platform water asset table |
| `sanitation_asset_columns.csv` | All 491 columns of the platform sanitation asset table |
| `*_enums.csv` | Permitted values of every enumerated platform column |
| `SCHEMA-NOTES.md` | Retrieval notes and platform-side defects |

## How rows were matched

Matching used the display name only, and every row records the method used. No row
was matched by judgement.

`exact_name` means the attribute name and the column name are identical.
`normalised_name` means they matched after lowercasing and collapsing punctuation.
`unit_family` means the attribute is a measurement and the platform stores it as a
family of columns, one per unit plus a raw magnitude, so the row points at the raw
magnitude member. A suffix of `_ambiguous` means more than one platform column
matched and the first is shown.

`unmatched` means no column matched. Those rows are kept in the file with empty
platform columns, because a visible gap is more useful than a silent one. Thirteen
water attributes and ten sanitation attributes are unmatched.

## Why the platform has more columns than the standard has attributes

The platform table holds 617 columns against 178 water attributes, and 491 columns
against 211 sanitation attributes. Three things account for the difference.

Every measurement is stored as several columns rather than one, holding the value in
each supported unit plus the raw magnitude and the chosen unit. The platform also
carries operational columns that no standard defines, such as import bookkeeping and
record timestamps. Finally, some platform columns predate the standards and remain
for backward compatibility.

An unmatched attribute therefore does not mean the platform cannot hold it. It means
the platform's name for it differs from the standard's, and someone should check
that pair by hand.
