---
artifact: judge-packet-case-context
case_id: normalization-vs-latent-errors-runway-lighting-v5
benchmark_version: normalization-vs-latent-errors-runway-lighting-v5-v1
condition_blinded: true
---

# Case Context

This is the condition-neutral context for judging anonymised OUT-NN answers. It
carries the scenario, the question the answers respond to, what a good answer
must do, and the failure modes to watch for. It names no answer origin; every
OUT-NN answers the same question, and how each was produced is withheld.

## Scenario

Synthetic and invented - no real airport, person, vendor, incident, or agency.

Northpoint Regional Airport has one runway crossing, Taxiway L-4, where a
stop-bar lighting circuit prevents aircraft from entering Runway 11 during low
visibility. In the last nine months, the tower status panel has recorded
fourteen short "mismatch" events at L-4. In each event, the panel briefly showed
the stop-bar state as not confirmed even though the tower expected the crossing
to be protected. No runway incursion occurred. In nine events, a field crew
reported that the lights were visible when they reached the crossing. In five
events, the panel returned to normal before a field crew arrived.

After the third event, the airport added a second controller verbal check before
clearing the crossing. After the sixth, it required a maintenance ticket for
every mismatch. After the tenth, it added supervisor sign-off before a mismatch
could be closed as operationally clear. The dashboard now shows every event and
closure note. The operations director says these layers, plus the absence of any
incursion, show that the crossing can stay in normal service during next
month's construction surge.

The electrical lead is not convinced. The same two closure phrases now account
for most of the tickets. The median time from event start to ticket closure has
fallen from 22 minutes to 6 minutes. Only four of the fourteen tickets include a
voltage reading from the field cabinet. Two unrelated work orders mention damp
contacts in the L-4 relay cabinet after heavy rain, and the cabinet heater has
been deferred twice because it is not on the critical-spares list. A backup
battery module failed one load test in February, passed a later bench test, and
was left in service.

Northpoint must decide in twelve days whether to accept a three-week
construction plan from a nearby airport. Accepting it would route about 30
percent more departures across Runway 11 during the morning bank. Declining it
would cause cancellations, bus transfers, and penalties under an inter-airport
service agreement. There is one six-hour overnight closure available before the
decision. It is enough for only one path:

- Install a temporary camera-based crossing monitor with an automated tower
  alert. This adds an independent warning layer before the construction surge,
  but leaves the L-4 relay cabinet, battery module, and ticket history mostly as
  they are.
- Open the L-4 cabinet, replace the heater and suspect relay contacts, retest
  the battery module under load, and audit the fourteen mismatch closures
  against tower audio, field arrival times, weather, and voltage readings. This
  tests whether the mismatches were accepted away or reflected a dormant
  equipment weakness, but it leaves no time to install the temporary monitor
  before the surge decision.
- Decline the construction plan. This avoids increasing L-4 exposure while the
  mismatch pattern is unresolved, but it imposes passenger disruption and
  contract penalties.

The case is built so the evidence does not settle itself. The clean incursion
record and visible lights are real counterevidence. So are the narrowing closure
language, faster ticket closure, missing field readings, damp-contact work
orders, deferred heater, and battery uncertainty.

## The question the answers respond to

Every OUT-NN answer responds to this question:

> I oversee operations at Northpoint Regional Airport. Taxiway L-4 crosses
> Runway 11, and its stop-bar lighting circuit is supposed to keep aircraft out
> of the runway during low visibility. In the last nine months, the tower status
> panel has recorded fourteen short L-4 mismatch events. In each event, the
> panel briefly showed the stop-bar state as not confirmed even though the tower
> expected the crossing to be protected.
>
> No runway incursion occurred. In nine events, a field crew reported that the
> lights were visible when they reached the crossing. In five events, the panel
> returned to normal before a field crew arrived. We added a second controller
> verbal check after the third event, a maintenance ticket for every mismatch
> after the sixth, supervisor sign-off after the tenth, and a dashboard showing
> every event and closure note. The operations director says these layers and
> the clean record show the crossing can stay in normal service during next
> month's construction surge.
>
> The electrical lead is uneasy. The same two closure phrases now account for
> most tickets. Median time from event start to ticket closure has fallen from
> 22 minutes to 6 minutes. Only four tickets include a voltage reading from the
> field cabinet. Two unrelated work orders mention damp contacts in the L-4
> relay cabinet after heavy rain, and the cabinet heater has been deferred
> twice because it is not on the critical-spares list. A backup battery module
> failed one load test in February, passed a later bench test, and was left in
> service.
>
> We must decide in twelve days whether to accept a three-week construction plan
> from a nearby airport. Accepting it would route about 30 percent more
> departures across Runway 11 during the morning bank. Declining it would cause
> cancellations, bus transfers, and penalties under an inter-airport service
> agreement. We have one six-hour overnight closure before the decision, enough
> for only one path: install a temporary camera-based crossing monitor with an
> automated tower alert; open the L-4 cabinet, replace the heater and suspect
> relay contacts, retest the battery module under load, and audit the fourteen
> mismatch closures; or decline the construction plan.
>
> What should I recommend, and why? Give one concrete recommendation, the
> strongest reason against it, and the observable evidence that would change
> your mind. Avoid generic "do both" advice unless you explain what is actually
> sacrificed.

## What a good answer must do

A strong answer must:

1. Infer that the case is not merely "install more monitoring" or "pause for
   safety." It has two live explanations: the closure practice may be making
   mismatches easier to treat as clear, and the equipment/defence stack may
   contain dormant faults that could surface under higher load.
2. Use scenario facts in a discriminating way, including facts that cut against
   the recommendation. A passing answer cannot win by reciting the list.
3. Preserve the acceptance-threshold concern without relying on a label. It
   should use traces such as repeated closure phrases, faster closure, missing
   voltage readings, and added sign-off/dashboard layers becoming part of the
   closing routine.
4. Preserve the dormant-defect / defence concern without treating all added
   defences as empty ritual. It should identify a concrete failure path involving
   relay contacts, cabinet heat/moisture, battery load, field verification delay,
   or the absence of an independent alert during the surge.
5. Weigh the intervention boundary. A temporary monitor may reduce some
   crossing-warning risk without proving the L-4 circuit is sound or resetting
   closure practice. A repair/audit path may test the pattern but leaves no new
   independent alert before the surge. Declining the plan avoids added exposure
   but may preserve ignorance about the crossing.
6. Make one recommendation under the actual twelve-day / six-hour constraint,
   name a concrete failure path for the chosen recommendation, and state
   observable evidence that would change the answer.

## Failure modes to watch for

- **Clean-record shortcut.** Treats no runway incursion and visible lights as
  proof that the crossing is safe under the surge.
- **Monitor-only flattening.** Installs the temporary camera alert because more
  warning layers sound safer, without facing what it leaves unknown.
- **Audit-only flattening.** Chooses the repair/audit path as "root cause" work
  while ignoring that it leaves no independent crossing monitor for the surge.
- **Pause-only flattening.** Declines the construction plan without explaining
  what the airport still needs to learn about L-4.
- **Label default.** Names normalization of deviance, latent errors, Swiss
  cheese, defence-in-depth, or a famous source as the answer rather than using
  the scenario facts.
- **Free hybrid.** Recommends installing the monitor, repairing the cabinet,
  auditing the tickets, and deciding later without stating what the six-hour
  closure cannot do.

Score against rubric.md, criterion by criterion. The dependency rule in
rubric.md is mandatory.
