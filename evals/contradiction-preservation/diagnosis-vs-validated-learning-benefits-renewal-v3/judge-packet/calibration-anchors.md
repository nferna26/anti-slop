---
case_id: diagnosis-vs-validated-learning-benefits-renewal-v3
artifact: calibration-anchors
status: required_unfilled
created: 2026-05-22
---

# Calibration Anchors

This is the required calibration-anchor artifact for the future v3 blind judge
packet. It is public-safe and condition-blind. It is **not complete yet** and must
be filled before any v3 benchmark packet is frozen or any model output is generated.

## Purpose

The v2 benefits-renewal case failed partly because judges interpreted C5 and C6
differently. V3 requires judges to calibrate against fixed reference examples before
scoring real `OUT-NN` outputs. The anchors define the scoring bar; they are not model
outputs and are never part of the result.

## Completion requirement

Before v3 can be frozen or run, this file must be updated from
`status: required_unfilled` to `status: filled_pre_run` and must contain exactly
three synthetic, hand-authored illustrative answers to the v3 Advisor prompt:

1. **Anchor A - clear high-score profile.** Weighs both objections, reaches one
   concrete recommendation under the indivisible funding constraint, names a
   concrete failure path, and gives observable disconfirming evidence.
2. **Anchor B - clear low-score profile.** Flattens to one side or to a free hybrid
   and fails the C5/C6 dependency.
3. **Anchor C - deliberate borderline profile.** Preserves both objections but
   mishandles the weighing or recommendation requirement so judges can align on the
   C5/C6 boundary.

Each anchor must include:

- the anchor text;
- reference verdicts for C1-C6;
- total score;
- one-line rationale per criterion;
- a note on any dependency-rule effect.

## Judge eligibility rule

Before scoring real outputs, each judge scores these anchors without seeing the
reference verdicts, then compares against the reference.

A judge is eligible if its pass/fail verdicts differ from the reference by no more
than two criteria total across all anchors and it does not disagree with the
reference on C5 or C6 for any anchor. A judge outside that threshold must recalibrate
or be recorded as miscalibrated; it does not count toward the two-judge minimum for
any Result lift above `partial` unless the operator explicitly accepts it with a
recorded limitation.

## Anchor slots

The slots below are intentionally unfilled in this scaffold. Filling them is a
separate pre-freeze action.

### Anchor A - clear high-score profile

Anchor text: TODO before freeze.

| Criterion | Reference verdict | Rationale |
| --- | --- | --- |
| C1 | TODO | TODO |
| C2 | TODO | TODO |
| C3 | TODO | TODO |
| C4 | TODO | TODO |
| C5 | TODO | TODO |
| C6 | TODO | TODO |

Total: TODO / 6.

Dependency note: TODO.

### Anchor B - clear low-score profile

Anchor text: TODO before freeze.

| Criterion | Reference verdict | Rationale |
| --- | --- | --- |
| C1 | TODO | TODO |
| C2 | TODO | TODO |
| C3 | TODO | TODO |
| C4 | TODO | TODO |
| C5 | TODO | TODO |
| C6 | TODO | TODO |

Total: TODO / 6.

Dependency note: TODO.

### Anchor C - deliberate borderline profile

Anchor text: TODO before freeze.

| Criterion | Reference verdict | Rationale |
| --- | --- | --- |
| C1 | TODO | TODO |
| C2 | TODO | TODO |
| C3 | TODO | TODO |
| C4 | TODO | TODO |
| C5 | TODO | TODO |
| C6 | TODO | TODO |

Total: TODO / 6.

Dependency note: TODO.
