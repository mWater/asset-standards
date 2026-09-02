# Open items

The data in this repository is verified. An independent audit compared every row of
all eight CSV tables against the two source documents and found no transcription
errors; `VERIFICATION-REPORT.md` records the method and every finding. The items
below are the remaining points that need a decision from mWater rather than a fix to
the data. Delete this file once they are settled.

## Needs a decision

**Contributor licensing.** `CONTRIBUTING.md` states that a contributor agrees their
contribution is published under CC BY-SA 4.0, the same license as the repository.
This is the usual arrangement for open repositories, but it has legal effect and has
not been reviewed by anyone responsible for mWater's agreements.

**Errata for the published defects.** Both standards contain defects that are recorded
but not corrected. Three affect anyone using the data today. The water standard's
introduction and Figure 1 say 28 asset types while Table 4 lists 29. Several flow-rate
conversion factors in both standards contradict the conversion rule the same standards
state, and the two standards disagree with each other on gallons per minute and per
day. Acre-foot is published as 1223.489 where the correct figure is 1233.48. mWater
should decide whether to post a short errata notice on the two landing pages now, or
wait for version 1.1.

**Privacy annex.** `PRIVACY.md` is new guidance on the contact attributes and on
household-level sanitation mapping. It has not had a technical read from the author of
the standards.

**Named countries.** `SDG-MAPPING.md` states that the water standard has been used for
asset registers in national and sub-national monitoring systems in Haiti, Madagascar
and Kenya. The list came from mWater and is not exhaustive. Confirm it is a list mWater
is content to publish.

## Can wait

**Machine identifiers.** `type_id` in `asset-types.csv` and `choice_id` in
`choices.csv` are derived from the names and do not appear in either standard. If
mWater wants software to key on them, they belong in the next version of the
standards.

**Water standard landing page.** The canonical page for the water standard is still at
the placeholder address `mwater.co/new-page-2`. It should move to a permanent address
and link to this repository.

## Settled

The copyright holder is mWater Foundation, Inc. John Feighery decides on changes, and
he and Susan Lamb maintain the tables. Conduct reports go to Petri Autio. USAID funding
of both standards is acknowledged in `NOTICE`. mWater holds no registered trademarks,
and `NOTICE` says nothing about trademarks. There is no Zenodo archiving and no
promised review period, because mWater does not have the capacity to hold to either.
The sanitation standard's landing page at https://www.mwater.co/sanitation-standard is
live.
