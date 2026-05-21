---
case_id: managerial-output-vs-industry-structure
eval_type: contradiction-preservation
scoring_status: scored
---

# Score Sheet

Score against the rubric in this case's `case.md` → `## Scoring rubric`. Each of the five criteria is scored `pass` or `fail` per model condition. Per-condition score is the count of criteria passed (0–5). The criteria below are copied verbatim from the case rubric — do not score against generic or remembered criteria.

First real-run pass: 2026-05-21. All five conditions produced real local-model outputs and are scored. See `run-packet.md` for the freeze, the packets, and the run receipts.

## Result

partial — all five conditions produced real local-model runs and were scored: `vanilla` 2/5, `famous_sources_supplied` 1/5, `substrate_workflow` 5/5, `vanilla_long_prompt` 2/5, `optional_local_model` 2/5. `substrate_workflow` beats every baseline by the `## Positive result` criterion, including the equal-length control `vanilla_long_prompt` by three points, so the substrate advantage on this pass is not explained by prompt length. The result is held at `partial`, not `benchmark_supported`: the runs are single (a benchmark pass needs at least three repeats per condition per `docs/eval-benchmark-upgrade.md`) and the judge is model-family-separated from the generator but not an independent third-party judge. `dry_run_supported` does not apply either — that status is defined by in-session simulated outputs and this case has none; the evidence is all-real but single-run, which is mid-evaluation toward a benchmark, i.e. `partial`. Per `docs/eval-result-status-policy.md` a `partial` result supports no public advice claim and is not eligible to support a canon candidate.

## Scores

One column per `model_condition` from the case. Each cell is `pass` or `fail`; per-condition score is the count of criteria passed (0–5).

| Criterion | vanilla | famous_sources_supplied | substrate_workflow | vanilla_long_prompt | optional_local_model |
| --- | --- | --- | --- | --- | --- |
| Tension recognised | fail | fail | pass | fail | fail |
| Scenario located | pass | pass | pass | pass | pass |
| No flattening | fail | fail | pass | fail | fail |
| Lineage and authority discipline | pass | fail | pass | pass | pass |
| Honest recommendation | fail | fail | pass | fail | fail |
| **Per-condition score (0–5)** | 2 | 1 | 5 | 2 | 2 |

## Comparative signal

Per-condition score is 0–5. The eval signal is comparative, not absolute: per `case.md` → `## Positive result`, `substrate_workflow` should out-score `vanilla`, `famous_sources_supplied`, and the equal-length control `vanilla_long_prompt`. Per `case.md` → `## Falsifier`, a `substrate_workflow` that does not beat both `vanilla` and `vanilla_long_prompt` falsifies the case; a win over bare `vanilla` but not the equal-length control would be a prompt-length effect, not substrate evidence.

Run so far (one real run per condition): `substrate_workflow` 5/5; `vanilla` 2/5; `vanilla_long_prompt` 2/5; `optional_local_model` 2/5; `famous_sources_supplied` 1/5. `substrate_workflow` beats every baseline — by 3 over `vanilla`, the equal-length control `vanilla_long_prompt`, and `optional_local_model`, and by 4 over `famous_sources_supplied`. The `## Falsifier` is not met on this pass: `substrate_workflow` beats both `vanilla` and the equal-length control.

Three observations. First, the equal-length control behaves as intended and is decisive here: `vanilla_long_prompt` (2/5) scored the *same* as bare `vanilla` (2/5) and three points below `substrate_workflow` — a token-matched prompt with no substrate did not reproduce any of the substrate's advantage, so the gap is a lineage effect, not a prompt-length effect. Second, the gap is concentrated where the substrate adds material: all five conditions passed `Scenario located` (the Advisor prompt hands the cues over directly), but only `substrate_workflow` passed `Tension recognised`, `No flattening`, and `Honest recommendation` — every non-substrate condition flattened the attribution to "the manager is the problem, not the territory". Third, `famous_sources_supplied` (1/5) scored *below* `vanilla` (2/5): name-level famous-framework awareness made it worse on `Lineage and authority discipline` — it wielded "Porter's Five Forces" and the two named principles as the settling framework, where bare `vanilla`, invoking no named framework, committed no authority abuse. The sample is one run per condition.

## Judge Notes

Conditions run, as of 2026-05-21: all five — `vanilla`, `famous_sources_supplied`, `substrate_workflow`, `vanilla_long_prompt`, and `optional_local_model` — one real local-model run each, all `qwen3.5:latest` via Ollama (server 0.24.0). There are **no in-session simulations** in this case. Generator: `qwen3.5:latest`; judge: Claude Opus 4.7 (`claude-opus-4-7`), a different model family — generation and scoring are separated. Limitation: the judge is the same agent orchestrating the pass, so this is model-family separation, not an independent third-party judge; no independent human judging occurred.

**vanilla — 2/5.**

- Tension recognised — FAIL. Names both readings (the "market environment (structural)" and "management execution (operational)") but concludes "the weight of evidence points toward management failure, not market failure" and that the adviser "is wrong about the cause" — it treats the attribution as essentially settled.
- Scenario located — PASS. Uses the Donner comparison ("the smoking gun"), the structural trade-group argument, the driver vacancies, the warehouse delay, the on-time-delivery lag, and the two-year margin slip.
- No flattening — FAIL. Resolves the attribution to one side — "management failure, not market failure".
- Lineage and authority discipline — PASS. No substrate supplied; the answer invokes no named framework as an authority ("attribution error", "sunk cost fallacy" are used as generic terms, not settling authorities). The criterion's fail conditions are not met.
- Honest recommendation — FAIL. The recommendation (a 90-day turnaround, then fix-or-replace) flows from the resolved one-side attribution; the open attribution question is not preserved.

**famous_sources_supplied — 1/5.**

- Tension recognised — FAIL. Names both readings but frames the structural one as a "hard territory excuse" and a "blind spot trap", and concludes "the manager is the problem, not the territory".
- Scenario located — PASS. Uses the Donner comparison, the structural argument, the operational cues, and the margin slip.
- No flattening — FAIL. Flattens to manager-blame.
- Lineage and authority discipline — FAIL. Recites the named frameworks as the settling authority: it structures the answer as "The Theoretical Framework" with "Principle 1" and "Principle 2: Profitability = Competitive Forces (Porter's Five Forces)", and closes with "Aligns with Principle 1 / Aligns with Principle 2". Naming "Porter's Five Forces" and wielding the two named principles as the authorities the conclusion aligns with is the authority abuse this criterion is built to catch.
- Honest recommendation — FAIL. Forces a one-side recommendation ("the manager is the problem, not the territory").

**substrate_workflow — 5/5.**

- Tension recognised — PASS. Names both readings as the two sides of a documented tension and credits each — "the structural argument is not wrong—it just doesn't tell the whole story"; "Your adviser is arguing on the first level (Structure). You are arguing on the second (Manager). To make a decision, you must run both diagnostics."
- Scenario located — PASS. Uses the cues (Donner, the structural argument, the vacancies/warehouse/on-time-delivery facts) and locates the case against the tension card's deciding conditions, quoting "Where the arena is approximately held constant and the variance is across units, [managerial output] is the one that discriminates."
- No flattening — PASS. Adopts the sequential-diagnostic reading the tension card names, and conditions its conclusion on a Step-1 structural-bound check ("If Donner has better contracts ... that is a structural difference. If the contracts are identical, the structure is the same, and the variance is managerial") — the attribution is kept open, not collapsed to one-side blame or a bare "both matter".
- Lineage and authority discipline — PASS. Attributes the managerial-output reading to Grove and the structural reading to Porter, correctly and distinctly; names the tension card as the synthesis-level artifact and quotes it as guidance, not canon; uses the source-card claims as evidence-level.
- Honest recommendation — PASS. A sequenced recommendation — validate the structural bound, then audit the operational failures, then decide with a timeline — that locates the case against the deciding conditions, keeps the attribution conditional on the Step-1 finding, and states an explicit decision criterion.

**vanilla_long_prompt — 2/5.** Equal-length control packet (30 distinct neutral filler paragraphs, no substrate).

- Tension recognised — FAIL. Names both readings but concludes "You likely have a management problem, not a territory problem" and calls the structural reading "an excuse, not a fact".
- Scenario located — PASS. Uses the Donner "control group", the structural argument, and the operational cues.
- No flattening — FAIL. Flattens — "The territory is not the problem; the execution is."
- Lineage and authority discipline — PASS. No substrate supplied; no named framework wielded as a settling authority. The criterion's fail conditions are not met.
- Honest recommendation — FAIL. The recommendation flows from the resolved one-side attribution; the open question is not preserved.

**optional_local_model — 2/5.** Real local-model run on the Advisor prompt only (the byte-identical packet to `vanilla`); `seed 105`.

- Tension recognised — FAIL. Leads with "The Verdict: Replace the Manager" and "the evidence points strongly to managerial execution failure, not market structure" — the attribution is treated as obvious.
- Scenario located — PASS. Uses the Donner "control group / smoking gun", the structural argument, the operational cues, the margin slip, and cost-to-serve.
- No flattening — FAIL. The "Replace the Manager" verdict is stated upfront; the attribution is resolved.
- Lineage and authority discipline — PASS. No substrate; no named framework wielded as a settling authority.
- Honest recommendation — FAIL. A forced "replace the manager" recommendation; the open attribution question is not preserved.

This run is on the byte-identical packet to `vanilla` and lands at the same 2/5 with the same failure profile — consistent with `optional_local_model` being, by design, a real local-model run on the `vanilla` packet.

## Follow-up

- All five conditions ran as real local-model runs and were scored; this is a single run per condition. `substrate_workflow` beats every baseline including the equal-length control, but the comparative signal is not yet shown stable across repeat runs.
- `Result` is `partial` per `docs/eval-result-status-policy.md`. To move toward `benchmark_supported` — the only status eligible to support a canon candidate — the case needs at least three repeats per condition, an independent judge (not the orchestrating agent), and the frozen-packet discipline in `docs/eval-benchmark-upgrade.md` carried through a dedicated benchmark pass.
- The equal-length control behaved as intended: `vanilla_long_prompt` (2/5) sits three points below `substrate_workflow` (5/5) and level with bare `vanilla`, so the substrate advantage on this pass is not a prompt-length artefact.
- If `substrate_workflow` stops beating `vanilla` and the equal-length control in later runs, treat the case as falsified per `case.md` → `## Falsifier`.
- This result is not eligible to support a canon candidate while it is `partial`.
