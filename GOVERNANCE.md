# Governance

mWater Foundation, Inc. owns both standards and publishes them under CC BY-SA 4.0. It
is a small non-profit, and it maintains these standards with a small amount of staff
time rather than through a standards committee. This document says how that works, so
that implementers know what to expect and are not promised more than mWater can
deliver.

## Who decides

John Feighery, COO of mWater, decides what changes enter a standard. He can be reached
at john@mwater.co. In practice he and Susan Lamb, Program Manager, do the work of
reviewing proposals and updating the tables.

There is no committee, no formal review period, and no guaranteed response time.
mWater reads every issue and answers when it can.

## How a change happens

Anyone may propose a change by opening an issue in this repository, as described in
[CONTRIBUTING.md](CONTRIBUTING.md). Proposals grounded in real asset data, where an
organization tried to record something and the standard did not fit, carry the most
weight.

When mWater accepts a change, it updates the CSV tables, regenerates the JSON and
schema files, runs the test suite, records the change in [CHANGELOG.md](CHANGELOG.md),
and tags a new version. Each standard is versioned on its own, because they are
separate documents.

## What implementers can rely on

A published version does not change. Once `water-v1.0` is tagged, the files under
that tag stay as they are, and every later version is a new tag. Software can pin a
version and expect it to hold.

An attribute code that has been published is not reused for a different attribute.
Both standards are built on permanent five-digit codes, and reassigning one would
break every dataset that used it. If mWater retires an attribute, the code is retired
with it.

Anything beyond those two points is intent rather than promise. mWater will try to
give notice before a change that breaks existing data, and will say in the changelog
when a change does.

## Known defects

Both standards shipped version 1.0 with defects, listed in the `EXTRACTION-NOTES.md`
file of each standard and in [VERIFICATION-REPORT.md](VERIFICATION-REPORT.md). mWater
published them rather than quietly correcting them, because a correction to a
published standard is a new version, not an edit. They will be addressed in version
1.1 of each standard when mWater has the capacity to prepare it.

## Contact

Proposals and defect reports belong in the issue tracker, where the discussion stays
public. Anything else, including offers of asset data to test a future version, goes
to info@mwater.co.
