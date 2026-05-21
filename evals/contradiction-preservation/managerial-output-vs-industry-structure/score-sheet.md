---
case_id: managerial-output-vs-industry-structure
eval_type: contradiction-preservation
scoring_status: unscored
---

# Score Sheet

Score against the rubric in this case's `case.md` → `## Scoring rubric`. Each of the five criteria is scored `pass` or `fail` per model condition. Per-condition score is the count of criteria passed (0–5). The criteria below are copied verbatim from the case rubric — do not score against generic or remembered criteria. This case is a draft: the table is the unfilled scaffold, every cell is `not run`, and nothing below has been judged.

## Result

partial — this case is a draft: no model condition has been run and no output has been scored, so scoring is incomplete. Per `docs/eval-result-status-policy.md`, a case with no runs in is `partial`; it supports no public advice claim and is not eligible to support a canon candidate. The status moves off `partial` only after the case is run and scored against the rubric, and can reach `dry_run_supported` or `benchmark_supported` only when the v1 support requirements in the policy are met.

## Scores

One column per `model_condition` from the case. Each cell is `pass` or `fail` once scored; per-condition score is the count of criteria passed (0–5). No condition has been run, so every cell is `not run`.

| Criterion | vanilla | famous_sources_supplied | substrate_workflow | vanilla_long_prompt | optional_local_model |
| --- | --- | --- | --- | --- | --- |
| Tension recognised | not run | not run | not run | not run | not run |
| Scenario located | not run | not run | not run | not run | not run |
| No flattening | not run | not run | not run | not run | not run |
| Lineage and authority discipline | not run | not run | not run | not run | not run |
| Honest recommendation | not run | not run | not run | not run | not run |
| **Per-condition score (0–5)** | not run | not run | not run | not run | not run |

## Comparative signal

The eval signal is comparative, not absolute. Per `case.md` → `## Positive result`, `substrate_workflow` should out-score `vanilla`, `famous_sources_supplied`, and the equal-length control `vanilla_long_prompt` across runs — a win over the equal-length control specifically is what separates a lineage effect from a prompt-length effect. Per `case.md` → `## Falsifier`, a `substrate_workflow` that does not beat both `vanilla` and `vanilla_long_prompt` across runs falsifies the case; a win over bare `vanilla` but not the equal-length control is a prompt-length effect, not substrate evidence. No condition has been run, so there is no signal yet.

## Judge Notes

No model output has been produced or scored. This case is a draft; an evaluation pass (`anti-slop-eval-run`) is run only after the case design is operator-reviewed. All five criterion rows above are copied verbatim from `case.md` → `## Scoring rubric` so the sheet does not drift from the case rubric when it is scored.

## Follow-up

- The case design (scenario, Advisor prompt, lineage, rubric, Positive result, Falsifier) awaits operator review before any evaluation pass.
- Once the design is reviewed, run the five conditions — `vanilla`, `famous_sources_supplied`, `substrate_workflow`, `vanilla_long_prompt`, and `optional_local_model` — via `anti-slop-eval-run`, recording one model-output file per run under `model-outputs/`.
- `optional_local_model` must be a real local-model run or be explicitly deferred; never simulate a real-model condition.
- The equal-length control `vanilla_long_prompt` is required for this case to be able to reach `benchmark_supported`: without it a substrate win cannot be separated from a prompt-length effect.
- `Result` moves off `partial` only after scoring, per `docs/eval-result-status-policy.md`; `benchmark_supported` additionally requires the frozen-packet, real-run, repeat-run, and judge-separation steps in `docs/eval-benchmark-upgrade.md`.
