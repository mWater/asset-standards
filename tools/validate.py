#!/usr/bin/env python3
"""Validate asset records against the mWater asset standards.

    python3 tools/validate.py water  record.json [more.json ...]
    python3 tools/validate.py sanitation records.ndjson

Accepts a JSON object, a JSON array of objects, or newline-delimited JSON.
Exits non-zero if any record fails. Requires `jsonschema` (pip install jsonschema).
"""
import json, pathlib, sys

try:
    from jsonschema import Draft202012Validator
except ImportError:
    sys.exit("This validator needs the `jsonschema` package: pip install jsonschema")

ROOT = pathlib.Path(__file__).resolve().parent.parent


def load_records(path):
    text = pathlib.Path(path).read_text()
    stripped = text.lstrip()
    if stripped.startswith("["):
        return json.loads(text)
    if stripped.startswith("{") and "\n{" not in stripped.strip():
        return [json.loads(text)]
    return [json.loads(line) for line in text.splitlines() if line.strip()]


def main(argv):
    if len(argv) < 3 or argv[1] not in ("water", "sanitation"):
        sys.exit(__doc__)
    standard, paths = argv[1], argv[2:]
    schema = json.loads((ROOT / "schema" / f"{standard}-asset.schema.json").read_text())
    validator = Draft202012Validator(schema)

    failures = 0
    for path in paths:
        for i, record in enumerate(load_records(path)):
            errors = sorted(validator.iter_errors(record), key=lambda e: list(e.path))
            label = f"{path}[{i}]" if len(load_records(path)) > 1 else path
            if errors:
                failures += 1
                print(f"FAIL {label}")
                for e in errors:
                    where = "/".join(str(p) for p in e.path) or "(record)"
                    print(f"     {where}: {e.message}")
            else:
                print(f"ok   {label}")
    print(f"\n{len(paths)} file(s) checked, {failures} record(s) failed.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
