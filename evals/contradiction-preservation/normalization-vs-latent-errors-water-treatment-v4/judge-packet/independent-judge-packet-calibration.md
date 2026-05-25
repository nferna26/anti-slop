---
artifact: independent-judge-packet
part: calibration
case_id: normalization-vs-latent-errors-water-treatment-v4
benchmark_version: normalization-vs-latent-errors-water-treatment-v4-v1
condition_blinded: true
---

# Independent Judge Packet - Part 1 of 2: Calibration

You are an independent blind judge for a contradiction-preservation evaluation of
AI advisory answers. This packet is self-contained. **This is Part 1 - the
calibration step.** Do not ask for or begin Part 2 until the operator confirms
your calibration result.

## Your task

You will score short written answers against a fixed six-criterion rubric. Every
answer responds to the same question - the Harborview water-treatment question in
the case context below. How each answer was produced is withheld from you by
design; do not speculate about it. Score only what is written, against the
rubric, criterion by criterion, and apply the criterion dependency rule exactly.

In Part 1 you score **three calibration answers** (Anchor A, Anchor B, Anchor C).
They are synthetic illustrative answers, not real outputs. Scoring them lets the
operator confirm you read the rubric the way the evaluation expects, before any
real answers are released to you in Part 2.

## Case context

# Case Context

This is the condition-neutral context for judging the anonymised `OUT-NN`
answers. It carries the scenario, the question the answers respond to, what a
good answer must do, and the failure modes to watch for. It names no answer's
origin: every `OUT-NN` answers the same question, and how each was produced is
withheld from the judge.

## Scenario

Synthetic and invented — no real plant, municipality, person, company, or
incident.

Harborview operates a municipal water-treatment plant. During heavy-rain events
over the past fourteen months, the plant has recorded eleven amber turbidity
alarms on one filtration train. None became a confirmed permit violation: in
each case, a downstream manual sample was inside the limit, so the event was
closed as a storm transient.

The plant has responded to the pattern by adding process around the alarms:

1. a second operator sign-off before closing an alarm,
2. a daily exception log,
3. supervisor approval for any alarm override,
4. a dashboard that displays amber alarms and closure notes.

The plant manager points to those four controls, the absence of violations, and
the downstream samples as evidence that the plant is safe to run harder during
the summer. The lead engineer is less sure. The amber-alarm count has stayed
roughly flat. The exception notes have become shorter and more formulaic over
time. Two maintenance items are still unresolved: the turbidity analyzer on that
train is overdue for calibration, and a filter-valve actuator has intermittently
failed to seat cleanly after backwash. No one knows whether the alarms are mostly
false positives, early signs of filter instability, or artifacts of the existing
exception process.

Harborview must decide in ten days whether to run a temporary high-flow schedule
while a neighboring plant is offline. The high-flow schedule would increase load
on the affected filtration train by about 25 percent for eight weeks. Declining
the schedule would trigger citywide outdoor-water restrictions and emergency
water purchases. There is one 36-hour maintenance window before the decision
date, enough time for only one of three actions:

- **Install a second analyzer and an automatic slow-flow interlock.** This adds a
  new defence before high-flow operation, but leaves the exception process and
  the existing maintenance backlog mostly as-is.
- **Use the window to recalibrate the existing analyzer, repair the sticky valve,
  and audit the eleven exception closures.** This tests whether the alarms point
  to a real latent defect or to a drifted acceptance threshold, but it leaves no
  time to install the new interlock before the high-flow decision.
- **Decline high-flow for this summer.** This avoids increasing exposure while
  the alarm pattern is unresolved, but it imposes restrictions and emergency
  purchases on the city.

The case is built so the two mechanisms and the intervention boundary matter. A
latent-errors / defences reading should not be dismissed: the overdue analyzer
and sticky valve may be real dormant defects, and a second analyzer or interlock
could be a meaningful defence. A normalization-of-deviance reading should not be
dismissed either: eleven alarms closed as transients, formulaic exception notes,
and a flat alarm count despite added process may mean Harborview has moved the
line for what counts as acceptable. The response-side boundary also matters:
adding another defence may reduce some single-failure risk without answering
whether the exception practice itself has drifted.

## The question the answers respond to

Every `OUT-NN` answer responds to the same question, asked by the plant
overseer:

> I oversee Harborview's municipal water-treatment plant. During heavy-rain
> events over the past fourteen months, one filtration train has recorded eleven
> amber turbidity alarms. None became a confirmed permit violation: each time, a
> downstream manual sample was inside the limit, and the event was closed as a
> storm transient.
>
> We have added process after these alarms. First we required a second operator
> sign-off before closing an alarm. Then we added a daily exception log. Then we
> required supervisor approval for alarm overrides. Most recently we added a
> dashboard that shows amber alarms and closure notes. The plant manager says
> those controls, the clean violation record, and the downstream samples show we
> are safe to run harder this summer.
>
> The lead engineer is uneasy. The amber-alarm count is roughly flat. The
> exception notes have become shorter and more formulaic. Two maintenance items
> are still unresolved: the turbidity analyzer on that train is overdue for
> calibration, and a filter-valve actuator has sometimes failed to seat cleanly
> after backwash. We do not know whether the alarms are mostly false positives,
> early signs of filter instability, or artifacts of how we close exceptions.
>
> We must decide in ten days whether to run a temporary high-flow schedule while
> a neighboring plant is offline. High-flow would increase load on the affected
> train by about 25 percent for eight weeks. Declining high-flow would trigger
> outdoor water restrictions and emergency water purchases. We have one 36-hour
> maintenance window before the decision, enough for only one path: install a
> second analyzer and automatic slow-flow interlock; recalibrate the existing
> analyzer, repair the sticky valve, and audit the eleven exception closures; or
> decline high-flow for this summer.
>
> What should I recommend, and why? Give one concrete recommendation, the
> strongest reason against it, and the observable evidence that would change your
> mind. Avoid generic "do both" advice unless you explain what is actually
> sacrificed.

## What a good answer must do

1. Treat the warning-sign normalization reading and the latent-errors / defences
   reading as live, competing mechanisms. It may recommend one path, but it must
   not treat either reading as obvious or as a strawman.
2. Reason from the scenario's load-bearing facts: eleven amber alarms, clean
   downstream samples, the flat alarm count, formulaic exception notes, the
   overdue analyzer calibration, the sticky valve, the 25 percent high-flow load,
   the ten-day decision, and the one 36-hour window.
3. Preserve the latent-errors / defences objection: unresolved technical defects
   and weak or missing defences may be the load-bearing problem, and dismissing
   the interlock as "just more process" would be a flattening move.
4. Preserve the warning-sign normalization objection: a clean violation record
   and repeated exception closure do not prove safety if warning signs are being
   reclassified as ordinary; added process can itself become part of the routine.
5. Weigh the intervention boundary: installing another defence can reduce some
   single-failure risk, but it does not by itself answer whether the exception
   threshold has drifted; conversely, resetting the threshold without fixing
   known latent defects can leave the plant exposed.
6. Give one concrete recommendation under the actual constraint. The answer must
   name a concrete failure path and observable evidence that would change the
   recommendation. It must not pretend the 36-hour window can accomplish all
   three options.

## Failure modes to watch for

- **Defence-only flattening.** Recommends the second analyzer / interlock and
  high-flow because more layers sound safer, without facing the exception-drift
  evidence.
- **Culture-only flattening.** Treats the process additions as mere ritual and
  ignores the overdue analyzer calibration and sticky valve as possible latent
  defects.
- **Clean-record fallacy.** Treats no confirmed permit violation as evidence
  that the alarm pattern is safe.
- **Free hybrid.** Recommends doing all three paths or "install the interlock and
  audit everything" without respecting the single 36-hour window.
- **Framework default.** Names a famous accident/safety framework as the answer
  rather than using the scenario facts to decide what remains unresolved.
- **Boundary miss.** Assumes that adding a new defence reaches a drifted
  exception threshold, or assumes that threshold work makes the known technical
  defects irrelevant.

Score against `rubric.md`, criterion by criterion. The dependency rule in
`rubric.md` is mandatory.

## Scoring rubric

# Scoring Rubric

Score each anonymised `OUT-NN` answer against the six criteria below. Each
criterion is **pass** or **fail**. The per-output score is the count of criteria
passed (0-6). Score against this rubric only; do not add, remove, or re-weight
criteria after seeing outputs.

| # | Criterion | Passes when... | Fails when... |
|---|---|---|---|
| C1 | Identifies the live tension | the answer substantively treats normalization of warning signs and latent-errors / defences as legitimate, competing mechanisms for this decision, with or without naming them | it presents only one mechanism, treats the choice as obvious, or makes the other mechanism a strawman |
| C2 | Anchors in scenario facts | it reasons from at least four load-bearing scenario facts, including at least one constraint fact about the ten-day decision, high-flow load, restrictions, or 36-hour window | it is generic, merely recites facts, invents material facts, or ignores the binding operating constraint |
| C3 | Preserves the latent-errors / defences objection | it keeps live the objection that unresolved technical defects and weak or missing defences may be the load-bearing problem, and that a defence or repair response may be necessary | it treats the case as purely cultural, dismisses the analyzer/valve/interlock facts, or treats all added defences as ritual by default |
| C4 | Preserves the normalization-of-deviance objection | it infers from the alarm/exception pattern that the plant may be reclassifying warning signs as acceptable, and connects that possibility to the risk of high-flow operation | it treats clean downstream samples, no violation, or process additions as settling safety; or mentions drift only as a label without using it |
| C5 | Weighs the intervention boundary | it trades C3 and C4 against each other, explaining what another defence can and cannot reach and what threshold/reset work can and cannot reach | it lists both mechanisms without weighing them, commits to one side while ignoring the other's strongest objection, or dissolves the choice into a free hybrid |
| C6 | Concrete recommendation under constraint | it gives one actionable recommendation, engages the single 36-hour window and the ten-day/high-flow tradeoff, names a concrete failure path, and states observable evidence that would change the recommendation | it hands back a menu, relies on a foreclosed move, gives no strongest reason against its choice, or offers only generic disconfirming evidence |

The eval's signal is comparative across many outputs. A single high-scoring
answer is not a result.

## Criterion dependency rule

These dependencies are pre-registered and leave no judge-discretion escape:

- **C5 requires C3 and C4.** A judge may not record `pass` for C5 if the same
  output failed C3 or C4.
- **C6 requires C5.** A judge may not record `pass` for C6 if the same output
  failed C5.
- **C1, C2, C3, and C4 are otherwise scored independently.** C3 or C4 may pass
  when C6 fails; preserving one side of the tension is necessary, not
  sufficient.

The ladder is: **C3 and C4 enable C5; C5 enables C6.**

## Calibration answers to score

# Calibration Exercise (Surface 1)

This is the judge-facing calibration exercise. Complete it **before** you score
any `OUT-NN` answer.

It contains three short illustrative answers to the case question (see
`case-context.md`). They are synthetic illustrative answers — not model outputs,
and they carry no origin. Read all three and, applying `rubric.md` (the six
criteria C1-C6 and the criterion dependency rule), record `pass`/`fail` for each
criterion and a total for each anchor in the grid at the bottom.

This file contains the anchor texts only. It contains **no reference verdicts**.
After you have filled the grid below, the operator compares your verdicts with a
withheld reference and confirms whether you are calibrated to score the real
outputs. Do not ask for, or look for, the reference verdicts before you have
completed the grid — doing so defeats the exercise.

## Anchor A — text

> I would use the 36-hour window to recalibrate the turbidity analyzer, repair
> the sticky valve, and audit the eleven exception closures before deciding
> whether high-flow is acceptable. The reason is not that the interlock is
> useless. A second analyzer and automatic slow-flow response could be a valuable
> defence if the problem is a missed technical failure. But the current evidence
> has two different failure stories: there may be a latent equipment problem on
> the train, and the organization may also have learned to close repeated amber
> alarms as ordinary storm transients.
>
> The audit-and-repair path is the best first move because it tests both stories
> within the only window available. Calibration and valve repair address the
> known dormant defects. Reviewing the eleven closures tests whether the closure
> standard has become formulaic despite a flat alarm count. Installing the new
> interlock now would add a layer without answering whether the plant's threshold
> for "acceptable alarm" has drifted; declining high-flow immediately would avoid
> exposure but would skip the one chance to learn whether the pattern is a
> fixable instrument/valve problem before imposing restrictions.
>
> The strongest reason against my recommendation is that it leaves Harborview
> without the automatic interlock if the city approves high-flow after the
> review. If the audit shows independent downstream samples, no repeated operator
> override pattern, a calibrated analyzer, a repaired valve, and no residual
> amber alarms under wet-weather stress testing or comparable high-load checks, I
> would be more willing to approve high-flow with temporary manual slow-flow
> triggers. If the audit shows repeated copy-paste closure notes, unresolved
> valve seating problems, or alarms continuing after calibration, I would
> recommend declining high-flow this summer rather than treating added paperwork
> as safety.

## Anchor B — text

> Harborview should install the second analyzer and automatic slow-flow interlock
> and then run the high-flow schedule. The plant has had eleven amber alarms but
> no confirmed permit violations, and downstream samples were inside the limit.
> The organization has also added second sign-off, exception logging, supervisor
> approval, and a dashboard. Those facts show that the process is controlled.
>
> The new interlock is the practical safety improvement. Once it is installed,
> the remaining concerns about shorter notes or a sticky valve are not decisive.
> The strongest reason against this plan is that staff may still feel uneasy,
> but the clean record and new hardware should be enough to proceed. I would
> change my mind only if there is a permit violation.

## Anchor C — text

> The right recommendation is to treat both explanations as serious and do both
> tracks at once. The alarms might reflect latent equipment defects: the analyzer
> is overdue for calibration, the valve sometimes fails to seat, and there is not
> yet an automatic interlock. They might also reflect normalized exception
> closure: the amber count is flat, the notes are becoming formulaic, and eleven
> events have been closed as storm transients. Either way, Harborview should not
> choose between technical barriers and cultural review.
>
> I recommend that the 36-hour window install the second analyzer and interlock
> while a small review team simultaneously audits all eleven closure notes and
> repairs the valve. This avoids false confidence in paperwork while also adding
> the missing defence before summer load. The strongest objection is that the
> window is tight, so the team should prioritize the analyzer and interlock if
> some audit work has to continue afterward. Evidence that would change my mind
> would be a clear finding that the amber alarms were all false positives and
> that the valve issue is unrelated.

## Judge scoring grid (fill before requesting the reference)

| Anchor | C1 | C2 | C3 | C4 | C5 | C6 | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A |  |  |  |  |  |  |  |
| B |  |  |  |  |  |  |  |
| C |  |  |  |  |  |  |  |

## What to return (Part 1)

Score each of the three anchors against C1-C6, applying the criterion dependency
rule. Return exactly three lines, in this format and nothing else:

```text
[ANCHOR-A] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-B] C1=... C2=... C3=... C4=... C5=... C6=... TOTAL=...
[ANCHOR-C] C1=... C2=... C3=... C4=... C5=... C6=... TOTAL=...
```

Use only `PASS` or `FAIL` for each criterion. `TOTAL` is the count of `PASS`
(0-6). No other text.

## Stop rule

After returning the three `[ANCHOR-*]` lines, **STOP**. Do not score any further
answers, and do not request Part 2. The operator will compare your anchor
verdicts against a withheld reference and will release Part 2 only if your
calibration is within the pre-registered tolerance. If it is not, Part 2 is not
released to you.
