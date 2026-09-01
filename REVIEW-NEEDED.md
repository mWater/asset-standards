# Claims in this repository that mWater has not confirmed

This repository was assembled quickly. The data is verified. Much of the prose is
not, and some of it commits mWater to things nobody at mWater has agreed to.

Everything listed here needs a decision from mWater before the repository is treated
as final, and certainly before it is cited in a Digital Public Goods application.
Delete this file once the list is cleared.

The items are grouped by how much they matter.

## What is verified, so it is not on this list

The eight CSV tables, the generated JSON and the two JSON Schemas were checked row by
row against the two source PDFs by an independent audit, not by sampling. It found no
transcription errors. `VERIFICATION-REPORT.md` records the method and every finding.
Counts, codes, names, data types, units, choice lists and asset types can be relied
on.

The crosswalk was built by name matching against mWater's own schema service, and
every row records how it was matched. The unmatched rows are visible.

The two specification PDFs are exports of the documents mWater already published.

## 1. Commitments made on mWater's behalf

These are the serious ones. Each states a policy, a role or a promise that was
drafted, not reported.

**`GOVERNANCE.md` is a proposal, not a description.** Nothing in it was supplied by
mWater. It invents a standards steward role, assigns the decision to a named
technical lead and a named product lead, defines three classes of change with review
periods of one, three and six weeks, promises that attribute codes and choice
identifiers are permanent, promises a deprecation window of one major version, and
commits to archiving each release to Zenodo. Every one of those is a live commitment
to implementers. Approve, amend, or replace the file.

**`CODE_OF_CONDUCT.md` invents a reporting process.** It routes reports to the Head
of Product and the COO, promises acknowledgement within five working days, and
describes an appeal route. Confirm who actually handles a report and what response
time mWater can hold to. The address has been corrected to info@mwater.co.

**`CONTRIBUTING.md` invents a contribution process.** It directs contributors to the
issue tracker, describes the review periods from `GOVERNANCE.md`, sets a policy for
translations, and states that contributors keep copyright while granting mWater the
right to publish under CC BY-SA 4.0. That last sentence has legal effect and should
be reviewed by whoever handles mWater's contracts.

**`PRIVACY.md` promises a future release.** It says the annex "will be folded into
the specification text at the next release." That is a commitment. The guidance
itself is ordinary data-protection practice and should be sound, but nobody at
mWater has reviewed it.

## 2. Statements of fact that were not sourced

**`NOTICE` asserts trademark.** The sentence "The mWater name and logo are trademarks
of mWater Foundation, Inc." was drafted, not verified. Confirm whether the marks are
registered, and where, or soften the wording.

**`SDG-MAPPING.md` claims deployment history.** It says the water standard "has been
the basis of asset registers in national and sub-national monitoring systems since
2022." Plausible, but no source was checked. Name the countries or systems, or cut
the sentence. A Digital Public Goods reviewer may ask for evidence.

**`README.md` says mWater implements both standards.** True in the sense that the
platform has water and sanitation asset tables built on them. The crosswalk shows the
platform and the standards do not line up field for field, and 13 water and 10
sanitation attributes have no matching platform column. Confirm the claim is one
mWater wants to make in that form.

**`PRIVACY.md` links to https://www.mwater.co/mwater-policies.** The page exists. The
specific privacy policy and terms of service were not read, so confirm the link
reaches what a reader needs.

**`PRIVACY.md` lists data protection regimes** in Kenya, Indonesia, India, Brazil,
Nigeria and South Africa. Those laws exist, but the list was written from general
knowledge rather than checked, and it is not exhaustive. Treat it as illustrative or
have someone verify it.

**`DATA-DICTIONARY.md` states the funders.** The USAID attributions come from the
foreword of the water standard and from mWater's own blog post about the sanitation
standard. Confirm the wording satisfies any award conditions.

## 3. Editorial choices that are defensible but were not asked for

**The repository name and layout.** `mWater/asset-standards`, with one directory per
standard, was chosen in conversation and is easy to change now and hard to change
later.

**Machine identifiers.** `type_id` in `asset-types.csv` and `choice_id` in
`choices.csv` do not appear in either standard. They were derived mechanically from
the names so that software has something stable to key on. If mWater intends these to
be normative, they belong in the next version of the standards. If not, the
`EXTRACTION-NOTES.md` files already flag them as derived.

**The `required` column.** It is set on exactly one attribute in the whole
repository, the water standard's Asset ID, taken from the one place a standard uses
"shall" about an attribute value. Neither document has a required column. Confirm
that reading.

**Contact addresses.** Every document routes correspondence to info@mwater.co.
Confirm that is where these messages should go.

**The GitHub Actions workflow.** `.github/workflows/validate.yml` runs the test suite
on every push. It installs packages from PyPI on GitHub's runners. Confirm that suits
mWater's policy for public repositories.

## 4. Known defects left in place on purpose

Both standards shipped version 1.0 with defects. None was corrected here, because
correcting a published standard is a decision for mWater, not for a transcription.
They are listed in the `EXTRACTION-NOTES.md` file of each standard and summarised in
`VERIFICATION-REPORT.md`.

Three deserve a decision soon. The water standard's introduction says 28 asset types
while Table 4 lists 29, and Figure 1 shows 28 by omitting Spring. Several flow-rate
conversion factors in both standards contradict the conversion rule the same
standards state, and the two standards contradict each other on gallons per minute
and gallons per day. Acre-foot is published as 1223.489 where the correct figure is
1233.48.
