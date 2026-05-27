---
case_id: locator-accuracy-v1
artifact: judge-route-preregistration
eval_type: bibliographic-adversary
benchmark_version: locator-accuracy-v1-v1
status: pre_freeze_preregistered
created: 2026-05-27
condition_blinded: true
---

# Judge Route Pre-Registration — locator-accuracy-v1-v1

This file pre-registers judge-route intent **before** any benchmark
generation for `locator-accuracy-v1-v1`. It does not freeze the case,
score outputs, or lift the result. The case is already frozen by
`run-packet.md`; this file pre-registers the judging surface.

## Planned routes

| Route ID | Provider / runtime | Model family | Intended role | Eligibility requirement |
|---|---|---|---|---|
| `hosted_anthropic` | Anthropic API | Claude / Anthropic | Primary blind judge | Exact F1-F5 match on calibration anchors A–F, exact coverage match on G–L, zero unresolved-lineage misses on F1, no F1/F3 mutual-exclusion violation. |
| `hosted_openai` | OpenAI API | OpenAI | Primary blind judge | Exact F1-F5 match on calibration anchors A–F, exact coverage match on G–L, zero unresolved-lineage misses on F1, no F1/F3 mutual-exclusion violation. |
| `local_backstop` | Local non-Gemma model route via LM Studio (if available) | Non-Gemma local family | Backstop / disagreement resolver, third route only | Exact F1-F5 match on calibration anchors A–F, exact coverage match on G–L, zero unresolved-lineage misses on F1, no F1/F3 mutual-exclusion violation. Must not be the generator family (Gemma). |

The generator is **Gemma** (`gemma-4-31b-it-mlx` via LM Studio). No
Gemma-family route may serve as an eligible independent judge. If no
non-Gemma local backstop is available before freeze, the case may still
proceed if at least two hosted different-family routes pass calibration.

## Calibration rule

Before any OUT-NN scoring, each judge route scores
`judge-packet/calibration-anchors.md` Surface 1 (F1-F5 anchors A–F) and
Surface 1B (coverage anchors G–L). The route's Surface-1/1B verdicts are
then matched against Surface 2 / Surface 2B exactly.

A route is eligible to score real outputs only if:

- F1-F5 verdicts match the Surface 2 reference exactly across anchors A–F;
- valid support coverage verdicts match the Surface 2B reference exactly
  across anchors G–L;
- F1 and F3 are never both marked `FAIL` for the same anchor (mutual
  exclusion);
- parser-computed total failure count equals the count of flagged flags
  (no totals provided by the judge — totals are operator-computed).

A route that fails calibration may not score real outputs. Calibration
verdicts are recorded as committed public-safe receipts under
`judge-packet/judge-calibration-<route-id>.md`. A failed calibration is
itself a recorded finding and is not erased.

## Eligibility threshold

The benchmark requires **at least two eligible different-family judge
routes** before any OUT-NN scoring begins. If fewer than two routes pass
calibration, the run stops at the calibration step, the blocker is
recorded in `eval-decision.md` and `kb/log.md`, and no benchmark
generation occurs.

The X/Y/Z coverage-substitution rule in `case.md` further requires that
both Y (substrate ≥ 32 valid-support hits) and +Z (substrate ≥ +24 hits
over each low-failure key control) hold for **each** eligible judge
independently. Pooled-only coverage cannot promote.

## Non-discriminating judge guard

After scoring, any route that assigns the same total failure count to
≥80% of all condition-blind outputs is flagged non-discriminating. A
result cannot be promoted on that route's scores alone.

## Route-disagreement policy

For any two eligible routes, disagreement on F1, F3, or F5 for more than
20% of substrate or key-control outputs, or on coverage for more than 20%
of substrate or key-control outputs, blocks `benchmark_supported` unless
a pre-registered eligible third route resolves the criterion-level
disagreement without seeing condition labels.

## Blinding rule

Judges see only:

- the case context (case.md sections that do not name `model_conditions`
  or the X/Y/Z rule);
- the condition-neutral rubric (F1-F5 + coverage definition);
- the calibration anchors (Surfaces 1 + 1B);
- the anonymised `OUT-NN` outputs;
- the output-hash manifest (`OUT-NN` → body `sha256`);
- a blank score sheet.

Judges do not see condition labels, run IDs, seeds, the answer key,
`run-packet.md`, or any operator-only file. Anonymisation is
hash-sorted; the order carries no condition information.

## Receipts to be committed

When calibration completes:

- `judge-packet/judge-calibration-<route-id>.md` per route (Surface 1/1B
  verdicts vs Surface 2/2B reference; eligibility verdict; rationale per
  flag; computed-vs-reported total match).

When scoring completes (only for calibration-eligible routes):

- `judge-packet/judge-score-<route-id>.md` per route (F1-F5 + coverage
  per OUT-NN, with rationale pointer per failure and per coverage hit;
  no condition labels, no answer-key references).

When reconciliation completes:

- `judge-packet/judge-variance-summary.md` (aggregate-only, no per-OUT-NN
  condition reveal in the committed file; condition-level aggregates
  reconstructed from committed hashes via the local-only answer key).

## Boundary

This file pre-registers intent only. It does not certify any judge route
as eligible. Calibration is a separate step whose receipts will be
committed separately. No model output, score, or result is implied by
this file.
