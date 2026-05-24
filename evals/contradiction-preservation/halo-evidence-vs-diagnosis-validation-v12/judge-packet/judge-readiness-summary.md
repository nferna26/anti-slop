---
case_id: halo-evidence-vs-diagnosis-validation-v12
benchmark_version: halo-evidence-vs-diagnosis-validation-v12-v1
artifact: judge-readiness-summary
condition_blinded: true
status: passed
---

# Judge Readiness Summary

This is a public-safe pre-generation readiness receipt. It records only
calibration and synthetic disagreement-smoke outcomes, not model-output scores
and not a benchmark result.

Rule: all three pre-registered routes must pass calibration and disagreement
smoke; pairwise C4-C6 disagreement on the ten synthetic smoke answers must be
at or below 0.20.

## Routes

| Route | Model | Route passed | C4-C6 calibration differences | Calibration dependency violations | Smoke dependency violations |
| --- | --- | --- | ---: | ---: | ---: |
| openai | `gpt-5.4` | True | 0 | 0 | 0 |
| anthropic | `claude-opus-4-7` | True | 0 | 0 | 0 |
| local | `gpt-oss:20b` | True | 0 | 0 | 0 |

## Pairwise Smoke Disagreement

| Pair | Compared | Disagreements | Rate | Passed |
| --- | ---: | ---: | ---: | --- |
| openai_vs_anthropic | 10 | 0 | 0.00 | True |
| openai_vs_local | 10 | 1 | 0.10 | True |
| anthropic_vs_local | 10 | 1 | 0.10 | True |

Overall readiness: `True`.

If readiness is false, v12-v1 must not generate. Revising the case, rubric,
smoke answers, or judge instructions starts a new frozen candidate.
