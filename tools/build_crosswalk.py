#!/usr/bin/env python3
"""Build a non-normative crosswalk between each standard's attribute codes and the
column ids of mWater's published data dictionary.

Matching is on the attribute/column display name only - exact first, then a
normalised comparison (lowercased, punctuation and whitespace collapsed). Nothing
is matched by guesswork: every row records how it was matched, and unmatched
attributes are kept in the file with an empty column id so the gaps are visible.

The crosswalk is a convenience for implementers. It is NOT part of the standard,
and where the two disagree the standard governs.
"""
import csv, pathlib, re, collections

PAIRS = [("water", "water_asset"), ("sanitation", "sanitation_asset")]


def norm(s):
    s = s.lower().replace("&", "and")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return " ".join(s.split())


rows_out = []
for std, table in PAIRS:
    attrs = list(csv.DictReader(open(f"{std}/attributes.csv")))
    cols = list(csv.DictReader(open(f"crosswalk/{table}_columns.csv")))

    exact = collections.defaultdict(list)
    normed = collections.defaultdict(list)
    for c in cols:
        exact[c["column_name"]].append(c)
        normed[norm(c["column_name"])].append(c)

    out, stats = [], collections.Counter()
    for a in attrs:
        cand, method = exact.get(a["name"]), "exact_name"
        if not cand:
            cand, method = normed.get(norm(a["name"])), "normalised_name"
        if not cand and a["data_type"] == "Unit":
            # mWater stores each measurement as a family of columns, one per unit
            # plus a raw magnitude, e.g. "Tank height (m)" / "(ft)" / "(raw magnitude)".
            # Match the family and point at its raw-magnitude member.
            family = [c for c in cols
                      if norm(c["column_name"]).startswith(norm(a["name"]) + " ")]
            if family:
                raw = [c for c in family if "raw magnitude" in norm(c["column_name"])]
                cand, method = (raw or family), "unit_family"
        if not cand:
            cand, method = None, "unmatched"
        if cand and len(cand) > 1:
            method += "_ambiguous"
        stats[method] += 1
        out.append({
            "attribute_code": a["code"],
            "attribute_name": a["name"],
            "asset_type": a["asset_type"],
            "standard_data_type": a["data_type"],
            "mwater_table": f"entities.{table}",
            "mwater_column_id": cand[0]["column_id"] if cand else "",
            "mwater_column_name": cand[0]["column_name"] if cand else "",
            "mwater_column_type": cand[0]["column_type"] if cand else "",
            "match_method": method,
            "candidate_count": len(cand) if cand else 0,
        })

    path = pathlib.Path("crosswalk") / f"{std}-to-mwater.csv"
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    print(f"{path}: {len(out)} rows  " + "  ".join(f"{k}={v}" for k, v in sorted(stats.items())))
    rows_out.append((std, table, len(cols), stats))
