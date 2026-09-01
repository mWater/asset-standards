#!/usr/bin/env bash
# Regression tests for the mWater asset standards repository.
# Every file under tests/fixtures/valid must validate; every file under
# tests/fixtures/invalid must fail. Also rebuilds the generated artefacts and
# checks they are identical to what is committed.
set -uo pipefail
cd "$(dirname "$0")/.."
fail=0

std_of() { case "$1" in *sanitation*) echo sanitation ;; *) echo water ;; esac; }

echo "== fixtures that must validate"
for f in tests/fixtures/valid/*.json; do
  if python3 tools/validate.py "$(std_of "$f")" "$f" >/dev/null 2>&1; then
    echo "  ok    $f"
  else
    echo "  FAIL  $f (expected valid)"; fail=1
    python3 tools/validate.py "$(std_of "$f")" "$f" | sed 's/^/        /'
  fi
done

echo "== fixtures that must be rejected"
for f in tests/fixtures/invalid/*.json; do
  if python3 tools/validate.py "$(std_of "$f")" "$f" >/dev/null 2>&1; then
    echo "  FAIL  $f (expected invalid, but it passed)"; fail=1
  else
    echo "  ok    $f"
  fi
done

echo "== generated artefacts match their CSV sources"
python3 tools/build_json.py >/dev/null && python3 tools/build_schema.py >/dev/null
if git diff --quiet -- water/*.json sanitation/*.json schema/*.json 2>/dev/null; then
  echo "  ok    JSON and schemas are up to date"
else
  echo "  FAIL  regenerated files differ from what is committed - run the build tools and commit"
  fail=1
fi

echo "== integrity checks"
python3 tools/check_integrity.py || fail=1

[ $fail -eq 0 ] && echo "ALL TESTS PASSED" || echo "TESTS FAILED"
exit $fail
