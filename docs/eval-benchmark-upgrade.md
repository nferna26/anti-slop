# Eval Benchmark Upgrade Path

This document turns `docs/eval-result-status-policy.md` into an operating plan for moving a case from `dry_run_supported` toward `benchmark_supported`. The wider operating frame for the proof surface — design vs benchmark evidence, design vs holdout cases, required conditions, and judge separation — is `docs/eval-lab-protocol.md`; `make eval-lab-status` reports which cases still need this upgrade, and `make eval-benchmark-readiness` reports, per case, the specific gap list between its current evidence and `benchmark_supported` (real-vs-simulated outputs, repeat-run count, equal-length control, and the independent-judge requirement).

A benchmark candidate is not ready for a `## Result` lift until its model-output receipts pass `make eval-receipt-lint` (every base and benchmark-only provenance field present), the case carries a regenerated `receipt-index.yaml` (`make receipt-index`), and an independent judge — not the agent that ran the eval — has scored it. These are read-only auditing aids; they change no Result and promote nothing.

The current contradiction-preservation cases are useful methodology evidence, but not canon-relevant benchmark evidence:

- `evals/contradiction-preservation/diagnosis-vs-validated-learning/` — `dry_run_supported`
- `evals/contradiction-preservation/normalization-vs-latent-errors/` — `dry_run_supported`

Both include in-session simulated comparison outputs. Those must be replaced or supplemented by real model runs before the cases can support a benchmark claim.

## Non-Negotiables

- Model outputs are test artifacts, never authorities.
- A benchmark result does not become canon by itself.
- Eval prompts, source packets, rubrics, and scoring rules freeze before benchmark runs begin.
- The model that generates an output should not be the sole judge of that output.
- Receipt consistency is part of the evidence. A strong answer with weak receipts is not benchmark evidence.

## Minimum Case-Level Upgrade

A single case may move from `dry_run_supported` toward `benchmark_supported` only after all of these are true:

1. **Frozen case packet.** `case.md`, `score-sheet.md`, rubric, Positive result, Falsifier, Advisor prompt, model conditions, and lineage packet are frozen for the benchmark pass. Any later edit starts a new benchmark version.
2. **Real outputs for every comparison.** Every condition the substrate-vs-baseline comparison depends on is run as a real local or hosted model call. In-session simulations may remain as historical dry-run receipts, but they do not count toward `benchmark_supported`.
3. **Exact run provenance.** Each model-output file records provider/runtime, exact model ID, model snapshot or version when available, date, temperature/top-p/seed when available, prompt source, prompt hash, source-packet hash, and output path.
4. **Repeat runs.** Run at least three outputs per required condition for the case-level benchmark pass. Prefer five when cost allows. Single-run results stay methodologically useful but fragile.
5. **Judge separation.** A judge must be separate from the generator. Prefer a different model family, a human judge, or a two-judge setup with disagreements escalated to the operator.
6. **Rubric-anchored judging.** Judge against the case's own `## Scoring rubric`, criterion by criterion. Do not add ad hoc criteria after seeing outputs.
7. **Receipt consistency.** `case.md`, `score-sheet.md`, model-output files, run metadata, and `kb/log.md` agree on what ran, what was scored, dry-run vs real-run status, and Result status.
8. **No critical substrate failure.** A substrate output with hidden canon, bad lineage, or flattened tension fails even if its total score is high.

If any requirement is missing, keep the case at `dry_run_supported`, `partial`, `inconclusive`, or `falsified` as appropriate.

## Recommended Conditions

For contradiction-preservation cases, keep these conditions unless the case explicitly says otherwise:

| Condition | Packet |
|---|---|
| `vanilla` | Advisor prompt only. |
| `famous_sources_supplied` | Advisor prompt plus name-level awareness of relevant famous frameworks only. No source cards or tension cards. |
| `substrate_workflow` | Advisor prompt plus the reviewed claim/tension card and reviewed source cards named in `case.md` Lineage. |
| `optional_local_model` | Same packet as `vanilla`, unless the case defines another local-model condition. |

Add `vanilla_long_prompt` only when testing whether the substrate's advantage is just more tokens rather than better lineage. Its packet should be token-matched but must not include reviewed substrate artifacts.

## Receipt Fields

Future model-output receipts should fill the expanded `runs/model-outputs/_metadata-template.yaml` fields:

- run identity: `run_id`, `created`, `eval_type`, `case_id`, `model_condition`
- model identity: `provider`, `runtime`, `model_name`, `model_id`, `model_snapshot`
- decoding: `temperature`, `top_p`, `seed`
- packet identity: `prompt_source`, `prompt_sha256`, `source_packet`, `source_packet_sha256`, `condition_packet_sha256`
- output identity: `output_file`, `raw_model_output_public_safe`
- judgment identity when scored: `judge_model_id`, `judge_prompt_sha256`, `judge_notes_source`

Hosted APIs may not expose every field. If unavailable, write `unavailable` and explain why in `operator_notes`; do not silently omit it.

## Current Two-Case Upgrade Tasks

For `diagnosis-vs-validated-learning`:

- Freeze a benchmark version of the case packet.
- Replace or supplement the six in-session simulated outputs with real model runs.
- Add at least two additional real `optional_local_model` repeats, or explicitly scope the benchmark to hosted conditions only.
- Re-score with judge separation and preserve the dry-run outputs as historical receipts.

For `normalization-vs-latent-errors`:

- Freeze a benchmark version of the case packet.
- Replace or supplement the three in-session simulated outputs with real model runs.
- Add at least two additional real `optional_local_model` repeats, or explicitly scope the benchmark to hosted conditions only.
- Re-score with judge separation and preserve the dry-run outputs as historical receipts.

## Promotion Discipline

`benchmark_supported` means the case has real benchmark evidence that the substrate beat the defined baselines under the case's rubric. It does not mean:

- the source-card claims are canon;
- the tension is resolved;
- the system should advise from the eval directly;
- a canon candidate may skip its own review.

A canon candidate may cite a `benchmark_supported` eval only as proof about model behavior under that eval, not as proof about the world.
