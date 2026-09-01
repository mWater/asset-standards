#!/usr/bin/env python3
"""Build the canonical JSON serialisation of each standard from its CSV tables.

The CSV files are the source of truth; the JSON is generated. Run this after any
change to a CSV, and commit both.
"""
import csv, json, pathlib, collections

META = {
    "water": {
        "name": "The Water System Management Standard, Part 1 - Asset Management",
        "shortName": "mWater Global Water Asset Standard",
        "version": "1.0",
        "issued": "2022-04-07",
    },
    "sanitation": {
        "name": "The Sanitation System Management Standard, Part 1 - Asset Management",
        "shortName": "mWater Global Sanitation Asset Standard",
        "version": "1.0",
        "issued": "2026-08-21",
    },
}
COMMON = {
    "publisher": "mWater Foundation, Inc.",
    "license": "CC-BY-SA-4.0",
    "licenseUrl": "https://creativecommons.org/licenses/by-sa/4.0/",
    "repository": "https://github.com/mWater/asset-standards",
}


def read(p):
    with open(p, newline="") as fh:
        return list(csv.DictReader(fh))


def build(std):
    base = pathlib.Path(std)
    types = read(base / "asset-types.csv")
    attrs = read(base / "attributes.csv")
    choices = read(base / "choices.csv")
    units = read(base / "units.csv")

    by_attr = collections.defaultdict(list)
    for c in choices:
        by_attr[c["attribute_code"]].append(
            {"id": c["choice_id"], "name": c["choice_name"],
             "description": c["description"] or None}
        )

    by_quantity = collections.OrderedDict()
    for u in units:
        by_quantity.setdefault(u["quantity"], {"siBaseUnit": u["si_base_unit"], "units": []})
        by_quantity[u["quantity"]]["units"].append({
            "unit": u["alternate_unit"],
            "conversionFactorToSi": u["conversion_factor_to_si"],
            "notes": u["notes"] or None,
        })

    def attr(a):
        rec = {
            "code": a["code"],
            "name": a["name"],
            "scope": a["scope"],
            "assetType": a["asset_type"] or None,
            "assetTypeId": a["asset_type_id"] or None,
            "dataType": a["data_type"],
            "attributeGroup": a["attribute_group"] or None,
            "description": a["description"] or None,
            "applicability": a["applicability"] or None,
            "required": a["required"].upper() == "TRUE",
        }
        if a["unit_quantity"]:
            rec["unitQuantity"] = a["unit_quantity"]
        if a["si_unit"]:
            rec["siUnit"] = a["si_unit"]
        if by_attr.get(a["code"]):
            rec["choices"] = by_attr[a["code"]]
        return rec

    doc = {
        "$schema": "https://github.com/mWater/asset-standards/schema/standard.schema.json",
        "standard": {**META[std], **COMMON},
        "assetClasses": sorted({t["asset_class"] for t in types if t["asset_class"]}),
        "assetTypes": [
            {"typeCode": t["type_code"], "assetClass": t["asset_class"], "id": t["type_id"],
             "name": t["type_name"], "description": t["description"] or None}
            for t in types
        ],
        "units": by_quantity,
        "attributes": [attr(a) for a in attrs],
    }
    doc["counts"] = {
        "assetClasses": len(doc["assetClasses"]),
        "assetTypes": len(doc["assetTypes"]),
        "attributes": len(doc["attributes"]),
        "generalAttributes": sum(1 for a in attrs if a["scope"] == "general"),
        "typeSpecificAttributes": sum(1 for a in attrs if a["scope"] == "type_specific"),
        "choiceOptions": len(choices),
        "unitQuantities": len(by_quantity),
    }
    out = base / f"{std}-asset-standard.json"
    out.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
    print(f"{out}: {doc['counts']}")


for s in ("water", "sanitation"):
    build(s)
