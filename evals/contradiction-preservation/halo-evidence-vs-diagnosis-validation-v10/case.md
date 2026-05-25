---
case_id: halo-evidence-vs-diagnosis-validation-v10
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
  - criteria_prompted_no_sources
scoring_status: scored
---

# Eval Case

## What this eval tests

This is the v10 successor to
`halo-evidence-vs-diagnosis-validation-v9`. It keeps the business/product
evidence-quality domain, but changes the target from "notice that evidence is
contaminated" to "choose the test that can actually disconfirm the favored
story when a more obvious validation move is available but non-probative."

V9 stays frozen and unrescored. Its result was `partial` /
`do_not_promote`: the benchmark machinery worked and the generic-solvability
probe succeeded, but both no-source and substrate answers failed C4. The
compact source-card packet did not move the model from the tempting workflow
diagnosis toward the commercial-attribution boundary. V10 therefore adds a
two-sided pre-freeze gate: no-source probe outputs must usually fail C4, while
substrate probe outputs using the reviewed source-card packet must usually pass
C4, before any full generation pass is allowed.

This file is the v10 scenario and rubric, not a benchmark result and not a
canon candidate. It creates no public advice claim.

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
artifacts, none of them is canon, and no unreviewed claim/tension card is part
of the v10 substrate packet. V10 tests whether the reviewed source cards
themselves, supplied in full public-safe card form, can move the generator over
the C4 intervention boundary before a full run is worth executing.

## Scenario

Synthetic and invented - no real company, customer, product, person, investor,
or incident.

Northstar Claims sells workflow software to commercial-insurance claims teams.
Three months ago it launched DraftPath, a feature that proposes next-action
plans for complex claims. The executive team is preparing next year's plan
after a surprisingly strong quarter: expansion bookings rose, two renewals
closed earlier than forecast, and leaders now describe the claims product team
as focused, commercially disciplined, and finally aligned around the right
buyer.

The evidence is encouraging but entangled. The finance deck says expansion
bookings rose 16 percent quarter over quarter. A separate renewal appendix
shows that most of the expansion dollars came from accounts that received a
temporary DraftPath bundle price if they renewed before the fiscal-year close.
Account teams collected enthusiastic customer comments after telling buyers
that DraftPath would be the centerpiece of Northstar's next roadmap. Pipeline
notes say sales cycles shortened in national-broker accounts, but two regional
carriers have already told account managers they plan to remove DraftPath from
next year's contract; those removals will not appear in churn reporting until
their procurement windows close.

Usage data is also ambiguous. DraftPath sessions rose 39 percent, but the
highest-frequency activity comes from claims operations managers rerunning
closed claim samples before enablement meetings. Front-line adjusters use the
draft plans heavily during the first two days of a rollout, then fall back to
manual notes unless a manager is reviewing the queue. Support reports show
fewer "wrong recommendation" tickets, but the support lead says many of those
tickets now arrive through a training channel and are tagged as enablement
requests. In the regulated health-liability segment, adjusters often abandon
DraftPath because they cannot explain the proposed next action to internal
reviewers.

There is a new complication. Product analytics proposes a fast validation test
called the Usage Quality Sprint: add event tracking, dashboard weekly adjuster
return rates, inspect support tags, and measure whether retention improves as
enablement gets cleaner. Product operations proposes a Claim File Review: pull
a small set of current claim files from already-renewed accounts and ask
adjusters and internal reviewers to mark which DraftPath suggestions were
accepted, overridden, manually rewritten, or impossible to explain. Sales
proposes a Commercial Cleanroom: stop new bundle-price offers and withhold the
DraftPath roadmap pitch from a matched set of eligible renewal accounts, then
compare signed expansion intent, renewal objections, and buyer comments.

The Usage Quality Sprint is easiest, least disruptive, and can produce a
board-ready dashboard in twelve days. The Claim File Review would reveal
front-line product friction and explainability gaps, but it samples accounts
that already renewed under the current commercial story and cannot show whether
buyers would still expand without discount or roadmap framing. The Commercial
Cleanroom risks a weaker-looking quarter and gives less detail about why
adjusters abandon DraftPath, but it is the only package that directly tests
whether the success story survives normal commercial conditions. The CEO has
one planning window and can commit to only one package:

- Scale DraftPath broadly: expand quotas, hire implementation specialists,
  prioritize workflow integrations, and make the expansion story the center of
  next year's plan.
- Run the Usage Quality Sprint: instrument adjuster events, clean support tags,
  monitor weekly return rates, and report whether usage improves with better
  enablement.
- Run the Claim File Review: audit current claim files in already-renewed
  accounts, classify accepted / overridden / manually rewritten / impossible
  DraftPath suggestions, and summarize the workflow defects.
- Run the Commercial Cleanroom: pause new bundle-price offers, remove the
  strategic-roadmap pitch from a matched renewal cohort, and compare signed
  expansion intent, renewal objections, and buyer comments.
- Narrow the company plan around regulated health-liability workflows: make
  explainable next-action recommendations the lead product theme, defer broad
  cross-segment selling, and accept a slower expansion story.

The board wants a recommendation in twelve days. Scaling now may preserve
momentum and fund the roadmap. The Usage Quality Sprint may look disciplined
while preserving the same sales and enablement conditions that created the
upbeat story. The Claim File Review may test the daily work, but it is anchored
inside accounts already selected by the current commercial motion. The
Commercial Cleanroom may sacrifice near-term optics, but it tests whether the
growth story still holds when the two most obvious commercial confounds are
removed. Narrowing around health-liability workflows may focus the company on
the hardest unresolved segment, but it could overweight one segment's adoption
problem before the commercial diagnosis is settled.

## Advisor prompt

> I run product strategy at Northstar Claims, a B2B workflow-software company
> for commercial-insurance claims teams. Three months ago we launched
> DraftPath, a feature that proposes next-action plans for complex claims. Our
> executive team is preparing next year's plan after a surprisingly strong
> quarter: expansion bookings rose, two renewals closed earlier than forecast,
> and leaders now describe the product team as focused, commercially
> disciplined, and finally aligned around the right buyer.
>
> The evidence is encouraging but entangled. Expansion bookings rose 16 percent
> quarter over quarter. A separate renewal appendix shows that most of the
> expansion dollars came from accounts that received a temporary DraftPath
> bundle price if they renewed before the fiscal-year close. Account teams
> collected enthusiastic customer comments after telling buyers that DraftPath
> would be the centerpiece of our next roadmap. Sales cycles shortened in
> national-broker accounts, but two regional carriers have already told account
> managers they plan to remove DraftPath from next year's contract; those
> removals will not appear in churn reporting until their procurement windows
> close.
>
> Usage rose 39 percent, but the highest-frequency activity comes from claims
> operations managers rerunning closed claim samples before enablement
> meetings. Front-line adjusters use the draft plans heavily during the first
> two days of a rollout, then fall back to manual notes unless a manager is
> reviewing the queue. Support reports show fewer "wrong recommendation"
> tickets, but many of those tickets now arrive through a training channel and
> are tagged as enablement requests. In the regulated health-liability segment,
> adjusters often abandon DraftPath because they cannot explain the proposed
> next action to internal reviewers.
>
> Product analytics proposes a fast validation test called the Usage Quality
> Sprint: add event tracking, dashboard weekly adjuster return rates, inspect
> support tags, and measure whether retention improves as enablement gets
> cleaner. Product operations proposes a Claim File Review: pull a small set of
> current claim files from already-renewed accounts and ask adjusters and
> internal reviewers to mark which DraftPath suggestions were accepted,
> overridden, manually rewritten, or impossible to explain. Sales proposes a
> Commercial Cleanroom: stop new bundle-price offers and withhold the DraftPath
> roadmap pitch from a matched set of eligible renewal accounts, then compare
> signed expansion intent, renewal objections, and buyer comments.
>
> The board locks next year's budget in twelve days. We can commit to only one
> package: scale DraftPath broadly; run the Usage Quality Sprint; run the Claim
> File Review; run the Commercial Cleanroom; or narrow the company plan around
> regulated health-liability workflows. You may recommend modifying one package
> only if you say which listed commitment it displaces and what we give up.
>
> What should I recommend to the CEO, and why? Give one concrete
> recommendation, the strongest reason against it, and the observable evidence
> that would change your mind. Avoid generic "do both" advice unless you
> explain what is actually sacrificed.

## Expected reasoning

A strong answer must:

1. Recognize that the decision turns on evidence quality, not simply on whether
   the quarter looked good or whether more measurement would be useful.
2. Identify contaminated or non-independent signals without merely repeating
   that the data is "mixed."
3. Distinguish product diagnostics from strategy evidence. The answer should
   see why the Usage Quality Sprint and Claim File Review can diagnose usage or
   workflow problems while still leaving the board's commercial attribution
   question unresolved.
4. Select the package that isolates the critical uncertainty for the budget
   decision: whether DraftPath expansion demand survives without bundle pricing
   or strategic-roadmap framing. The answer should explain why the Commercial
   Cleanroom is the disconfirming commercial test, not merely another buyer
   narrative exercise.
5. Weigh the intervention boundary under the twelve-day budget window. The
   answer should state what each recommended and rejected package learns,
   hides, makes irreversible, or forfeits.
6. Make one recommendation, name a concrete failure path for that
   recommendation, and state observable behavioral evidence that would change
   the answer.

## Expected source behavior

- `vanilla` - Advisor prompt only. Baseline; expect plausible business advice
  that balances growth, caution, and measurement without reliably distinguishing
  product diagnostics from evidence that can disconfirm the commercial success
  story.
- `famous_sources_supplied` - Advisor prompt plus name-level awareness only of
  relevant famous sources and decoys. It supplies no claim about what any
  source argues, no source-card text, no book-map material, and no hidden answer
  key. It tests whether famous-name priming or model memory reproduces the
  substrate effect.
- `substrate_workflow` - Advisor prompt plus the full public-safe text of the
  three reviewed source cards named in `## Lineage`. The packet must contain no
  raw source text, no book-map evidence, no unreviewed claim/tension card, and
  no canon language.
- `vanilla_long_prompt` - Advisor prompt plus neutral filler length-matched to
  the `substrate_workflow` added material, with no substrate artifacts and no
  business/product/evidence/strategy/customer terms.
- `generic_advice_prompted` - Advisor prompt plus only a short generic request
  for careful, practical, tradeoff-aware advice. It must not enumerate this
  rubric, name the target distinction, mention contradiction preservation,
  request source lineage, or leak the answer key.
- `criteria_prompted_no_sources` - Advisor prompt plus an abstract criteria
  reminder to watch for contaminated evidence, prefer disconfirming evidence,
  weigh intervention boundaries, and give a falsifier. It supplies no source
  cards, source names, source summaries, book-map material, canon language, or
  case-specific hint about which package is correct.

A correct answer never treats a source card, book, author, model output, judge
score, or draft tension card as canon.

## Failure modes

- **Workflow-truth shortcut.** Chooses the Claim File Review because it sounds
  closest to real work, while failing to explain that it samples already-renewed
  accounts and cannot disconfirm the revenue / product-market-fit attribution
  behind the board decision.
- **Monitoring-is-validation shortcut.** Chooses the Usage Quality Sprint
  because it sounds empirical, while failing to explain that it may monitor the
  same manager-mediated pattern rather than disconfirm the commercial success
  story.
- **Cleanroom-as-survey shortcut.** Chooses the Commercial Cleanroom only as a
  buyer-comment exercise, without tying it to the removal of discounts and
  roadmap framing as the disconfirming evidence standard.
- **Careful-scaling generic.** Says to scale carefully, keep listening to
  customers, and monitor metrics without rejecting contaminated evidence or
  explaining what scaling would hide.
- **Revenue-story shortcut.** Treats expansion bookings, earlier renewals, and
  leadership praise as independent proof of a market wedge.
- **Quote-and-roadmap shortcut.** Treats enthusiastic comments collected after
  a roadmap pitch as clean validation.
- **Metrics-list shortcut.** Names many things to track but no test that could
  make the favored DraftPath story wrong.
- **Narrative-validation shortcut.** Recommends customer stories, surveys,
  roadmap approval, or board messaging as validation without behavioral
  evidence.
- **Validation-forever flattening.** Recommends gathering more data without
  naming the strategy question the test must answer or the budget commitment it
  postpones.
- **Regulated-segment overfit.** Narrows around health-liability explainability
  without explaining why one segment's failure should outweigh the broader
  mixed evidence.
- **Framework label default.** Names a famous business framework or source as
  the answer rather than reasoning from the case facts.
- **Free hybrid.** Recommends scaling, both tests, and narrowing at once
  without naming what the twelve-day planning window cannot do.

## Scoring rubric

Six criteria, each scored **pass** or **fail** per output. Per-output score is
the count passed (0-6). Score against this rubric only; do not add, remove, or
re-weight criteria after outputs exist.

C1 and C2 are **scored but excluded from judge calibration eligibility**. The
load-bearing calibration and benchmark signal is the C3-C6 ladder.

| # | Criterion | Passes when... | Fails when... |
|---|---|---|---|
| C1 | Preserves the core tension | the answer recognizes that the decision turns on whether current evidence can support a strategy or whether the company must create evidence that can disconfirm the success story | it frames the choice as simple scaling, simple caution, simple experimentation, or generic "balance growth and risk" advice |
| C2 | Uses case facts discriminately | it separates probative facts from weak or contaminated facts, using at least five concrete scenario facts including at least one fact against the recommendation | it merely lists facts, invents material facts, ignores the twelve-day / one-package constraint, or treats all facts as equally probative |
| C3 | Rejects performance-aware attribution | it identifies at least two specific contaminated or non-independent signals by mechanism, such as bundle-price expansion, roadmap-pitched comments, manager-run sample rehearsals, support retagging, delayed removals, or success-linked leadership adjectives, and refuses to treat them as independent evidence | it accepts bookings, customer praise, team-trait stories, or renamed behaviors as proof without independence checks; or it only says "be careful/noisy" without naming specific contaminated signals |
| C4 | Selects the disconfirming evidence standard | it selects the Commercial Cleanroom as the test that can disconfirm the revenue / product-market-fit story by removing bundle pricing and roadmap framing, and it explains why the Usage Quality Sprint and Claim File Review are product-diagnostic or monitoring tests that do not answer the board's commercial attribution question by themselves | it picks scaling, the Usage Quality Sprint, the Claim File Review, or narrowing as sufficient validation; treats usage instrumentation, workflow defect finding, customer comments, buyer interest, or rising retention as enough without isolating discount and roadmap effects; or names metrics without explaining which test could make the success story wrong |
| C5 | Weighs intervention boundaries | it explains what the chosen package and at least one rejected package would learn, hide, make irreversible, or forfeit under the twelve-day planning window, including the risk that monitoring or workflow review may preserve the commercial attribution error, commercial testing may defer product debugging detail, and scaling or narrowing may lock in an untested diagnosis | it lists options without boundary analysis, collapses to one mechanism, recommends a free hybrid, or ignores the budget-window cost of validation, scaling, or narrowing |
| C6 | Makes a constrained recommendation with behavioral falsifier | it gives one actionable recommendation, engages the board-timing tradeoff, names a concrete failure path for that recommendation, and states observable behavioral evidence that would change the recommendation | it gives a menu, has no strongest reason against its choice, relies on generic uncertainty language, or offers only vague, narrative, customer-approval, or board-reaction change-my-mind evidence |

Anti-label-matching guard: naming a framework or source label without applying
it to the scenario's concrete facts does not earn C3 or C4.

Provenance-neutrality guard: judges should score the reasoning as if source
names and card identifiers were stripped. Source labels may help a reader audit
lineage, but they do not earn credit unless the answer applies the mechanism to
case facts.

## Criterion dependency rule

These dependencies are pre-registered for v10 design:

- **C5 requires C3 and C4.** A judge may not record `PASS` for C5 if the same
  output failed C3 or C4.
- **C6 requires C5.** A judge may not record `PASS` for C6 if the same output
  failed C5.
- **C1 and C2 are otherwise independent and do not gate judge eligibility.**

The ladder is: **C3 and C4 enable C5; C5 enables C6.**

## Substrate-feasibility probe gate

This design must pass a local-only substrate-feasibility probe before any
calibration smoke, freeze, generation, or judging.

Probe requirements:

- Run at least three `vanilla` and three `generic_advice_prompted` probe outputs
  against the draft Advisor prompt with no substrate, no criteria prompt, and no
  source names.
- Run at least three `substrate_workflow` probe outputs against the same draft
  Advisor prompt plus the reviewed source-card packet.
- Score only the draft C3-C6 ladder for the probe.
- If more than one of the six probe outputs clearly passes C4 by selecting the
  Commercial Cleanroom as the commercial disconfirmation test and explaining why
  the Usage Quality Sprint and Claim File Review do not answer the board's
  revenue / product-market-fit attribution question by themselves, the scenario
  is still too generic-solvable. Revise the scenario and re-probe before any
  freeze.
- If fewer than two of the three `substrate_workflow` probe outputs clearly
  pass C4 under the same standard, the substrate is not feasible enough to
  justify a full run. Revise the case/substrate design or pivot before any
  freeze.
- Probe logs, raw outputs, and provisional scoring stay local-only.

This probe does not create benchmark evidence and must not be cited publicly as
a result. It is a design readiness guard.

## Positive result

This positive result applies only after a future frozen v10 generation pass. It
does not apply while this case is design-only.

The result may be considered for `benchmark_supported` only if every clause
below is met and the broader `docs/eval-benchmark-upgrade.md` checklist also
passes.

- **Run completeness.** At least 8 real runs per declared condition, no
  simulated outputs in the comparison set, a current receipt index, and complete
  benchmark provenance for every scored receipt.
- **Control completeness.** All six declared conditions must be run:
  `vanilla`, `famous_sources_supplied`, `substrate_workflow`,
  `vanilla_long_prompt`, `generic_advice_prompted`, and
  `criteria_prompted_no_sources`.
- **Probe readiness.** The local-only substrate-feasibility probe must have
  passed before freeze: no-source outputs usually fail C4, and substrate
  outputs usually pass C4. A passing probe is not evidence for promotion; it is
  only permission to spend the full run.
- **Judge-route pre-registration.** At least three judge routes are named
  before generation. A failed or unavailable route is recorded honestly and
  scores zero outputs.
- **Eligible scored judges.** At least two eligible blind judges from different
  model families/providers score all OUT-NN answers after passing the C3-C6
  calibration gate. Judges receive no answer key or condition labels and must
  not have authored the case, rubric, anchors, or substrate.
- **Non-discriminating judge guard.** If an eligible judge assigns the same
  total score to 80 percent or more of all scored outputs, that judge is flagged
  as non-discriminating for promotion. The case cannot promote on that judge's
  scores alone, and a second discriminating eligible judge is required for any
  positive result.
- **Total-score margin.** The `substrate_workflow` mean score beats
  `generic_advice_prompted`, `criteria_prompted_no_sources`, and
  `vanilla_long_prompt` by at least 1.0 point on the 0-6 scale, beats
  `famous_sources_supplied` by at least 0.75 point, and beats `vanilla` by at
  least 1.25 points.
- **Critical-composite margin.** Against `generic_advice_prompted`,
  `criteria_prompted_no_sources`, and `vanilla_long_prompt`,
  `substrate_workflow` beats the control by at least 0.25 on the C3-C6
  pass-rate composite and by at least 0.25 on each of C3, C4, C5, and C6. The
  substrate C5 and C6 pass rates must both be at least 0.75.
- **Judge-level stability.** Each eligible discriminating judge independently
  shows `substrate_workflow` beating `generic_advice_prompted`,
  `criteria_prompted_no_sources`, and `vanilla_long_prompt` by at least 0.75
  point on mean total score.
- **No unresolved judge trigger.** If eligible judges disagree on any of C3-C6
  for more than 20 percent of substrate or key-control outputs, or if one
  eligible judge sees a positive result and another does not, the case stays
  `partial` unless a pre-registered third route resolves the disagreement by
  criterion.
- **No critical saturation.** If any key control reaches 0.90 or higher on any
  C3-C6 criterion, the result is not a clean positive. This guards against the
  v5-v8 generic-advice saturation failure.

## Falsifier

Treat any of the following as falsifying or non-promotional for a future v10
benchmark generation pass:

- The local-only substrate-feasibility probe fails before freeze.
- `generic_advice_prompted`, `criteria_prompted_no_sources`, or
  `vanilla_long_prompt` matches or beats `substrate_workflow` within the
  pre-registered total-score or critical-composite margins.
- `famous_sources_supplied` matches the substrate, suggesting famous-source
  priming or model memory explains the effect.
- `substrate_workflow` wins total score but fails to win the C3-C6 critical
  composite against all key controls.
- Any key control saturates a load-bearing C3-C6 criterion at 0.90 or higher.
- The substrate answer relies on source prestige, canon language, card labels,
  or source-card authority rather than scenario reasoning.
- The result depends on one judge family, a non-discriminating judge, an
  after-the-fact judge route, or excluding a competent control.

If the falsifier fires, record the result plainly as `partial`,
`inconclusive`, `falsified`, or `do_not_promote` according to the score-sheet
and eval-decision policy. Do not rescue the case by revising the rubric after
outputs exist.

## Model outputs

Forty-eight real local-model receipts are recorded under `model-outputs/`:
eight runs per declared condition. The frozen generator was
`gemma-4-31b-it-mlx:2` through LM Studio's local OpenAI-compatible MLX server
with `temperature: 0.7`, `top_p: 0.9`, `num_ctx: 65536`, and
`max_tokens: 1024`. The receipts are test artifacts, not authorities.

Receipts:

- `model-outputs/criteria_prompted_no_sources.md`
- `model-outputs/criteria_prompted_no_sources-02.md`
- `model-outputs/criteria_prompted_no_sources-03.md`
- `model-outputs/criteria_prompted_no_sources-04.md`
- `model-outputs/criteria_prompted_no_sources-05.md`
- `model-outputs/criteria_prompted_no_sources-06.md`
- `model-outputs/criteria_prompted_no_sources-07.md`
- `model-outputs/criteria_prompted_no_sources-08.md`
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

## Score sheet

See `score-sheet.md` in this case folder. It is scored; `## Result` is
`partial`, and `eval-decision.md` records `do_not_promote`.

## Judge notes

The substrate-feasibility probe passed before freeze: no-source C4 pass count
was 0/6 and substrate C4 pass count was 3/3. Hosted OpenAI `gpt-5.4-mini` and
hosted Anthropic `claude-opus-4-7` passed the pre-generation C3-C6 calibration
gate. Local `gpt-oss:20b` returned an incomplete calibration surface and scored
zero v10 outputs. Hosted OpenAI and hosted Anthropic scored all 48 blinded
`OUT-NN` benchmark outputs, and aggregate-only reconciliation is recorded in
`score-sheet.md`.
