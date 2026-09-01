#!/usr/bin/env python3
"""Referential-integrity checks over the CSV tables of both standards."""
import csv, collections, pathlib, sys, re

CODE = re.compile(r"^\d{5}$")
DATA_TYPES = {"Text", "Choice", "Number", "Date", "Geometry", "Checkbox", "Image",
              "Unit", "Asset ID"}
problems = []


def read(p):
    with open(p, newline="") as fh:
        return list(csv.DictReader(fh))


for std in ("water", "sanitation"):
    b = pathlib.Path(std)
    types = read(b / "asset-types.csv")
    attrs = read(b / "attributes.csv")
    choices = read(b / "choices.csv")
    units = read(b / "units.csv")

    codes = [a["code"] for a in attrs]
    dupes = [c for c, n in collections.Counter(codes).items() if n > 1]
    if dupes:
        problems.append(f"{std}: duplicate attribute codes {dupes}")
    bad = [c for c in codes if not CODE.match(c)]
    if bad:
        problems.append(f"{std}: attribute codes that are not five digits {bad}")

    type_ids = {t["type_id"] for t in types}
    orphan_types = {a["asset_type_id"] for a in attrs if a["asset_type_id"]} - type_ids
    if orphan_types:
        problems.append(f"{std}: attributes reference unknown asset types {orphan_types}")

    dupe_types = [t for t, n in collections.Counter(t["type_id"] for t in types).items() if n > 1]
    if dupe_types:
        problems.append(f"{std}: duplicate asset type ids {dupe_types}")

    codeset = set(codes)
    orphan_choices = {c["attribute_code"] for c in choices} - codeset
    if orphan_choices:
        problems.append(f"{std}: choices reference unknown attributes {sorted(orphan_choices)}")

    choice_attrs = {a["code"] for a in attrs if a["data_type"] == "Choice"}
    non_choice_with_choices = {c["attribute_code"] for c in choices} - choice_attrs
    if non_choice_with_choices:
        problems.append(f"{std}: choices attached to non-Choice attributes "
                        f"{sorted(non_choice_with_choices)}")

    for a in attrs:
        if a["data_type"] not in DATA_TYPES:
            problems.append(f"{std}: attribute {a['code']} has undefined data type "
                            f"{a['data_type']!r}")

    quantities = {u["quantity"] for u in units}
    missing_q = {a["unit_quantity"] for a in attrs if a["unit_quantity"]} - quantities
    if missing_q:
        problems.append(f"{std}: Unit attributes reference quantities absent from "
                        f"units.csv {sorted(missing_q)}")

    dup_choice = [(k, n) for k, n in collections.Counter(
        (c["attribute_code"], c["choice_id"]) for c in choices).items() if n > 1]
    if dup_choice:
        problems.append(f"{std}: duplicate choice ids within an attribute {dup_choice}")

    print(f"  {std}: {len(types)} types, {len(attrs)} attributes, "
          f"{len(choices)} choices, {len(units)} unit rows")

if problems:
    print("\nINTEGRITY PROBLEMS")
    for p in problems:
        print(f"  - {p}")
    sys.exit(1)
print("  integrity: OK")
