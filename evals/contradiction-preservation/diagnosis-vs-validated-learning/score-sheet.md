---
case_id: diagnosis-vs-validated-learning
eval_type: contradiction-preservation
scoring_status: scored
---

# Score Sheet

Score against the rubric in `case.md` → `## Scoring rubric`. Each of the five criteria is scored `pass` or `fail` per model condition. Per-condition score is the count of criteria passed (0–5).

## Result

partial — 3 of 4 conditions run, two runs each (`optional_local_model` not yet run). The comparative signal favours `substrate_workflow` (5/5 in both runs) over `vanilla` and `famous_sources_supplied` (both 2/5 in both runs), and is stable across the repeat runs — but the case is not yet settled: `optional_local_model` is unrun and the workflow defines no threshold for moving beyond `partial`. See Judge Notes.

## Scores — run 01

Mark each cell `pass` or `fail`. One column per `model_condition` from the case; leave a column blank if that condition was not run.

| Criterion | vanilla | famous_sources_supplied | substrate_workflow | optional_local_model |
| --- | --- | --- | --- | --- |
| Tension recognised | pass | pass | pass |  |
| Scenario located | fail | fail | pass |  |
| No framework-default | fail | fail | pass |  |
| Lineage discipline | fail | fail | pass |  |
| Honest recommendation | pass | pass | pass |  |
| **Per-condition score (0–5)** | 2 | 2 | 5 |  |

## Repeat runs — run 02

Second run of each condition, recorded as `*-02.md` under `model-outputs/`. Same condition definitions as run 01.

| Criterion | vanilla | famous_sources_supplied | substrate_workflow | optional_local_model |
| --- | --- | --- | --- | --- |
| Tension recognised | pass | pass | pass |  |
| Scenario located | fail | fail | pass |  |
| No framework-default | fail | fail | pass |  |
| Lineage discipline | fail | fail | pass |  |
| Honest recommendation | pass | pass | pass |  |
| **Per-condition score (0–5)** | 2 | 2 | 5 |  |

Per-condition score across runs:

| Condition | run 01 | run 02 |
| --- | --- | --- |
| vanilla | 2 | 2 |
| famous_sources_supplied | 2 | 2 |
| substrate_workflow | 5 | 5 |
| optional_local_model | — | — |

## Comparative signal

Per-condition score is 0–5. The eval signal is comparative, not absolute: `substrate_workflow` should beat `vanilla` and `famous_sources_supplied` across runs. A single high-scoring answer does not settle the case; `substrate_workflow` failing to beat `vanilla` across runs falsifies it (see `case.md` → `## Falsifier`).

Runs so far — two per condition: `substrate_workflow` 5/5 and 5/5; `vanilla` 2/5 and 2/5; `famous_sources_supplied` 2/5 and 2/5. The substrate condition beats both baselines by a gap of 3 in both runs, and the signal is stable across the repeat. `famous_sources_supplied` again did not beat `vanilla` — being handed the famous frameworks changed the *shape* of the failure (framework-arbitration, name-dropping) but not the score. Two runs per condition is more than a single data point but still small; `optional_local_model` remains unrun.

## Judge Notes

Conditions run so far, as of 2026-05-20: `vanilla`, `famous_sources_supplied`, and `substrate_workflow` — two runs each. `optional_local_model` has not been run; its columns are left blank. All six runs are recorded under `model-outputs/`; all are test artifacts, not authorities. This is a dry run using in-session simulated outputs — useful for validating the eval harness end to end, but not yet a settled empirical benchmark.

### Run 01

**vanilla — 2/5.**

- Tension recognised — PASS. Names both the diagnosis-first and the experiment-first posture and gives the head of product's view a sequenced place rather than dismissing it.
- Scenario located — FAIL. Identifies the patient-adoption unknown and uses the cheap-experiment cue, but waves the clinic-workflow study aside ("not really the thing in doubt") instead of treating the clinic side as a legible part to diagnose from the four years of data. No two-track split.
- No framework-default — FAIL. Settles the question with "this is essentially the lean-startup playbook ... and your situation fits it well."
- Lineage discipline — FAIL. Treats the lean framework as the universal right approach. (No misattribution of authors; the failure is framework-as-universal.)
- Honest recommendation — PASS. Gives a clear, structured, contingent recommendation — run the demand test, regroup at three weeks, branch on the signal.

**famous_sources_supplied — 2/5.**

- Tension recognised — PASS. Names both frameworks — Rumelt's strategy kernel and Ries's Lean Startup / validated learning — as respected and legitimate.
- Scenario located — FAIL. Gives a generic week-by-week plan but does not split the situation into a legible clinic-workflow part and an unknown patient-adoption part, and does not use challenge legibility or experiment cost as deciding levers. It points its "diagnosis" step at the patient-portal bet — the part least diagnosable from existing data.
- No framework-default — FAIL. Settles the weighting with "validated learning is the safer master framework" and "let Lean Startup lead."
- Lineage discipline — FAIL. Treats the named frameworks as authorities — a "master framework" with a "central teaching." Authorship attribution is correct; the failure is framework-as-canon.
- Honest recommendation — PASS. Gives a concrete, week-by-week, contingent plan.

**substrate_workflow — 5/5.**

- Tension recognised — PASS. Names both postures as legitimate and cites the claim/tension card holding them unresolved.
- Scenario located — PASS. Explicitly splits the situation into a legible clinic-workflow part and an unknown patient-adoption part, and uses the experiment-cost cue.
- No framework-default — PASS. Reasons from the scenario's specifics and states explicitly that neither posture is a universal rule.
- Lineage discipline — PASS. Attributes the diagnosis claim to `BK-0001-card-001` and the validated-learning claim to `BK-0007-card-001` at evidence level, and the tension to `strategy-diagnosis-vs-validated-learning` at synthesis level; states explicitly that the claims are not canon; no misattribution.
- Honest recommendation — PASS. Gives a specifics-conditional two-track recommendation and states that changing the specifics would shift the balance.

### Run 02

A second run of each condition, recorded as `*-02.md`. Each second run reproduced its condition's run-01 score and pass/fail profile.

- **vanilla-02 — 2/5.** Tension recognised and Honest recommendation pass; Scenario located, No framework-default, and Lineage discipline fail. The answer again leaned experiment-first and settled the question with a generic "validate first, then invest" rule taken as the universally safer order, rather than reasoning from the scenario's specifics; no legible/unknown split, and the four years of clinic data go unused.
- **famous_sources_supplied-02 — 2/5.** Tension recognised and Honest recommendation pass; the other three fail. The answer again framed the question as a "Rumelt-versus-Ries debate" and concluded "this is a textbook Lean Startup situation"; framework-arbitration, no scenario split, frameworks treated as authorities.
- **substrate_workflow-02 — 5/5.** All five pass. The answer again used the deciding conditions to split the legible clinic part from the unknown patient part, attributed the claims to the source cards at evidence level and the tension card at synthesis level, marked them not canon, and gave a specifics-conditional recommendation.

The repeat runs hold the first-run signal: `substrate_workflow` 5/5 in both runs; `vanilla` and `famous_sources_supplied` 2/5 in both runs. Per `case.md` → `## Falsifier`, the case is not yet settled.

## Follow-up

- Run the remaining condition: `optional_local_model`.
- The repeat runs in this pass give two runs per condition; further runs would tighten the signal but are not blocking.
- If `substrate_workflow` stops beating `vanilla` in later runs, treat the case as falsified per `case.md` → `## Falsifier`.
- The eval result is not yet eligible to support any canon candidate; `Result` stays `partial` until `optional_local_model` is run, and unless a threshold for moving beyond `partial` is defined in the workflow.
