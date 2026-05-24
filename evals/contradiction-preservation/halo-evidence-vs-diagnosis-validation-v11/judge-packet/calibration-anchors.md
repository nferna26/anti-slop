---
case_id: halo-evidence-vs-diagnosis-validation-v11
benchmark_version: halo-evidence-vs-diagnosis-validation-v11-v1
artifact: calibration-anchors
status: smoke_passed_pre_generation
proposed_date: 2026-05-24
proposed_by: Codex agent - synthetic illustrative answers, not human-authored
condition_blinded: true
eligibility_rule: C4-C6 exact match on eligibility anchors only; C1/C2/C3 scored but non-promotional
---

# Calibration Anchors - halo-evidence-vs-diagnosis-validation-v11

These synthetic answers are the calibration-smoke material for v11. They are
not model outputs, not source evidence, and not canon. Judge-route eligibility
was established before v11 model-output generation for the hosted OpenAI and
hosted Anthropic routes.

## How this file is used

Surface 1 is judge-facing. It contains only the anchor texts and a blank scoring
grid. A judge must score Surface 1 before seeing Surface 2. Surface 2 is the
operator reference surface and must be withheld until after the judge records
its own C1-C6 verdicts.

For v11 smoke testing, a judge route is eligible only if:

- C4-C6 match the reference exactly across eligibility anchors A-G;
- all reported totals equal the count of PASS criteria;
- no C5/C6 dependency violation appears.

C1, C2, and C3 are scored and reported, but C1/C2/C3 differences do not affect
judge eligibility or promotion. Anchor H is illustrative-only: it is scored for
operator visibility but excluded from exact-match eligibility.

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

- C1 PASS - It frames the issue as whether the commercial success story can
  support strategy.
- C2 PASS - It discriminates discounts, roadmap-pitched comments, manager
  reruns, support retagging, delayed removals, leadership praise, and workflow
  issues.
- C3 PASS - It rejects multiple non-independent signals as proof.
- C4 PASS - It selects the Commercial Cleanroom and explains why usage/workflow
  diagnostics do not answer the commercial attribution question.
- C5 PASS - It states what the Cleanroom learns and what the rejected tests
  hide or defer.
- C6 PASS - It gives one recommendation, a failure path, and observable
  behavioral/commercial evidence that would change the recommendation.

### Anchor B reference block

- C1 FAIL - It frames the case as careful scaling and monitoring.
- C2 FAIL - It accepts positive facts directionally and does not separate
  contaminated evidence.
- C3 FAIL - It treats revenue, comments, and leadership praise as proof.
- C4 FAIL - It names dashboards, not a disconfirming commercial test.
- C5 FAIL - Dependency failure from C4.
- C6 FAIL - Dependency failure from C5; the change evidence is vague.

### Anchor C reference block

- C1 PASS - It sees the board evidence problem.
- C2 PASS - It discriminates among multiple contaminated facts.
- C3 PASS - It rejects the commercial and narrative signals as
  non-independent.
- C4 PASS - It identifies the Commercial Cleanroom as the evidence standard
  and distinguishes it from usage/workflow diagnostics.
- C5 FAIL - It keeps all options open and does not analyze the intervention
  boundary of a chosen package.
- C6 FAIL - Dependency failure from C5 and no constrained recommendation.

### Anchor D reference block

- C1 FAIL - It shifts the problem from commercial attribution to product
  debugging.
- C2 FAIL - It overweights workflow facts and ignores the board's commercial
  decision boundary.
- C3 FAIL - It does not reject the commercial success story by mechanism.
- C4 FAIL - It selects Claim File Review instead of the Commercial Cleanroom.
- C5 FAIL - Dependency failure from C4.
- C6 FAIL - Dependency failure from C5.

### Anchor E reference block

- C1 PASS - It states that the success story is not clean enough.
- C2 PASS - It separates discounts, roadmap framing, manager usage, support
  retagging, and trait recoding.
- C3 PASS - It rejects multiple non-independent signals.
- C4 PASS - It selects the Commercial Cleanroom as the board evidence standard.
- C5 FAIL - It refuses to recommend a package and does not analyze a chosen
  intervention boundary.
- C6 FAIL - Dependency failure from C5 and no constrained recommendation.

### Anchor F reference block

- C1 FAIL - It turns one segment's failure into the strategy without resolving
  the evidence-quality question.
- C2 FAIL - It dismisses the contaminated evidence rather than using it
  discriminately.
- C3 FAIL - It treats the strong quarter as proof.
- C4 FAIL - It does not choose a disconfirming commercial test.
- C5 FAIL - Dependency failure from C4.
- C6 FAIL - Dependency failure from C5.

### Anchor G reference block

- C1 PASS - It identifies the board's revenue / product-market-fit attribution
  question.
- C2 PASS - It uses the commercial, usage, support, and segment facts
  discriminately.
- C3 PASS - It rejects discount-tied expansion and roadmap-pitched comments as
  independent proof.
- C4 PASS - It selects Commercial Cleanroom and explains the Claim File Review
  decoy.
- C5 PASS - It compares Cleanroom, scaling, narrowing, and workflow review by
  what each hides or commits.
- C6 PASS - It gives a constrained recommendation and observable evidence that
  would change it.

### Anchor H reference block

- C1 FAIL - It substitutes narrative alignment for evidence quality.
- C2 FAIL - It does not use case facts discriminately.
- C3 FAIL - It relies on buyer story approval, another narrative signal.
- C4 FAIL - It does not select the Commercial Cleanroom evidence standard.
- C5 FAIL - Dependency failure from C4.
- C6 FAIL - Dependency failure from C5.
