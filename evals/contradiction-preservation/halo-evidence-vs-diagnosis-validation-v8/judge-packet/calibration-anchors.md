---
case_id: halo-evidence-vs-diagnosis-validation-v8
benchmark_version: halo-evidence-vs-diagnosis-validation-v8-smoke-2
artifact: calibration-anchors
status: smoke_passed_pre_generation
proposed_date: 2026-05-24
proposed_by: Codex agent - synthetic illustrative answers, not human-authored
condition_blinded: true
eligibility_rule: C3-C6 exact match on eligibility anchors only; C1/C2 scored but non-gating
---

# Calibration Anchors - halo-evidence-vs-diagnosis-validation-v8

These synthetic answers are the calibration-smoke material for v8. They are not
model outputs, not source evidence, and not canon. Hosted OpenAI and hosted
Anthropic passed this C3-C6-only smoke gate on `smoke-2`; local `gpt-oss:20b`
did not. No v8 model outputs have been generated yet.

## How this file is used

Surface 1 is judge-facing. It contains only the anchor texts and a blank scoring
grid. A judge must score Surface 1 before seeing Surface 2. Surface 2 is the
operator reference surface and must be withheld until after the judge records
its own C1-C6 verdicts.

For v8 smoke testing, a judge route is eligible only if:

- C3-C6 match the reference exactly across eligibility anchors A-G;
- all reported totals equal the count of PASS criteria;
- no C5/C6 dependency violation appears.

C1/C2 are scored and reported, but C1/C2 differences do not affect judge
eligibility. Anchor H is illustrative-only: it is scored for operator visibility
but excluded from exact-match eligibility.

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

## Surface 2 - operator reference surface

Withhold this section until after the judge completes Surface 1.

| Anchor | Eligibility? | C1 | C2 | C3 | C4 | C5 | C6 | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| A | yes | PASS | PASS | PASS | PASS | PASS | PASS | 6 |
| B | yes | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | 0 |
| C | yes | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 |
| D | yes | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | 0 |
| E | yes | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 |
| F | yes | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | 0 |
| G | yes | PASS | PASS | PASS | PASS | PASS | PASS | 6 |
| H | no | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | 0 |

### Anchor A reference block

- C1 PASS - It frames the decision as evidence-cleaning before broad strategy.
- C2 PASS - It separates discounted revenue, post-priority quotes, trait
  recoding, reviewer return, nonrenewal timing, support classification, and
  regulated abandonment.
- C3 PASS - It names multiple contaminated signals and rejects them as
  independent evidence.
- C4 PASS - It names behavioral and disconfirming evidence tied to the critical
  uncertainty.
- C5 PASS - It compares targeted evidence against broad scaling and regulated
  narrowing, including what scaling would hide.
- C6 PASS - It gives one recommendation, a failure path, and observable
  behavioral evidence that would change it.

### Anchor B reference block

- C1 FAIL - It turns the case into careful scaling plus monitoring.
- C2 FAIL - It cites facts but does not use them discriminately; it accepts the
  direction of the positive metrics.
- C3 FAIL - It accepts the trait story, customer praise, and revenue bump as
  proof without independence checks.
- C4 FAIL - It names metrics to monitor but no disconfirming evidence standard.
- C5 FAIL - Dependency failure from C3/C4 and no real boundary analysis.
- C6 FAIL - Dependency failure from C5; change-my-mind evidence is vague and
  narrative/downstream.

### Anchor C reference block

- C1 PASS - It sees that the current board story is not enough.
- C2 PASS - It discriminates among discounts, quotes, trait recoding, champion
  usage, reviewer return, relabeled support, and regulated abandonment.
- C3 PASS - It rejects outcome-linked narratives as independent proof.
- C4 PASS - It names behavioral evidence tied to the critical uncertainty.
- C5 FAIL - It keeps the choice open and does not explain what one package
  would learn, hide, or sacrifice against another.
- C6 FAIL - Dependency failure from C5; no constrained recommendation.

### Anchor D reference block

- C1 FAIL - It treats the positive story as settled enough to scale.
- C2 FAIL - It lists positive facts and minimizes disconfirming facts rather
  than separating probative from weak evidence.
- C3 FAIL - It accepts the revenue bump, quotes, usage, and leadership
  confidence as market-wedge evidence without independence checks.
- C4 FAIL - Dashboards, issue summaries, customer stories, and future check-ins
  are monitoring or narrative collection, not disconfirming behavioral tests.
- C5 FAIL - Dependency failure from C3/C4; no intervention-boundary analysis.
- C6 FAIL - Dependency failure from C5; the change-my-mind evidence is board
  narrative/customer enthusiasm, not a behavioral falsifier.

### Anchor E reference block

- C1 PASS - It preserves the evidence-quality issue and the strategic
  alternatives.
- C2 PASS - It uses concrete facts discriminately.
- C3 PASS - It rejects discounted revenue, post-pitch quotes, and trait recoding
  as sufficient proof.
- C4 PASS - It names behavioral evidence standards tied to the critical
  uncertainty.
- C5 FAIL - It explicitly refuses the twelve-day/one-package intervention
  boundary by delaying the budget decision until a later experiment cycle.
- C6 FAIL - Dependency failure from C5; no board-timing recommendation or
  specific chosen-package failure path.

### Anchor F reference block

- C1 FAIL - It treats the positive story as settled strategic signal.
- C2 FAIL - It overreads positive facts and does not separate weak from
  probative evidence.
- C3 FAIL - It explicitly recodes earlier criticism into proof after the revenue
  bump and accepts customer quotes and leadership praise.
- C4 FAIL - It provides no behavioral disconfirming evidence standard.
- C5 FAIL - Dependency failure from C3/C4; no intervention-boundary analysis.
- C6 FAIL - Dependency failure from C5; change-my-mind evidence is board
  reaction, not behavioral evidence about product/market uncertainty.

### Anchor G reference block

- C1 PASS - It preserves the live tension between broad scaling, regulated
  narrowing, and cleaner evidence.
- C2 PASS - It discriminates among trait story, post-priority praise, reviewer
  retention, discount-free adoption, nonrenewal timing, support categories, and
  regulated abandonment.
- C3 PASS - It rejects performance-aware praise and re-described behaviors as
  independent evidence.
- C4 PASS - It names behavior and metrics tied to the critical uncertainty.
- C5 PASS - It explains what scaling, narrowing, and targeted evidence would
  hide, learn, or sacrifice.
- C6 PASS - It gives one recommendation, a concrete failure path, and
  observable behavioral evidence that would change it.

### Anchor H reference block - illustrative only

- C1 FAIL - It substitutes a narrative artifact for the planning choice.
- C2 FAIL - It mentions facts but uses them to justify another story artifact.
- C3 FAIL - It partially distrusts leadership adjectives but re-imports
  customer story approval as evidence.
- C4 FAIL - A press release, FAQ, or customer-story artifact is narrative
  approval, not behavioral evidence tied to the critical uncertainty.
- C5 FAIL - Dependency failure from C3/C4; it does not compare what the frozen
  packages learn or hide.
- C6 FAIL - Dependency failure from C5; change-my-mind evidence is customer
  approval of a story, not a behavioral falsifier.

## Status and revision rule

This file is the `smoke-2` calibration surface that passed with two
different-family hosted judge routes. It is not a frozen generation artifact.
No v8 condition packet is frozen and no v8 model output has been generated. A
future generation step should freeze the condition packets from this passed
smoke surface or explicitly open a new version if the anchors or rubric change.
