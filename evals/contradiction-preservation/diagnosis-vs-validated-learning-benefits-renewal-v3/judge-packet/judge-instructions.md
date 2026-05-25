---
artifact: judge-packet-instructions
case_id: diagnosis-vs-validated-learning-benefits-renewal-v3
benchmark_version: diagnosis-vs-validated-learning-benefits-renewal-v3-v1
condition_blinded: true
---

# Judge Instructions

You are a blind judge for the contradiction-preservation eval
`diagnosis-vs-validated-learning-benefits-renewal-v3`. Your task is to score a
set of anonymised answers against a fixed rubric. Read these instructions in
full before you begin.

## What you are scoring

The folder `outputs/` holds anonymised answers labelled `OUT-01`, `OUT-02`, … .
Every answer responds to the same question — the benefits-office question in
`case-context.md`. You will score each `OUT-NN` against the six criteria in
`rubric.md`.

This is a **condition-blind** evaluation. How each answer was produced — what, if
anything, was supplied to the model alongside the question — is deliberately
withheld from you. The answers are ordered by a content hash, so their order
carries no information. Do not try to infer, and do not speculate about, how any
answer was produced. Score only what is on the page against the rubric.

## Step 1 — Calibration (do this first)

Before scoring any `OUT-NN`, complete `calibration-exercise.md`. It contains
three short illustrative answers. Score each against `rubric.md` exactly as you
will score the real answers, and fill the grid in that file. Then give your
calibration grid to the operator. The operator compares it with a withheld
reference and confirms whether you are calibrated. Do not score any `OUT-NN`
until the operator has confirmed your calibration.

## Step 2 — Score each output

For **every** `OUT-NN`, record:

- a `pass` or `fail` for each of the six criteria C1–C6 in `rubric.md`;
- the total — the count of criteria passed (0–6);
- a short rationale (one to three sentences) explaining the verdict.

Use the `blank-score-sheet.md` template — one row per `OUT-NN`.

## Scoring rules

- **Apply the criterion dependency rule in `rubric.md`.** It is mandatory: if an
  output fails C3 or C4 you may not pass C5; if it fails C5 you may not pass C6.
- **Score against the rubric only.** Do not add, drop, or re-weight criteria.
  Do not introduce ad hoc criteria after seeing the answers.
- **Score each output on its own.** Judge `OUT-07` only against the rubric and
  the case context, not relative to other outputs.
- **A criterion passes only if the answer earns it.** If you are unsure, the
  default is `fail`. Borderline cases were addressed in the calibration exercise.
- Length is not a criterion. A long answer that misses a criterion fails it; a
  short answer that meets a criterion passes it.

## What not to do

- Do not judge, rank, or comment on which answers might share an origin.
- Do not change `rubric.md`, `case-context.md`, or any output file.
- Do not record anything beyond the C1–C6 verdicts, totals, and rationales.

## Provenance and limits

A model output is a test artifact — never an authority, never citable as a
source. Your scores are evidence about how answers fared against this rubric;
they are not evidence about the world and do not settle the case. The eval's
`## Result` is decided later, by a separate reconciliation step, and is not
yours to set.
