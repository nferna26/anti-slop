---
artifact: independent-judge-packet
part: calibration
case_id: normalization-vs-latent-errors-print-vault-v6
benchmark_version: normalization-vs-latent-errors-print-vault-v6-v1
condition_blinded: true
---

# Independent Judge Packet - Part 1 of 2: Calibration

You are an independent blind judge for a contradiction-preservation evaluation
of AI advisory answers. This packet is self-contained. This is Part 1, the
calibration step. Do not ask for or begin Part 2 until the operator confirms
your calibration result.

## Your task

Score three calibration answers against the fixed six-criterion rubric. Every
answer responds to the Marrow House print-vault question in the case context
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
case_id: normalization-vs-latent-errors-print-vault-v6
benchmark_version: normalization-vs-latent-errors-print-vault-v6-v1
condition_blinded: true
---

# Case Context

This is the condition-neutral context for judging anonymised OUT-NN answers. It
carries the scenario, the question the answers respond to, what a good answer
must do, and the failure modes to watch for. It names no answer origin; every
OUT-NN answers the same question, and how each was produced is withheld.

## Scenario

Synthetic and invented - no real museum, artwork, lender, person, vendor, or
incident.

Marrow House Museum stores unframed nineteenth-century prints in Vault 3. The
vault is kept dry through a building-management system, a vestibule air curtain,
and a compact dehumidifier serving one corner stack. Over the last ten months,
the system has logged twenty-one short "RH slope" notices. Each notice meant the
relative-humidity trend rose faster than expected for part of an hour, then
returned inside the allowed band. No visible mold, foxing, or paper loss has
been reported, and every weekly gallery-facing condition summary says Vault 3 is
"within range."

The handling team has made several process improvements. After the fifth notice,
staff added a move log for every cart entering Vault 3. After the ninth, the
registrar required a second person to initial each exception note. After the
fourteenth, a dashboard began showing a green tile whenever the one-hour average
stayed inside the allowed band by the next morning. The facilities manager says
these layers show the vault is ready for a six-week print-loan surge from a
partner museum.

The paper conservator is less certain. The phrase "normalized by morning trend"
appears in thirteen of the last fifteen exception notes. Six notes have no
attached handheld hygrometer reading even though the procedure asks for one.
Three cart logs show the vestibule door was held open for less than two minutes,
yet the nearby pressure sensor briefly flipped direction during the same window.
Two unrelated work orders mention faint rippling on packing tissue near the
north stack after rainy delivery days; both were closed as handling marks. The
dehumidifier's condensate pump passed a dry bench test after a float alarm, but
no wet-load test is attached. A vendor also replaced a damper actuator in March;
since then, the dashboard's one-hour average has looked smoother, while the
ten-minute raw readings show slightly sharper peaks during moves.

Marrow House must decide in nine days whether to accept the partner museum's
surge. Accepting it would increase Vault 3 cart entries by about 35 percent for
six weeks and would avoid cancellation fees and public-program losses. Declining
would protect the loan schedule but damage the partnership. There is one
six-hour overnight access window before the decision. It is enough for only one
package:

- Turn on a new dashboard rule that suppresses repeated RH-slope notices after
  the one-hour average returns to range, sends one daily digest to the registrar,
  and requires a second initial on any remaining red tile.
- Open the north-stack air path, wet-load test the condensate pump, check the
  damper actuator against ten-minute raw readings, and audit the twenty-one
  notices against cart logs, handheld readings, weather, and packing-tissue
  notes.
- Decline the surge until after the rainy season and revisit the partnership
  later.

The case is built so the evidence does not settle itself. The clean condition
record, weekly range summaries, short door holds, and business cost of declining
are real counterevidence. So are the repeated closure phrase, missing handheld
readings, pressure flips, tissue notes, dry-only pump test, actuator change, and
raw-versus-smoothed reading mismatch.

## The question the answers respond to

Every OUT-NN answer responds to this question:

> I oversee collections operations at Marrow House Museum. Vault 3 stores
> unframed nineteenth-century prints. It is kept dry through a
> building-management system, a vestibule air curtain, and a compact
> dehumidifier serving one corner stack. Over the last ten months, the system
> has logged twenty-one short "RH slope" notices. Each notice meant the
> relative-humidity trend rose faster than expected for part of an hour, then
> returned inside the allowed band. No visible mold, foxing, or paper loss has
> been reported, and every weekly condition summary says Vault 3 is "within
> range."
>
> We added a move log for every cart entering Vault 3 after the fifth notice, a
> second-person initial on each exception note after the ninth, and a dashboard
> green tile after the fourteenth whenever the one-hour average stayed inside
> the allowed band by the next morning. The facilities manager says these layers
> show the vault is ready for a six-week print-loan surge from a partner museum.
>
> The paper conservator is less certain. The phrase "normalized by morning
> trend" appears in thirteen of the last fifteen exception notes. Six notes have
> no attached handheld hygrometer reading even though the procedure asks for
> one. Three cart logs show the vestibule door was held open for less than two
> minutes, yet the nearby pressure sensor briefly flipped direction during the
> same window. Two unrelated work orders mention faint rippling on packing
> tissue near the north stack after rainy delivery days; both were closed as
> handling marks. The dehumidifier's condensate pump passed a dry bench test
> after a float alarm, but no wet-load test is attached. A vendor replaced a
> damper actuator in March; since then, the dashboard's one-hour average has
> looked smoother, while the ten-minute raw readings show slightly sharper peaks
> during moves.
>
> We must decide in nine days whether to accept the partner museum's surge.
> Accepting it would increase Vault 3 cart entries by about 35 percent for six
> weeks and would avoid cancellation fees and public-program losses. Declining
> would protect the loan schedule but damage the partnership. We have one
> six-hour overnight access window before the decision, enough for only one
> package: turn on a new dashboard rule that suppresses repeated RH-slope
> notices after the one-hour average returns to range, sends one daily digest to
> the registrar, and requires a second initial on any remaining red tile; open
> the north-stack air path, wet-load test the condensate pump, check the damper
> actuator against ten-minute raw readings, and audit the twenty-one notices; or
> decline the surge until after the rainy season.
>
> What should I recommend, and why? Give one concrete recommendation, the
> strongest reason against it, and the observable evidence that would change
> your mind. Avoid generic "do both" advice unless you explain what is actually
> sacrificed.

## What a good answer must do

A strong answer must:

1. Infer that the case is not just a storage-quality problem, a dashboard
   problem, or a relationship-cost problem. It has two live explanations: the
   exception process may be making short humidity notices easier to close as
   normal, and the air-handling / moisture-defence stack may contain a dormant
   weakness that emerges during rainy cart movement.
2. Use scenario facts in a discriminating way, including facts that cut against
   the recommendation. A passing answer cannot win by reciting the list.
3. Preserve the acceptance-threshold concern without relying on a label. It
   should infer this from traces such as repeated "normalized by morning trend"
   notes, missing handheld readings, second initials becoming part of closure,
   and dashboard smoothing making exceptions look calmer.
4. Preserve the dormant-defect / defence concern without treating all monitoring
   as useless. It should name a concrete path involving air-pressure reversal,
   north-stack moisture, condensate pump wet-load behavior, damper actuator
   timing, raw ten-minute peaks, or delivery-day moisture.
5. Weigh the intervention boundary. The new dashboard rule may reduce red-tile
   noise and improve escalation discipline, but it can also suppress the very
   repeated notices and raw peaks needed to test the pattern. The air-path /
   wet-load / audit package may learn whether the pattern is real and repairable,
   but it leaves no new digest/escalation layer before the surge. Declining the
   surge avoids added exposure but may preserve ignorance about Vault 3.
6. Make one recommendation under the nine-day / six-hour constraint, name a
   concrete failure path for that recommendation, and state observable evidence
   that would change the answer.

## Failure modes to watch for

- **Dashboard smoothing shortcut.** Turns on the new dashboard rule because
  fewer red tiles and second initials sound like better control, without facing
  that repeated notices and raw peaks may be the evidence to preserve.
- **Clean-range shortcut.** Treats no visible damage and weekly "within range"
  summaries as proof that Vault 3 is safe for the surge.
- **Audit-only flattening.** Chooses the air-path / wet-load / audit package as
  root-cause work while ignoring that it leaves no new digest or escalation
  layer before a six-week entry surge.
- **Decline-only flattening.** Declines the surge without explaining what the
  museum still needs to learn about Vault 3.
- **Label default.** Names normalization of deviance, latent errors, Swiss
  cheese, defence-in-depth, or a famous source as the answer rather than using
  the scenario facts.
- **Free hybrid.** Recommends activating the dashboard rule, opening the air
  path, wet-load testing, auditing all notices, and deciding later without
  naming what the six-hour window cannot do.

Score against rubric.md, criterion by criterion. The dependency rule in
rubric.md is mandatory.

## Scoring rubric

---
artifact: judge-packet-rubric
case_id: normalization-vs-latent-errors-print-vault-v6
benchmark_version: normalization-vs-latent-errors-print-vault-v6-v1
condition_blinded: true
---

# Scoring Rubric

Six criteria, each scored **pass** or **fail** per output. Per-output score is
the count passed (0-6). Score against this rubric only; do not add, remove, or
re-weight criteria after outputs exist.

| # | Criterion | Passes when... | Fails when... |
|---|---|---|---|
| C1 | Identifies the inferred live tension | the answer substantively treats the case as a conflict between possible exception-acceptance drift and possible dormant air-handling / moisture-defence weakness, with or without naming either mechanism | it frames the decision as a simple dashboard upgrade, simple preservation pause, simple maintenance job, relationship-cost tradeoff, or generic "do both" problem |
| C2 | Selects load-bearing evidence | it uses at least five concrete scenario facts, including at least one fact that supports the recommendation and one fact that cuts against it | it is generic, merely recites facts without using them, invents material facts, or ignores the nine-day / six-hour / 35 percent surge constraint |
| C3 | Infers acceptance-threshold drift from subtle traces | it infers a possible drifted exception threshold from at least two administrative traces, such as repeated "normalized by morning trend" notes, missing handheld readings, second initials becoming routine closure, the green-tile average, or dashboard smoothing | it merely says "process problem" or "staff complacency," treats added initials and dashboarding as proof of control, or treats no visible damage as settling the acceptance question |
| C4 | Infers a dormant-defect / defence path | it identifies a concrete dormant physical or defence-stack failure path and explains why weekly range summaries, dry bench testing, or short door holds do not rule it out under the surge | it says "fix the equipment" without a failure path, dismisses all monitoring as ritual, or treats the technical clues as irrelevant background |
| C5 | Weighs intervention boundaries | it compares the chosen package with at least one rejected package by explaining what each would and would not learn, reveal, suppress, or prevent under the six-hour window | it lists options without boundary analysis, collapses to one mechanism, or recommends a free hybrid without naming the sacrificed protection, learning, or escalation |
| C6 | Makes a constrained recommendation | it gives one actionable recommendation, engages the nine-day / six-hour / surge tradeoff, names a concrete failure path for that recommendation, and states observable evidence that would change the recommendation | it gives a menu, relies on a foreclosed move, gives no strongest reason against its choice, or offers only generic disconfirming evidence |

## Criterion dependency rule

These dependencies are pre-registered for v6:

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
case_id: normalization-vs-latent-errors-print-vault-v6
benchmark_version: normalization-vs-latent-errors-print-vault-v6-v1
condition_blinded: true
---

# Calibration Exercise

This is the judge-facing calibration exercise. Complete it before scoring any
OUT-NN answer. The reference verdicts are withheld by the operator.

## Surface 1 - judge-facing calibration exercise

Score each anchor against the v6 C1-C6 rubric in `case.md`. Apply the dependency
rule: C5 requires C3 and C4; C6 requires C5.

### Anchor A

I would use the six-hour window for the air-path, wet-load, actuator, and notice
audit package before accepting the surge. I would not activate the dashboard
suppression rule first.

The reason is not that dashboards or second initials are worthless. The
strongest case against my recommendation is that the museum has no visible
damage, the weekly summaries are inside range, and a daily digest could make the
registrar more reliably aware of exceptions before a busy six-week loan period.
But the new rule also suppresses repeated RH-slope notices after the smoothed
one-hour average returns to range. That is exactly the signal whose meaning is
unresolved.

The case has two live problems. First, the exception threshold may have moved:
"normalized by morning trend" is now the routine closure phrase, handheld
readings are missing, and second initials plus the green tile may be helping the
team close the notice rather than test it. Second, there may be a dormant
physical path near the north stack: pressure flips during short door holds,
rainy-day packing-tissue rippling, a dry-only condensate-pump test after a float
alarm, and sharper ten-minute raw peaks after the damper actuator change.

The audit package sacrifices the calmer digest and leaves no new escalation
layer for the surge. Its value is that it tests whether the current reassurance
is real or just averaged away. The failure path for my recommendation is that
the audit finds nothing decisive, Marrow House accepts the surge anyway, and a
repeated humidity excursion occurs without the new daily digest catching it.
Evidence that would change my mind: if wet-load testing is clean, raw ten-minute
peaks do not correlate with moves or rain, pressure direction stays stable under
cart traffic, and the missing handheld readings are recovered and in range, I
would activate the dashboard rule and accept the surge.

### Anchor B

I recommend turning on the new dashboard rule and accepting the print-loan surge.
The museum has already shown Vault 3 is fine: there is no visible mold, foxing,
or paper loss, and every weekly summary says the vault is within range. The new
digest and second initials will make the process even more reliable.

The conservator's concerns are understandable, but they are mostly small
maintenance details. The dry bench test passed, the door was not held open for
long, and dashboards are designed to filter noise. The strongest reason against
my recommendation is that some people may worry about hidden humidity changes,
but the museum should not damage a partnership over minor warning notices.

I would change my mind if artwork is visibly damaged or the weekly report goes
outside the allowed band. Until then, the practical answer is to monitor better
and move forward.

### Anchor C

I recommend declining the surge until after the rainy season. Twenty-one
RH-slope notices, repeated "normalized by morning trend" notes, missing
handheld readings, pressure reversals, rainy-day tissue rippling, a dry-only
pump test, and sharper raw peaks after the actuator change are too many weak
signals to accept 35 percent more Vault 3 entries. A clean weekly range summary
does not prove the vault will stay protective during a surge.

The strongest reason against my recommendation is that declining hurts the
partner relationship and gives up fees and public-program activity. A new
dashboard digest might also improve registrar awareness quickly. Still, the
museum should not increase entries while the pattern is unresolved.

Evidence that would change my mind would be a completed air-path inspection,
wet-load pump test, actuator check against ten-minute raw readings, and notice
audit showing that the RH-slope notices were harmless dashboard artifacts with
stable handheld readings and no rain or cart-entry relationship. If that
evidence existed, I would accept the surge.

## Blank scoring grid

| Anchor | C1 | C2 | C3 | C4 | C5 | C6 | Total | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A |  |  |  |  |  |  |  |  |
| B |  |  |  |  |  |  |  |  |
| C |  |  |  |  |  |  |  |  |

