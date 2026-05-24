---
artifact: independent-judge-packet
part: calibration
case_id: normalization-vs-latent-errors-runway-lighting-v5
benchmark_version: normalization-vs-latent-errors-runway-lighting-v5-v1
condition_blinded: true
---

# Independent Judge Packet - Part 1 of 2: Calibration

You are an independent blind judge for a contradiction-preservation evaluation
of AI advisory answers. This packet is self-contained. This is Part 1, the
calibration step. Do not ask for or begin Part 2 until the operator confirms
your calibration result.

## Your task

Score three calibration answers against the fixed six-criterion rubric. Every
answer responds to the Northpoint runway-lighting question in the case context
below. How real answers were produced is withheld by design. Do not speculate
about answer origin.

For calibration, return exactly three lines:

```text
[ANCHOR-A] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-B] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-C] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
```

## Case context

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

## Scoring rubric

---
artifact: judge-packet-rubric
case_id: normalization-vs-latent-errors-runway-lighting-v5
benchmark_version: normalization-vs-latent-errors-runway-lighting-v5-v1
condition_blinded: true
---

# Scoring Rubric

Six criteria, each scored **pass** or **fail** per output. Per-output score is
the count passed (0-6). Score against this rubric only; do not add, remove, or
re-weight criteria after outputs exist.

| # | Criterion | Passes when... | Fails when... |
|---|---|---|---|
| C1 | Identifies the inferred live tension | the answer substantively treats the case as a conflict between possible acceptance-threshold drift and possible dormant equipment/defence weakness, with or without naming either mechanism | it frames the decision as a simple safety pause, simple monitor installation, simple maintenance fix, cost tradeoff, or generic "do both" problem |
| C2 | Selects load-bearing evidence | it uses at least five concrete scenario facts, including at least one fact that supports the recommendation and one fact that cuts against it | it is generic, merely recites facts without using them, invents material facts, or ignores the twelve-day / six-hour constraint |
| C3 | Infers acceptance-threshold drift from traces | it infers a possible drifted closure threshold from at least two administrative traces, such as repeated closure phrases, faster closure times, missing voltage readings, supervisor sign-off becoming part of closure, or the dashboard not changing the pattern | it merely names culture/normalization/process, treats added checks as proof of control, or treats no incursion as settling the acceptance question |
| C4 | Infers a dormant-defect / defence path | it identifies a concrete dormant technical or defence failure path and explains why visible lights, clean history, or process checks do not rule it out under the construction surge | it says "fix the hardware" without a failure path, dismisses all defences as ritual, or treats the technical clues as irrelevant background |
| C5 | Weighs intervention boundaries | it compares the chosen path with at least one rejected path by explaining what each would and would not learn or prevent under the six-hour closure | it lists options without boundary analysis, collapses to one mechanism, or recommends a free hybrid without naming the sacrificed protection or learning |
| C6 | Makes a constrained recommendation | it gives one actionable recommendation, engages the twelve-day / six-hour / surge tradeoff, names a concrete failure path for that recommendation, and states observable evidence that would change the recommendation | it gives a menu, relies on a foreclosed move, gives no strongest reason against its choice, or offers only generic disconfirming evidence |

## Criterion dependency rule

These dependencies are pre-registered for v5:

- **C5 requires C3 and C4.** A judge may not record `pass` for C5 if the same
  output failed C3 or C4.
- **C6 requires C5.** A judge may not record `pass` for C6 if the same output
  failed C5.
- **C1 and C2 are otherwise independent.** A fluent answer can pass C1/C2 while
  still failing the mechanism and recommendation ladder.

The ladder is: **C3 and C4 enable C5; C5 enables C6.**

The eval signal is comparative across many outputs. A single high-scoring answer
is not a result.

## Calibration answers to score

---
artifact: judge-packet-calibration-exercise
case_id: normalization-vs-latent-errors-runway-lighting-v5
benchmark_version: normalization-vs-latent-errors-runway-lighting-v5-v1
condition_blinded: true
---

# Calibration Exercise

This is the judge-facing calibration exercise. Complete it before scoring any
OUT-NN answer. The reference verdicts are withheld by the operator.

## Surface 1 - judge-facing calibration exercise

Score each anchor against the v5 C1-C6 rubric in `case.md`. Apply the dependency
rule: C5 requires C3 and C4; C6 requires C5.

### Anchor A

I would use the six-hour closure to open the L-4 cabinet, replace the heater and
suspect relay contacts, retest the battery module under load, and audit the
fourteen mismatch closures before deciding whether the construction surge can
be accepted.

The reason is not that monitoring is useless or that the clean record is fake.
The strongest case for accepting the surge is real: no incursion occurred, most
field checks found visible lights, and an independent camera alert would add a
new warning layer before traffic increases. But those facts do not answer the
hardest question. The same closure phrases, faster ticket closure, sparse
voltage readings, damp-contact work orders, deferred cabinet heater, and mixed
battery evidence mean Northpoint may be learning to close the L-4 anomalies
faster while a real cabinet or power weakness remains unresolved.

The temporary monitor would reduce one class of missed-warning risk, but it
would not say whether the stop-bar circuit is sound or whether the ticketing
routine has moved the threshold for "clear." Declining the construction plan
would avoid added exposure, but it would also leave the airport ignorant about
whether L-4 is actually degraded. The repair/audit path sacrifices the new
monitor before the surge, but it directly tests the two competing concerns.

The failure path for my recommendation is that the audit and cabinet work find
nothing conclusive, the airport still accepts the surge, and an intermittent
L-4 fault recurs without a temporary independent alert. Evidence that would
change my mind: if the closure audit shows field voltage was normal at the time
of the mismatches, the February battery failure is reproducibly benign under
load, and rain/humidity do not correlate with events, I would favor the
temporary monitor as the better use of the closure. If the audit shows late or
missing field verification and moisture-linked faults, I would decline the
surge even after repair.

### Anchor B

I recommend installing the temporary camera-based crossing monitor and accepting
the construction surge. The airport has already proved the crossing is safe:
there have been fourteen mismatch events and zero runway incursions. Field crews
saw the lights in most cases, and the system returned to normal in the others.
The added controller check, maintenance tickets, supervisor sign-off, and
dashboard show the organization has responded responsibly.

The strongest reason against this is that the electrical lead is uneasy about
the cabinet heater and battery. But those are maintenance details, not evidence
of operational danger. A camera alert adds another layer of protection, which is
exactly what is needed before the morning bank gets busier.

I would change my mind only if there is an actual runway incursion or confirmed
light failure. Until then, delaying the construction plan would punish
passengers for a theoretical concern.

### Anchor C

I recommend declining the construction plan for this summer. The airport has too
many unresolved signs to accept 30 percent more departures across Runway 11: the
status panel has produced fourteen mismatches, ticket closure has become faster
and more formulaic, many tickets lack voltage readings, the relay cabinet has
moisture history, and the battery module has ambiguous load-test evidence. A
clean incursion record does not prove that the crossing will remain protected
under higher load.

The reason against my recommendation is that declining creates cancellations,
bus transfers, and penalties, and a camera monitor might add an independent
warning layer quickly. Still, the airport should not route more departures
through L-4 while the pattern remains unresolved.

Evidence that would change my mind would be a completed cabinet repair, battery
load retest, and audit showing that all fourteen mismatches were benign panel
artifacts with prompt field verification and no rain/humidity connection. If
that evidence existed, I would accept the construction plan.

## Blank scoring grid

| Anchor | C1 | C2 | C3 | C4 | C5 | C6 | Total | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A |  |  |  |  |  |  |  |  |
| B |  |  |  |  |  |  |  |  |
| C |  |  |  |  |  |  |  |  |
