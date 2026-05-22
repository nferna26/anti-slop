---
case_id: managerial-output-vs-industry-structure
eval_type: contradiction-preservation
scoring_status: scored
---

# Score Sheet

Score against the rubric in this case's `case.md` → `## Scoring rubric`. Each of the five criteria is scored `pass` or `fail` per model condition per run. Per-run, per-condition score is the count of criteria passed (0–5). The criteria below are copied verbatim from the case rubric — do not score against generic or remembered criteria.

Three real-run passes: 2026-05-21. Run 01 ran each condition once; runs 02 and 03 added two more real local-model repeats per condition. `vanilla_long_prompt-03` timed out at 420s on its first attempt (seed 304) and was re-attempted on a fresh deterministic seed (314), which completed. All five conditions now have **three completed real runs each** — fifteen real outputs in total, no in-session simulations and no outstanding deferrals.

## Result

partial — all five conditions ran as real local-model runs across three passes and were scored: every run of `substrate_workflow` is 5/5; every run of `vanilla`, `vanilla_long_prompt`, and `optional_local_model` is 2/5; every run of `famous_sources_supplied` is 1/5. `substrate_workflow` beats every baseline on every run, including the equal-length control `vanilla_long_prompt`, by three points — under this orchestrator scoring the signal was stable across all three runs. The three-repeats-per-condition bar in `docs/eval-benchmark-upgrade.md` is now met for every condition; the result is nonetheless held at `partial`, not `benchmark_supported`, because the judge is model-family-separated from the generator but is **not an independent third-party judge** (the judge is the agent that orchestrated the eval), and the runs were accumulated across goals rather than executed as a single declared frozen benchmark pass. `dry_run_supported` does not apply — that status is defined by in-session simulated outputs and this case has none. Per `docs/eval-result-status-policy.md` a `partial` result supports no public advice claim and is not eligible to support a canon candidate. **Update (2026-05-21):** an independent blind judge pass has since been run and reconciled to conditions — it **weakens** the result recorded above; see `## Independent blind judge reconciliation` immediately below. The status stays `partial` and the case must not advance to `benchmark_supported` on the current evidence.

## Independent blind judge reconciliation

After the scoring above (Claude Opus 4.7 — the agent that orchestrated the eval), the fifteen answers were re-scored **blind** by `gemma4:31b` (Gemma family — a different model family from the `qwen3.5:latest` generator), each answer scored in its own call without its condition known. Reconciled to conditions, the per-condition blind means are: `substrate_workflow` 4.33, `vanilla_long_prompt` 3.67, `optional_local_model` 3.00, `vanilla` 2.67, `famous_sources_supplied` 2.33.

`substrate_workflow` still has the highest mean, but its margin over the equal-length control `vanilla_long_prompt` collapses from +3.0 in the orchestrator pass above to **+0.67**, and the per-run distributions overlap — the control produced a 5/5 run and the substrate a 3/5 run. The decisive substrate-vs-control comparison is **inconclusive** under blind judging; the blind pass does not confirm the substrate hypothesis at benchmark strength. Full detail and the per-output blind scores are in `judge-packet/independent-judge-reconciliation-gemma4-31b.md` and `judge-packet/independent-judge-score-gemma4-31b.md`. This reconciliation changes no score above and does not lift `## Result`; it is an explicit reason the case must not be promoted to `benchmark_supported`.

## Scores

Each cell is `pass` or `fail`; per-condition score is the count of criteria passed (0–5).

### Run 01 (seeds 101–105)

| Criterion | vanilla | famous_sources_supplied | substrate_workflow | vanilla_long_prompt | optional_local_model |
| --- | --- | --- | --- | --- | --- |
| Tension recognised | fail | fail | pass | fail | fail |
| Scenario located | pass | pass | pass | pass | pass |
| No flattening | fail | fail | pass | fail | fail |
| Lineage and authority discipline | pass | fail | pass | pass | pass |
| Honest recommendation | fail | fail | pass | fail | fail |
| **Per-condition score (0–5)** | 2 | 1 | 5 | 2 | 2 |

### Run 02 (seeds 201–205)

| Criterion | vanilla | famous_sources_supplied | substrate_workflow | vanilla_long_prompt | optional_local_model |
| --- | --- | --- | --- | --- | --- |
| Tension recognised | fail | fail | pass | fail | fail |
| Scenario located | pass | pass | pass | pass | pass |
| No flattening | fail | fail | pass | fail | fail |
| Lineage and authority discipline | pass | fail | pass | pass | pass |
| Honest recommendation | fail | fail | pass | fail | fail |
| **Per-condition score (0–5)** | 2 | 1 | 5 | 2 | 2 |

### Run 03 (seeds 301–303, 305; vanilla_long_prompt re-attempt seed 314)

| Criterion | vanilla | famous_sources_supplied | substrate_workflow | vanilla_long_prompt | optional_local_model |
| --- | --- | --- | --- | --- | --- |
| Tension recognised | fail | fail | pass | fail | fail |
| Scenario located | pass | pass | pass | pass | pass |
| No flattening | fail | fail | pass | fail | fail |
| Lineage and authority discipline | pass | fail | pass | pass | pass |
| Honest recommendation | fail | fail | pass | fail | fail |
| **Per-condition score (0–5)** | 2 | 1 | 5 | 2 | 2 |

### Aggregate by condition

| Condition | Runs scored | Per-run scores | Mean |
| --- | --- | --- | --- |
| `substrate_workflow` | 3 | 5, 5, 5 | 5.0 |
| `vanilla` | 3 | 2, 2, 2 | 2.0 |
| `vanilla_long_prompt` | 3 | 2, 2, 2 | 2.0 |
| `optional_local_model` | 3 | 2, 2, 2 | 2.0 |
| `famous_sources_supplied` | 3 | 1, 1, 1 | 1.0 |

## Comparative signal

*Orchestrator-scored only.* The signal described in this section is from the Claude-orchestrated scoring above. Independent blind judging (`gemma4:31b`) did not reproduce it — see `## Independent blind judge reconciliation` — so read the claims below as a record of that orchestrator pass, not as the case's current finding.

Per-condition score is 0–5. The eval signal is comparative, not absolute: per `case.md` → `## Positive result`, `substrate_workflow` should out-score `vanilla`, `famous_sources_supplied`, and the equal-length control `vanilla_long_prompt` across runs. Per `case.md` → `## Falsifier`, a `substrate_workflow` that does not beat both `vanilla` and `vanilla_long_prompt` across runs falsifies the case; a win over bare `vanilla` but not the equal-length control is a prompt-length effect, not substrate evidence.

Across three runs the orchestrator scoring was **stable**: `substrate_workflow` scored 5/5 on every run; `vanilla`, `vanilla_long_prompt`, and `optional_local_model` scored 2/5 on every run; `famous_sources_supplied` scored 1/5 on every run. Under that scoring `substrate_workflow` beat every baseline on every run — by 3 over `vanilla`, the equal-length control `vanilla_long_prompt`, and `optional_local_model`, and by 4 over `famous_sources_supplied`, and the `## Falsifier` was not met on any run. Independent blind judging did not reproduce this separation (see `## Independent blind judge reconciliation`).

Three observations hold across all three passes of the orchestrator scoring. First, the equal-length control: `vanilla_long_prompt` scored 2/5 on all three runs — identical to bare `vanilla` — and three points below `substrate_workflow`, so under this orchestrator scoring a token-matched no-substrate prompt reproduced none of the substrate's advantage. Independent blind judging did not reproduce that result (see `## Independent blind judge reconciliation`), so whether the gap is a lineage effect rather than a prompt-length effect is **not currently established**. Second, the gap is concentrated where the substrate adds material: every condition passed `Scenario located` on every run, but only `substrate_workflow` passed `Tension recognised`, `No flattening`, and `Honest recommendation` — every non-substrate run flattened the attribution to "the manager is the problem, not the territory". Third, `famous_sources_supplied` scored below `vanilla` on every run: name-level famous-framework awareness consistently made it worse on `Lineage and authority discipline` — it wielded "Porter's Five Forces" and the named principles as the settling framework. The sample is three runs per condition; the comparative signal is consistent across all of them.

## Judge Notes

Conditions run, as of 2026-05-21: three passes. Run 01 — all five conditions (seeds 101–105). Run 02 — all five (seeds 201–205). Run 03 — `vanilla`, `famous_sources_supplied`, `substrate_workflow`, `optional_local_model` (seeds 301, 302, 303, 305); `vanilla_long_prompt-03` first attempted on seed 304 (timed out at 420s) and re-attempted on a fresh deterministic seed 314, which completed in 108.9s. All fifteen runs are real local-model runs, all `qwen3.5:latest` via Ollama (server 0.24.0) — there are **no in-session simulations** in this case. Generator: `qwen3.5:latest`; judge: Claude Opus 4.7 (`claude-opus-4-7`), a different model family — generation and scoring are separated. Limitation: the judge is the same agent orchestrating the passes, so this is model-family separation, not an independent third-party judge; no independent human judging occurred.

The run-01 per-condition reasoning is unchanged from the first pass; the run-02 and run-03 outputs reproduced the same failure/pass profile per condition, so the per-criterion verdicts are identical run to run.

- **vanilla (2/5, all 3 runs).** Tension recognised — FAIL: each run names both readings but resolves the attribution as obvious ("management failure, not market failure" / "Replace the Westfield manager" / "managerial underperformance, not a structural inevitability"). Scenario located — PASS: uses the Donner comparison, the structural argument, and the operational cues. No flattening — FAIL: each run flattens to one-side blame. Lineage and authority discipline — PASS: no substrate, no named framework wielded as a settling authority. Honest recommendation — FAIL: the recommendation flows from the resolved one-side attribution.
- **famous_sources_supplied (1/5, all 3 runs).** Tension recognised — FAIL. Scenario located — PASS. No flattening — FAIL. Lineage and authority discipline — FAIL: each run recites the named frameworks as the settling authority — "Applying the Management Frameworks", "Framework B: Competitive Structure (Porter's Five Forces)", "structural determinism (Porter's Five Forces)". Honest recommendation — FAIL.
- **substrate_workflow (5/5, all 3 runs).** All five criteria pass on every run: names both readings as an open tension and credits each; uses the cues and quotes the tension card's deciding conditions ("Where the arena is approximately held constant and the variance is across units…"); runs the sequential diagnostic and conditions the conclusion on a structural-bound check rather than collapsing to one-side blame; attributes the managerial-output reading to Grove and the structural reading to Porter, correctly and distinctly, and treats the tension card as synthesis-level guidance, not canon ("I am not providing canon advice"); reaches a sequenced recommendation with an explicit decision criterion that preserves the open attribution question.
- **vanilla_long_prompt (2/5, all 3 runs).** Tension recognised — FAIL: names both but resolves ("management execution is the differentiator" / "the territory is not the problem; the execution is"). Scenario located — PASS. No flattening — FAIL. Lineage and authority discipline — PASS: no substrate, no named framework as authority. Honest recommendation — FAIL. The equal-length control scores level with bare `vanilla` on every run. Run 03 was completed on a fresh seed (314) after the seed-304 attempt timed out.
- **optional_local_model (2/5, all 3 runs).** Same packet as `vanilla`; same profile — Tension FAIL, Scenario PASS, No flattening FAIL, Lineage PASS, Honest FAIL. Each run leads with or resolves to "Replace the Westfield manager".

## Follow-up

- All three real-run passes are complete: every condition has three completed real runs, and under the orchestrator scoring the comparative signal was stable — `substrate_workflow` 5/5 on all three, beating every baseline (independent blind judging later weakened this; see `## Independent blind judge reconciliation`). The deferred `vanilla_long_prompt-03` run has been completed.
- `Result` is `partial` per `docs/eval-result-status-policy.md`. The three-repeats-per-condition bar is now met; the remaining gaps to `benchmark_supported` — the only status eligible to support a canon candidate — are an independent judge (not the agent that orchestrated the eval) and a dedicated declared frozen benchmark pass per `docs/eval-benchmark-upgrade.md`.
- Under the orchestrator scoring the equal-length control behaved as intended on all three runs — `vanilla_long_prompt` sat three points below `substrate_workflow` and level with bare `vanilla`, which under that scoring would have indicated the substrate advantage was not a prompt-length artefact. The blind judge pass did not reproduce that (see `## Independent blind judge reconciliation`): the control's blind mean is 3.67 and the substrate-over-control margin only +0.67, so whether the advantage is a prompt-length effect is **not currently resolved**.
- If `substrate_workflow` stops beating `vanilla` and the equal-length control in later runs, treat the case as falsified per `case.md` → `## Falsifier`.
- This result is not eligible to support a canon candidate while it is `partial`.
- An independent blind judge pass (`gemma4:31b`) has been run and reconciled to conditions (`judge-packet/independent-judge-reconciliation-gemma4-31b.md`): it **weakened** the result — under blind judging the substrate's win over the equal-length control is not robust across runs. The remaining gap to `benchmark_supported` is therefore larger than an independent judge alone: it needs more runs per condition, a fully independent third-party or human judge (not orchestrated by the eval agent), and a substrate-over-control win that holds across runs.
