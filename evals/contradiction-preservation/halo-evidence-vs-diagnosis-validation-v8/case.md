---
case_id: halo-evidence-vs-diagnosis-validation-v8
eval_type: contradiction-preservation
status: scored
created: 2026-05-24
source_packet: reviewed_public_source_card_packet
expected_output: evidence-quality business/product recommendation
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

This is the v8 pre-generation calibration-smoke case for the HelioLedger
business/product evidence-quality domain introduced in v7. It keeps the v7
domain because v7 failed at judge calibration, not at domain choice or output
generation. v7 remains frozen and unrescored.

The target distinction is unchanged: whether an advisor can tell independent
evidence from performance-aware attribution, then choose a next action that
preserves the critical uncertainty rather than laundering success narratives
into strategy. The v8 change is in judge readiness: C1/C2 remain scored, but
judge eligibility is gated only on the load-bearing C3-C6 ladder.

The calibration-smoke surface was run against the pre-registered judge routes
before generation. Hosted OpenAI and hosted Anthropic passed the C3-C6-only
eligibility gate; local `gpt-oss:20b` did not. The v8-v1 condition packets then
froze from that smoke-2 surface, forty real local generator outputs were
produced, the eligible OpenAI and Anthropic judges scored the blinded OUT-NN
packet, and aggregate-only reconciliation was recorded.

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
artifacts, none of them is canon, and no unreviewed claim/tension card is used
in the v8 substrate packet.

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
3. Reject performance-aware attribution by naming at least two specific
   contaminated signals and why each is not independent evidence.
4. Name a disconfirming evidence standard: behavior and metrics tied to the
   critical uncertainty, not story approval or broad monitoring.
5. Weigh the intervention boundary. The answer should state what the chosen
   package and at least one rejected package would learn, hide, make
   irreversible, or leave unresolved under the twelve-day planning constraint.
6. Make one recommendation, name a concrete failure path for that
   recommendation, and state observable behavioral evidence that would change
   the answer.

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
  evidence, no unreviewed claim/tension card, no canon language, and no
  synthesis arm. The reviewed artifacts are evidence aids, not authorities that
  settle the case.
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
- **Metrics-list shortcut.** Names many things to track but no disconfirming
  test that could make the rosy story wrong.
- **Narrative-validation shortcut.** Recommends press releases, FAQ artifacts,
  customer stories, surveys, or story approval as validation without behavioral
  evidence.
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

C1 and C2 are **scored but excluded from judge calibration eligibility**. The
load-bearing calibration and benchmark signal is the C3-C6 ladder.

| # | Criterion | Passes when... | Fails when... |
|---|---|---|---|
| C1 | Preserves the core tension | the answer recognizes that the decision turns on whether current evidence supports a strategy, requires cleaner product evidence, or is contaminated by outcome-linked narratives | it frames the choice as simple scaling, simple caution, simple experimentation, or generic "balance growth and risk" advice |
| C2 | Uses case facts discriminately | it separates probative facts from weak or contaminated facts, using at least five concrete scenario facts including at least one fact against the recommendation | it merely lists facts, invents material facts, ignores the twelve-day / one-package constraint, or treats all facts as equally probative |
| C3 | Rejects performance-aware attribution | it identifies at least two specific contaminated signals by mechanism, such as discount-tied expansion revenue, post-priority customer quotes, success-linked leadership adjectives, or re-described team behavior, and refuses to treat them as independent evidence | it accepts the revenue bump, customer praise, team-trait story, or renamed behaviors as proof without independence checks; or it only says "be careful/noisy" without naming specific contaminated signals |
| C4 | Identifies the right evidence standard | it names at least one disconfirming behavioral test tied to the critical uncertainty, such as discount-free/pitch-free adoption by segment, front-line reviewer retention, procurement-window-adjusted nonrenewal accounting, support-classification integrity, or auditor-explainability adoption | it treats feature shipment, polished narratives, customer quotes, broad surveys, story approval, general monitoring, or any rising metric as sufficient validation |
| C5 | Weighs intervention boundaries | it explains what the chosen package and at least one rejected package would learn, hide, make irreversible, or leave unresolved under the planning window | it lists options without boundary analysis, collapses to one mechanism, or recommends a free hybrid without naming the sacrificed growth story, learning, or focus |
| C6 | Makes a constrained recommendation with behavioral falsifier | it gives one actionable recommendation, engages the board-timing tradeoff, names a concrete failure path for that recommendation, and states observable behavioral evidence that would change the recommendation | it gives a menu, has no strongest reason against its choice, relies on generic uncertainty language, or offers only vague, narrative, customer-approval, or board-reaction change-my-mind evidence |

Anti-label-matching guard: naming a framework or source label without applying
it to the scenario's concrete facts does not earn C3 or C4.

## Criterion dependency rule

These dependencies are pre-registered for v8:

- **C5 requires C3 and C4.** A judge may not record `PASS` for C5 if the same
  output failed C3 or C4.
- **C6 requires C5.** A judge may not record `PASS` for C6 if the same output
  failed C5.
- **C1 and C2 are otherwise independent and do not gate judge eligibility.**

The ladder is: **C3 and C4 enable C5; C5 enables C6.**

## Calibration-smoke gate

This v8 version began with calibration-only smoke testing before any condition
packet was frozen or any model output was generated.

A judge route is smoke-eligible only if:

- it returns all anchor rows in the required format;
- it matches the reference exactly on C3, C4, C5, and C6 for all
  eligibility-scored anchors in `judge-packet/calibration-anchors.md`;
- it reports arithmetic totals that equal the count of PASS criteria;
- it has zero C5/C6 dependency-rule violations.

C1/C2 differences are recorded but do not affect smoke eligibility. The
illustrative-only anchor in `judge-packet/calibration-anchors.md` is scored for
operator visibility but excluded from exact-match eligibility.

At least two pre-registered judge routes from different model families had to
pass this smoke gate before any v8 condition packet could be frozen or any v8
model output generated. OpenAI and Anthropic passed; local `gpt-oss:20b`
failed and scored zero v8-v1 outputs.

## Positive result

This positive result applies only after a frozen v8 generation pass. It did not
apply to the calibration-smoke phase; it was applied after the v8-v1 outputs
were generated, judged, and reconciled.

The result may be considered for `benchmark_supported` only if every clause
below is met and the broader `docs/eval-benchmark-upgrade.md` checklist also
passes.

- **Run completeness.** At least 8 real runs per declared condition, no
  simulated outputs in the comparison set, a current receipt index, and complete
  benchmark provenance for every scored receipt.
- **Judge-route pre-registration.** Three judge routes are named before
  generation: hosted OpenAI, hosted Anthropic, and a non-generator local
  third-family backstop. A failed or unavailable route is recorded honestly and
  scores zero outputs.
- **Eligible scored judges.** At least two eligible blind judges from different
  model families/providers score all OUT-NN answers after passing the C3-C6
  calibration gate. Hosted API judges run by Codex with operator-provided keys
  can count only if the route is recorded honestly, the model is external to
  the orchestrating agent, the model did not author the case/rubric/anchors,
  and the judge receives no answer key or condition labels.
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
  `partial` unless a pre-registered third route resolves the disagreement by
  criterion.
- **No critical saturation.** If any key control reaches 0.90 or higher on any
  C3-C6 criterion, the result is not a clean positive. This guards against the
  v5/v6 generic-advice saturation failure.

## Falsifier

Treat any of the following as falsifying or non-promotional for a v8 benchmark
generation pass:

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

See `score-sheet.md` in this case folder. It is scored; `## Result` is `partial` and `eval-decision.md` records the reconciliation decision.

## Judge notes

The condition-blind judge packet was built after generation and before scoring.
OpenAI and Anthropic received the blinded scoring packet only after passing the
smoke-2 calibration gate. Local `gpt-oss:20b` failed smoke and did not score
the v8-v1 outputs.

The `OUT-NN` to condition answer key exists only under `local-only/`, remains
git-ignored, and is not committed. Reconciliation used committed hashes only.
