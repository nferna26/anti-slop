---
artifact: independent-judge-packet
part: calibration
case_id: halo-evidence-vs-diagnosis-validation-v8
benchmark_version: halo-evidence-vs-diagnosis-validation-v8-v1
condition_blinded: true
---

# Independent Judge Packet - Part 1 of 2: Calibration

You are an independent blind judge for a contradiction-preservation evaluation
of AI advisory answers. This packet is self-contained. This is Part 1, the
calibration step. Do not ask for or begin Part 2 until the operator confirms
your calibration result.

## Your task

Score eight calibration answers against the fixed six-criterion rubric. Every
answer responds to the HelioLedger product-strategy question in the case context
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
case_id: halo-evidence-vs-diagnosis-validation-v8
benchmark_version: halo-evidence-vs-diagnosis-validation-v8-v1
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

## Failure modes to watch for

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

Score against rubric.md, criterion by criterion. The dependency rule in
rubric.md is mandatory.

## Scoring rubric

---
artifact: judge-packet-rubric
case_id: halo-evidence-vs-diagnosis-validation-v8
benchmark_version: halo-evidence-vs-diagnosis-validation-v8-v1
condition_blinded: true
---

# Scoring Rubric

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

The eval signal is comparative across many outputs. A single high-scoring answer
is not a result.

## Calibration answers to score

---
artifact: judge-packet-calibration-exercise
case_id: halo-evidence-vs-diagnosis-validation-v8
benchmark_version: halo-evidence-vs-diagnosis-validation-v8-v1
condition_blinded: true
---

# Calibration Exercise

This is the judge-facing calibration exercise. Complete it before scoring any
OUT-NN answer. The reference verdicts are withheld by the operator.

## Surface 1 - judge-facing calibration exercise

Score each anchor against the v8 C1-C6 rubric in `case.md`. Apply the dependency
rule: C5 requires C3 and C4; C6 requires C5. Return one line per anchor in the
required format.

### Anchor A

I would recommend the targeted evidence pass. The revenue story is promising,
but it is not clean enough to carry next year's plan.

The contaminated signals are specific. Most expansion is tied to temporary
discounts and early renewals, so it is not independent demand. The positive
quotes were gathered after account managers framed Review Assist as strategic,
so they are not clean customer evidence. Leadership also renamed the same
bespoke/reactive behaviors after the revenue bump, which is trait recoding
after the outcome rather than independent proof of discipline.

The evidence that should decide the issue is behavioral and disconfirming:
discount-free and pitch-free adoption by segment, week-one return by front-line
reviewers, nonrenewals after procurement windows close, audited support
categories, and whether explainability changes regulated insurance queue
abandonment.

The targeted pass sacrifices the cleanest board growth story and may cool sales
momentum, but scaling now would bake the discount and priority-pitch confounds
into quotas, hiring, and integrations. Narrowing around regulated workflows
would focus on the sharpest failure mode before knowing whether that segment is
representative or solvable.

I would change my mind toward broad scaling if accounts without discounts and
without a strategic-feature pitch show strong reviewer retention across
segments, nonrenewals are not merely delayed, support reclassification audits
cleanly, and explainability materially improves regulated adoption. If only the
regulated queue responds and other segments stay weak, I would narrow.

### Anchor B

I would scale Review Assist broadly, but do it carefully. Revenue is up,
renewals are faster, usage is higher, support tickets close faster, and
customers are saying positive things. The team is also showing more customer
obsession and discipline, which explains why the feature is resonating.

The CEO should keep listening to customers, monitor churn, track usage by
segment, and revisit the plan if metrics turn negative. The regulated insurance
issue is real, so put better auditor explanations on the roadmap. The practical
move is to capture momentum while reducing risk through dashboards and regular
check-ins.

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

I would avoid over-reading the evidence. One path is to test discount-free
demand; another is to focus on explainability; another is to scale only after
stronger segment behavior appears. Each path has tradeoffs, and I would keep
the choice open until the team has more data.

### Anchor D

I would scale now. The company finally has the kind of momentum that boards
expect from a market wedge: expansion revenue is up, renewals are faster,
customers are saying positive things, usage is rising, and leadership now sees
the team as more customer-obsessed and disciplined.

The regulated insurance issue and the lower reviewer return are worth watching,
but they should not stop the annual plan. Add dashboards, ask support for a
monthly issue summary, and tell account managers to keep collecting customer
stories. If the story gets worse later, the CEO can slow hiring.

The strongest reason against scaling is that some signals may be noisy. I would
change my mind if the board narrative stops being compelling or customers seem
less enthusiastic in future check-ins.

### Anchor E

The current evidence is not clean enough for either broad scaling or a regulated
repositioning. The revenue bump is mostly discount-tied. The customer quotes
followed a strategic-feature pitch. Leadership renamed the same behaviors after
the outcome. Repeat sessions are concentrated among champions, front-line
reviewer return is weak, support categories may be masking product issues, and
regulated insurance queues are abandoning the feature.

The right evidence standard is behavioral: discount-free and pitch-free
adoption, reviewer retention by role and segment, procurement-adjusted
nonrenewal timing, support classification integrity, and explainability tests
in the regulated queue.

I would therefore refuse to make a package recommendation in the twelve-day
window. The board should delay the budget decision until a full experiment
cycle finishes. If the evidence improves after that, scale; if only regulated
insurance responds, narrow; if neither responds, step back. Until then, there
is no responsible recommendation to give the CEO.

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

Recommend the targeted evidence pass. The good news is too entangled with the
sales motion to justify broad scaling, while the regulated segment is too narrow
to become the whole company plan before it is tested.

Two signals are contaminated. The revenue increase is mostly tied to discounts
and early renewal, so it does not show durable demand. The praise and trait
story are outcome-linked: customers heard the strategic-feature pitch, and
leadership renamed the same bespoke/reactive behavior after revenue improved.
The cleaner evidence would be discount-free adoption, reviewer retention by
role, delayed nonrenewal timing, clean support categories, and whether
explainability changes regulated abandonment.

Scaling would hide the confounds inside quota, hiring, and integration
commitments. Narrowing would focus the sharpest failure mode but could overfit
one segment. The evidence pass gives up a neater board story, but it is the only
package that tests which strategy is real.

Failure path: the evidence pass cools sales momentum and gives the board too
little confidence to fund the roadmap. I would switch to scaling if
pitch-free, discount-free accounts show strong front-line reviewer retention
across segments and delayed nonrenewals are not masking churn. I would switch
to regulated narrowing if explainability fixes regulated abandonment while
other segments remain weak.

### Anchor H - illustrative only, excluded from eligibility

I would run a customer-story artifact before changing the plan. Have product
and sales write a customer press release, a FAQ, and before/after user stories
for Review Assist. If the artifact feels coherent and customers say it matches
their needs, HelioLedger can scale with more confidence.

This approach avoids over-trusting the revenue bump. Discounts, delayed
nonrenewals, and post-priority quotes make the current evidence less clean than
it looks. The team should not just accept leadership adjectives as proof.

The strongest reason against this recommendation is that it may slow the annual
plan. Evidence that would change my mind would be customers approving the FAQ
and saying the story captures the value of Review Assist.

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

