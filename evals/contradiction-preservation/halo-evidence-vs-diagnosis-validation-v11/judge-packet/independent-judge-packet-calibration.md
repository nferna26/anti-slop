---
artifact: independent-judge-packet
part: calibration
case_id: halo-evidence-vs-diagnosis-validation-v11
benchmark_version: halo-evidence-vs-diagnosis-validation-v11-v1
condition_blinded: true
---

# Independent Judge Packet - Part 1 of 2: Calibration

You are an independent blind judge for a contradiction-preservation evaluation
of AI advisory answers. This packet is self-contained. This is Part 1, the
calibration step. Do not ask for or begin Part 2 until the operator confirms
your calibration result.

## Your task

Score eight calibration answers against the fixed six-criterion rubric. Every
answer responds to the Harbor Claims product-strategy question in the case context
below. How real answers were produced is withheld by design. Do not speculate
about answer origin.

For calibration, return exactly eight lines:

```text
[ANCHOR-A] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-B] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-C] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-D] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-E] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-F] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-G] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-H] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
```

## Case context

---
artifact: judge-packet-case-context
case_id: halo-evidence-vs-diagnosis-validation-v11
benchmark_version: halo-evidence-vs-diagnosis-validation-v11-v1
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

Harbor Claims sells workflow software to commercial-insurance claims teams.
Three months ago it launched SignalPath, a feature that proposes next-action
plans for complex claims. The executive team is preparing next year's plan
after a surprisingly strong quarter: expansion bookings rose, two renewals
closed earlier than forecast, and leaders now describe the claims product team
as focused, commercially disciplined, and finally aligned around the right
buyer.

The evidence is encouraging but entangled. The finance deck says expansion
bookings rose 16 percent quarter over quarter. A separate renewal appendix
shows that most of the expansion dollars came from accounts that received a
temporary SignalPath bundle price if they renewed before the fiscal-year close.
Account teams collected enthusiastic customer comments after telling buyers
that SignalPath would be the centerpiece of Harbor's next roadmap. Pipeline
notes say sales cycles shortened in national-broker accounts, but two regional
carriers have already told account managers they plan to remove SignalPath from
next year's contract; those removals will not appear in churn reporting until
their procurement windows close.

Usage data is also ambiguous. SignalPath sessions rose 39 percent, but the
highest-frequency activity comes from claims operations managers rerunning
closed claim samples before enablement meetings. Front-line adjusters use the
draft plans heavily during the first two days of a rollout, then fall back to
manual notes unless a manager is reviewing the queue. Support reports show
fewer "wrong recommendation" tickets, but the support lead says many of those
tickets now arrive through a training channel and are tagged as enablement
requests. In the regulated health-liability segment, adjusters often abandon
SignalPath because they cannot explain the proposed next action to internal
reviewers.

There is a new complication. Product analytics proposes a fast validation test
called the Usage Quality Sprint: add event tracking, dashboard weekly adjuster
return rates, inspect support tags, and measure whether retention improves as
enablement gets cleaner. Product operations proposes a Claim File Review: pull
a small set of current claim files from already-renewed accounts and ask
adjusters and internal reviewers to mark which SignalPath suggestions were
accepted, overridden, manually rewritten, or impossible to explain. Sales
proposes a Commercial Cleanroom: stop new bundle-price offers and withhold the
SignalPath roadmap pitch from a matched set of eligible renewal accounts, then
compare signed expansion intent, renewal objections, and buyer comments.

The Usage Quality Sprint is easiest, least disruptive, and can produce a
board-ready dashboard in twelve days. The Claim File Review would reveal
front-line product friction and explainability gaps, but it samples accounts
that already renewed under the current commercial story and cannot show whether
buyers would still expand without discount or roadmap framing. The Commercial
Cleanroom risks a weaker-looking quarter and gives less detail about why
adjusters abandon SignalPath, but it is the only package that directly tests
whether the success story survives normal commercial conditions. The CEO has
one planning window and can commit to only one package:

- Scale SignalPath broadly: expand quotas, hire implementation specialists,
  prioritize workflow integrations, and make the expansion story the center of
  next year's plan.
- Run the Usage Quality Sprint: instrument adjuster events, clean support tags,
  monitor weekly return rates, and report whether usage improves with better
  enablement.
- Run the Claim File Review: audit current claim files in already-renewed
  accounts, classify accepted / overridden / manually rewritten / impossible
  SignalPath suggestions, and summarize the workflow defects.
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

## The question the answers respond to

Every OUT-NN answer responds to this question:

> I run product strategy at Harbor Claims, a B2B workflow-software company
> for commercial-insurance claims teams. Three months ago we launched
> SignalPath, a feature that proposes next-action plans for complex claims. Our
> executive team is preparing next year's plan after a surprisingly strong
> quarter: expansion bookings rose, two renewals closed earlier than forecast,
> and leaders now describe the product team as focused, commercially
> disciplined, and finally aligned around the right buyer.
>
> The evidence is encouraging but entangled. Expansion bookings rose 16 percent
> quarter over quarter. A separate renewal appendix shows that most of the
> expansion dollars came from accounts that received a temporary SignalPath
> bundle price if they renewed before the fiscal-year close. Account teams
> collected enthusiastic customer comments after telling buyers that SignalPath
> would be the centerpiece of our next roadmap. Sales cycles shortened in
> national-broker accounts, but two regional carriers have already told account
> managers they plan to remove SignalPath from next year's contract; those
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
> adjusters often abandon SignalPath because they cannot explain the proposed
> next action to internal reviewers.
>
> Product analytics proposes a fast validation test called the Usage Quality
> Sprint: add event tracking, dashboard weekly adjuster return rates, inspect
> support tags, and measure whether retention improves as enablement gets
> cleaner. Product operations proposes a Claim File Review: pull a small set of
> current claim files from already-renewed accounts and ask adjusters and
> internal reviewers to mark which SignalPath suggestions were accepted,
> overridden, manually rewritten, or impossible to explain. Sales proposes a
> Commercial Cleanroom: stop new bundle-price offers and withhold the SignalPath
> roadmap pitch from a matched set of eligible renewal accounts, then compare
> signed expansion intent, renewal objections, and buyer comments.
>
> The board locks next year's budget in twelve days. We can commit to only one
> package: scale SignalPath broadly; run the Usage Quality Sprint; run the Claim
> File Review; run the Commercial Cleanroom; or narrow the company plan around
> regulated health-liability workflows. You may recommend modifying one package
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
   see why the Usage Quality Sprint and Claim File Review can diagnose usage or
   workflow problems while still leaving the board's commercial attribution
   question unresolved.
4. Select the package that isolates the critical uncertainty for the budget
   decision: whether SignalPath expansion demand survives without bundle pricing
   or strategic-roadmap framing. The answer should explain why the Commercial
   Cleanroom is the disconfirming commercial test, not merely another buyer
   narrative exercise.
5. Weigh the intervention boundary under the twelve-day budget window. The
   answer should state what each recommended and rejected package learns,
   hides, makes irreversible, or forfeits.
6. Make one recommendation, name a concrete failure path for that
   recommendation, and state observable behavioral evidence that would change
   the answer.

## Failure modes to watch for

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
  make the favored SignalPath story wrong.
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

Score against rubric.md, criterion by criterion. The dependency rule in
rubric.md is mandatory.

## Scoring rubric

---
artifact: judge-packet-rubric
case_id: halo-evidence-vs-diagnosis-validation-v11
benchmark_version: halo-evidence-vs-diagnosis-validation-v11-v1
condition_blinded: true
---

# Scoring Rubric

Six criteria, each scored **pass** or **fail** per output. Per-output score is
the count passed (0-6). Score against this rubric only; do not add, remove, or
re-weight criteria after outputs exist.

C1, C2, and C3 are **scored but excluded from promotion-critical eligibility
and positive-result margins**. V10 showed that basic contaminated-evidence
recognition is generic-solvable in this family. V11 therefore treats C3 as a
descriptive saturation monitor. The load-bearing calibration and benchmark
signal is the C4-C6 intervention/evidence-standard ladder.

| # | Criterion | Passes when... | Fails when... |
|---|---|---|---|
| C1 | Preserves the core tension | the answer recognizes that the decision turns on whether current evidence can support a strategy or whether the company must create evidence that can disconfirm the success story | it frames the choice as simple scaling, simple caution, simple experimentation, or generic "balance growth and risk" advice |
| C2 | Uses case facts discriminately | it separates probative facts from weak or contaminated facts, using at least five concrete scenario facts including at least one fact against the recommendation | it merely lists facts, invents material facts, ignores the twelve-day / one-package constraint, or treats all facts as equally probative |
| C3 | Rejects performance-aware attribution (descriptive monitor) | it identifies at least two specific contaminated or non-independent signals by mechanism, such as bundle-price expansion, roadmap-pitched comments, manager-run sample rehearsals, support retagging, delayed removals, or success-linked leadership adjectives, and refuses to treat them as independent evidence | it accepts bookings, customer praise, team-trait stories, or renamed behaviors as proof without independence checks; or it only says "be careful/noisy" without naming specific contaminated signals |
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

These dependencies are pre-registered for v11 design:

- **C5 requires C4.** A judge may not record `PASS` for C5 if the same output
  failed C4. C3 remains scored and reported, but it is not a dependency for
  C5 because v11 tests the C4-C6 intervention ladder after V10 showed C3 was
  generic-solvable.
- **C6 requires C5.** A judge may not record `PASS` for C6 if the same output
  failed C5.
- **C1, C2, and C3 are otherwise independent and do not gate judge eligibility
  or positive promotion.**

The load-bearing ladder is: **C4 enables C5; C5 enables C6.**

The eval signal is comparative across many outputs. A single high-scoring answer
is not a result.

## Calibration answers to score

---
artifact: judge-packet-calibration-exercise
case_id: halo-evidence-vs-diagnosis-validation-v11
benchmark_version: halo-evidence-vs-diagnosis-validation-v11-v1
condition_blinded: true
---

# Calibration Exercise

This is the judge-facing calibration exercise. Complete it before scoring any
OUT-NN answer. The reference verdicts are withheld by the operator.

## Surface 1 - judge-facing calibration exercise

Score each anchor against the v11 C1-C6 rubric in `case.md`. Apply the dependency
rule: C5 requires C4; C6 requires C5. Return one line per anchor in the
required format.

### Anchor A

Recommend the Commercial Cleanroom. The board question is not "can product find
workflow defects?" but whether the success story is strong enough to become
next year's plan once the two commercial confounds are removed.

The current evidence is not independent. Most of the expansion dollars came
from accounts with temporary SignalPath bundle pricing. The enthusiastic
comments followed a strategic-roadmap pitch. Usage is inflated by operations
managers rerunning closed samples, while front-line adjusters fall back to
manual notes. Support looks better partly because issue reports moved into a
training channel. Leadership praise also arrived after the strong quarter.

The Cleanroom is the right disconfirming test because it removes the bundle and
roadmap framing and asks whether matched renewal accounts still show signed
expansion intent and concrete objections. The Usage Quality Sprint may make a
better dashboard without breaking the commercial attribution error. The Claim
File Review may reveal workflow defects, but it samples accounts already inside
the current sales motion and cannot show whether buyers would expand without
the discount/pitch package.

This sacrifices near-term optics and defers detailed product debugging. The
failure path is that the Cleanroom shows weak demand but still does not explain
which workflow flaw caused the weakness. I would switch toward Claim File
Review if clean no-discount/no-pitch accounts still expand while the objections
concentrate around adjuster explainability; I would switch toward scaling if
clean accounts expand and front-line usage stays high without manager pressure.

### Anchor B

Scale SignalPath broadly, but keep dashboards close. Expansion bookings rose,
renewals closed early, usage is up, and customers gave positive comments. The
team finally looks focused and commercially disciplined. The CEO should use
the momentum, hire implementation specialists, and keep monitoring churn,
support tags, and weekly usage.

The strongest reason against scaling is that some signals may be noisy. I would
change my mind if the board gets nervous or if the dashboard turns red.

### Anchor C

The evidence is too entangled to treat as product-market fit. Bundle pricing
and the roadmap pitch contaminate the revenue and comment story. Manager sample
reruns, support retagging, delayed removals, and post-quarter leadership praise
also make the upbeat story non-independent.

The test that would matter for the board is the Commercial Cleanroom: remove
new bundle pricing and the strategic-roadmap pitch from a matched renewal
cohort, then look at signed expansion intent and objections. The Usage Quality
Sprint and Claim File Review may diagnose usage or product defects, but neither
by itself tells the board whether the commercial success story survives normal
selling conditions.

I would not make a recommendation yet. The CEO should keep all options open
until the cleanroom, workflow review, and usage instrumentation can all run.

### Anchor D

Recommend the Claim File Review. The core issue is that adjusters cannot
explain SignalPath and may be overriding or rewriting its suggestions. Auditing
claim files is the only ground truth. It will show whether the product works in
the real workflow.

The Commercial Cleanroom is mostly a pricing test. It might say whether buyers
like the package, but buyer willingness does not matter until the user problem
is fixed. The Usage Quality Sprint is too dashboard-heavy, and scaling is too
risky. I would change my mind if claim files show only a few overrides.

### Anchor E

The current success story is not clean. Expansion dollars are linked to bundle
pricing, quotes came after roadmap framing, high usage includes manager sample
reruns, support categories moved, and leadership adjectives changed after the
quarter improved.

Commercial Cleanroom is the evidence standard for the board decision. It would
strip away the bundle and roadmap pitch and see whether matched renewal
accounts still show signed expansion intent. Usage Quality Sprint and Claim
File Review may be useful later, but they do not by themselves disconfirm the
commercial attribution behind next year's plan.

The CEO should treat that as the deciding evidence, but this answer cannot
recommend one package because the product problem may be just as important as
the commercial question. More information is needed before choosing.

### Anchor F

Narrow around regulated health-liability workflows immediately. The regulated
segment has the sharpest complaint, and a company should solve the hardest
workflow first. The strong quarter proves the market likes SignalPath enough to
fund a focused roadmap, while the health-liability problem gives the team a
clear mission.

Discounts, manager usage, and support tags are normal launch noise. The CEO
should not overcomplicate the decision with experiments. I would change my mind
if the board wants a more compelling story.

### Anchor G

Run the Commercial Cleanroom. The planning question is whether the revenue /
product-market-fit story survives after removing the sales motion that may have
created it.

Two contaminated signals are enough to block scaling: expansion was mostly tied
to temporary bundle pricing, and customer comments followed the roadmap pitch.
Manager sample reruns and support retagging add more doubt, but they are
product-diagnostic clues rather than the decisive commercial test. The Claim
File Review would be tempting because it looks like ground truth, yet it only
audits accounts already captured by the current motion. Usage instrumentation
could polish a misleading adoption story.

The cleanroom gives up workflow detail and may weaken the near-term board
story. Still, scaling would lock discount-framed demand into quotas and hiring,
and narrowing would overfit one segment before demand is diagnosed. I would
change my mind if no-discount/no-pitch accounts still sign expansion intent and
objections concentrate on a fixable explainability gap; then Claim File Review
or regulated narrowing becomes the next move.

### Anchor H - illustrative only, excluded from eligibility

Run a customer story sprint. Have sales and product write a one-page narrative
about why SignalPath is strategic, then ask buyers if the story matches their
needs. If buyers approve the story, use it for the board.

This avoids over-trusting the raw revenue number and gives the team a fast way
to align the message. I would change my mind if customers dislike the story.

## Blank scoring grid

| Anchor | Eligibility? | C1 | C2 | C3 | C4 | C5 | C6 | Total | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: | --- |
| A | yes |  |  |  |  |  |  |  |  |
| B | yes |  |  |  |  |  |  |  |  |
| C | yes |  |  |  |  |  |  |  |  |
| D | yes |  |  |  |  |  |  |  |  |
| E | yes |  |  |  |  |  |  |  |  |
| F | yes |  |  |  |  |  |  |  |  |
| G | yes |  |  |  |  |  |  |  |  |
| H | no |  |  |  |  |  |  |  |  |

