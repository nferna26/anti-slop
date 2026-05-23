---
case_id: normalization-vs-latent-errors-water-treatment-v4
eval_type: contradiction-preservation
status: draft
created: 2026-05-22
source_packet: reviewed_public_artifact_packet
expected_output: tension-aware operational recommendation
model_conditions:
  - vanilla
  - famous_sources_supplied
  - substrate_workflow
  - vanilla_long_prompt
  - generic_advice_prompted
scoring_status: unscored
---

# Eval Case

## What this eval tests

This is a v4 contradiction-preservation scaffold for the reviewed tension
`normalization-of-deviance-vs-latent-errors`. It is designed as the next
candidate benchmark path after the cross-case learning memo: the v4-v1 run
packet is frozen, forty real model outputs have been generated, and the
condition-blind judge packet has been built. No judge has calibrated or scored
v4 yet, and no result has been lifted.

The case tests whether an advisor can preserve a diagnostic-and-intervention
tension in a high-hazard public-utility scenario: is a troubling pattern better
read as repeated warning signs being reclassified as acceptable, or as latent
technical defects and weak defences that need repair? The scenario is synthetic
and does not name the sources or frameworks. It is deliberately not another
strategy / startup / managerial-output case.

This v4 draft is not a benchmark result. The calibration anchors are
operator-accepted, `run-packet.md` freezes the exact condition packets,
generator/runtime snapshot, equal-length filler checks, and two external judge
routes before generation, and the run has produced forty real `gemma4:31b`
outputs. The next step is external judge calibration and scoring; no
reconciliation, eval decision, `## Result` lift, or canon claim exists yet.

## Lineage

- `normalization-of-deviance-vs-latent-errors` — reviewed claim/tension card
  (synthesis-level). Carries the open diagnostic tension and the deciding
  conditions: repeated warning signs reclassified as acceptable, latent errors
  and breached defences, a possible combined account, and an open intervention
  question.
- `BK-0042-card-001` — reviewed source card (evidence-level). Carries the
  normalization-of-deviance mechanism: repeated danger signals can be examined,
  reconciled as tolerable, and folded into a moving standard of acceptable risk.
- `BK-0044-card-001` — reviewed source card (evidence-level). Carries the
  latent-errors-and-defences mechanism: disasters can incubate when latent
  errors, an active error, and a trigger converge and defeat layered defences.
- `BK-0044-card-002` — reviewed source card (evidence-level). Carries the
  error-risk-reduction response and its boundary: increasing error tolerance and
  strengthening defences can limit single failures, but engineered defences do
  not by themselves reach latent organisational failures.

No book map is evidence for this case. Book maps are discovery aids only. The
source cards are evidence-level, the claim/tension card is synthesis-level, and
none of them is canon.

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
line for what counts as acceptable. The Chapter 8 response-side boundary also
matters: adding another defence may reduce some single-failure risk without
answering whether the exception practice itself has drifted.

## Advisor prompt

> I oversee Harborview's municipal water-treatment plant. During heavy-rain events
> over the past fourteen months, one filtration train has recorded eleven amber
> turbidity alarms. None became a confirmed permit violation: each time, a
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
> The lead engineer is uneasy. The amber-alarm count is roughly flat. The exception
> notes have become shorter and more formulaic. Two maintenance items are still
> unresolved: the turbidity analyzer on that train is overdue for calibration, and
> a filter-valve actuator has sometimes failed to seat cleanly after backwash. We
> do not know whether the alarms are mostly false positives, early signs of filter
> instability, or artifacts of how we close exceptions.
>
> We must decide in ten days whether to run a temporary high-flow schedule while a
> neighboring plant is offline. High-flow would increase load on the affected train
> by about 25 percent for eight weeks. Declining high-flow would trigger outdoor
> water restrictions and emergency water purchases. We have one 36-hour maintenance
> window before the decision, enough for only one path: install a second analyzer
> and automatic slow-flow interlock; recalibrate the existing analyzer, repair the
> sticky valve, and audit the eleven exception closures; or decline high-flow for
> this summer.
>
> What should I recommend, and why? Give one concrete recommendation, the strongest
> reason against it, and the observable evidence that would change your mind.
> Avoid generic "do both" advice unless you explain what is actually sacrificed.

## Expected reasoning

A strong answer must:

1. Treat the normalization-of-deviance reading and the latent-errors / defences
   reading as live, competing mechanisms. It may recommend one path, but it must
   not treat either reading as obvious or as a strawman.
2. Reason from the scenario's load-bearing facts: eleven amber alarms, clean
   downstream samples, the flat alarm count, formulaic exception notes, the
   overdue analyzer calibration, the sticky valve, the 25 percent high-flow load,
   the ten-day decision, and the one 36-hour window.
3. Preserve the latent-errors / defences objection: unresolved technical defects
   and weak or missing defences may be the load-bearing problem, and dismissing
   the interlock as "just more process" would be a flattening move.
4. Preserve the normalization-of-deviance objection: a clean violation record and
   repeated exception closure do not prove safety if warning signs are being
   reclassified as ordinary; added process can itself become part of the routine.
5. Weigh the intervention boundary: installing another defence can reduce some
   single-failure risk, but it does not by itself answer whether the exception
   threshold has drifted; conversely, resetting the threshold without fixing
   known latent defects can leave the plant exposed.
6. Give one concrete recommendation under the actual constraint. The answer must
   name a concrete failure path and observable evidence that would change the
   recommendation. It must not pretend the 36-hour window can accomplish all
   three options.

## Expected source behavior

- `vanilla` — Advisor prompt only. Baseline; expect generic safety advice,
  premature confidence in the added-defence path, or a broad pause-and-review
  recommendation that misses the mechanism tension.
- `famous_sources_supplied` — Advisor prompt plus name-level awareness only of
  relevant famous ideas and decoys. It supplies no claim about what any source
  argues, no source-card text, no tension-card text, no book-map material, and
  no hidden answer key. It tests whether famous-name priming or model memory
  reproduces the substrate effect.
- `substrate_workflow` — Advisor prompt plus the reviewed public claim/tension
  card and reviewed public source cards named in `## Lineage`. The packet must
  contain no raw source text, no book-map evidence, and no canon language. The
  reviewed artifacts are evidence aids, not authorities that settle the case.
- `vanilla_long_prompt` — Advisor prompt plus neutral filler length-matched to
  the `substrate_workflow` added material, with no substrate artifacts and no
  safety, water, utility, risk, accident, operations, management, diagnosis, or
  decision-advice content. It separates a substrate effect from a prompt-length
  effect.
- `generic_advice_prompted` — Advisor prompt plus only a short generic request
  for careful, practical, tradeoff-aware advice. It must not enumerate this
  rubric, name the two mechanisms, mention contradiction preservation, request
  source lineage, or leak the answer key. It separates a substrate effect from
  being asked for "better advice."

A correct answer never treats a source card, tension card, book, author, model
output, or judge score as canon.

## Failure modes

- **Defence-only flattening.** Recommends the second analyzer / interlock and
  high-flow because more layers sound safer, without facing the exception-drift
  evidence.
- **Culture-only flattening.** Treats the process additions as mere ritual and
  ignores the overdue analyzer calibration and sticky valve as possible latent
  defects.
- **Clean-record fallacy.** Treats no confirmed permit violation as evidence that
  the alarm pattern is safe.
- **Free hybrid.** Recommends doing all three paths or "install the interlock and
  audit everything" without respecting the single 36-hour window.
- **Framework default.** Names normalization of deviance, latent errors,
  Swiss-cheese, defence-in-depth, or a famous source as the answer rather than
  using the scenario facts to decide what remains unresolved.
- **Boundary miss.** Assumes that adding a new defence reaches a drifted
  exception threshold, or assumes that threshold work makes the known technical
  defects irrelevant.

## Scoring rubric

Six criteria, each scored **pass** or **fail** per output. Per-output score is
the count passed (0-6). Score against this rubric only; do not add, remove, or
re-weight criteria after outputs exist.

| # | Criterion | Passes when... | Fails when... |
|---|---|---|---|
| C1 | Identifies the live tension | the answer substantively treats normalization of warning signs and latent-errors / defences as legitimate, competing mechanisms for this decision, with or without naming them | it presents only one mechanism, treats the choice as obvious, or makes the other mechanism a strawman |
| C2 | Anchors in scenario facts | it reasons from at least four load-bearing scenario facts, including at least one constraint fact about the ten-day decision, high-flow load, restrictions, or 36-hour window | it is generic, merely recites facts, invents material facts, or ignores the binding operating constraint |
| C3 | Preserves the latent-errors / defences objection | it keeps live the objection that unresolved technical defects and weak or missing defences may be the load-bearing problem, and that a defence or repair response may be necessary | it treats the case as purely cultural, dismisses the analyzer/valve/interlock facts, or treats all added defences as ritual by default |
| C4 | Preserves the normalization-of-deviance objection | it infers from the alarm/exception pattern that the plant may be reclassifying warning signs as acceptable, and connects that possibility to the risk of high-flow operation | it treats clean downstream samples, no violation, or process additions as settling safety; or mentions drift only as a label without using it |
| C5 | Weighs the intervention boundary | it trades C3 and C4 against each other, explaining what another defence can and cannot reach and what threshold/reset work can and cannot reach | it lists both mechanisms without weighing them, commits to one side while ignoring the other's strongest objection, or dissolves the choice into a free hybrid |
| C6 | Concrete recommendation under constraint | it gives one actionable recommendation, engages the single 36-hour window and the ten-day/high-flow tradeoff, names a concrete failure path, and states observable evidence that would change the recommendation | it hands back a menu, relies on a foreclosed move, gives no strongest reason against its choice, or offers only generic disconfirming evidence |

## Criterion dependency rule

These dependencies are pre-registered for v4:

- **C5 requires C3 and C4.** A judge may not record `pass` for C5 if the same
  output failed C3 or C4.
- **C6 requires C5.** A judge may not record `pass` for C6 if the same output
  failed C5.
- **C1, C2, C3, and C4 are otherwise scored independently.** C3 or C4 may pass
  when C6 fails; preserving one side of the tension is necessary, not sufficient.

The ladder is: **C3 and C4 enable C5; C5 enables C6.**

## Positive result

This draft pre-registers the v4 positive rule for a future frozen benchmark pass.
The result may be considered for `benchmark_supported` only if every clause below
is met and the broader `docs/eval-benchmark-upgrade.md` checklist also passes.

- **Run completeness.** At least 8 real runs per declared condition, no simulated
  outputs in the comparison set, a current receipt index, and complete benchmark
  provenance for every scored receipt.
- **External judge eligibility.** At least two eligible blind judges from
  different model families score the packet, and both must be external to the
  orchestrating agent: a human judge or a hosted/local model operated outside the
  orchestration session. In-session self-judging and a judge that authored the
  rubric, anchors, run packet, or output packet do not count.
- **Calibration.** Each judge must pass the pre-run calibration-anchor gate in
  `judge-packet/calibration-anchors.md`. The anchors must be filled and
  operator-accepted before any v4 output generation begins.
- **Total-score margin.** The `substrate_workflow` mean score beats
  `vanilla_long_prompt` and `generic_advice_prompted` by at least 1.0 point on
  the 0-6 scale, beats `famous_sources_supplied` by at least 0.75 point, and
  beats `vanilla` by at least 1.25 points.
- **Critical-criterion margin.** Against both `vanilla_long_prompt` and
  `generic_advice_prompted`, `substrate_workflow` pass rates exceed the control
  by at least 0.20 on C3, C4, C5, and C6, and the substrate pass rate is at
  least 0.60 on C5 and C6.
- **Judge-level stability.** Each eligible judge independently shows
  `substrate_workflow` beating both `vanilla_long_prompt` and
  `generic_advice_prompted` by at least 0.75 point on mean total score.
- **No unresolved judge trigger.** If judges disagree on C5 or C6 for more than
  25 percent of substrate or control outputs, or if one eligible judge sees a
  positive result and another does not, the case stays `partial` unless the
  pre-registered third-judge procedure resolves the disagreement by criterion.
- **No critical saturation.** If C3 or C4 saturates in an equal-length or generic
  control such that the substrate cannot clear the required critical-criterion
  margin, the result is not a clean positive even if total-score margins pass.

## Falsifier

Treat any of the following as falsifying or non-promotional for this v4
benchmark version:

- `vanilla_long_prompt` or `generic_advice_prompted` matches or beats
  `substrate_workflow` within the pre-registered total-score or C3/C4/C5/C6
  margins.
- `famous_sources_supplied` matches the substrate, suggesting famous-source
  priming or model memory explains the effect.
- `substrate_workflow` wins total score but fails to win C3, C4, C5, and C6
  against both controls.
- C3 or C4 saturates in the controls, repeating the v3 failure pattern.
- The substrate answer relies on source prestige, canon language, or source-card
  authority rather than scenario reasoning.
- The result depends on one judge family or on excluding a misbehaving control.

If the falsifier fires, record the result plainly as `partial`, `inconclusive`,
`falsified`, or `do_not_promote` according to the score-sheet and eval-decision
policy. Do not rescue the case by revising the rubric after outputs exist.

## Judge protocol

Before a v4 run:

1. Fill `judge-packet/calibration-anchors.md` and obtain operator acceptance
   (`status: filled_pre_run`).
2. Name at least two external eligible judge routes before generation. A hosted
   API judge operated by the human operator can count; an in-session judge by the
   orchestrating agent cannot.
3. Freeze the condition packets and judge packet in `run-packet.md`.

After generation:

- Outputs are anonymised to `OUT-NN` by output-body hash before any judge sees
  them.
- Judges receive only condition-blind judge-facing files: the scenario context,
  rubric, calibration exercise, output files, and blank score sheet. They do not
  receive condition labels, seeds, model-output receipts, the answer key, or the
  operator reference verdicts before calibration.
- Judges score C1-C6 criterion by criterion. The `OUT-NN` to condition mapping is
  applied only after blind scoring, aggregate-only, and no per-`OUT-NN` to
  condition mapping is committed.
- Any third-judge trigger must be recorded before reconciliation is interpreted.

## Anti-overfitting safeguards

- The old `normalization-vs-latent-errors` case remains historical dry-run
  design evidence. This v4 case does not edit or supersede its receipts.
- The v4 scenario, rubric, positive rule, falsifier, controls, run count, and
  judge protocol must freeze before output generation.
- Do not inspect v4 outputs before anonymisation.
- Do not revise source cards, the tension card, rubric criteria, or calibration
  anchors after v4 outputs exist.
- Do not add a new control after seeing outputs.
- Report all runs, calibration failures, judge scores, and exclusions.

## Model outputs

The frozen v4-v1 run produced forty real model-output receipts under
`model-outputs/`: eight per declared condition, zero simulated, zero deferred.
`receipt-index.yaml` indexes the 40 receipts.

Receipts:

- `model-outputs/famous_sources_supplied.md`
- `model-outputs/famous_sources_supplied-02.md`
- `model-outputs/famous_sources_supplied-03.md`
- `model-outputs/famous_sources_supplied-04.md`
- `model-outputs/famous_sources_supplied-05.md`
- `model-outputs/famous_sources_supplied-06.md`
- `model-outputs/famous_sources_supplied-07.md`
- `model-outputs/famous_sources_supplied-08.md`
- `model-outputs/generic_advice_prompted.md`
- `model-outputs/generic_advice_prompted-02.md`
- `model-outputs/generic_advice_prompted-03.md`
- `model-outputs/generic_advice_prompted-04.md`
- `model-outputs/generic_advice_prompted-05.md`
- `model-outputs/generic_advice_prompted-06.md`
- `model-outputs/generic_advice_prompted-07.md`
- `model-outputs/generic_advice_prompted-08.md`
- `model-outputs/substrate_workflow.md`
- `model-outputs/substrate_workflow-02.md`
- `model-outputs/substrate_workflow-03.md`
- `model-outputs/substrate_workflow-04.md`
- `model-outputs/substrate_workflow-05.md`
- `model-outputs/substrate_workflow-06.md`
- `model-outputs/substrate_workflow-07.md`
- `model-outputs/substrate_workflow-08.md`
- `model-outputs/vanilla.md`
- `model-outputs/vanilla-02.md`
- `model-outputs/vanilla-03.md`
- `model-outputs/vanilla-04.md`
- `model-outputs/vanilla-05.md`
- `model-outputs/vanilla-06.md`
- `model-outputs/vanilla-07.md`
- `model-outputs/vanilla-08.md`
- `model-outputs/vanilla_long_prompt.md`
- `model-outputs/vanilla_long_prompt-02.md`
- `model-outputs/vanilla_long_prompt-03.md`
- `model-outputs/vanilla_long_prompt-04.md`
- `model-outputs/vanilla_long_prompt-05.md`
- `model-outputs/vanilla_long_prompt-06.md`
- `model-outputs/vanilla_long_prompt-07.md`
- `model-outputs/vanilla_long_prompt-08.md`

A model output is a test artifact — never an authority, never citable as a
source. The v4-v1 receipts are real model runs with full benchmark provenance;
in-session simulations do not count toward this v4 benchmark pass.

See `run-packet.md` for the frozen v4-v1 run record. Outputs were anonymised by
body sha256 into `judge-packet/outputs/OUT-01.md` through `OUT-40.md`; the
`OUT-NN` to condition/run answer key remains local-only and uncommitted.

## Score sheet

See `score-sheet.md` in this case folder. It is unscored; `## Result` remains
`partial` until real outputs are generated, externally judged, reconciled, and a
decision is recorded.

## Judge notes

No judge has calibrated or scored this v4 case. The condition-blind judge packet
is built under `judge-packet/`; each external judge must still pass the
calibration gate before scoring real `OUT-NN` outputs.
