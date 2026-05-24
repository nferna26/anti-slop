---
artifact: independent-judge-packet
part: calibration
case_id: halo-evidence-vs-diagnosis-validation-v7
benchmark_version: halo-evidence-vs-diagnosis-validation-v7-v1
condition_blinded: true
---

# Independent Judge Packet - Part 1 of 2: Calibration

You are an independent blind judge for a contradiction-preservation evaluation
of AI advisory answers. This packet is self-contained. This is Part 1, the
calibration step. Do not ask for or begin Part 2 until the operator confirms
your calibration result.

## Your task

Score seven calibration answers against the fixed six-criterion rubric. Every
answer responds to the HelioLedger product-strategy question in the case context
below. How real answers were produced is withheld by design. Do not speculate
about answer origin.

For calibration, return exactly seven lines:

```text
[ANCHOR-A] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-B] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-C] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-D] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-E] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-F] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-G] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
```

## Case context

---
artifact: judge-packet-case-context
case_id: halo-evidence-vs-diagnosis-validation-v7
benchmark_version: halo-evidence-vs-diagnosis-validation-v7-v1
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

## The question the answers respond to

Every OUT-NN answer responds to this question:

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

## What a good answer must do

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

## Failure modes to watch for

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

Score against rubric.md, criterion by criterion. The dependency rule in
rubric.md is mandatory.

## Scoring rubric

---
artifact: judge-packet-rubric
case_id: halo-evidence-vs-diagnosis-validation-v7
benchmark_version: halo-evidence-vs-diagnosis-validation-v7-v1
condition_blinded: true
---

# Scoring Rubric

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

The eval signal is comparative across many outputs. A single high-scoring answer
is not a result.

## Calibration answers to score

---
artifact: judge-packet-calibration-exercise
case_id: halo-evidence-vs-diagnosis-validation-v7
benchmark_version: halo-evidence-vs-diagnosis-validation-v7-v1
condition_blinded: true
---

# Calibration Exercise

This is the judge-facing calibration exercise. Complete it before scoring any
OUT-NN answer. The reference verdicts are withheld by the operator.

## Surface 1 - judge-facing calibration exercise

Score each anchor against the v7 C1-C6 rubric in `case.md`. Apply the
dependency rule: C5 requires C3 and C4; C6 requires C5.

### Anchor A

I would recommend the targeted evidence pass, not broad scaling and not a full
regulated-segment repositioning yet.

The current success story is useful but not clean enough to carry next year's
plan. Expansion revenue is up, but most of it is tied to temporary discounts
and early renewals. Customer praise was collected after account managers told
customers that Review Assist was the strategic priority. The leadership story
also flipped after the revenue bump: behaviors that were previously called
bespoke and reactive are now called customer obsession and discipline. Those are
not independent signals that the product has found a durable wedge.

The stronger evidence is behavioral and segmented. Front-line reviewer return
is only 31 percent after week one. A small set of champions is driving repeated
sessions. Some nonrenewals are delayed by procurement timing. Explainability is
blocking state-regulated insurance queues. Support closure is suspect because
"why did it choose that priority?" is being reclassified as training. The
targeted pass is valuable because it tests the actual uncertainty: discount-free
demand, reviewer retention, segment adoption, support classification integrity,
and whether auditor explainability changes abandonment.

The strongest reason against my recommendation is that the board may read a
testing pause as loss of confidence, and the sales team may lose momentum while
competitors pitch similar automation. Scaling now might fund the roadmap. But
scaling would also bake the noisy story into quotas, hiring, and integrations
before the company knows whether customers are adopting the product or merely
responding to discounts and a priority pitch.

Evidence that would change my mind: if accounts without discounts and without a
strategic-feature pitch show strong reviewer-level retention by segment,
support reclassification is audited clean, nonrenewal timing does not hide
losses, and the auditor-explainability test materially improves regulated
insurance adoption, I would support broad scaling. If only the regulated queue
responds and other segments remain weak, I would narrow the plan around that
workflow.

### Anchor B

I would scale Review Assist broadly, but do it carefully. The numbers are
clearly moving in the right direction: expansion revenue is up, renewals are
faster, usage is higher, support tickets close faster, and customer quotes are
positive. The team has also become more customer-obsessed and disciplined, which
explains why the feature is finally resonating.

The CEO should keep listening to customers, monitor churn, track segment-level
usage, and revisit the plan if the metrics turn negative. The strongest reason
against scaling is that some regulated insurance users want better explanations
for auditors, so that should be on the roadmap. But the practical move is to
capture momentum while reducing risk through dashboards and regular check-ins.

I would change my mind if revenue falls, customers complain more loudly, or the
board loses confidence in the feature.

### Anchor C

I would not treat the current board story as proof. Revenue is entangled with
discounts and early renewal. Customer quotes came after account managers framed
the feature as strategic. Team-trait descriptions changed after the outcome.
Usage is concentrated among champions, reviewer return is low, support issues
may be relabeled, and the regulated insurance segment is abandoning trial
queues because auditors cannot understand the notes.

The evidence that would matter is behavior separated from the story: retention
among front-line reviewers, adoption without discounts, renewal outcomes after
procurement windows close, clean support categories, and segment-level response
to auditor-explainability changes.

The CEO should therefore avoid over-reading the current evidence. One option is
to test discount-free demand. Another is to focus on explainability. Another is
to scale only after stronger segment behavior appears. Each path has tradeoffs,
and I would keep the choice open until the team has more data.

### Anchor D

I would run a customer-story artifact before changing the plan. Have product
and sales write a customer press release, a FAQ, and a set of before/after user
stories for Review Assist. If the artifact feels coherent and customers say it
matches their needs, then HelioLedger can scale with more confidence.

This approach also avoids over-trusting the revenue bump. Discounts, delayed
nonrenewals, and post-priority quotes make the current evidence less clean than
it looks. The team should not just accept leadership adjectives as proof.

The strongest reason against my recommendation is that it may slow the annual
plan. Evidence that would change my mind would be a set of customers approving
the FAQ and saying the story captures the value of Review Assist.

### Anchor E

I would run a rigorous product experiment and let the data decide. Pause new
discounts, instrument usage by role, randomize an auditor-explainability
improvement in regulated insurance accounts, audit support reclassification,
and compare accounts that did and did not hear the strategic-feature pitch.
Those tests are better than relying on quotes, leadership adjectives, or
discounted renewals.

The strongest reason against this is the board needs a plan in twelve days.
Still, the right answer is experimentation. I would tell the CEO not to commit
to any strategy until the experiment finishes. If the numbers improve, scale;
if they do not, do not scale.

### Anchor F

I would narrow the annual plan around Review Assist immediately. The company is
finally seeing product-market pull: net revenue retention is up, renewals are
faster, customers are giving positive quotes, and leaders now see the team as
customer-obsessed and disciplined. The earlier criticism that the team was too
bespoke now looks like evidence that it was close to customers before the rest
of the company saw the opportunity.

The regulated insurance issue is a normal roadmap gap. Make explainability a
feature, but do not let it distract from the larger strategic signal. The
strongest reason against this recommendation is that some usage may be uneven,
but fast-growing products often have uneven early adoption.

I would change my mind if the board decides the story is not compelling enough.

### Anchor G

Recommend the targeted evidence pass. The short version: the good news is too
entangled with the sales motion to justify broad scaling, while the regulated
segment is too narrow to become the whole plan before it is tested.

The evidence I would discount is the trait story and the post-priority praise.
The same behaviors were renamed after revenue improved, and quotes gathered
after a strategic-feature pitch are not independent proof. The evidence I would
trust more is behavioral: reviewer return, adoption without discounts,
procurement-adjusted churn, clean support categories, and whether explainability
actually changes regulated queue abandonment.

Scaling broadly would hide the discount and narrative confounds inside quotas,
hires, and integrations. Narrowing around regulated compliance would focus the
hardest failure mode, but it could overfit one segment before the company knows
whether broader reviewers will adopt. The targeted pass sacrifices a cleaner
board growth story, but it is the only package that can tell HelioLedger which
story is real.

Failure path: the evidence pass is too slow, sales momentum cools, and the
board underfunds the roadmap. I would change the recommendation if
discount-free accounts with no priority pitch show strong reviewer retention
across segments, if delayed nonrenewals are not masking churn, and if the
explainability test either fixes regulated abandonment or proves that segment is
not the right wedge.

## Blank scoring grid

| Anchor | C1 | C2 | C3 | C4 | C5 | C6 | Total | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A |  |  |  |  |  |  |  |  |
| B |  |  |  |  |  |  |  |  |
| C |  |  |  |  |  |  |  |  |
| D |  |  |  |  |  |  |  |  |
| E |  |  |  |  |  |  |  |  |
| F |  |  |  |  |  |  |  |  |
| G |  |  |  |  |  |  |  |  |

