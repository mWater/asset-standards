# Contributing

The most useful contribution is to try to record real asset data with one of these
standards and report what did not fit. mWater welcomes defect reports, change
proposals, translations and implementation reports from anyone.

mWater is a small team with limited time for review. Issues are read and answered
when capacity allows, and [GOVERNANCE.md](GOVERNANCE.md) explains who decides.

## Before opening an issue

Read `EXTRACTION-NOTES.md` in the affected standard's directory first. Both standards
shipped version 1.0 with known defects, and those are already listed there with the
source text quoted. Confirming a known defect is still useful, and saying how it
affected real data is more useful still. Check the open issues as well.

## Reporting a defect

Open an issue titled with the attribute code or asset type it concerns, for example
`30203 pump power rating: unit quantity is wrong`. State what the standard says, what
is wrong with it, and what the effect is on data already collected. Quote the source
text rather than paraphrasing it.

A transcription error in a CSV table, where the table differs from the published
document, is fixed directly. An error in the document itself is a change to the
standard and becomes part of the next version.

## Proposing a change

A change proposal is an issue that states the current text, the proposed text, the
problem the current text causes in practice, and the asset types and attribute codes
affected. A proposal to add an attribute should also say what field data exists to
populate it, because an attribute nobody can fill is a cost with no benefit.

## Sending a pull request

Pull requests are welcome for editorial corrections and for tooling. For any change to
what a standard means, open an issue first so the change can be discussed before code
is written.

Edit the CSV files, never the generated JSON or schema files. Then regenerate and
test:

```bash
pip install jsonschema
python3 tools/build_json.py
python3 tools/build_schema.py
bash tests/run-tests.sh
```

The test suite fails if the generated files do not match their CSV sources, so commit
both. Keep CSV files as RFC 4180, UTF-8, LF line endings, and keep attribute codes as
five-digit strings. Add a fixture under `tests/fixtures/` for any change that alters
what validates.

## Translations

Both standards are published in English only. Translations of attribute names,
descriptions and choice names are welcome, and they belong in a separate file rather
than in the English tables, so that the code and the English name stay stable. Open an
issue before starting so that two people do not translate the same standard.

## Reporting an implementation

Anyone implementing either standard outside the mWater platform is asked to say so in
an issue, including what was easy, what was ambiguous, and what had to be extended.
Implementation reports carry more weight than any other kind of input.

Organizations willing to share water or sanitation asset data to test the standards
can write to info@mwater.co.

## Conduct and licensing

Participants are expected to follow the [code of conduct](CODE_OF_CONDUCT.md).

This repository is licensed CC BY-SA 4.0. By contributing, a contributor agrees that
their contribution is published under that same license. Do not contribute material
that belongs to someone else unless its license permits redistribution under
CC BY-SA 4.0, and say so in the issue when it does.
