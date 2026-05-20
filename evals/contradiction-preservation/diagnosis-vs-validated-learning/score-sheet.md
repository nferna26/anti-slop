---
case_id: diagnosis-vs-validated-learning
eval_type: contradiction-preservation
scoring_status: scored
---

# Score Sheet

Score against the rubric in `case.md` → `## Scoring rubric`. Each of the five criteria is scored `pass` or `fail` per model condition. Per-condition score is the count of criteria passed (0–5).

## Result

partial — first pass; 2 of 4 conditions run, one run each. The comparative signal favours `substrate_workflow` (5/5 vs `vanilla` 2/5) but is not yet settled. See Judge Notes.

## Scores

Mark each cell `pass` or `fail`. One column per `model_condition` from the case; leave a column blank if that condition was not run.

| Criterion | vanilla | famous_sources_supplied | substrate_workflow | optional_local_model |
| --- | --- | --- | --- | --- |
| Tension recognised | pass |  | pass |  |
| Scenario located | fail |  | pass |  |
| No framework-default | fail |  | pass |  |
| Lineage discipline | fail |  | pass |  |
| Honest recommendation | pass |  | pass |  |
| **Per-condition score (0–5)** | 2 |  | 5 |  |

## Comparative signal

Per-condition score is 0–5. The eval signal is comparative, not absolute: `substrate_workflow` should beat `vanilla` and `famous_sources_supplied` across runs. A single high-scoring answer does not settle the case; `substrate_workflow` failing to beat `vanilla` across runs falsifies it (see `case.md` → `## Falsifier`).

First-pass result: `substrate_workflow` 5/5 vs `vanilla` 2/5 — a gap of 3, consistent with the eval's hypothesis. This is one run per condition; it does not settle the case.

## Judge Notes

First evaluation pass — 2026-05-20. Two of four conditions run, `vanilla` and `substrate_workflow`, one run each. `famous_sources_supplied` and `optional_local_model` were not run; their columns are left blank. Both runs are recorded under `model-outputs/`; both are test artifacts, not authorities. This is a first-pass dry run using in-session simulated outputs — useful for validating the eval harness end to end, but not yet a settled empirical benchmark.

**vanilla — 2/5.**

- Tension recognised — PASS. Names both the diagnosis-first and the experiment-first posture and gives the head of product's view a sequenced place rather than dismissing it.
- Scenario located — FAIL. Identifies the patient-adoption unknown and uses the cheap-experiment cue, but waves the clinic-workflow study aside ("not really the thing in doubt") instead of treating the clinic side as a legible part to diagnose from the four years of data. No two-track split.
- No framework-default — FAIL. Settles the question with "this is essentially the lean-startup playbook ... and your situation fits it well."
- Lineage discipline — FAIL. Treats the lean framework as the universal right approach. (No misattribution of authors; the failure is framework-as-universal.)
- Honest recommendation — PASS. Gives a clear, structured, contingent recommendation — run the demand test, regroup at three weeks, branch on the signal.

**substrate_workflow — 5/5.**

- Tension recognised — PASS. Names both postures as legitimate and cites the claim/tension card holding them unresolved.
- Scenario located — PASS. Explicitly splits the situation into a legible clinic-workflow part and an unknown patient-adoption part, and uses the experiment-cost cue.
- No framework-default — PASS. Reasons from the scenario's specifics and states explicitly that neither posture is a universal rule.
- Lineage discipline — PASS. Attributes the diagnosis claim to `BK-0001-card-001` and the validated-learning claim to `BK-0007-card-001` at evidence level, and the tension to `strategy-diagnosis-vs-validated-learning` at synthesis level; states explicitly that the claims are not canon; no misattribution.
- Honest recommendation — PASS. Gives a specifics-conditional two-track recommendation and states that changing the specifics would shift the balance.

The first-pass comparative signal (substrate 5 vs vanilla 2) is consistent with the eval's hypothesis that the substrate produces better tension-handling. Per `case.md` → `## Falsifier`, one run per condition does not settle the case.

## Follow-up

- Run the two conditions not covered in this pass: `famous_sources_supplied` and `optional_local_model`.
- Add repeat runs of `vanilla` and `substrate_workflow` so the comparative signal rests on more than a single run per condition.
- If `substrate_workflow` stops beating `vanilla` across repeat runs, treat the case as falsified per `case.md` → `## Falsifier`.
- The eval result is not yet eligible to support any canon candidate; `Result` stays `partial` until the remaining conditions and repeat runs are in.
