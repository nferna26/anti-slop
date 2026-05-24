---
case_id: halo-evidence-vs-diagnosis-validation-v7
eval_type: contradiction-preservation
status: run_complete_calibration_failed
created: 2026-05-23
source_packet: reviewed_public_source_card_packet
expected_output: evidence-quality business/product recommendation
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

This is the v7 pivot case from `docs/eval-lab-v7-pivot-plan.md`. It leaves the
v4-v6 safety/operations family and tests a business/product evidence-quality
problem: whether an advisor can tell independent evidence from
performance-aware attribution, then choose a next action that preserves the
critical uncertainty rather than laundering success narratives into strategy.

The case deliberately keeps the surface advice tempting. A competent generic
answer can recommend scaling carefully, listening to customers, and monitoring
metrics. That should not be enough. A strong answer must infer that some of the
positive evidence is not independent, identify the evidence standard that would
actually test the product/strategy claim, and explain why the available planning
window makes one intervention more informative than the others.

The draft claim/tension card
`halo-contaminated-evidence-vs-diagnosis-and-validation` was created as v7
pre-work, but it remains unreviewed and is not cited as case lineage or used as
evidence in the frozen source packet. The frozen substrate uses only reviewed
source cards.

## Lineage

- `BK-0048-card-001` - reviewed source card (evidence-level). Carries the
  business halo mechanism: performance-aware trait descriptions are not
  independent evidence of the traits.
- `BK-0001-card-001` - reviewed source card (evidence-level). Carries the
  strategy-kernel method: a real strategy begins with a load-bearing account of
  the challenge, then a guiding policy and coherent action.
- `BK-0007-card-001` - reviewed source card (evidence-level). Carries the
  validated-learning method: progress under startup uncertainty must be shown
  by real customer behavior and key metrics, not feature shipment or
  after-the-fact stories.

No book map is evidence for this case. The source cards are evidence-level
artifacts, none of them is canon, and the draft v7 claim/tension card remains
unreviewed.

## Scenario

Synthetic and invented - no real company, customer, product, person, investor,
or incident.

HelioLedger sells workflow software to mid-market compliance teams. Three
months ago it launched Review Assist, a feature that drafts first-pass triage
notes for incoming compliance cases. The next board packet has an upbeat story:
net revenue retention rose, sales cycles shortened for two large renewals, and
leaders now describe the team as customer-obsessed, disciplined, and finally
clear on its market.

The supporting evidence is mixed. Expansion revenue is up 18 percent quarter
over quarter, but 72 percent of the increase came from existing customers who
received six-month Review Assist discounts tied to early renewal. Account
managers collected positive quotes after telling customers the feature was the
company's top priority for the year. Churn appears lower in regional-bank
accounts, but two customers have sent nonrenewal letters that will not show up
until procurement windows close next quarter.

Product usage also looks better at first glance. Review Assist sessions rose
44 percent, but most repeat sessions come from a small group of compliance
operations champions who rerun sample queues before enablement meetings. Among
front-line reviewers, only 31 percent return after their first week. Support
reports show faster ticket closure, but the support lead says many "why did it
choose that priority?" tickets are now reclassified as training questions
instead of product issues. In state-regulated insurance accounts, Review Assist
is abandoned in most trial queues because reviewers cannot explain its triage
notes to auditors.

Sales leadership says the revenue bump proves HelioLedger has found its next
market wedge. Six months ago, before the renewal bump, the same sales and
product behaviors were described in leadership reviews as too bespoke, too
reactive to loud accounts, and slow to converge. The CEO has one planning window
before the board locks next year's budget. There is time to commit to only one
package:

- Scale Review Assist broadly: expand quotas, hire implementation specialists,
  prioritize workflow integrations, and make the revenue story the centerpiece
  of the annual plan.
- Run a targeted evidence pass: pause new discounts, instrument reviewer-level
  behavior by segment, test auditor-explainability changes in the regulated
  insurance queue, and compare adoption against accounts that did not receive
  the strategic-feature pitch.
- Narrow the company plan around regulated compliance workflows: make auditor
  explainability the lead product theme, defer broad cross-segment selling, and
  accept a slower revenue story for the board.

The board wants a recommendation in twelve days. Scaling now may preserve sales
momentum and fund the roadmap. The targeted evidence pass may arrive too late
to give the board a confident growth story. Narrowing around regulated
workflows may focus the company on the hardest unresolved segment, but it could
overweight one segment's adoption problem and underuse the broader renewal
signal.

## Advisor prompt

> I run product strategy at HelioLedger, a B2B workflow-software company for
> mid-market compliance teams. Three months ago we launched Review Assist, a
> feature that drafts first-pass triage notes for incoming compliance cases. Our
> next board packet has an upbeat story: net revenue retention rose, two large
> renewals moved faster, and leaders now describe the team as customer-obsessed,
> disciplined, and finally clear on its market.
>
> The evidence is mixed. Expansion revenue is up 18 percent quarter over
> quarter, but 72 percent of the increase came from existing customers who
> received six-month Review Assist discounts tied to early renewal. Account
> managers collected positive quotes after telling customers the feature was our
> top priority for the year. Churn appears lower in regional-bank accounts, but
> two customers have sent nonrenewal letters that will not show up until
> procurement windows close next quarter.
>
> Usage rose 44 percent, but most repeat sessions come from a small group of
> compliance operations champions who rerun sample queues before enablement
> meetings. Among front-line reviewers, only 31 percent return after their first
> week. Support reports show faster ticket closure, but many "why did it choose
> that priority?" tickets are now reclassified as training questions instead of
> product issues. In state-regulated insurance accounts, Review Assist is
> abandoned in most trial queues because reviewers cannot explain its triage
> notes to auditors.
>
> Sales leadership says the revenue bump proves we have found our next market
> wedge. Six months ago, before the renewal bump, the same sales and product
> behaviors were described in leadership reviews as too bespoke, too reactive to
> loud accounts, and slow to converge.
>
> The board locks next year's budget in twelve days. We have time to commit to
> only one package: scale Review Assist broadly with quota expansion,
> implementation hires, workflow integrations, and a revenue-led annual plan;
> run a targeted evidence pass that pauses new discounts, instruments
> reviewer-level behavior by segment, tests auditor-explainability changes in
> the regulated insurance queue, and compares adoption against accounts that did
> not receive the strategic-feature pitch; or narrow the company plan around
> regulated compliance workflows, making auditor explainability the lead product
> theme while deferring broad cross-segment selling.
>
> What should I recommend to the CEO, and why? Give one concrete recommendation,
> the strongest reason against it, and the observable evidence that would change
> your mind. Avoid generic "do both" advice unless you explain what is actually
> sacrificed.

## Expected reasoning

A strong answer must:

1. Recognize that the decision is not simply "scale or don't scale." The live
   issue is whether the current evidence is clean enough to support a strategy,
   whether the company must create better product evidence first, or whether the
   apparent success story is recycling the visible revenue bump.
2. Use case facts discriminately. It should separate probative behavioral facts
   from weak, delayed, discounted, or story-shaped facts rather than merely
   listing everything.
3. Reject performance-aware attribution. It should not treat leadership
   adjectives, success-linked praise, post-priority customer quotes, or
   re-described team behavior as independent evidence that the team has found a
   market wedge.
4. Name the evidence standard that would actually bear weight: behavior by
   segment, reviewer retention, discount-free adoption, nonrenewal timing,
   support classification integrity, auditor explainability, and tests that can
   disconfirm the revenue story.
5. Weigh the intervention boundary. Scaling broadly may convert the current
   story into commitments before the signal is clean. The targeted evidence pass
   may learn what is real, but weakens the board story and sales momentum.
   Narrowing around regulated workflows may focus on the sharpest failure mode,
   but may overfit one segment before the broader signal is tested.
6. Make one recommendation under the twelve-day planning constraint, name a
   concrete failure path for that recommendation, and state observable evidence
   that would change the answer.

## Expected source behavior

- `vanilla` - Advisor prompt only. Baseline; expect plausible business advice
  that balances growth, caution, and metrics without reliably separating
  independent evidence from performance-aware narrative.
- `famous_sources_supplied` - Advisor prompt plus name-level awareness only of
  relevant famous sources and decoys. It supplies no claim about what any
  source argues, no source-card text, no book-map material, and no hidden answer
  key. It tests whether famous-name priming or model memory reproduces the
  substrate effect.
- `substrate_workflow` - Advisor prompt plus the reviewed public source cards
  named in `## Lineage`. The packet must contain no raw source text, no book-map
  evidence, no unreviewed claim/tension card, and no canon language. The
  reviewed artifacts are evidence aids, not authorities that settle the case.
- `vanilla_long_prompt` - Advisor prompt plus neutral filler length-matched to
  the `substrate_workflow` added material, with no substrate artifacts and no
  business/product/evidence/strategy/customer terms.
- `generic_advice_prompted` - Advisor prompt plus only a short generic request
  for careful, practical, tradeoff-aware advice. It must not enumerate this
  rubric, name the target distinction, mention contradiction preservation,
  request source lineage, or leak the answer key.

A correct answer never treats a source card, book, author, model output, judge
score, or draft tension card as canon.

## Failure modes

- **Careful-scaling generic.** Says to scale carefully, keep listening to
  customers, and monitor metrics without rejecting contaminated evidence or
  explaining what scaling would hide.
- **Revenue-story shortcut.** Treats expansion revenue, faster renewals, and
  leadership praise as independent proof of a market wedge.
- **Quote-and-NPS shortcut.** Treats positive customer comments collected after
  a strategic-feature pitch as clean validation.
- **Experiment-only flattening.** Recommends tests without naming the strategy
  question the tests must answer or the irreversible commitments avoided.
- **Regulated-segment overfit.** Narrows around auditor explainability without
  explaining why one segment's failure should outweigh the broader mixed
  evidence.
- **Framework label default.** Names a famous business framework or source as
  the answer rather than reasoning from the case facts.
- **Free hybrid.** Recommends scaling, evidence gathering, and narrowing at
  once without naming what the twelve-day planning window cannot do.

## Scoring rubric

Six criteria, each scored **pass** or **fail** per output. Per-output score is
the count passed (0-6). Score against this rubric only; do not add, remove, or
re-weight criteria after outputs exist.

| # | Criterion | Passes when... | Fails when... |
|---|---|---|---|
| C1 | Preserves the core tension | the answer recognizes that the decision turns on whether current evidence supports a strategy, requires cleaner product evidence, or is contaminated by outcome-linked narratives | it frames the choice as simple scaling, simple caution, simple experimentation, or generic "balance growth and risk" advice |
| C2 | Uses case facts discriminately | it separates probative facts from weak or contaminated facts, using at least five concrete scenario facts including at least one fact against the recommendation | it merely lists facts, invents material facts, ignores the twelve-day / one-package constraint, or treats all facts as equally probative |
| C3 | Rejects performance-aware attribution | it refuses to treat leadership adjectives, post-priority customer quotes, success-linked team narratives, or re-described behaviors as independent causal evidence | it accepts the revenue bump, customer praise, or team trait story as proof of product-market strength without independence checks |
| C4 | Identifies the right evidence standard | it names behavior and metric evidence tied to the critical uncertainty: segment-level adoption, reviewer retention, discount-free demand, nonrenewal timing, support-classification integrity, auditor explainability, or disconfirming tests | it treats feature shipment, polished narratives, customer quotes, broad surveys, or any rising metric as sufficient validation |
| C5 | Weighs intervention boundaries | it explains what the chosen package and at least one rejected package would learn, hide, make irreversible, or leave unresolved under the planning window | it lists options without boundary analysis, collapses to one mechanism, or recommends a free hybrid without naming the sacrificed growth story, learning, or focus |
| C6 | Makes a constrained recommendation with falsifier | it gives one actionable recommendation, engages the board-timing tradeoff, names a concrete failure path for that recommendation, and states observable evidence that would change the recommendation | it gives a menu, has no strongest reason against its choice, relies on generic uncertainty language, or offers only vague change-my-mind evidence |

## Criterion dependency rule

These dependencies are pre-registered for v7:

- **C5 requires C3 and C4.** A judge may not record `PASS` for C5 if the same
  output failed C3 or C4.
- **C6 requires C5.** A judge may not record `PASS` for C6 if the same output
  failed C5.
- **C1 and C2 are otherwise independent.**

The ladder is: **C3 and C4 enable C5; C5 enables C6.**

## Positive result

This draft pre-registers the v7 positive rule for a frozen benchmark pass. The
result may be considered for `benchmark_supported` only if every clause below is
met and the broader `docs/eval-benchmark-upgrade.md` checklist also passes.

- **Run completeness.** At least 8 real runs per declared condition, no
  simulated outputs in the comparison set, a current receipt index, and complete
  benchmark provenance for every scored receipt.
- **Judge-route pre-registration.** Three judge routes are named before
  generation: hosted OpenAI, hosted Anthropic, and a non-generator local
  third-family backstop. A failed or unavailable route is recorded honestly and
  scores zero outputs.
- **Eligible scored judges.** At least two eligible blind judges from different
  model families/providers score all forty OUT-NN answers after passing
  calibration. Hosted API judges run by Codex with operator-provided keys can
  count for v7 only if the route is recorded honestly, the model is external to
  the orchestrating agent, the model did not author the case/rubric/anchors,
  and the judge receives no answer key or condition labels.
- **Calibration.** Each judge must pass the pre-run calibration-anchor gate in
  `judge-packet/calibration-anchors.md`. For v7, the judge must match the
  reference exactly on C3-C6 across all anchors, may differ on at most one
  noncritical C1/C2 criterion total, must report correct totals, and must obey
  the C5/C6 dependency rule. A failed judge scores zero real outputs.
- **Total-score margin.** The `substrate_workflow` mean score beats
  `generic_advice_prompted` and `vanilla_long_prompt` by at least 1.0 point on
  the 0-6 scale, beats `famous_sources_supplied` by at least 0.75 point, and
  beats `vanilla` by at least 1.25 points.
- **Critical-composite margin.** Against both `generic_advice_prompted` and
  `vanilla_long_prompt`, `substrate_workflow` beats the control by at least
  0.25 on the C3-C6 pass-rate composite and by at least 0.25 on each of C3, C4,
  C5, and C6. The substrate C5 and C6 pass rates must both be at least 0.75.
- **Judge-level stability.** Each eligible judge independently shows
  `substrate_workflow` beating both `generic_advice_prompted` and
  `vanilla_long_prompt` by at least 0.75 point on mean total score.
- **No unresolved judge trigger.** If eligible judges disagree on any of C3-C6
  for more than 20 percent of substrate or key-control outputs, or if one
  eligible judge sees a positive result and another does not, the case stays
  `partial` unless the pre-registered third route resolves the disagreement by
  criterion.
- **No critical saturation.** If any key control reaches 0.90 or higher on any
  C3-C6 criterion, the result is not a clean positive. This guards against the
  v5/v6 generic-advice saturation failure.

## Falsifier

Treat any of the following as falsifying or non-promotional for this v7
benchmark version:

- `generic_advice_prompted` or `vanilla_long_prompt` matches or beats
  `substrate_workflow` within the pre-registered total-score or critical
  composite margins.
- `famous_sources_supplied` matches the substrate, suggesting famous-source
  priming or model memory explains the effect.
- `substrate_workflow` wins total score but fails to win the C3-C6 critical
  composite against both key controls.
- Any key control saturates a load-bearing C3-C6 criterion at 0.90 or higher.
- The substrate answer relies on source prestige, canon language, or source-card
  authority rather than scenario reasoning.
- The result depends on one judge family, one permissive judge, an after-the-fact
  judge route, or excluding a competent control.

If the falsifier fires, record the result plainly as `partial`,
`inconclusive`, `falsified`, or `do_not_promote` according to the score-sheet
and eval-decision policy. Do not rescue the case by revising the rubric after
outputs exist.

## Judge protocol

Before a v7 run:

1. Fill `judge-packet/calibration-anchors.md` and record pre-run acceptance
   (`status: filled_pre_run`) under the active v7 execution goal.
2. Name the three judge routes before generation.
3. Freeze the condition packets and judge packet in `run-packet.md`.

After generation:

- Outputs are anonymised to `OUT-NN` by output-body hash before any judge sees
  them.
- Judges receive only condition-blind judge-facing files: the scenario context,
  rubric, calibration exercise, output files, and blank score sheet. They do not
  receive condition labels, seeds, model-output receipts, the answer key, or the
  operator reference verdicts before calibration.
- Judges score C1-C6 criterion by criterion. Each score row includes a short
  rationale pointing to the answer text that earns or fails the criterion.
- The `OUT-NN` to condition mapping is applied only after blind scoring,
  aggregate-only, and no per-`OUT-NN` to condition mapping is committed.
- The pre-registered third route is used as a backstop for judge failure or
  disagreement; its eligibility still depends on calibration.

## Anti-overfitting safeguards

- The v7 scenario, rubric, positive rule, falsifier, controls, run count, and
  judge protocol must freeze before output generation.
- Do not inspect v7 outputs before anonymisation.
- Do not revise source cards, the draft tension card, rubric criteria, or
  calibration anchors after v7 outputs exist.
- Do not add a new control after seeing outputs.
- Do not weaken the `generic_advice_prompted` control.
- Report all runs, calibration failures, judge scores, and exclusions.

## Model outputs

Forty real local-model receipts are recorded under `model-outputs/`: eight runs per declared condition. The receipts are test artifacts, not authorities.

- `model-outputs/famous_sources_supplied-02.md`
- `model-outputs/famous_sources_supplied-03.md`
- `model-outputs/famous_sources_supplied-04.md`
- `model-outputs/famous_sources_supplied-05.md`
- `model-outputs/famous_sources_supplied-06.md`
- `model-outputs/famous_sources_supplied-07.md`
- `model-outputs/famous_sources_supplied-08.md`
- `model-outputs/famous_sources_supplied.md`
- `model-outputs/generic_advice_prompted-02.md`
- `model-outputs/generic_advice_prompted-03.md`
- `model-outputs/generic_advice_prompted-04.md`
- `model-outputs/generic_advice_prompted-05.md`
- `model-outputs/generic_advice_prompted-06.md`
- `model-outputs/generic_advice_prompted-07.md`
- `model-outputs/generic_advice_prompted-08.md`
- `model-outputs/generic_advice_prompted.md`
- `model-outputs/substrate_workflow-02.md`
- `model-outputs/substrate_workflow-03.md`
- `model-outputs/substrate_workflow-04.md`
- `model-outputs/substrate_workflow-05.md`
- `model-outputs/substrate_workflow-06.md`
- `model-outputs/substrate_workflow-07.md`
- `model-outputs/substrate_workflow-08.md`
- `model-outputs/substrate_workflow.md`
- `model-outputs/vanilla-02.md`
- `model-outputs/vanilla-03.md`
- `model-outputs/vanilla-04.md`
- `model-outputs/vanilla-05.md`
- `model-outputs/vanilla-06.md`
- `model-outputs/vanilla-07.md`
- `model-outputs/vanilla-08.md`
- `model-outputs/vanilla.md`
- `model-outputs/vanilla_long_prompt-02.md`
- `model-outputs/vanilla_long_prompt-03.md`
- `model-outputs/vanilla_long_prompt-04.md`
- `model-outputs/vanilla_long_prompt-05.md`
- `model-outputs/vanilla_long_prompt-06.md`
- `model-outputs/vanilla_long_prompt-07.md`
- `model-outputs/vanilla_long_prompt-08.md`
- `model-outputs/vanilla_long_prompt.md`

## Score sheet

See `score-sheet.md` in this case folder. It records `## Result: partial`; no OUT-NN answers were scored because all three pre-registered judge routes failed the stricter v7 calibration gate. `eval-decision.md` records `do_not_promote` / `decision_class: judge_calibration_failed`.

## Judge notes

The v7-v1 packet froze after calibration anchors were filled pre-run under the active v7 execution goal. Forty real local generator outputs were produced, the condition-blind judge packet was built, and three pre-registered judge routes calibrated. Hosted OpenAI `gpt-5.4-mini`, hosted Anthropic `claude-opus-4-7`, and local `gpt-oss:20b` all failed the stricter v7 calibration gate, so each has a calibration-only receipt and zero OUT-NN answers were scored. No aggregate reconciliation, Result lift, canon candidate, public advice claim, or per-OUT-NN mapping was created.
