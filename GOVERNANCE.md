# Governance

> **Draft for mWater review.** This document was drafted alongside the machine-readable
> release of the standards. It is a proposal, not a record of an existing mWater policy,
> and it commits mWater to things nobody at mWater has yet agreed to. See
> [REVIEW-NEEDED.md](REVIEW-NEEDED.md) before relying on it or citing it.

A standard that changes without warning is worse than no standard, because
implementers build against a target that moves under them. This document states who
decides what goes into the mWater Asset Standards, how a change is proposed and
reviewed, and what an implementer can rely on between releases.

## Who owns the standards

mWater Foundation, Inc. holds the copyright in both standards and publishes them
under CC BY-SA 4.0. mWater Foundation, Inc. is a 501(c)(3) non-profit corporation
incorporated in Colorado on 6 June 2012, doing business as Solstice Institute.

The license lets anyone fork these standards. Governance here covers the versions
that mWater publishes in this repository.

## Who decides

A standards steward at mWater is accountable for each release. The steward keeps the
issue tracker current, runs the review period on every proposal, and decides what
enters a release.

Two named roles hold the decision:

| Role | Holder | Decides |
|---|---|---|
| Technical lead | Dr. John Feighery, COO | Whether a change is technically correct and consistent with the rest of the standard |
| Product lead | Petri Autio, Head of Product | Whether a change is worth the cost it imposes on implementers |

Where the two disagree, the change waits for the next release rather than shipping
unresolved. Silence is not agreement. A proposal with no response by the end of its
review period is deferred, not accepted.

## How a change is proposed

Anyone may propose a change, and no relationship with mWater is required. The route
is a GitHub issue in this repository, described in [CONTRIBUTING.md](CONTRIBUTING.md).

Every proposal states what the standard says today, what it should say instead, why
the current text causes a problem in practice, and which asset types and attribute
codes the change touches. Proposals that add an attribute also state what field data
already exists to populate it. mWater weights evidence from real asset registers
above argument from first principles.

## Classes of change

The review period depends on how much work a change creates for implementers.

**Editorial.** Corrections to spelling, formatting, or a description that does not
alter meaning. Review period of one week. These may ship in a patch release.

**Compatible.** New asset types, new attributes, new choices, corrections to a
conversion factor, and repairs to an applicability condition that names something
that does not exist. Existing conforming data stays conforming. Review period of
three weeks. These ship in a minor release.

**Breaking.** Removing or renumbering an attribute, removing a choice, changing the
data type or unit quantity of an existing attribute, or removing an asset type. Data
already collected may stop conforming. Review period of six weeks, and the proposal
must include a migration path. These ship in a major release.

## Stability guarantees

Implementers can rely on the following within a major version.

An attribute code is permanent. Once a code is published, it keeps its meaning, and
it is never reassigned to a different attribute. A retired attribute is marked as
deprecated in the tables and stays there for at least one major version before
removal.

A choice identifier is permanent in the same way. Renaming a choice is an editorial
change to `choice_name`; the `choice_id` does not move with it.

New attributes and new choices may appear in any minor release. Software that reads
these tables should ignore codes it does not recognize rather than reject the file.

## Release process

Releases follow semantic versioning applied to the standard, not to the repository.
The steward prepares a release by closing the accepted issues, updating the CSV
tables, regenerating the JSON and schema files with the scripts in `tools/`, running
`tests/run-tests.sh`, and recording every change in `CHANGELOG.md`.

Each release is tagged, for example `water-v1.1`, and archived to Zenodo so that the
version carries a permanent digital object identifier. The two standards version
independently, because they are separate documents with separate scopes.

## Known defects

Both standards shipped version 1.0 with defects, and mWater publishes them rather
than quietly correcting them. Each is recorded in the `EXTRACTION-NOTES.md` file of
the standard it affects and tracked as an issue.

Correcting a published defect still goes through the process above. A conversion
factor that looks wrong is a compatible change; renumbering an attribute whose code
breaks the code grammar is a breaking change, and version 1.0 data would need
migrating. That is why neither has been changed yet.

## Contact

Proposals and defect reports belong in the issue tracker, where the discussion stays
public. For anything that does not fit an issue, including offers of asset data to
validate a future version, write to info@mwater.co.
