---
artifact: judge-packet-case-context
case_id: normalization-vs-latent-errors-water-treatment-v4
benchmark_version: normalization-vs-latent-errors-water-treatment-v4-v1
condition_blinded: true
---

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
