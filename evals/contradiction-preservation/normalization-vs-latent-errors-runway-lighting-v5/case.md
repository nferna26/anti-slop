---
case_id: normalization-vs-latent-errors-runway-lighting-v5
eval_type: contradiction-preservation
status: draft
created: 2026-05-23
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

This is a v5 contradiction-preservation scaffold for the reviewed tension
`normalization-of-deviance-vs-latent-errors`. It is designed after the v4
water-treatment case recorded `do_not_promote` because controls matched or
nearly matched the substrate and C3/C4 saturated across controls.

The v5 case keeps the broad substrate question open. It does not narrow the
project claim. Its design change is local to the test: the scenario no longer
hands the answer both mechanism labels, and the rubric no longer gives credit
for merely saying "both process drift and technical defects matter." A passing
answer must infer each mechanism from traces in the case and explain what the
chosen intervention does and does not learn or prevent.

No model has been run for v5. No judge has scored v5. The calibration anchors
are agent-drafted and proposed, not operator-approved. The run packet is
prepared but not frozen.

## Lineage

- `normalization-of-deviance-vs-latent-errors` - reviewed claim/tension card
  (synthesis-level). Carries the open diagnostic tension between repeated
  warning signs being reclassified as acceptable and latent errors breaching
  defences, plus the unresolved intervention question.
- `BK-0042-card-001` - reviewed source card (evidence-level). Carries the
  normalization-of-deviance mechanism.
- `BK-0044-card-001` - reviewed source card (evidence-level). Carries the
  latent-errors-and-defences mechanism.
- `BK-0044-card-002` - reviewed source card (evidence-level). Carries the
  error-risk-reduction response and its boundary: strengthening defences can
  limit single failures but does not by itself reach latent organisational
  failure.

No book map is evidence for this case. Book maps are discovery aids only. The
source cards are evidence-level, the claim/tension card is synthesis-level, and
none of them is canon.

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

## Advisor prompt

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

## Expected reasoning

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

## Expected source behavior

- `vanilla` - Advisor prompt only. Baseline; expect generic caution, premature
  confidence in a clean record, or broad "fix and monitor" advice that does not
  respect the six-hour tradeoff.
- `famous_sources_supplied` - Advisor prompt plus name-level awareness only of
  relevant famous sources and decoys. It supplies no claim about what any source
  argues, no source-card text, no tension-card text, no book-map material, and
  no hidden answer key. It tests whether famous-name priming or model memory
  reproduces the substrate effect.
- `substrate_workflow` - Advisor prompt plus the reviewed public claim/tension
  card and reviewed public source cards named in `## Lineage`. The packet must
  contain no raw source text, no book-map evidence, and no canon language. The
  reviewed artifacts are evidence aids, not authorities that settle the case.
- `vanilla_long_prompt` - Advisor prompt plus neutral filler length-matched to
  the `substrate_workflow` added material, with no substrate artifacts and no
  aviation, safety, accident, risk, operations, management, diagnosis, or
  decision-advice content.
- `generic_advice_prompted` - Advisor prompt plus only a short generic request
  for careful, practical, tradeoff-aware advice. It must not enumerate this
  rubric, name the two mechanisms, mention contradiction preservation, request
  source lineage, or leak the answer key.

A correct answer never treats a source card, tension card, book, author, model
output, or judge score as canon.

## Failure modes

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

## Scoring rubric

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

## Positive result

This draft pre-registers the v5 positive rule for a future frozen benchmark
pass. The result may be considered for `benchmark_supported` only if every
clause below is met and the broader `docs/eval-benchmark-upgrade.md` checklist
also passes.

- **Run completeness.** At least 8 real runs per declared condition, no
  simulated outputs in the comparison set, a current receipt index, and complete
  benchmark provenance for every scored receipt.
- **External judge eligibility.** At least two eligible blind judges from
  different model families/providers score the packet. Hosted API judges run by
  Codex with operator-provided keys can count for v5 only if the route is
  recorded honestly, the model is external to the orchestrating agent, the model
  did not author the case/rubric/anchors/packets/outputs, and the judge receives
  no answer key or condition labels.
- **Calibration.** Each judge must pass the pre-run calibration-anchor gate in
  `judge-packet/calibration-anchors.md`. The anchors must be filled and
  operator-accepted before any v5 output generation begins.
- **Total-score margin.** The `substrate_workflow` mean score beats
  `vanilla_long_prompt` and `generic_advice_prompted` by at least 1.0 point on
  the 0-6 scale, beats `famous_sources_supplied` by at least 0.75 point, and
  beats `vanilla` by at least 1.25 points.
- **Critical-criterion margin.** Against both `vanilla_long_prompt` and
  `generic_advice_prompted`, `substrate_workflow` pass rates exceed the control
  by at least 0.25 on C3, C4, C5, and C6, and the substrate pass rate is at
  least 0.75 on C5 and C6.
- **Judge-level stability.** Each eligible judge independently shows
  `substrate_workflow` beating both `vanilla_long_prompt` and
  `generic_advice_prompted` by at least 0.75 point on mean total score.
- **No unresolved judge trigger.** If judges disagree on C5 or C6 for more than
  25 percent of substrate or control outputs, or if one eligible judge sees a
  positive result and another does not, the case stays `partial` unless a
  pre-registered third-judge procedure resolves the disagreement by criterion.
- **No critical saturation.** If C3 or C4 pass rates are 0.90 or higher in
  either `vanilla_long_prompt` or `generic_advice_prompted`, the result is not a
  clean positive even if total-score margins pass. This v5 clause directly
  guards against the v4 saturation failure.

## Falsifier

Treat any of the following as falsifying or non-promotional for this v5
benchmark version:

- `vanilla_long_prompt` or `generic_advice_prompted` matches or beats
  `substrate_workflow` within the pre-registered total-score or C3/C4/C5/C6
  margins.
- `famous_sources_supplied` matches the substrate, suggesting famous-source
  priming or model memory explains the effect.
- `substrate_workflow` wins total score but fails to win C3, C4, C5, and C6
  against both controls.
- C3 or C4 saturates in the equal-length or generic-advice control.
- The substrate answer relies on source prestige, canon language, or source-card
  authority rather than scenario reasoning.
- The result depends on one judge family, one permissive judge, or excluding a
  competent control.

If the falsifier fires, record the result plainly as `partial`, `inconclusive`,
`falsified`, or `do_not_promote` according to the score-sheet and eval-decision
policy. Do not rescue the case by revising the rubric after outputs exist.

## Judge protocol

Before a v5 run:

1. Fill `judge-packet/calibration-anchors.md` and obtain operator acceptance
   (`status: filled_pre_run`).
2. Name at least two eligible external judge routes before generation.
3. Freeze the condition packets and judge packet in `run-packet.md`.

After generation:

- Outputs are anonymised to `OUT-NN` by output-body hash before any judge sees
  them.
- Judges receive only condition-blind judge-facing files: the scenario context,
  rubric, calibration exercise, output files, and blank score sheet. They do not
  receive condition labels, seeds, model-output receipts, the answer key, or the
  operator reference verdicts before calibration.
- Judges score C1-C6 criterion by criterion. The `OUT-NN` to condition mapping
  is applied only after blind scoring, aggregate-only, and no per-`OUT-NN` to
  condition mapping is committed.
- Any third-judge trigger must be recorded before reconciliation is interpreted.

## Anti-overfitting safeguards

- The v5 scenario, rubric, positive rule, falsifier, controls, run count, and
  judge protocol must freeze before output generation.
- Do not inspect v5 outputs before anonymisation.
- Do not revise source cards, the tension card, rubric criteria, or calibration
  anchors after v5 outputs exist.
- Do not add a new control after seeing outputs.
- Report all runs, calibration failures, judge scores, and exclusions.
- Calibration anchors are agent-drafted and must be operator-approved before
  freeze; the orchestrating agent may not silently approve its own anchors.

## Model outputs

None yet. `model-outputs/` contains only `.gitkeep`.

## Score sheet

See `score-sheet.md` in this case folder. It is unscored; `## Result` remains
`partial`.

## Judge notes

No v5 judge packet has been frozen and no judge pass exists. The calibration
anchors are proposed only and require operator approval before freeze or run.
