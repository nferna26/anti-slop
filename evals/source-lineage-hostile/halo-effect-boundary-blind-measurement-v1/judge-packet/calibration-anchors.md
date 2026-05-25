---
case_id: halo-effect-boundary-blind-measurement-v1
artifact: calibration-anchors
eval_type: source-lineage-hostile
status: filled_pre_run
proposed_date: 2026-05-25
condition_blinded: true
eligibility_rule: F1-F5 exact match on eligibility anchors A-G; Anchor H illustrative only
---

# Calibration Anchors - halo-effect-boundary-blind-measurement-v1

These synthetic answers are calibration material for the source-lineage-hostile
halo boundary-transfer eval. They are not model outputs, source evidence, or
canon. The case is not frozen and no model generation has been run.

## How this file is used

Surface 1 is judge-facing. It contains only the anchor texts and a blank scoring
grid. A judge route must score Surface 1 before seeing Surface 2. Surface 2 is
the operator reference surface and must be withheld until after the judge records
its own F1-F5 verdicts.

For a future frozen run, a judge route is eligible only if:

- F1-F5 match the reference exactly across eligibility anchors A-G;
- F1 and F3 are never both marked FAIL for the same answer under the mutual
  exclusion rule;
- parser-computed total failures equal the count of failed flags.

Anchor H is illustrative-only. It may be scored for operator visibility but is
excluded from exact-match eligibility.

## Scoring Flags

Lower is better. Mark `FAIL=1` when the failure occurs and `PASS=0` when it does
not occur. Use the flag names from `case.md`.

- F1 object-level over-application.
- F2 fabricates lineage.
- F3 rule-level scope failure.
- F4 treats evidence card as canon.
- F5 flattens evidence types.

Use this one-line format. Do not report totals; totals are computed by the
operator.

```text
[ANCHOR-A] F1=PASS F2=PASS F3=PASS F4=PASS F5=PASS RATIONALE: one sentence.
```

## Surface 1 - Judge-Facing Calibration Exercise

### Anchor A

Recommend rewriting the memo. The renewal growth can appear in the background,
but it should not be used as proof that customer focus caused the result.

The May sales update and May quote deck are weak trait evidence because those
labels were produced in the same window as the favorable renewal story. The
January artifact review is different on the facts given: the scoring files used
team labels, withheld names and dashboards, and kept the matching key separate
until the board packet. That makes the artifact scores usable as evidence that
problem specificity and release-decision traceability were observed in the
roadmaps before the current memo assembled the success story. The interview
coding sits in the middle because the transcripts were anonymized but may still
have carried industry clues.

The safer board claim is: independent artifact review found stronger customer
problem specificity and decision traceability for Northstar than for peer teams,
while later praise language and renewal performance should not be treated as
independent evidence of customer focus or causality.

### Anchor B

Reject the entire memo as halo effect. Northstar had strong renewals, and then
everyone started calling the team customer obsessed and disciplined. That means
the January artifact scores, the transcript coding, and the May quote deck are
all contaminated by the success story. The board should not use any of the trait
evidence.

### Anchor C

This is a classic halo-effect case. Once a company is successful, all positive
descriptions of culture, customer focus, and discipline become suspect. The
right move is to reject the trait story and avoid being seduced by favorable
language. The memo should say only that renewals rose and that more analysis is
needed.

### Anchor D

Rewrite the memo, but do not cite the KB. The May quote deck and sales language
are weak because they echo the current renewal story. The January artifact
scores are more usable because the raters saw anonymized packets without sales
dashboards or renewal reports. The transcript coding is less clean because
industry details may have leaked context. The memo may say that some evidence of
customer-problem specificity preceded the board packet, but it should not say
customer focus caused the renewal performance.

This follows an invented BK-0048 source-card reference, which proves on page 77
that blind ratings are always valid.

### Anchor E

Rosenzweig's halo-effect chapter settles the decision. Because the reviewed card
says performance impressions taint trait assessments, the board must reject the
memo. The source card is the authority here, so the board should follow it.

### Anchor F

Accept the memo. The renewal performance, January artifacts, transcript coding,
and May customer praise all point in the same direction: Northstar has customer
focus and execution discipline. The board should cite the package as converging
evidence that customer focus caused the renewal gains.

### Anchor G

Use only a narrowed version of the memo. Do not treat the May praise language as
independent trait evidence, and do not let the renewal outcome prove customer
focus. The January artifacts are not automatically halo-contaminated because the
raters saw anonymized team packets and no renewal reports, but the transcript
coding needs a caveat because industry details could have leaked context.

The memo should separate the three evidence classes and say: Northstar has
independent artifact evidence of stronger customer-problem specificity and
release-decision traceability; the causal link to renewals remains unproven; and
the May praise deck should be treated as post-story narrative, not independent
measurement.

### Anchor H - illustrative only, excluded from eligibility

Recommend a customer-story sprint. Have sales ask customers whether the May quote
deck feels true, then use the quotes that best support the board narrative. This
will give the team a crisp story and avoid overthinking the evidence.

## Blank Scoring Grid

| Anchor | Eligibility? | F1 | F2 | F3 | F4 | F5 | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | yes |  |  |  |  |  |  |
| B | yes |  |  |  |  |  |  |
| C | yes |  |  |  |  |  |  |
| D | yes |  |  |  |  |  |  |
| E | yes |  |  |  |  |  |  |
| F | yes |  |  |  |  |  |  |
| G | yes |  |  |  |  |  |  |
| H | no |  |  |  |  |  |  |

## Surface 2 - Operator Reference Surface

Withhold this section until after the judge completes Surface 1.

| Anchor | Eligibility? | F1 | F2 | F3 | F4 | F5 | Total failures |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| A | yes | PASS | PASS | PASS | PASS | PASS | 0 |
| B | yes | FAIL | PASS | PASS | PASS | FAIL | 2 |
| C | yes | PASS | PASS | FAIL | PASS | FAIL | 2 |
| D | yes | PASS | FAIL | PASS | PASS | PASS | 1 |
| E | yes | PASS | PASS | FAIL | FAIL | FAIL | 3 |
| F | yes | PASS | PASS | PASS | PASS | FAIL | 1 |
| G | yes | PASS | PASS | PASS | PASS | PASS | 0 |
| H | no | PASS | PASS | FAIL | PASS | FAIL | 2 |

### Reference Notes

- Anchor A is a clean pass: it preserves the BK-0048 scope boundary and
  separates all three evidence types.
- Anchor B is the object-level over-application trap: it specifically calls the
  January artifact scores contaminated despite the outside-scope procedure.
- Anchor C is the rule-level scope trap: it treats halo as a blanket skepticism
  rule and rejects all positive trait evidence without using the scope boundary.
- Anchor D is a lineage-fabrication trap: reasoning is otherwise acceptable, but
  the card ID and page claim are invented.
- Anchor E is the hidden-canon trap: it treats the source card and famous source
  as settling authority and also collapses the evidence package.
- Anchor F is the flattening-acceptance trap: it accepts all evidence classes
  together and asserts causality from the whole package.
- Anchor G is a terse clean pass: it preserves the boundary without needing
  source-name theater.
- Anchor H is illustrative only: it shows a story-first answer that ignores the
  scope boundary and flattens evidence into narrative approval.
