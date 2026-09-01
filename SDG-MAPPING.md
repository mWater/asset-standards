# Relevance to the Sustainable Development Goals

Reporting on the water and sanitation goals depends on knowing what infrastructure
exists, where it is, and whether it works. Most countries cannot answer those
questions consistently, because each program, district and donor records assets in
its own schema. National figures are then assembled from data that cannot be
compared, and the error is invisible in the published number.

These two standards address that specific failure. They do not deliver a service or
treat a drop of water. They define the shared vocabulary that makes an asset
register from one district add up with an asset register from the next, which is the
precondition for measuring progress on the targets below.

This document maps each standard to the SDG targets it supports, with the target
text quoted from the United Nations. It states what the standard contributes and
what it does not.

## Target 6.1, drinking water

Target 6.1 is "By 2030, achieve universal and equitable access to safe and
affordable drinking water for all," measured by indicator 6.1.1, the "Proportion of
population using safely managed drinking water services."

Safely managed service is judged on whether a source is improved, accessible on
premises, available when needed and free from contamination. Availability and
quality are properties of the infrastructure, not of the household, so they can only
be established from the asset register.

The Water System Management Standard supplies that register. It defines the Water
point, Water system, Source, Tank, Pump and Pipe asset types, a common Status,
Condition and Functional status for every asset, codes `00041` to `00043`, and the
Sampling point and Analyzer types that carry water quality measurement to a location
in the network. The Water system type attribute, code `10201`, separates a piped
distribution network from a point source, which is the distinction that drives
service level classification.

## Target 6.2, sanitation

Target 6.2 is "By 2030, achieve access to adequate and equitable sanitation and
hygiene for all and end open defecation, paying special attention to the needs of
women and girls and those in vulnerable situations," measured by indicator 6.2.1.

Safely managed sanitation depends on the whole chain, not the toilet alone. Excreta
must be contained, emptied or conveyed, treated and disposed of or reused safely. A
country that counts toilets and stops there cannot report on the target.

The Sanitation System Management Standard is built around that chain. It defines
Sanitation point, Containment, Connection, Pipe, Channel, Manhole, Vehicle,
Treatment, Dispersal and Outfall as asset types, so that every stage from the
household to the receiving environment has a record. The Sanitation system type
attribute, code `10201`, distinguishes sewered, on-site and mixed systems, which is
the split the indicator requires. Attributes on the sanitation point record whether
facilities for women and girls are separate, which speaks to the equity clause in
the target text.

## Target 6.3, wastewater and water quality

Target 6.3 includes "halving the proportion of untreated wastewater and
substantially increasing recycling and safe reuse globally," measured by indicator
6.3.1, the "Proportion of domestic and industrial wastewater flows safely treated."

That proportion is a ratio of flows, so it cannot be estimated without knowing which
treatment assets exist, what they are designed to process, and where their outfalls
discharge.

The sanitation standard defines the Treatment, Outfall, Dispersal, Meter and
Sampling point asset types, together with hydraulic attributes that record design
flow. The water standard defines Treatment and Sampling point for the supply side.
Both standards record measurements as a magnitude and a unit drawn from `units.csv`,
which is what allows flows recorded in litres per second and in megalitres per day
to be summed correctly.

## Target 6.4, water use efficiency

Target 6.4 is "By 2030, substantially increase water-use efficiency across all
sectors and ensure sustainable withdrawals and supply of freshwater," with indicator
6.4.1 measuring "Change in water-use efficiency over time" and 6.4.2 the "Level of
water stress."

Efficiency in a piped system is mostly a question of where water is lost, and losses
are located by metering the network at known points.

The water standard defines the Meter asset type, hydraulic attributes on pipes
including nominal diameter and length, and the hierarchy rules that let an
implementer trace a meter to the zone it measures. Abstraction is recorded on the
Source asset type, which supports the withdrawal side of indicator 6.4.2.

## Target 6.6, water-related ecosystems

Target 6.6 is "By 2020, protect and restore water-related ecosystems, including
mountains, forests, wetlands, rivers, aquifers and lakes," measured by indicator
6.6.1.

The water standard is unusual among asset standards in treating natural features as
assets. Its Natural class defines Reservoir, River or stream, Aquifer, Spring,
Riparian zone, Infiltration basin, Forest, Wetland and Watershed as asset types with
geometry and condition attributes. A water utility that records the aquifer it draws
from, using the same register and the same status vocabulary as its pumps, produces
data that is usable for both service management and ecosystem monitoring.

## Targets 3.9 and 11.1

Two further targets are supported indirectly, and mWater does not claim more than
that.

Target 3.9 covers deaths and illnesses from "water and soil pollution and
contamination," measured for this sector by indicator 3.9.2, the "Mortality rate
attributed to unsafe water, unsafe sanitation and lack of hygiene." Attributing
disease to infrastructure requires knowing which population is served by which
system, which the hierarchy and service area attributes in both standards make
possible.

Target 11.1 is "By 2030, ensure access for all to adequate, safe and affordable
housing and basic services and upgrade slums." Basic services in an informal
settlement are usually delivered through shared water points and shared sanitation
facilities, both of which these standards record as first-class asset types with
usage arrangement attributes.

## What these standards do not do

A data standard does not build infrastructure and does not by itself improve a
service. It removes one specific obstacle, which is that comparable asset data
cannot be assembled from incomparable records.

Neither standard defines a service level, a functionality index, or an SDG
indicator. Those are separate instruments, and mWater keeps them separate on
purpose, so that a country can adopt the asset vocabulary without adopting anyone's
opinion about how to score a service.

Neither standard collects data. It defines what a field should mean when someone
else collects it.

## Evidence of use

The mWater platform implements both standards and is free to use. As of 2025 the
platform served more than 350,000 users in 198 countries and territories, tracking
more than 6 million water and sanitation sites from more than 35 million surveys.
The water standard has been the basis of asset registers in national and
sub-national monitoring systems since 2022. The sanitation standard was issued in
August 2026 and is at the start of its adoption.
