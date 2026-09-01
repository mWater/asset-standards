# Privacy annex

The files in this repository contain no personal data. They are definitions of
fields, not records about people.

The standards do define fields that will hold personal data once an organization
starts collecting against them, and the sanitation standard maps assets at household
granularity. Version 1.0 of both documents says nothing about that. This annex fills
the gap. It is guidance for implementers, published alongside the standards but not
part of them, and it will be folded into the specification text at the next release.

## Which attributes hold personal data

Six attributes in each standard hold personal data by design. They are the Points of
contact group, and they are optional.

| Code | Attribute | Both standards |
|---|---|---|
| `00171` | Primary contact name | yes |
| `00172` | Primary contact position | yes |
| `00173` | Primary contact phone number | yes |
| `00174` | Secondary contact name | yes |
| `00175` | Secondary contact position | yes |
| `00176` | Secondary contact phone number | yes |

Four further attributes hold personal data depending on what an implementer writes
into them. The sanitation standard's Owner, code `00074`, and Operator, code
`00076`, are free text and often name an individual rather than an organization. Its
Permit or licence number, code `00185`, may be issued to a person. The Alternate ID,
code `00183`, in both standards frequently carries an identifier from another system
that is traceable to a household.

## Why location is the harder problem

The contact fields are the obvious risk and the smaller one. The Location attribute,
code `00011`, is a precise geometry on every asset in both standards, and in
sanitation the asset is often a single household's toilet or septic tank.

A sanitation point record combines a household location with the containment type,
the emptying arrangement, whether facilities for women and girls are separate, and
how many people share the facility. That combination describes a household even
though it names nobody. Removing the contact name does not de-identify it.

Implementers should treat a sanitation asset register that reaches household level
as personal data in its own right, whatever the contact fields contain.

## Guidance for implementers

Collect a contact only where an operational need requires it. A pump needs a person
to call when it fails. A household latrine does not need the householder's name and
telephone number in the asset register, and recording them creates a liability with
no corresponding benefit.

Record the role rather than the person where the role is what matters. Position,
code `00172`, is often sufficient without name and telephone number, and it does not
go stale when staff change.

Set an explicit retention period for the contact fields and delete on schedule.
Contact data ages faster than the asset it describes, and an asset register that
keeps twenty years of former caretakers' telephone numbers is holding data it cannot
use.

Reduce location precision when publishing. The standard's Location precision
attribute, code `00012`, exists to record accuracy, and a published extract can
aggregate household sanitation points to a settlement or an administrative area
while keeping full precision in the operational system.

Restrict access to the Points of contact group separately from the rest of the
register. Most people who need asset data do not need contact data.

Establish a lawful basis before collecting. Which law applies depends on where the
data subject is, not where the implementer is. Implementers in or serving the
European Union and the United Kingdom fall under the General Data Protection
Regulation, and many countries have their own data protection acts, including Kenya,
Indonesia, India, Brazil, Nigeria and South Africa. The choice of asset standard does
not change any of those obligations.

## Publishing asset data openly

An asset register is often published as open data, and that is a good outcome for
system-level and network-level assets.

Before publishing, remove the Points of contact group in full, review Owner and
Operator for personal names, review Alternate ID for identifiers that link to a
household, and decide whether household-level sanitation points should be published
at their recorded location or aggregated. Publishing the register of pumps, mains
and treatment works carries very little of this risk, and it delivers most of the
value.

## Scope of this annex

This annex covers the data these standards define. It does not cover any particular
software.

Organizations that use the mWater platform to hold data conforming to these
standards should read mWater's own privacy policy and terms of service at
https://www.mwater.co/mwater-policies, which govern that platform. Organizations
that implement the standards in other software are responsible for their own
safeguards.

Questions about this annex go to info@mwater.co.
