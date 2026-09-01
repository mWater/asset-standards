# Contributing

> **Draft for mWater review.** This document was drafted alongside the machine-readable
> release of the standards. It is a proposal, not a record of an existing mWater policy,
> and it commits mWater to things nobody at mWater has yet agreed to. See
> [REVIEW-NEEDED.md](REVIEW-NEEDED.md) before relying on it or citing it.

The fastest way to improve these standards is to try to record real asset data with
them and report what does not fit. mWater welcomes defect reports, change proposals,
translations, and implementation reports from anyone, with no prior relationship
required.

## Before opening an issue

Read `EXTRACTION-NOTES.md` in the affected standard's directory first. Both standards
shipped version 1.0 with known defects, and those are already listed there with the
source text quoted. Confirming a known defect is still useful, and saying how it
affected real data is more useful still.

Check the open issues as well, in case the point is already under review.

## Reporting a defect

Open an issue titled with the attribute code or asset type it concerns, for example
`30203 pump power rating: unit quantity is wrong`. State what the standard says,
what is wrong with it, and what the effect is on data already collected. Quote the
source text rather than paraphrasing it.

Defects in the CSV tables and defects in the underlying specification document are
both in scope, and they are handled differently. A transcription error in a table is
fixed directly. An error in the specification is a change to the standard and goes
through the review in [GOVERNANCE.md](GOVERNANCE.md).

## Proposing a change

A change proposal is an issue that states four things: the current text, the
proposed text, the problem the current text causes in practice, and the asset types
and attribute codes affected. Proposals to add an attribute should also say what
field data exists to populate it, because an attribute nobody can fill is a cost
with no benefit.

The standards steward assigns each proposal a class, editorial, compatible or
breaking, and opens a review period of one, three or six weeks. The classes and
periods are defined in [GOVERNANCE.md](GOVERNANCE.md).

## Sending a pull request

Pull requests are welcome for editorial corrections and for tooling. For any change
to what the standard means, open an issue first, because a merged pull request
cannot substitute for the review period.

Edit the CSV files, never the generated JSON or schema files. Then regenerate and
test:

```bash
pip install jsonschema
python3 tools/build_json.py
python3 tools/build_schema.py
bash tests/run-tests.sh
```

The test suite fails if the generated files do not match their CSV sources, so
commit both. Keep CSV files as RFC 4180, UTF-8, LF line endings, and keep attribute
codes as five-digit strings.

Add a fixture under `tests/fixtures/` for any change that alters what validates.
A fixture in `valid/` must pass and a fixture in `invalid/` must fail.

## Translations

Both standards are published in English only. Translations of attribute names,
descriptions and choice names are welcome, and they belong in a new file rather than
in the English tables, so that the code and the English name stay stable.

Open an issue before starting a translation so that mWater can agree the file layout
and avoid two people translating the same standard.

## Reporting an implementation

Anyone implementing either standard outside the mWater platform is asked to say so
in an issue, including what was easy, what was ambiguous, and what had to be
extended. Implementation reports carry more weight in review than any other kind of
input, and version 1.0 of both standards needs them.

Organizations willing to share water or sanitation asset data to validate the
standards can write to info@mwater.co.

## Conduct and licensing

Participants are expected to follow the [code of conduct](CODE_OF_CONDUCT.md).

Contributions are accepted under CC BY-SA 4.0, the license of this repository.
Contributors keep the copyright in what they write and grant mWater Foundation, Inc.
the right to publish it under that license. Do not contribute material that is
copyrighted by someone else unless its license permits redistribution under
CC BY-SA 4.0, and say so in the issue when it does.
