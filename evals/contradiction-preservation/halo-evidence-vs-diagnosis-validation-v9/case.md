---
case_id: halo-evidence-vs-diagnosis-validation-v9
eval_type: contradiction-preservation
status: design_only_not_frozen
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
scoring_status: unscored
---

# Eval Case

## What this eval tests

This is a v9 design-only successor to
`halo-evidence-vs-diagnosis-validation-v8`. It keeps the business/product
evidence-quality domain, but changes the target from "notice that evidence is
contaminated" to "choose the test that can actually disconfirm the favored
story when a more obvious validation move is available but non-probative."

V8 stays frozen and unrescored. Its result was `partial` /
`do_not_promote`: the benchmark machinery worked, but competent generic advice
matched the substrate because the HelioLedger prompt listed the contaminated
signals and the targeted evidence pass directly. V9 is therefore not allowed to
freeze until a local-only generic-solvability probe shows that vanilla/generic
answers do not reliably identify the discriminating test.

This file is a scenario and rubric draft, not a benchmark result and not a
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
of the v9 substrate packet while this case remains design-only. Any draft
synthesis about this evidence-quality tension may inform operator pre-work, but
it must be operator-reviewed before any future run may include it as substrate.

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
enablement gets cleaner. Sales prefers a different test called the Clean Cohort
Challenge: stop new bundle-price offers, withhold the DraftPath roadmap pitch
from a matched set of eligible renewal accounts, require front-line adjuster
use without manager-run sample rehearsals, and compare renewal expansion,
adjuster return behavior, and explainability-related abandonment across broker,
regional-carrier, and health-liability segments.

The Usage Quality Sprint is easier, less politically risky, and can produce a
board-ready dashboard in twelve days. The Clean Cohort Challenge is narrower
and more disruptive: it weakens the near-term revenue story, irritates sales,
and may not produce a clean answer before the board locks the budget. The CEO
has one planning window and can commit to only one package:

- Scale DraftPath broadly: expand quotas, hire implementation specialists,
  prioritize workflow integrations, and make the expansion story the center of
  next year's plan.
- Run the Usage Quality Sprint: instrument adjuster events, clean support tags,
  monitor weekly return rates, and report whether usage improves with better
  enablement.
- Run the Clean Cohort Challenge: pause new bundle-price offers, remove the
  strategic-roadmap pitch from a matched renewal cohort, prevent manager-run
  sample rehearsals from counting as real adoption, and compare segment-level
  renewal expansion, adjuster return behavior, and explainability abandonment.
- Narrow the company plan around regulated health-liability workflows: make
  explainable next-action recommendations the lead product theme, defer broad
  cross-segment selling, and accept a slower expansion story.

The board wants a recommendation in twelve days. Scaling now may preserve
momentum and fund the roadmap. The Usage Quality Sprint may look disciplined
while preserving the same sales and enablement conditions that created the
upbeat story. The Clean Cohort Challenge may test the story more directly, but
it sacrifices momentum and may leave the CEO with a less polished board
message. Narrowing around health-liability workflows may focus the company on
the hardest unresolved segment, but it could overweight one segment's adoption
problem.

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
> cleaner. Sales prefers the Clean Cohort Challenge: stop new bundle-price
> offers, withhold the DraftPath roadmap pitch from a matched set of eligible
> renewal accounts, require front-line adjuster use without manager-run sample
> rehearsals, and compare renewal expansion, adjuster return behavior, and
> explainability-related abandonment across broker, regional-carrier, and
> health-liability segments.
>
> The board locks next year's budget in twelve days. We can commit to only one
> package: scale DraftPath broadly; run the Usage Quality Sprint; run the Clean
> Cohort Challenge; or narrow the company plan around regulated
> health-liability workflows.
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
3. Distinguish monitoring from disconfirmation. The answer should see why the
   Usage Quality Sprint is tempting but not load-bearing: it may improve and
   polish the same manager-mediated, enablement-shaped usage pattern that made
   the success story look good.
4. Select a test that isolates the critical uncertainty: whether DraftPath has
   discount-free, pitch-free, manager-rehearsal-free value for front-line
   adjusters and renewal expansion across segments, including the
   explainability constraint.
5. Weigh the intervention boundary under the twelve-day budget window. The
   answer should state what each recommended and rejected package learns,
   hides, makes irreversible, or forfeits.
6. Make one recommendation, name a concrete failure path for that
   recommendation, and state observable behavioral evidence that would change
   the answer.

## Expected source behavior

- `vanilla` - Advisor prompt only. Baseline; expect plausible business advice
  that balances growth, caution, and measurement without reliably distinguishing
  a monitoring dashboard from a disconfirming test.
- `famous_sources_supplied` - Advisor prompt plus name-level awareness only of
  relevant famous sources and decoys. It supplies no claim about what any
  source argues, no source-card text, no book-map material, and no hidden answer
  key. It tests whether famous-name priming or model memory reproduces the
  substrate effect.
- `substrate_workflow` - Advisor prompt plus the reviewed public source cards
  named in `## Lineage`. The packet must contain no raw source text, no
  book-map evidence, no unreviewed claim/tension card, and no canon language
  unless a later reviewed run packet explicitly adds a reviewed synthesis card
  before freeze.
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

- **Monitoring-is-validation shortcut.** Chooses the Usage Quality Sprint
  because it sounds empirical, while failing to explain that it may monitor the
  same contaminated usage pattern rather than disconfirm the strategy story.
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
| C4 | Selects the disconfirming evidence standard | it selects the Clean Cohort Challenge, or an equivalent design, as the test that isolates the critical uncertainty; it must explain why the Usage Quality Sprint is only monitoring or polishing the existing pattern and would not by itself disconfirm the favored story | it picks the Usage Quality Sprint as sufficient validation, treats general instrumentation or rising retention as enough, fails to choose between the two tests, or names metrics without explaining which test could make the success story wrong |
| C5 | Weighs intervention boundaries | it explains what the chosen package and at least one rejected package would learn, hide, make irreversible, or forfeit under the twelve-day planning window, including the risk that monitoring-only work preserves the contaminated story or that clean testing sacrifices near-term board momentum | it lists options without boundary analysis, collapses to one mechanism, recommends a free hybrid, or ignores the budget-window cost of validation, scaling, or narrowing |
| C6 | Makes a constrained recommendation with behavioral falsifier | it gives one actionable recommendation, engages the board-timing tradeoff, names a concrete failure path for that recommendation, and states observable behavioral evidence that would change the recommendation | it gives a menu, has no strongest reason against its choice, relies on generic uncertainty language, or offers only vague, narrative, customer-approval, or board-reaction change-my-mind evidence |

Anti-label-matching guard: naming a framework or source label without applying
it to the scenario's concrete facts does not earn C3 or C4.

Provenance-neutrality guard: judges should score the reasoning as if source
names and card identifiers were stripped. Source labels may help a reader audit
lineage, but they do not earn credit unless the answer applies the mechanism to
case facts.

## Criterion dependency rule

These dependencies are pre-registered for v9 design:

- **C5 requires C3 and C4.** A judge may not record `PASS` for C5 if the same
  output failed C3 or C4.
- **C6 requires C5.** A judge may not record `PASS` for C6 if the same output
  failed C5.
- **C1 and C2 are otherwise independent and do not gate judge eligibility.**

The ladder is: **C3 and C4 enable C5; C5 enables C6.**

## Generic-solvability probe gate

This design must pass a local-only generic-solvability probe before any
calibration smoke, freeze, generation, or judging.

Probe requirements:

- Run at least three `vanilla` and three `generic_advice_prompted` probe outputs
  against the draft Advisor prompt with no substrate, no criteria prompt, and no
  source names.
- Score only the draft C3-C6 ladder for the probe.
- If more than one of the six probe outputs clearly passes C4 by selecting the
  Clean Cohort Challenge and explaining why the Usage Quality Sprint is
  non-disconfirming, the scenario is still too generic-solvable. Revise the
  scenario and re-probe before any freeze.
- Probe logs, raw outputs, and provisional scoring stay local-only.

This probe does not create benchmark evidence and must not be cited publicly as
a result. It is a design readiness guard.

## Positive result

This positive result applies only after a future frozen v9 generation pass. It
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
- **Probe readiness.** The local-only generic-solvability probe must have
  passed before freeze. A passing probe is not evidence for promotion; it is
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

Treat any of the following as falsifying or non-promotional for a future v9
benchmark generation pass:

- The local-only generic-solvability probe fails before freeze.
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

No v9 model outputs exist. This design-only case must not generate or score
benchmark outputs until the generic-solvability probe and later calibration
smoke gate have passed.

## Score sheet

See `score-sheet.md` in this case folder. It is unscored and records no result
lift; `## Result` is `partial` because no benchmark evidence exists.

## Judge notes

No judge has scored this design-only case.
