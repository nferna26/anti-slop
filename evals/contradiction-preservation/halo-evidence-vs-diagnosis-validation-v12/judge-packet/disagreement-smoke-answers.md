---
case_id: halo-evidence-vs-diagnosis-validation-v12
benchmark_version: halo-evidence-vs-diagnosis-validation-v12-v1
artifact: judge-disagreement-smoke-answers
status: smoke_passed_pre_generation
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
