# mWater asset-table schema retrieval notes

**Retrieval date:** 2026-09-01 (UTC). Column pagination and enum detail calls all executed
on this date; enum retrieval ran from 2026-09-01T08:45:51Z to 2026-09-01T08:53:12Z.

**Source:** mWater MCP server, live schema for the authenticated user.
Corresponds to the published data dictionaries at
https://portal.mwater.co/#/data-dictionary/site-types/water_asset and
https://portal.mwater.co/#/data-dictionary/site-types/sanitation_asset

## Tools and pagination

- `get_table_columns` — called with `limit: 50` and `offset` incremented by 50 until the
  reported `totalColumns` was covered.
  - `entities.water_asset`: offsets 0,50,…,600 (13 pages; last page returned 17 rows).
  - `entities.sanitation_asset`: offsets 0,50,…,450 (10 pages; last page returned 41 rows).
  - Raw per-page JSON is preserved under `raw/` (`wa_*.json`, `sa_*.json`).
- `get_column_details` — called once per `enum`/`enumset` column (262 calls total).
  Raw responses condensed to `raw/wa_enums.jsonl` and `raw/sa_enums.jsonl`.

## Counts retrieved

| Table | API totalColumns | Rows written | Enum/enumset columns | Enum option rows |
|---|---|---|---|---|
| entities.water_asset | 617 | 617 | 143 | 730 |
| entities.sanitation_asset | 491 | 491 | 119 | 665 |

Both match the expected ~617 / ~491 figures exactly. No enum column type was `enumset`;
all 262 were plain `enum`. Every enum column was fetched — none skipped, none errored.

## Columns / sections

- The API returns no section, group, folder, or category attribute on any column of either
  table. The `section` column in both CSVs is therefore **empty for all rows**. Section
  grouping is only visible in the portal's data-dictionary UI, not through
  `get_table_columns` or `get_column_details`.
- `join_target` is populated from `joinTo` (for `join` columns) or `idTable`
  (for `id` columns); empty otherwise.

## Anomalies observed in the API response

- **Duplicate column_id (water_asset):** `pump_h_min_unit_in_water` is returned **twice**
  in the offset-300 page, both times as name "Head at maximum flow (H-min) (in H₂O)",
  type `number`. It is retained twice in the CSV so the row count matches the API's
  `totalColumns` of 617 (616 distinct ids). No duplicate ids in sanitation_asset.
- **Duplicate enum option ids** (returned by the API, retained verbatim):
  - water_asset `pump_sleeve_material`: `steel` ("Steel") appears twice.
  - water_asset `riser_pipe_material`: `steel` ("Steel") appears twice.
  - water_asset `pump_h_min_unit`: `in_water` ("inches of water") appears twice; note
    the water_asset variant of this list omits `ft_water`, unlike the sanitation variant.
  - water_asset `tank_base_material`: `wood` ("Wood") appears twice.
  - No duplicate enum option ids in sanitation_asset.
- **Transcription note:** a few enum display names contain the characters °F, °C, ³, ² and
  ₂ (e.g. "feet of water (39.2 °F)"). In the enum CSVs these were written in ASCII form
  ("feet of water (39.2 F)", "m3/s"). Column display names in the `*_columns.csv` files
  retain the original Unicode characters.
- No column returned an error or incomplete data.

## Files

- `water_asset_columns.csv` / `sanitation_asset_columns.csv` —
  `column_id,column_name,column_type,section,join_target`
- `water_asset_enums.csv` / `sanitation_asset_enums.csv` —
  `column_id,enum_id,enum_name`
- `raw/` — unmodified per-page column JSON and condensed enum responses.
