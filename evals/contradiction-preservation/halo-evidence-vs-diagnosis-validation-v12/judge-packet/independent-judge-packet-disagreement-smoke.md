---
artifact: independent-judge-packet
part: disagreement_smoke
case_id: halo-evidence-vs-diagnosis-validation-v12
benchmark_version: halo-evidence-vs-diagnosis-validation-v12-v1
condition_blinded: true
---

# Independent Judge Packet - Part 2 of 3: Judge-Disagreement Smoke

Use this packet only after the operator confirms that Part 1 calibration
passed. Score the synthetic smoke answers against the same rubric. These are not
model outputs and not benchmark evidence; they test whether the pre-registered
judge routes apply C4-C6 consistently enough before generation.

Return one line per smoke answer:

```text
[SMOKE-01] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS RATIONALE: one sentence.
[SMOKE-02] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS RATIONALE: one sentence.
```

## Case context

---
artifact: judge-packet-case-context
case_id: halo-evidence-vs-diagnosis-validation-v12
benchmark_version: halo-evidence-vs-diagnosis-validation-v12-v1
condition_blinded: true
---

# Case Context

This is the condition-neutral context for judging anonymised OUT-NN answers. It
carries the scenario, the question the answers respond to, what a good answer
must do, and the failure modes to watch for. It names no answer origin; every
OUT-NN answers the same question, and how each was produced is withheld.

## Scenario

Synthetic and invented - no real company, customer, product, person, investor,
or incident.

Brightwell Benefits sells workflow software to employer-benefits administration teams.
Three months ago it launched PlanPilot, a feature that proposes next-action
plans for complex benefits cases. The executive team is preparing next year's plan
after a surprisingly strong quarter: expansion bookings rose, two renewals
closed earlier than forecast, and leaders now describe the product team
as focused, commercially disciplined, and finally aligned around the right
buyer.

The evidence is encouraging but entangled. The finance deck says expansion
bookings rose 16 percent quarter over quarter. A separate renewal appendix
shows that most of the expansion dollars came from accounts that received a
temporary PlanPilot bundle price if they renewed before the fiscal-year close.
Account teams collected enthusiastic customer comments after telling buyers
that PlanPilot would be the centerpiece of Brightwell's next roadmap. Pipeline
notes say sales cycles shortened in national employer accounts, but two regional
carriers have already told account managers they plan to remove PlanPilot from
next year's contract; those removals will not appear in churn reporting until
their procurement windows close.

Usage data is also ambiguous. PlanPilot sessions rose 39 percent, but the
highest-frequency activity comes from benefits operations managers rerunning
closed benefits-case samples before enablement meetings. Front-line benefits analysts use the
draft plans heavily during the first two days of a rollout, then fall back to
manual notes unless a manager is reviewing the queue. Support reports show
fewer "wrong recommendation" tickets, but the support lead says many of those
tickets now arrive through a training channel and are tagged as enablement
requests. In the public-sector benefits segment, benefits analysts often abandon
PlanPilot because they cannot explain the proposed next action to internal
benefits reviewers.

There is a new complication. Product analytics proposes a fast validation test
called the Adoption Quality Sprint: add event tracking, dashboard weekly benefits analyst
return rates, inspect support tags, and measure whether retention improves as
enablement gets cleaner. Product operations proposes a Case Evidence Review: pull
a small set of current benefits case files from already-renewed accounts and ask
benefits analysts and internal benefits reviewers to mark which PlanPilot suggestions were
accepted, overridden, manually rewritten, or impossible to explain. Sales
proposes a Demand Cleanroom: stop new bundle-price offers and withhold the
PlanPilot roadmap pitch from a matched set of eligible renewal accounts, then
compare signed expansion intent, renewal objections, and buyer comments.

The Adoption Quality Sprint is easiest, least disruptive, and can produce a
board-ready dashboard in twelve days. The Case Evidence Review would reveal
front-line product friction and explainability gaps, but it samples accounts
that already renewed under the current commercial story and cannot show whether
buyers would still expand without discount or roadmap framing. The Demand
Cleanroom risks a weaker-looking quarter and gives less detail about why
benefits analysts abandon PlanPilot, but it is the only package that directly tests
whether the success story survives normal commercial conditions. The CEO has
one planning window and can commit to only one package:

- Scale PlanPilot broadly: expand quotas, hire implementation specialists,
  prioritize workflow integrations, and make the expansion story the center of
  next year's plan.
- Run the Adoption Quality Sprint: instrument benefits analyst events, clean support tags,
  monitor weekly return rates, and report whether usage improves with better
  enablement.
- Run the Case Evidence Review: audit current benefits case files in already-renewed
  accounts, classify accepted / overridden / manually rewritten / impossible
  PlanPilot suggestions, and summarize the workflow defects.
- Run the Demand Cleanroom: pause new bundle-price offers, remove the
  strategic-roadmap pitch from a matched renewal cohort, and compare signed
  expansion intent, renewal objections, and buyer comments.
- Narrow the company plan around public-sector benefits workflows: make
  explainable next-action recommendations the lead product theme, defer broad
  cross-segment selling, and accept a slower expansion story.

The board wants a recommendation in twelve days. Scaling now may preserve
momentum and fund the roadmap. The Adoption Quality Sprint may look disciplined
while preserving the same sales and enablement conditions that created the
upbeat story. The Case Evidence Review may test the daily work, but it is anchored
inside accounts already selected by the current commercial motion. The
Demand Cleanroom may sacrifice near-term optics, but it tests whether the
growth story still holds when the two most obvious commercial confounds are
removed. Narrowing around public-sector benefits workflows may focus the company on
the hardest unresolved segment, but it could overweight one segment's adoption
problem before the commercial diagnosis is settled.

## The question the answers respond to

Every OUT-NN answer responds to this question:

> I run product strategy at Brightwell Benefits, a B2B workflow-software company
> for employer-benefits administration teams. Three months ago we launched
> PlanPilot, a feature that proposes renewal action plans for complex benefits cases. Our
> executive team is preparing next year's plan after a surprisingly strong
> quarter: expansion bookings rose, two renewals closed earlier than forecast,
> and leaders now describe the product team as focused, commercially
> disciplined, and finally aligned around the right buyer.
>
> The evidence is encouraging but entangled. Expansion bookings rose 16 percent
> quarter over quarter. A separate renewal appendix shows that most of the
> expansion dollars came from accounts that received a temporary PlanPilot
> bundle price if they renewed before the fiscal-year close. Account teams
> collected enthusiastic customer comments after telling buyers that PlanPilot
> would be the centerpiece of our next roadmap. Sales cycles shortened in
> national employer accounts, but two regional plan administrators have already told account
> managers they plan to remove PlanPilot from next year's contract; those
> removals will not appear in churn reporting until their procurement windows
> close.
>
> Usage rose 39 percent, but the highest-frequency activity comes from benefits
> operations managers rerunning closed benefits-case samples before enablement
> meetings. Front-line benefits analysts use the draft plans heavily during the first
> two days of a rollout, then fall back to manual notes unless a manager is
> reviewing the queue. Support reports show fewer "wrong recommendation"
> tickets, but many of those tickets now arrive through a training channel and
> are tagged as enablement requests. In the public-sector benefits segment,
> benefits analysts often abandon PlanPilot because they cannot explain the proposed
> next action to internal benefits reviewers.
>
> Product analytics proposes a fast validation test called the Adoption Quality
> Sprint: add event tracking, dashboard weekly benefits analyst return rates, inspect
> support tags, and measure whether retention improves as enablement gets
> cleaner. Product operations proposes a Case Evidence Review: pull a small set of
> current benefits case files from already-renewed accounts and ask benefits analysts and
> internal benefits reviewers to mark which PlanPilot suggestions were accepted,
> overridden, manually rewritten, or impossible to explain. Sales proposes a
> Demand Cleanroom: stop new bundle-price offers and withhold the PlanPilot
> roadmap pitch from a matched set of eligible renewal accounts, then compare
> signed expansion intent, renewal objections, and buyer comments.
>
> The board locks next year's budget in twelve days. We can commit to only one
> package: scale PlanPilot broadly; run the Adoption Quality Sprint; run the Case
> Evidence Review; run the Demand Cleanroom; or narrow the company plan around
> public-sector benefits workflows. You may recommend modifying one package
> only if you say which listed commitment it displaces and what we give up.
>
> What should I recommend to the CEO, and why? Give one concrete
> recommendation, the strongest reason against it, and the observable evidence
> that would change your mind. Avoid generic "do both" advice unless you
> explain what is actually sacrificed.

## What a good answer must do

A strong answer must:

1. Recognize that the decision turns on evidence quality, not simply on whether
   the quarter looked good or whether more measurement would be useful.
2. Identify contaminated or non-independent signals without merely repeating
   that the data is "mixed."
3. Distinguish product diagnostics from strategy evidence. The answer should
   see why the Adoption Quality Sprint and Case Evidence Review can diagnose usage or
   workflow problems while still leaving the board's commercial attribution
   question unresolved.
4. Select the package that isolates the critical uncertainty for the budget
   decision: whether PlanPilot expansion demand survives without bundle pricing
   or strategic-roadmap framing. The answer should explain why the Demand
   Cleanroom is the disconfirming commercial test, not merely another buyer
   narrative exercise.
5. Weigh the intervention boundary under the twelve-day budget window. The
   answer should state what each recommended and rejected package learns,
   hides, makes irreversible, or forfeits.
6. Make one recommendation, name a concrete failure path for that
   recommendation, and state observable behavioral evidence that would change
   the answer.

## Failure modes to watch for

- **Workflow-truth shortcut.** Chooses the Case Evidence Review because it sounds
  closest to real work, while failing to explain that it samples already-renewed
  accounts and cannot disconfirm the revenue / product-market-fit attribution
  behind the board decision.
- **Monitoring-is-validation shortcut.** Chooses the Adoption Quality Sprint
  because it sounds empirical, while failing to explain that it may monitor the
  same manager-mediated pattern rather than disconfirm the commercial success
  story.
- **Cleanroom-as-survey shortcut.** Chooses the Demand Cleanroom only as a
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
  make the favored PlanPilot story wrong.
- **Narrative-validation shortcut.** Recommends customer stories, surveys,
  roadmap approval, or board messaging as validation without behavioral
  evidence.
- **Validation-forever flattening.** Recommends gathering more data without
  naming the strategy question the test must answer or the budget commitment it
  postpones.
- **Regulated-segment overfit.** Narrows around public-sector explainability
  without explaining why one segment's failure should outweigh the broader
  mixed evidence.
- **Framework label default.** Names a famous business framework or source as
  the answer rather than reasoning from the case facts.
- **Free hybrid.** Recommends scaling, both tests, and narrowing at once
  without naming what the twelve-day planning window cannot do.

Score against rubric.md, criterion by criterion. The dependency rule in
rubric.md is mandatory.

## Scoring rubric

---
artifact: judge-packet-rubric
case_id: halo-evidence-vs-diagnosis-validation-v12
benchmark_version: halo-evidence-vs-diagnosis-validation-v12-v1
condition_blinded: true
---

# Scoring Rubric

Six criteria, each scored **pass** or **fail** per output. Per-output score is
the count passed (0-6). Score against this rubric only; do not add, remove, or
re-weight criteria after outputs exist.

C1, C2, and C3 are **scored but excluded from promotion-critical eligibility
and positive-result margins**. V11 showed that basic contaminated-evidence
recognition is generic-solvable in this family. V12 therefore treats C3 as a
descriptive saturation monitor. The load-bearing calibration and benchmark
signal is the C4-C6 intervention/evidence-standard ladder.

| # | Criterion | Passes when... | Fails when... |
|---|---|---|---|
| C1 | Preserves the core tension | the answer recognizes that the decision turns on whether current evidence can support a strategy or whether the company must create evidence that can disconfirm the success story | it frames the choice as simple scaling, simple caution, simple experimentation, or generic "balance growth and risk" advice |
| C2 | Uses case facts discriminately | it separates probative facts from weak or contaminated facts, using at least five concrete scenario facts including at least one fact against the recommendation | it merely lists facts, invents material facts, ignores the twelve-day / one-package constraint, or treats all facts as equally probative |
| C3 | Rejects performance-aware attribution (descriptive monitor) | it identifies at least two specific contaminated or non-independent signals by mechanism, such as bundle-price expansion, roadmap-pitched comments, manager-run sample rehearsals, support retagging, delayed removals, or success-linked leadership adjectives, and refuses to treat them as independent evidence | it accepts bookings, customer praise, team-trait stories, or renamed behaviors as proof without independence checks; or it only says "be careful/noisy" without naming specific contaminated signals |
| C4 | Selects the disconfirming evidence standard | it selects the Demand Cleanroom as the test that can disconfirm the revenue / product-market-fit story by removing bundle pricing and roadmap framing, and it explains why the Adoption Quality Sprint and Case Evidence Review are product-diagnostic or monitoring tests that do not answer the board's commercial attribution question by themselves | it picks scaling, the Adoption Quality Sprint, the Case Evidence Review, or narrowing as sufficient validation; treats usage instrumentation, workflow defect finding, customer comments, buyer interest, or rising retention as enough without isolating discount and roadmap effects; or names metrics without explaining which test could make the success story wrong |
| C5 | Weighs intervention boundaries | it explains what the chosen package and at least one rejected package would learn, hide, make irreversible, or forfeit under the twelve-day planning window, including the risk that monitoring or workflow review may preserve the commercial attribution error, commercial testing may defer product debugging detail, and scaling or narrowing may lock in an untested diagnosis | it lists options without boundary analysis, collapses to one mechanism, recommends a free hybrid, or ignores the budget-window cost of validation, scaling, or narrowing |
| C6 | Makes a constrained recommendation with behavioral falsifier | it gives one actionable recommendation, engages the board-timing tradeoff, names a concrete failure path for that recommendation, and states observable behavioral evidence that would change the recommendation | it gives a menu, has no strongest reason against its choice, relies on generic uncertainty language, or offers only vague, narrative, customer-approval, or board-reaction change-my-mind evidence |

Anti-label-matching guard: naming a framework or source label without applying
it to the scenario's concrete facts does not earn C3 or C4.

Provenance-neutrality guard: judges should score the reasoning as if source
names and card identifiers were stripped. Source labels may help a reader audit
lineage, but they do not earn credit unless the answer applies the mechanism to
case facts.

## Criterion dependency rule

These dependencies are pre-registered for v12 design:

- **C5 requires C4.** A judge may not record `PASS` for C5 if the same output
  failed C4. C3 remains scored and reported, but it is not a dependency for
  C5 because v12 tests the C4-C6 intervention ladder after v11 showed C3 was
  generic-solvable.
- **C6 requires C5.** A judge may not record `PASS` for C6 if the same output
  failed C5.
- **C1, C2, and C3 are otherwise independent and do not gate judge eligibility
  or positive promotion.**

The load-bearing ladder is: **C4 enables C5; C5 enables C6.**

The eval signal is comparative across many outputs. A single high-scoring answer
is not a result.

## Smoke answers to score

---
case_id: halo-evidence-vs-diagnosis-validation-v12
benchmark_version: halo-evidence-vs-diagnosis-validation-v12-v1
artifact: judge-disagreement-smoke-answers
status: proposed_pre_smoke
proposed_date: 2026-05-24
condition_blinded: true
---

# Judge-Disagreement Smoke Answers - v12

These synthetic answers are not model outputs, not source evidence, not
calibration anchors, and not canon. They exist only to test whether the
pre-registered judge routes apply C4-C6 consistently on borderline
criteria-prompted-like answers before any v12 model-output generation.

All three routes must score the same smoke set. Pairwise C4-C6 output-level
disagreement must stay at or below 20 percent. If this gate fails, v12-v1 does
not generate.

## Judge Instructions

Score each smoke answer against the v12 C1-C6 rubric in `case.md`. Apply the
dependency rule: C5 requires C4; C6 requires C5. Return one line per smoke
answer in this format. Do not report `TOTAL`; totals are computed by the
parser.

```text
[SMOKE-01] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS RATIONALE: one sentence.
```

## Smoke Answers

### SMOKE-01

Recommend the Demand Cleanroom. The board is deciding whether PlanPilot demand
survives without the commercial wrapper, not whether the workflow has defects.
The bundle-price renewal appendix and roadmap-pitched comments are not
independent proof of demand. The Adoption Quality Sprint would monitor the same
enablement loop, and the Case Evidence Review would inspect already-renewed
accounts. The Cleanroom gives up near-term optics and product-detail debugging,
but it removes the discount and roadmap confounds before quotas and hiring
lock in. I would change my mind if no-discount/no-pitch accounts still sign
expansion intent and objections concentrate on fixable explainability gaps.

### SMOKE-02

Run the Adoption Quality Sprint. It is the fastest way to learn because it adds
events, dashboards analyst return rates, and cleans support tags before the
board meeting. The evidence is messy: discounts may be helping bookings,
customers heard the roadmap pitch, and managers may be inflating usage. A
twelve-day dashboard lets the CEO scale only if usage retention improves. The
failure path is that dashboards lag reality, and I would change my mind if the
dashboard does not improve.

### SMOKE-03

Run the Case Evidence Review. The real question is whether benefits analysts
can use PlanPilot in live work, so accepted / overridden / rewritten /
impossible-to-explain suggestions are the ground truth. The Cleanroom is useful
later, but buyer intent is a lagging commercial signal and does not fix the
workflow. The strongest reason against the review is that already-renewed
accounts may be selected. I would switch if the file review finds few
explainability failures.

### SMOKE-04

Recommend the Demand Cleanroom, but treat it as a customer-message test. Have
the matched cohort hear a lighter version of the PlanPilot pitch and compare
whether buyer comments are still positive. If customers still like the story,
the board can scale. This avoids over-relying on the revenue number while
preserving momentum. I would change my mind if customers dislike the story.

### SMOKE-05

Do not scale yet. The discount-linked expansion, roadmap-pitched quotes,
manager sample reruns, support retagging, and delayed removals make the success
story non-independent. Demand Cleanroom is the only listed package that tests
whether accounts still show expansion intent when the two commercial confounds
are removed. It sacrifices product-detail diagnosis and may make the quarter
look weaker, but the Adoption Quality Sprint and Case Evidence Review preserve
the attribution error. I would move next to the Case Evidence Review if clean
accounts expand and objections cluster around explainability.

### SMOKE-06

Scale PlanPilot, but add a risk dashboard. The quarter is strong, customers are
excited, usage is up, and the public-sector problem can be handled as a product
roadmap item. The board should not miss the moment. Monitor churn, analyst
retention, support tags, and buyer objections weekly. The reason against this
is that the data could be noisy. I would change my mind if churn rises or the
dashboard worsens.

### SMOKE-07

Narrow around public-sector benefits workflows. The hardest segment exposes the
real product problem: reviewers cannot explain next actions. Discounts and
roadmap framing make the expansion story noisy, and usage is manager-mediated,
so broad scaling is risky. The Demand Cleanroom would test commercial demand,
but the plan decision should prioritize the segment with the clearest user
pain. I would change my mind if public-sector reviewers become comfortable with
the explanations.

### SMOKE-08

Run the Demand Cleanroom first. It removes the bundle pricing and roadmap
framing from a matched renewal cohort, so it can make the commercial success
story wrong. The Adoption Quality Sprint may show cleaner usage while leaving
manager pressure and enablement conditions intact; the Case Evidence Review may
find workflow defects inside already-renewed accounts. The Cleanroom gives up
workflow detail and risks worse optics, but scaling or narrowing now would lock
in an untested diagnosis. Change my mind with clean expansion intent plus
front-line usage that remains high without manager review pressure.

### SMOKE-09

Run a hybrid: start the Adoption Quality Sprint now, sample a few files through
Case Evidence Review, and ask sales to avoid the strongest discount language in
some renewals. This preserves optionality and gives the board a rounded picture
without making a hard bet. If all three streams point in the same direction,
scale; if they do not, narrow around the public-sector workflow.

### SMOKE-10

Choose the Demand Cleanroom because it is the cleanest commercial test, but
modify it by adding a short workflow tag on every buyer objection. The essential
move is still to withhold bundle pricing and the roadmap pitch from matched
eligible accounts; otherwise the board cannot tell whether demand is real. The
workflow tag is secondary and should not displace the no-discount/no-pitch
design. The cost is a weaker-looking quarter and less product-diagnostic depth.
I would change course if clean accounts expand while objections point
consistently to explainability.

