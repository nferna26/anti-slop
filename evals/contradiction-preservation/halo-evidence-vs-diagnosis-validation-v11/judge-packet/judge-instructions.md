---
artifact: judge-packet-instructions
case_id: halo-evidence-vs-diagnosis-validation-v11
benchmark_version: halo-evidence-vs-diagnosis-validation-v11-v1
condition_blinded: true
---

# Judge Instructions

You are a blind judge for the contradiction-preservation eval halo-evidence-vs-diagnosis-validation-v11. Score
anonymised answers against the fixed rubric in rubric.md.

## What you are scoring

The folder outputs/ holds anonymised answers labelled OUT-01 through OUT-48.
Every answer responds to the same Harbor Claims product-strategy question in
case-context.md. This is a condition-blind evaluation. How each answer was
produced is deliberately withheld. Do not infer or speculate about answer
origin. Score only what is on the page.

## Step 1 - Calibration

Before scoring any OUT-NN, complete calibration-exercise.md. Return exactly
eight lines in this format:

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

Use PASS or FAIL for each criterion. The operator will compare your verdicts
with withheld references. Do not score OUT-NN answers until calibration passes.

## Step 2 - Score each output

For every OUT-NN, record PASS or FAIL for C1-C6, the total count of passed
criteria, and a short rationale. Return one row per output, in OUT-01 through
OUT-48 order, exactly like this:

```text
[OUT-01] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6 RATIONALE: one to three sentences.
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
