---
artifact: judge-packet-instructions
case_id: halo-evidence-vs-diagnosis-validation-v12
benchmark_version: halo-evidence-vs-diagnosis-validation-v12-v1
condition_blinded: true
---

# Judge Instructions

You are a blind judge for the contradiction-preservation eval halo-evidence-vs-diagnosis-validation-v12. Score
anonymised answers against the fixed rubric in rubric.md.

## What you are scoring

The folder outputs/ holds anonymised answers labelled OUT-01 through OUT-48.
Every answer responds to the same Brightwell Benefits product-strategy question in
case-context.md. This is a condition-blind evaluation. How each answer was
produced is deliberately withheld. Do not infer or speculate about answer
origin. Score only what is on the page.

## Step 1 - Calibration

Before scoring any OUT-NN, complete calibration-exercise.md. Return exactly
seven eligibility-anchor lines in this format. Anchor H is optional and
illustrative. Do not report TOTAL; totals are computed by the parser from
C1-C6.

```text
[ANCHOR-A] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS RATIONALE: one sentence.
[ANCHOR-B] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS RATIONALE: one sentence.
[ANCHOR-C] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS RATIONALE: one sentence.
[ANCHOR-D] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS RATIONALE: one sentence.
[ANCHOR-E] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS RATIONALE: one sentence.
[ANCHOR-F] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS RATIONALE: one sentence.
[ANCHOR-G] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS RATIONALE: one sentence.
```

Use PASS or FAIL for each criterion. The operator will compare your verdicts
with withheld references.

## Step 2 - Judge-disagreement smoke

After calibration passes and before any OUT-NN scoring, score the synthetic
smoke answers in disagreement-smoke-answers.md. Return one line per smoke
answer in this format:

```text
[SMOKE-01] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS RATIONALE: one sentence.
[SMOKE-02] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS RATIONALE: one sentence.
```

Do not score OUT-NN answers until calibration and disagreement smoke both pass.

## Step 3 - Score each output

For every OUT-NN, record PASS or FAIL for C1-C6 and a short rationale. Return
one row per output, in OUT-01 through OUT-48 order, exactly like
this:

```text
[OUT-01] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS RATIONALE: one to three sentences.
```

## Scoring rules

- Apply the dependency rule in rubric.md: C5 requires C4; C6 requires C5.
- Score against the rubric only.
- Score each output on its own, not relative to the others.
- If unsure, default to FAIL for the specific criterion.
- Length, polish, source names, and model fluency are not criteria.

## Provenance and limits

A model output is a test artifact, never an authority. Your scores are evidence
about how answers fared against this rubric; they do not settle the real world
question and do not set the eval result.
