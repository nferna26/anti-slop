---
artifact: judge-packet-case-context
case_id: halo-evidence-vs-diagnosis-validation-v9
benchmark_version: halo-evidence-vs-diagnosis-validation-v9-v1
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

## The question the answers respond to

Every OUT-NN answer responds to this question:

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

Score against rubric.md, criterion by criterion. The dependency rule in
rubric.md is mandatory.
