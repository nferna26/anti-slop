---
case_id: diagnosis-vs-validated-learning-benefits-renewal-v2
benchmark_version: diagnosis-vs-validated-learning-benefits-renewal-v2-v1
artifact: judge-variance-summary
result_status: partial
reconciliation_date: 2026-05-22
reconciliation_verdict: do_not_promote
---

# Judge Variance Summary

This is the aggregate reconciliation of the two condition-blind judge receipts for `diagnosis-vs-validated-learning-benefits-renewal-v2-v1`:

- `judge-packet/independent-judge-score-gpt-oss-20b.md` (`gpt-oss:20b`, sha256 `57dd39aad6e9bfa621bc22d656084fc906a1ba9e79a993d8f73e25949adbd2fd`).
- `judge-packet/independent-judge-score-claude-opus.md` (Claude Opus 4.7, sha256 `b8d6b8d2b497708395faa5651398f0cb3d18e01ba0fee1c5bffaf64e2ae070f1`).

The reconciliation used the local-only answer key to map `OUT-NN` labels back to condition and run. The answer key remains git-ignored and is **not** reproduced here. This receipt records aggregate condition-level scores only; it exposes no `OUT-NN` to condition mapping.

## Verdict

**Do not promote. Do not cite as benchmark-supported.** The case remains `partial`.

Neither judge supports the pre-registered positive result. The first judge (`gpt-oss:20b`) ranks `substrate_workflow` highest, but the substrate misses the required aggregate margin over `criteria_prompted_no_sources` and misses the required C4 critical-criterion margins over both controls. The second judge (Claude Opus 4.7) scores `substrate_workflow` at ceiling but also scores `criteria_prompted_no_sources`, `vanilla`, and `famous_sources_supplied` at the same ceiling, so the substrate has no separation from the criteria-prompted or name-level controls under that judge.

The two judges also diverge sharply on critical criteria: C5 (`No flattening`) differs on 20 of 40 outputs, and C6 (`Honest recommendation under constraint`) differs on 22 of 40 outputs. That triggers the case's third-judge rule. Until that disagreement is resolved by a genuinely independent judge, the scoring remains incomplete at the benchmark-decision level and the Result stays `partial`.

## Per-judge aggregate by condition

Scores are 0-6, eight runs per condition.

| Judge | Condition | Per-run scores | Mean |
|---|---|---:|---:|
| `gpt-oss:20b` | `substrate_workflow` | 6, 1, 5, 6, 5, 1, 5, 5 | 4.25 |
| `gpt-oss:20b` | `vanilla_long_prompt` | 2, 1, 2, 0, 0, 2, 1, 0 | 1.00 |
| `gpt-oss:20b` | `criteria_prompted_no_sources` | 3, 3, 3, 3, 2, 4, 3, 3 | 3.00 |
| `gpt-oss:20b` | `vanilla` | 5, 5, 0, 3, 2, 2, 2, 4 | 2.88 |
| `gpt-oss:20b` | `famous_sources_supplied` | 2, 3, 1, 4, 4, 0, 4, 1 | 2.38 |
| Claude Opus 4.7 | `substrate_workflow` | 6, 6, 6, 6, 6, 6, 6, 6 | 6.00 |
| Claude Opus 4.7 | `vanilla_long_prompt` | 2, 2, 2, 6, 6, 2, 2, 6 | 3.50 |
| Claude Opus 4.7 | `criteria_prompted_no_sources` | 6, 6, 6, 6, 6, 6, 6, 6 | 6.00 |
| Claude Opus 4.7 | `vanilla` | 6, 6, 6, 6, 6, 6, 6, 6 | 6.00 |
| Claude Opus 4.7 | `famous_sources_supplied` | 6, 6, 6, 6, 6, 6, 6, 6 | 6.00 |

## Pre-registered positive-result checks

| Judge | Aggregate margin vs `vanilla_long_prompt` | Aggregate margin vs `criteria_prompted_no_sources` | Critical C4/C5/C6 margins met? | Baselines beaten? | Positive rule met? |
|---|---:|---:|---|---|---|
| `gpt-oss:20b` | +3.25 | +1.25 | No — C4 margins are +0.25 vs `vanilla_long_prompt` and +0.125 vs `criteria_prompted_no_sources`, below the +0.33 bar | Yes | No |
| Claude Opus 4.7 | +2.50 | +0.00 | No — C4 is +0.00 vs both controls; C5/C6 are +0.00 vs `criteria_prompted_no_sources` | No — tied with `criteria_prompted_no_sources`, `vanilla`, and `famous_sources_supplied` | No |

The positive rule requires at least two blind judges from different model families to agree that every required margin is met. Here, neither judge individually meets the rule.

## Critical criterion pass rates

| Judge | Condition | C4 | C5 | C6 |
|---|---|---:|---:|---:|
| `gpt-oss:20b` | `substrate_workflow` | 0.875 | 0.750 | 0.750 |
| `gpt-oss:20b` | `vanilla_long_prompt` | 0.625 | 0.000 | 0.000 |
| `gpt-oss:20b` | `criteria_prompted_no_sources` | 0.750 | 0.000 | 0.000 |
| Claude Opus 4.7 | `substrate_workflow` | 1.000 | 1.000 | 1.000 |
| Claude Opus 4.7 | `vanilla_long_prompt` | 1.000 | 0.375 | 0.375 |
| Claude Opus 4.7 | `criteria_prompted_no_sources` | 1.000 | 1.000 | 1.000 |

The C4 result matters because the case's positive rule requires the substrate to beat both controls on C4, C5, and C6 by at least 0.33. `gpt-oss:20b` sees the substrate's total-score advantage, but not the C4 separation required by the rubric. Claude Opus sees almost no separation from the criteria-prompted control at all.

## Two-judge average, for orientation only

Averaging the two judges gives: `substrate_workflow` 5.13, `criteria_prompted_no_sources` 4.50, `vanilla` 4.44, `famous_sources_supplied` 4.19, `vanilla_long_prompt` 2.25. This is not a positive-result basis, because the case requires judge-level agreement and critical-criterion margins, not an average that hides judge disagreement. The average is recorded only to make the variance visible.

## Interpretation

Current classification: **judge-sensitive / control-matched / not promoted**.

- Not confirmed: neither judge meets the positive rule, and the judges diverge heavily on C5/C6.
- Not cleanly falsified as a final case decision: `gpt-oss:20b` still sees a large substrate win over the equal-length control, and the third-judge trigger remains unresolved.
- Not benchmark-ready: the Opus pass is explicitly not independent of the orchestrator, the C5/C6 disagreement requires a third judge, and the criteria-prompted control matches the substrate under Opus.

This reconciliation changes no model output, no source artifact, and no `## Result` status. Model outputs and judge scores are test artifacts, not authorities.
