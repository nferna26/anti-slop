# The Eval Lab Protocol

The Eval Lab is the books-kb proof surface: the eval cases under `evals/`, their score sheets, and their model-output receipts. This document is the operating frame for that surface — what an eval result is, what controls a case must carry, and the bright line between an eval result and canon evidence.

It complements two existing documents and does not restate them:

- `docs/eval-result-status-policy.md` — the controlled vocabulary for a case's `## Result`.
- `docs/eval-benchmark-upgrade.md` — the step-by-step checklist for moving a case from `dry_run_supported` toward `benchmark_supported`.

Run `make eval-lab-status` for a read-only dashboard of every case's current readiness, and `make eval-benchmark-readiness` for a read-only dashboard of the gap between each case's current evidence and a `benchmark_supported` Result.

Before a benchmark-candidate case's `## Result` is lifted toward `benchmark_supported`, its model-output receipts must pass `make eval-receipt-lint` (full provenance, including the benchmark-only fields), the case must carry a regenerated `receipt-index.yaml` (`make receipt-index`), and an independent judge — not the agent that ran the eval — must have scored it. Receipt lint and the receipt index are read-only; they change no Result.

## Evals are proof-surface artifacts, not world evidence

An eval case tests **model behaviour under a defined condition**. It does not establish that a source card's claim is true, that a tension is resolved, or that any advice is correct. A model output is a test artifact — never an authority, never citable as a source. An eval result is evidence about how a model behaves when given a particular prompt and a particular packet; it is never, on its own, evidence about the world.

This is the failure the Eval Lab exists to prevent: a strong eval score being quietly upgraded into "the substrate is right." It is not. It is "under this case, this model behaved this way."

## Design evidence vs benchmark evidence

Two strengths of evidence, and they must never be conflated.

- **`dry_run_supported`** — the harness and the substrate behave as intended, but the evidence rests wholly or partly on **in-session simulated outputs** (outputs written in-session as a good-faith simulation of how a model would answer). This is *design evidence*: it validates that the case, the rubric, and the substrate work end to end. It informs methodology. It is **not** canon-eligible.
- **`benchmark_supported`** — every output the substrate-vs-baseline comparison rests on is a **real external model run** (local or hosted), recorded with full provenance. This is *benchmark evidence*: evidence that real models behave the way the case predicts.

Only `benchmark_supported` is strong enough to support a canon candidate. Both current contradiction-preservation cases are `dry_run_supported` and carry simulated comparison outputs; they are design evidence only.

## Design cases vs holdout cases

- A **design case** is written, iterated, and exercised while the substrate is being built. Its scenario and rubric may have been shaped with the substrate's strengths in view. Design cases are honest methodology evidence but are vulnerable to teaching-to-the-test.
- A **holdout case** is constructed against criteria fixed *before* the case author sees the substrate's specific content, and is not iterated against substrate outputs. Holdout cases are the stronger evidence that an effect generalises.

A `benchmark_supported` result on a design case is still benchmark evidence about that case, but the score sheet must say the case is a design case so a reader does not over-generalise. The current two cases are design cases.

## The frozen-packet rule

Before a benchmark pass begins, the case packet **freezes**: `case.md`, `score-sheet.md`, the `## Scoring rubric`, `## Positive result`, `## Falsifier`, the Advisor prompt, the model conditions, and the lineage packet. Any edit to a frozen packet starts a new benchmark version — it does not silently re-base the old one. Rubric criteria are never added after outputs are seen. Design iteration happens *before* the freeze, never during the benchmark pass.

## Required conditions

A contradiction-preservation case is run under these conditions:

| Condition | Packet | Role |
|---|---|---|
| `vanilla` | Advisor prompt only. | Baseline. |
| `substrate_workflow` | Advisor prompt plus the reviewed claim/tension card and reviewed source cards named in `case.md` Lineage. | The substrate condition under test. |
| `vanilla_long_prompt` (equal-length control) | A token-matched prompt with **no** reviewed substrate artifacts — filler or unrelated material of the same length as the substrate packet. | Separates the substrate's advantage from a mere more-tokens effect. |
| `famous_sources_supplied` (optional) | Advisor prompt plus name-level awareness of the relevant famous frameworks only — no source cards, no tension card. | Antipattern comparison: tests whether bare famous-name awareness mimics the substrate. |

The **equal-length control is required**, not optional: without it, a substrate win could be explained by prompt length rather than by lineage-grounded content. A case with no `vanilla_long_prompt` / equal-length control cannot reach `benchmark_supported`; `make eval-lab-status` flags its absence. `famous_sources_supplied` is an optional antipattern comparison — useful, but it is not the length control and does not substitute for it.

## Real-run receipt expectations

Every real model run records a receipt under `model-outputs/`, using the fields in `runs/model-outputs/_metadata-template.yaml`. A real-run receipt must carry, at minimum:

- **condition** — `model_condition`.
- **model identity** — `provider`, `model_id` (and `model_snapshot` / version when available), `runtime`.
- **date** — `created`.
- **decoding parameters** — `temperature`, `top_p`, `seed` when the runtime exposes them.
- **prompt hash** — `prompt_sha256` over the exact prompt text.
- **source-packet hash** — `source_packet_sha256` (and `condition_packet_sha256`) over the exact packet supplied for the condition.
- **output path** — `output_file`, and `raw_model_output_public_safe`.

If a hosted API does not expose a field, write `unavailable` and explain in `operator_notes` — never silently omit it. A strong answer with weak receipts is not benchmark evidence. An in-session simulation is labelled as such in its `operator_notes` and never carries a fabricated `runtime` or model snapshot.

## Judge separation and no self-scoring

The model that generates an output must not be the sole judge of that output. For a benchmark pass, the judge is a different model family, a human judge, or a two-judge setup with disagreements escalated to the operator. Judging is rubric-anchored — criterion by criterion against the case's own `## Scoring rubric`, with no ad hoc criteria introduced after outputs are seen. The score sheet records the judge identity (`judge_model_id`, `judge_prompt_sha256`).

In-session design passes that are self-scored are design evidence only; they cannot lift a result past `dry_run_supported`.

## Canon promotion limit

Canon promotion is operator-gated and is a separate, later artifact action. An eval result never promotes itself. A canon candidate that cites an eval result must cite a `benchmark_supported` one, and may cite it only as proof about model behaviour under that eval — not as proof about the world. A `dry_run_supported` result may inform methodology and substrate iteration; it may not back a canon candidate or a "the substrate produces better advice" claim.

`make eval-lab-status` reports readiness; it runs nothing, scores nothing, and promotes nothing.
