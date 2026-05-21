---
name: anti-slop-eval-run
description: "Five-workflow eval-run pipeline for the books-kb proof surface: run-eval-condition, score-eval-output, repair-eval-receipts, summarize-eval-result, and run-approval-ready-eval-pass. Judgment rails for running and scoring eval cases — model outputs are test artifacts, scoring uses each case's own rubric, and case / score-sheet / model-output / kb-log files stay receipt-consistent."
---

# anti-slop-eval-run

This skill encodes the eval-run workflow for the books-kb proof surface — the workflow used to run and score the `contradiction-preservation/diagnosis-vs-validated-learning` case across its four model conditions. It is judgment rails, not a tooling framework. There are no helper scripts; Claude follows the discipline by reading the relevant workflow section, the case's own files, and the eval result status policy.

It applies to any eval case under `evals/`, and is shaped for contradiction-preservation cases in particular.

## When to invoke

Invoke this skill when the operator asks Claude to run an eval condition, score an eval output, repair eval receipt drift, summarise an eval result, or run a complete approval-ready eval pass for a books-kb eval case.

## Workflow selector

| Workflow | Section | Writes public? |
|---|---|---|
| `run-eval-condition` | `## Workflow 1` | Yes — one model-output file |
| `score-eval-output` | `## Workflow 2` | Yes — score sheet and receipts |
| `repair-eval-receipts` | `## Workflow 3` | Yes — receipt text only |
| `summarize-eval-result` | `## Workflow 4` | No, unless the Result status changes per policy |
| `run-approval-ready-eval-pass` | `## Workflow 5` | Yes |

## Shared contract

Every workflow inherits these rules. If a workflow would violate any rule, stop and surface to the operator.

- **Model outputs are test artifacts, never authorities.** A model output is never citable as a source and never an authority — it is evidence about model behaviour under a condition, nothing more.
- **Use only the source packet the condition defines.** Each model condition gets exactly its packet — no more, no less:
  - `vanilla` — the case's Advisor prompt only. No substrate, no framework material.
  - `famous_sources_supplied` — the Advisor prompt plus high-level, name-level awareness of the relevant famous frameworks. No claim/tension card, no source cards, no book-map or source-card prose.
  - `substrate_workflow` — the Advisor prompt plus the lineage artifacts the case names in its `## Lineage` section (the reviewed claim/tension card and reviewed source cards).
  - `optional_local_model`, or any external/local model condition — the same packet as `vanilla` unless the case explicitly defines otherwise.
- **Never simulate a real-model condition.** For `optional_local_model` or any condition defined as an external or local model run: run a real model and record its exact model ID and runtime, or defer the condition. Do not write a model-output file for a real-model condition that was not actually run.
- **Label simulated vs real outputs.** An in-session simulation and a real external model run are different evidence (see `docs/eval-result-status-policy.md`). Every model-output file states which it is, in frontmatter and in its condition note.
- **Score against the case's own rubric.** Score each output against `case.md` → `## Scoring rubric`, criterion by criterion — never against generic or remembered criteria.
- **Keep receipts consistent.** After any run or scoring change, `case.md`, `score-sheet.md`, the `model-outputs/` files, and `kb/log.md` must agree (see `## Receipt-consistency check`).
- **Preserve prior scores.** Do not overwrite an existing run's score unless the operator explicitly asks to supersede it; new runs are added, not substituted.
- **Status vocabulary is fixed.** A score sheet's `## Result` uses only the values defined in `docs/eval-result-status-policy.md`.
- **No higher artifacts.** Do not create canon candidates, graph edges, source cards, claim/tension cards, or extra eval cases.
- **No `git add` or `git commit`** unless the operator explicitly requests it. Run the closing-gate suite and report results.

## Workflow 1 — run-eval-condition

**When to use it.** Producing one model-output file for one model condition of one eval case.

**Inputs.**
- `case.md` — the Advisor prompt, the `## Lineage` artifacts, the `model_conditions` list, the per-condition packet definitions.
- `docs/eval-result-status-policy.md` — the dry-run vs real-run distinction.
- `runs/model-outputs/_metadata-template.yaml` — the model-output frontmatter fields.

**Steps.**

1. Identify the condition and assemble exactly its source packet, per the Shared contract. Include nothing the packet does not name.
2. For `vanilla`, `famous_sources_supplied`, `substrate_workflow`: the run may be a real external model run or an in-session good-faith simulation. Prefer a real run when one is available; either way, label it honestly.
3. For `optional_local_model` or any external/local model condition: detect a local runtime safely (for example, an Ollama or LM Studio server), pick the model the operator named or the strongest available, run it, and capture the verbatim output. If no real model can be run, stop and report — do not create a file.
4. Write one file `model-outputs/<condition>.md` (or `<condition>-NN.md` for a repeat run). Frontmatter carries `run_id`, `created`, `eval_type`, `case_id`, `model_condition`, `model_name`, `runtime` (for real runs), `prompt_source`, `output_file`, `source_packet`, `operator_notes`, and `raw_model_output_public_safe`. The body records the condition and the output.
5. Add the new file to `case.md` → `## Model outputs`.
6. Run the receipt-consistency check and the closing-gate suite. Scoring is Workflow 2.

## Workflow 2 — score-eval-output

**When to use it.** Judging one model output against the case rubric and recording the score.

**Steps.**

1. Read the model-output file and `case.md` → `## Scoring rubric`.
2. Score each rubric criterion `pass` or `fail`, strictly by the case's own rubric. Cite the output's actual wording in the reasoning.
3. Fill that condition's column (and run) in `score-sheet.md`. Preserve every prior score.
4. Record per-criterion reasoning in the score sheet's Judge Notes; recompute the per-condition score.
5. Update the Comparative signal.
6. Evaluate `## Result` against `docs/eval-result-status-policy.md`. Change the Result status only if the policy's requirements for the new status are met; never overclaim.
7. Update `case.md` → `## Score sheet` so it states which conditions are scored, `scoring_status`, and the Result.
8. Append one public-safe `kb/log.md` bullet.
9. Run the receipt-consistency check and the closing-gate suite.

## Workflow 3 — repair-eval-receipts

**When to use it.** `case.md`, `score-sheet.md`, the `model-outputs/` files, or `kb/log.md` disagree about what has been run or scored.

**Steps.**

1. Run the receipt-consistency check to find every disagreement.
2. Fix only the stale receipt text — the prose that misstates which conditions ran, which files exist, `scoring_status`, the Result status, or the dry-run vs real-run mix.
3. Do not change the scenario, Advisor prompt, rubric, scores, model outputs, the result status policy, or score-sheet scoring semantics. This workflow corrects descriptions, not findings.
4. Append one public-safe `kb/log.md` bullet.
5. Run the receipt-consistency check again and the closing-gate suite.

## Workflow 4 — summarize-eval-result

**When to use it.** Reporting where an eval case stands.

**Steps.**

1. Read `case.md`, `score-sheet.md`, and `docs/eval-result-status-policy.md`.
2. Report: the per-condition scores and runs; the comparative signal; the dry-run vs real-run mix; the current `## Result` status; the limitations; and what the result is and is not eligible to support — in particular, whether it may support a canon candidate.
3. Check the recorded Result against the policy. If it is wrong, either update it (when the policy clearly determines the correct status) or flag it for `repair-eval-receipts`.
4. This workflow writes a public file only if it changes the Result status; otherwise it only reports.

## Workflow 5 — run-approval-ready-eval-pass

**When to use it.** Running a complete pass — one or more conditions of a case, run, scored, and receipt-checked — and reporting whether the result has reached an approval-ready status.

**Hard limits.**
- One model-output file per condition per run.
- Never simulate a real-model condition; defer it if no real model is available.
- Do not create canon candidates, graph edges, source cards, claim/tension cards, or extra eval cases.
- Do not `git add` or `git commit` unless the operator explicitly requested a commit.

**Steps.**

1. For each condition in scope, run Workflow 1 then Workflow 2. Defer any real-model condition that cannot be run, and record the deferral.
2. After every condition in the pass is scored, run Workflow 4 to evaluate the `## Result` status against the policy.
3. Run the receipt-consistency check and the closing-gate suite.
4. Report: per-condition scores, the comparative signal, the Result status, what it is eligible to support, and any deferred conditions. Append one consolidated `kb/log.md` bullet for the pass, rather than one per condition.

## Receipt-consistency check

After any run or scoring update, verify that `case.md`, `score-sheet.md`, the `model-outputs/` files, and `kb/log.md` all agree on:

1. **Conditions run** — the conditions named as run match across `case.md` → `## Model outputs`, the filled `score-sheet.md` columns, and the `model-outputs/` files on disk.
2. **Files exist** — every model-output file listed in `case.md` or implied by a filled score-sheet column exists on disk, and every file on disk is listed.
3. **`scoring_status`** — the `score-sheet.md` frontmatter flag and the `case.md` → `## Score sheet` paragraph agree.
4. **Result status** — the `score-sheet.md` → `## Result` value and any mention of it in `case.md` agree, and the value is one of the `docs/eval-result-status-policy.md` statuses.
5. **Dry-run vs real-run** — each model-output file's simulated-or-real label is consistent with how the score sheet and the Result justification describe the evidence.

Any disagreement is receipt drift — run Workflow 3.

## Commands to run

After any workflow that writes a public file, run the closing-gate suite from the repo root:

```sh
make validate
make check-raw
make kb-lint
make report
make phase2-queue
python3 -m py_compile scripts/*.py
git diff --check
```

Then sweep the public directories — `corpus/`, `kb/`, `docs/`, `evals/`, `runs/` — for private home-directory paths and archive-bundle names, the markers `scripts/kb_lint.py` and `scripts/check_no_raw_text.py` guard against; expect zero matches. None of these commands ever runs `git add` or `git commit`.

## Reference pass

The `contradiction-preservation/diagnosis-vs-validated-learning` case is the worked reference: four model conditions run (three as in-session simulations, one — `optional_local_model` — as a real local-model run), scored against the case's own five-criterion rubric, with a `dry_run_supported` Result recorded under the eval result status policy. Match its shape.
