#!/usr/bin/env python3
"""Generate a JSON Schema (draft 2020-12) for asset records conforming to each standard.

Generated from the CSV tables. An asset record is a JSON object keyed by the
standard's five-digit attribute codes. Section 6.2 of each standard says an
unknown or not-applicable value "shall be left blank", so every attribute also
accepts null. Type-specific attributes are constrained to their own asset type.
"""
import csv, json, pathlib, collections

BASE_URL = "https://raw.githubusercontent.com/mWater/asset-standards/main/schema"

GEOMETRY = {
    "type": "object",
    "description": "GeoJSON geometry (RFC 7946).",
    "required": ["type", "coordinates"],
    "properties": {
        "type": {"enum": ["Point", "LineString", "Polygon", "MultiPoint",
                          "MultiLineString", "MultiPolygon"]},
        "coordinates": {"type": "array"},
    },
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
        by_attr[c["attribute_code"]].append(c["choice_id"])
    unit_options = collections.defaultdict(list)
    for u in units:
        unit_options[u["quantity"]].append(u["alternate_unit"])
    type_ids = [t["type_id"] for t in types]

    defs = {
        "geometry": GEOMETRY,
        "measurement": {
            "type": "object",
            "description": "A magnitude paired with one of the units the standard "
                           "defines for that physical quantity (section 4.2).",
            "required": ["magnitude", "unit"],
            "additionalProperties": False,
            "properties": {"magnitude": {"type": "number"}, "unit": {"type": "string"}},
        },
    }

    def value_schema(a):
        dt, code = a["data_type"], a["code"]
        if dt in ("Text", "Image"):
            s = {"type": "string"}
        elif dt == "Asset ID":
            s = {"type": "string",
                 "description": "Reference to the Asset ID of another asset."}
        elif dt == "Choice":
            opts = by_attr.get(code) or (type_ids if code == "00001" else [])
            s = {"type": "string", "enum": opts} if opts else {"type": "string"}
        elif dt == "Number":
            s = {"type": "number"}
        elif dt == "Date":
            s = {"type": "string", "format": "date"}
        elif dt == "Geometry":
            s = {"$ref": "#/$defs/geometry"}
        elif dt == "Checkbox":
            s = {"type": "boolean"}
        elif dt == "Unit":
            s = {"allOf": [{"$ref": "#/$defs/measurement"}]}
            q = a["unit_quantity"]
            if q and unit_options.get(q):
                s["allOf"].append({"properties": {"unit": {"enum": unit_options[q]}}})
                s["description"] = f"Quantity: {q}."
        else:
            s = {}
        return s

    properties, required = {}, []
    allowed_general, per_type = [], collections.defaultdict(list)
    for a in attrs:
        code = a["code"]
        inner = value_schema(a)
        title = a["name"]
        properties[code] = {
            "title": title,
            "description": a["description"] or None,
            "anyOf": [inner, {"type": "null"}],
        }
        properties[code] = {k: v for k, v in properties[code].items() if v is not None}
        if a["applicability"]:
            properties[code]["$comment"] = f"Applicability: {a['applicability']}"
        if a["required"].upper() == "TRUE":
            required.append(code)
        if a["scope"] == "general":
            allowed_general.append(code)
        else:
            per_type[a["asset_type_id"]].append(code)

    all_of = []
    for t in types:
        tid = t["type_id"]
        allowed = allowed_general + per_type.get(tid, [])
        all_of.append({
            "$comment": f"{t['type_name']} ({t['asset_class']})",
            "if": {"required": ["00001"], "properties": {"00001": {"const": tid}}},
            "then": {"propertyNames": {"enum": sorted(allowed)}},
        })

    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": f"{BASE_URL}/{std}-asset.schema.json",
        "title": f"{std.capitalize()} asset record",
        "description": (
            f"One asset conforming to the mWater Global {std.capitalize()} Asset Standard "
            f"v1.0. Keys are the standard's five-digit attribute codes. "
            f"Licensed CC BY-SA 4.0 by mWater Foundation, Inc."
        ),
        "type": "object",
        "required": sorted(set(required + ["00001"])),
        "additionalProperties": False,
        "properties": properties,
        "allOf": all_of,
        "$defs": defs,
    }
    out = pathlib.Path("schema") / f"{std}-asset.schema.json"
    out.write_text(json.dumps(schema, indent=2, ensure_ascii=False) + "\n")
    print(f"{out}: {len(properties)} properties, {len(all_of)} type constraints, "
          f"required={schema['required']}")


for s in ("water", "sanitation"):
    build(s)
