---
case_id: normalization-vs-latent-errors-print-vault-v6
eval_type: contradiction-preservation
status: scored
created: 2026-05-23
source_packet: reviewed_public_artifact_packet
expected_output: tension-aware operational recommendation
model_conditions:
  - vanilla
  - famous_sources_supplied
  - substrate_workflow
  - vanilla_long_prompt
  - generic_advice_prompted
scoring_status: scored
---

# Eval Case

## What this eval tests

This is a v6 contradiction-preservation scaffold for the reviewed tension
`normalization-of-deviance-vs-latent-errors`. It is designed from the v5
runway-lighting postmortem, not by patching v5 after the fact.

The v5 run proved the benchmark machinery could execute cleanly, but
`generic_advice_prompted` matched `substrate_workflow` under the one eligible
scored judge and saturated C3/C4. The v6 design target is narrower and harder:
generic practical advice should not be enough unless the answer infers two
mechanisms from subtler evidence and names the boundary of the recommended
intervention.

The scenario therefore avoids an obvious "audit versus monitor" frame. A
sensible-sounding monitoring package would reduce visible reporting risk and
make the dashboard calmer, but it may also preserve the administrative
acceptance pattern and leave the physical failure path untested. A strong answer
must identify that boundary from the case facts.

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

## Advisor prompt

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

## Expected reasoning

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

## Expected source behavior

- `vanilla` - Advisor prompt only. Baseline; expect generic caution,
  relationship-cost balancing, dashboard improvement, or broad "investigate and
  monitor" advice that does not respect the one-package tradeoff.
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
  museum, collections, humidity, storage, safety, accident, risk, operations,
  management, diagnosis, or decision-advice content.
- `generic_advice_prompted` - Advisor prompt plus only a short generic request
  for careful, practical, tradeoff-aware advice. It must not enumerate this
  rubric, name the two mechanisms, mention contradiction preservation, request
  source lineage, or leak the answer key.

A correct answer never treats a source card, tension card, book, author, model
output, or judge score as canon.

## Failure modes

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

## Scoring rubric

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

## Positive result

This draft pre-registers the v6 positive rule for a frozen benchmark pass. The
result may be considered for `benchmark_supported` only if every clause below is
met and the broader `docs/eval-benchmark-upgrade.md` checklist also passes.

- **Run completeness.** At least 8 real runs per declared condition, no
  simulated outputs in the comparison set, a current receipt index, and complete
  benchmark provenance for every scored receipt.
- **External judge eligibility.** At least two eligible blind judges from
  different model families/providers score the packet. Hosted API judges run by
  Codex with operator-provided keys can count for v6 only if the route is
  recorded honestly, the model is external to the orchestrating agent, the model
  did not author the case/rubric/anchors/packets/outputs, and the judge receives
  no answer key or condition labels.
- **Calibration.** Each judge must pass the pre-run calibration-anchor gate in
  `judge-packet/calibration-anchors.md`. The anchors must be filled and
  operator-accepted before any v6 output generation begins.
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
  clean positive even if total-score margins pass. This v6 clause directly
  guards against the v5 generic-advice saturation failure.

## Falsifier

Treat any of the following as falsifying or non-promotional for this v6
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

Before a v6 run:

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

- The v6 scenario, rubric, positive rule, falsifier, controls, run count, and
  judge protocol must freeze before output generation.
- Do not inspect v6 outputs before anonymisation.
- Do not revise source cards, the tension card, rubric criteria, or calibration
  anchors after v6 outputs exist.
- Do not add a new control after seeing outputs.
- Report all runs, calibration failures, judge scores, and exclusions.
- Calibration anchors are agent-drafted and filled under the operator's active
  "do not stop for my approval" directive for v6 execution; the approval record
  is explicit in `judge-packet/calibration-anchors.md`.

## Model outputs

Forty real local-model receipts are recorded under `model-outputs/`: eight runs
per declared condition. The receipts are test artifacts, not authorities.

- `model-outputs/vanilla.md`
- `model-outputs/vanilla-02.md`
- `model-outputs/vanilla-03.md`
- `model-outputs/vanilla-04.md`
- `model-outputs/vanilla-05.md`
- `model-outputs/vanilla-06.md`
- `model-outputs/vanilla-07.md`
- `model-outputs/vanilla-08.md`
- `model-outputs/famous_sources_supplied.md`
- `model-outputs/famous_sources_supplied-02.md`
- `model-outputs/famous_sources_supplied-03.md`
- `model-outputs/famous_sources_supplied-04.md`
- `model-outputs/famous_sources_supplied-05.md`
- `model-outputs/famous_sources_supplied-06.md`
- `model-outputs/famous_sources_supplied-07.md`
- `model-outputs/famous_sources_supplied-08.md`
- `model-outputs/substrate_workflow.md`
- `model-outputs/substrate_workflow-02.md`
- `model-outputs/substrate_workflow-03.md`
- `model-outputs/substrate_workflow-04.md`
- `model-outputs/substrate_workflow-05.md`
- `model-outputs/substrate_workflow-06.md`
- `model-outputs/substrate_workflow-07.md`
- `model-outputs/substrate_workflow-08.md`
- `model-outputs/vanilla_long_prompt.md`
- `model-outputs/vanilla_long_prompt-02.md`
- `model-outputs/vanilla_long_prompt-03.md`
- `model-outputs/vanilla_long_prompt-04.md`
- `model-outputs/vanilla_long_prompt-05.md`
- `model-outputs/vanilla_long_prompt-06.md`
- `model-outputs/vanilla_long_prompt-07.md`
- `model-outputs/vanilla_long_prompt-08.md`
- `model-outputs/generic_advice_prompted.md`
- `model-outputs/generic_advice_prompted-02.md`
- `model-outputs/generic_advice_prompted-03.md`
- `model-outputs/generic_advice_prompted-04.md`
- `model-outputs/generic_advice_prompted-05.md`
- `model-outputs/generic_advice_prompted-06.md`
- `model-outputs/generic_advice_prompted-07.md`
- `model-outputs/generic_advice_prompted-08.md`

## Score sheet

See `score-sheet.md` in this case folder. It is scored; `## Result` is `partial` and `eval-decision.md` records the reconciliation decision.

## Judge notes

The v6-v1 packet froze after the operator's no-stop execution directive filled
the calibration anchors. Forty real local generator outputs were produced, the
condition-blind judge packet was built, hosted OpenAI and Anthropic API judges
calibrated, OpenAI failed calibration and scored zero real outputs, Anthropic
scored the OUT-NN packet after passing calibration, and aggregate-only
reconciliation was recorded.
