---
case_id: managerial-output-vs-industry-structure
artifact: run-packet
eval_type: contradiction-preservation
frozen: 2026-05-21
---

# Run Packet — managerial-output-vs-industry-structure

Public-safe freeze and run receipt for the contradiction-preservation eval case in this folder. It records the condition packets, their `sha256` hashes, the decoding parameters, and the outcomes of the real-run passes — the first pass and the runs 02/03 repeats. A model output is a test artifact — never an authority and never citable as a source.

**This is not a frozen benchmark pass.** See `## Status` below: the `Result` stays `partial`.

## Freeze

Frozen at `2026-05-21T20:02:30Z`. All hashes are `sha256` over the exact UTF-8 packet text, computed with the Python standard library (`hashlib`) — no third-party tooling.

Frozen for this pass and not edited during it: `case.md`, `score-sheet.md`, the `## Scoring rubric`, `## Positive result`, `## Falsifier`, the Advisor prompt, the `model_conditions` list, and the Lineage packet (the reviewed claim/tension card and the two reviewed source cards). The case design was treated as operator-approved for a first run; all three lineage artifacts are `operator_review_status: reviewed`.

- **Advisor prompt** — `sha256: d2a42fb2cf7a5ac57cd0095a343b2931c723e1ab07cc1cfce50725c404f80e15`; 277 words. Source: `case.md` → `## Advisor prompt` (the block-quote paragraphs with the `> ` prefix stripped).

## Condition packets

| Condition | Packet | Words | sha256 (first 16) | Seed |
|---|---|---|---|---|
| `vanilla` | Advisor prompt only | 277 | `d2a42fb2cf7a5ac5` | 101 |
| `famous_sources_supplied` | Famous-framework preamble + Advisor prompt | 437 | `74d1c708a5552a57` | 102 |
| `substrate_workflow` | Substrate preamble + 3 reviewed artifacts + Advisor prompt | 5285 | `df7988d08e481caf` | 103 |
| `vanilla_long_prompt` | Distinct-filler preamble + 30 distinct filler paragraphs + Advisor prompt | 4854 | `8dc2a0d8b7cab867` | 104 |
| `optional_local_model` | Advisor prompt only (byte-identical to `vanilla`) | 277 | `d2a42fb2cf7a5ac5` | 105 |

Full hashes: `vanilla`/`optional_local_model` `d2a42fb2cf7a5ac57cd0095a343b2931c723e1ab07cc1cfce50725c404f80e15`; `famous_sources_supplied` `74d1c708a5552a5713a16667ae830faf4c8b98c5b153d603815a3dd5e5eaf432`; `substrate_workflow` `df7988d08e481cafa310263694efe3c0c139bb527fd43de4590f4a1351ef3fa4`; `vanilla_long_prompt` `8dc2a0d8b7cab867571503761a65613231c2ef17ac8cd522f7ee99d8f8ae16e0`.

The `substrate_workflow` packet (5285 words) and the equal-length control `vanilla_long_prompt` (4854 words) are token-matched within ~8%, so a `substrate_workflow` advantage over the control would not be a mere prompt-length effect.

### Packet recipes (for reproducibility)

- **`vanilla`** and **`optional_local_model`**: the Advisor prompt verbatim, nothing else. The two packets are byte-identical; `optional_local_model` is, by the case design, a real local-model run on the Advisor prompt only (the same packet as `vanilla`).
- **`famous_sources_supplied`**: a preamble giving name-level awareness of two famous management ideas only — (1) that a manager's true output is the output of the teams the manager runs and influences, not the manager's personal activity; (2) that the long-run profitability achievable in a line of business is governed by the structure of its competitive forces (buyer and supplier power, the threat of entry and of substitutes, rivalry), which sets a ceiling on returns — then a blank line, then the Advisor prompt. Name-level awareness only — no source cards, no claim/tension card, no card text.
- **`substrate_workflow`**: a preamble naming the artifacts and their authority levels (source cards are evidence-level, the claim/tension card synthesis-level, none of it canon, the tension explicitly open), then the three reviewed artifacts supplied verbatim in order — (1) `corpus/claim-tension-cards/managerial-output-vs-industry-structure.md`, (2) `corpus/source-cards/BK-0002-card-001.md`, (3) `corpus/source-cards/BK-0023-card-001.md` — each behind an `--- ARTIFACT n of 3 ---` separator, then a transition line, then the Advisor prompt. The artifact files are the committed public versions at their head as of the freeze.
- **`vanilla_long_prompt`**: a one-line note that unrelated background follows, then **30 distinct, non-repetitive neutral filler paragraphs** — one per everyday topic — then a transition line, then the Advisor prompt. The topics: clouds, rivers, bread baking, brewing tea, coastal-path walking, moon phases, tending a vegetable patch, autumn leaves, snow, tides, morning birdsong, stargazing, pottery, a rainy afternoon, mountain weather, a quiet beach, cycling a country lane, reading paper maps, hand-brewed coffee, woodworking, knitting, a lake at dawn, deserts, a forest floor, kite flying, sandcastles, paper folding, jigsaw puzzles, beekeeping, and shells and pebbles. The runner scanned the assembled filler for the forbidden vocabulary the goal named (management / strategy / competition / industry / branch / distribution / manager / accountability / market / source / framework, and close variants) and recorded zero hits; one occurrence of "manage" in an early build of the filler was reworded before the freeze. The filler is length-matched to the substrate added-material word count (4577 filler added words against 5008 substrate added words). The filler paragraphs are distinct, not repeated, so they do not trigger the generation loop that a repeated-paragraph filler caused in an earlier case.

## Decoding parameters

Model `qwen3.5:latest` run via the Ollama HTTP API (server version 0.24.0), endpoint `/api/chat`, `stream: false`. Decoding: `temperature 0.7`, `top_p 0.9`, per-condition `seed` as in the table above. Per-call timeout 420s.

## Run outcome — first real-run pass, 2026-05-21

Every condition was run as a **real local-model run** against `qwen3.5:latest`. **No condition was simulated**; no output was fabricated. All five completed — none deferred.

| Condition | Outcome | Generation | Tokens (prompt_eval / output) | Output file |
|---|---|---|---|---|
| `vanilla` | real run — OK | 55.1s | 342 / 2880 | `model-outputs/vanilla.md` |
| `famous_sources_supplied` | real run — OK | 83.4s | 524 / 3601 | `model-outputs/famous_sources_supplied.md` |
| `substrate_workflow` | real run — OK | 103.1s | 7566 / 3848 | `model-outputs/substrate_workflow.md` |
| `vanilla_long_prompt` | real run — OK | 72.1s | 5781 / 2657 | `model-outputs/vanilla_long_prompt.md` |
| `optional_local_model` | real run — OK | 89.4s | 342 / 3808 | `model-outputs/optional_local_model.md` |

All five conditions produced real outputs and have model-output files in `model-outputs/`. Each model-output file records its full provenance; the model also emitted a separate reasoning/thinking block per run, captured in the git-ignored local-only run receipts and not reproduced in the public files.

## Repeat runs — runs 02 and 03, 2026-05-21

Two further real local-model repeats were run for each condition, toward the three-repeats-per-condition bar for a benchmark pass. The frozen packet text files from the first pass were reused unchanged; before running, each packet's `sha256` was re-verified against the frozen hashes in `## Condition packets` above — all five matched. Decoding unchanged — `temperature 0.7`, `top_p 0.9`; per-call timeout 420s. Fresh deterministic seeds: run 02 uses `2NN`, run 03 uses `3NN`.

| Condition / run | Seed | Outcome | Generation | Tokens (prompt_eval / output) | Output file |
|---|---|---|---|---|---|
| `vanilla-02` | 201 | real run — OK | 49.2s | 342 / 2480 | `model-outputs/vanilla-02.md` |
| `vanilla-03` | 301 | real run — OK | 60.3s | 342 / 3051 | `model-outputs/vanilla-03.md` |
| `famous_sources_supplied-02` | 202 | real run — OK | 76.4s | 524 / 3429 | `model-outputs/famous_sources_supplied-02.md` |
| `famous_sources_supplied-03` | 302 | real run — OK | 99.5s | 524 / 4480 | `model-outputs/famous_sources_supplied-03.md` |
| `substrate_workflow-02` | 203 | real run — OK | 97.0s | 7566 / 3503 | `model-outputs/substrate_workflow-02.md` |
| `substrate_workflow-03` | 303 | real run — OK | 158.1s | 7566 / 4431 | `model-outputs/substrate_workflow-03.md` |
| `vanilla_long_prompt-02` | 204 | real run — OK | 184.4s | 5781 / 3400 | `model-outputs/vanilla_long_prompt-02.md` |
| `vanilla_long_prompt-03` | 304 | **deferred** — timed out at 420s | — | — | none (not fabricated) |
| `optional_local_model-02` | 205 | real run — OK | 101.8s | 342 / 4657 | `model-outputs/optional_local_model-02.md` |
| `optional_local_model-03` | 305 | real run — OK | 65.1s | 342 / 3121 | `model-outputs/optional_local_model-03.md` |

Nine of the ten repeat runs completed as real local-model runs; **`vanilla_long_prompt-03` (seed 304) timed out at 420s** and is deferred — no output file was written and no output was fabricated. With this pass `vanilla`, `famous_sources_supplied`, `substrate_workflow`, and `optional_local_model` have three completed real runs each; `vanilla_long_prompt` has two (runs 01 and 02). All fourteen completed runs are real; there are no simulations anywhere in this case.

## Judge separation

Generator: `qwen3.5:latest` (local, via Ollama). Judge: Claude Opus 4.7 (`claude-opus-4-7`) — a different model family and provider from the generator, so generation and scoring are performed by separate models. **Limitation:** the judge is the same agent orchestrating these passes; this is model-family separation, not an independent third-party or human judge. No independent human judging occurred. A benchmark pass should add an independent judge per `docs/eval-benchmark-upgrade.md`.

## Status

This is **not** a benchmark pass and does not move the case to `benchmark_supported`. Across three passes, every run completed as a **real local-model run** — there are no in-session simulations anywhere in this case. The `score-sheet.md` `## Result` stays **`partial`**:

- `vanilla`, `famous_sources_supplied`, `substrate_workflow`, and `optional_local_model` have three completed real runs each, but the equal-length control `vanilla_long_prompt` has only two — `vanilla_long_prompt-03` timed out and is deferred — one short of the three-repeats-per-condition bar in `docs/eval-benchmark-upgrade.md`;
- the judge is model-family-separated from the generator but is not an independent third-party judge;
- `dry_run_supported` does not fit either, since that status is defined by in-session simulated outputs and this case has none.

`substrate_workflow` scored 5/5 on all three runs and beats every baseline on every run, including the equal-length control `vanilla_long_prompt` (2/5 on both its runs) by three points, so the substrate advantage is stable across runs and is not a prompt-length effect. Per `docs/eval-result-status-policy.md` a `partial` result informs methodology only and is **not** eligible to support a canon candidate or any "the substrate produces better advice" claim.
