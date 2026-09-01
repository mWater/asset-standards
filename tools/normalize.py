#!/usr/bin/env python3
"""Normalise the two extracted attribute tables onto one common header.

Two mechanical additions, both derived from files already in this repository:
  * `si_unit` is added to the water table (empty) so both standards share a header.
  * `asset_type_id` is added to both, joined from asset-types.csv on `type_name`.
Nothing is inferred from outside the source documents.
"""
import csv, pathlib, sys

HEADER = ["code", "name", "scope", "asset_class", "asset_type", "asset_type_id",
          "data_type", "unit_quantity", "si_unit", "description", "applicability",
          "required", "attribute_group"]

for std in ("water", "sanitation"):
    base = pathlib.Path(std)
    types = {r["type_name"]: r["type_id"] for r in csv.DictReader(open(base / "asset-types.csv"))}
    rows = list(csv.DictReader(open(base / "attributes.csv")))
    out = []
    for r in rows:
        rec = {k: (r.get(k) or "") for k in HEADER}
        rec["code"] = r["code"]
        name = r.get("asset_type") or ""
        rec["asset_type_id"] = types.get(name, "")
        if name and not rec["asset_type_id"]:
            sys.exit(f"{std}: asset_type {name!r} not found in asset-types.csv")
        out.append(rec)
    with open(base / "attributes.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=HEADER, lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    print(f"{std}: {len(out)} attributes normalised")
