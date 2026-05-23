---
case_id: strategy-diagnosis-vs-structural-positioning
artifact: run-packet
eval_type: contradiction-preservation
frozen: 2026-05-21
---

# Run Packet — strategy-diagnosis-vs-structural-positioning

Public-safe freeze and run receipt for the contradiction-preservation eval case in this folder. It records the condition packets, their `sha256` hashes, the decoding parameters, and the outcomes of the real-run passes — the first pass and the v2 follow-up that completed the two deferred conditions. A model output is a test artifact — never an authority and never citable as a source.

**This is not a frozen benchmark pass.** See `## Status` below: the `Result` stays `partial`.

## Freeze

Frozen at `2026-05-21T14:30:37Z`. All hashes are `sha256` over the exact UTF-8 packet text, computed with the Python standard library (`hashlib`) — no third-party tooling.

Frozen for this pass and not edited during it: `case.md`, `score-sheet.md`, the `## Scoring rubric`, `## Positive result`, `## Falsifier`, the Advisor prompt, the `model_conditions` list, and the Lineage packet (the reviewed claim/tension card and the two reviewed source cards). The pre-run review found no blockers; all three lineage artifacts were confirmed `operator_review_status: reviewed`.

- **Advisor prompt** — `sha256: 1a462aef8cb5e7dd7315530870829df5c6c937623126a82e5c2ed439f0af02dd`; 307 words. Source: `case.md` → `## Advisor prompt` (the four block-quote paragraphs with the `> ` prefix stripped).

## Condition packets

| Condition | Packet | Words | sha256 (first 16) | Seed |
|---|---|---|---|---|
| `vanilla` | Advisor prompt only | 307 | `1a462aef8cb5e7dd` | 101 |
| `famous_sources_supplied` | Famous-framework preamble + Advisor prompt | 466 | `627ef43885c9841e` | 102 |
| `substrate_workflow` | Substrate preamble + 3 reviewed artifacts + Advisor prompt | 5348 | `89425b11beb87130` | 103 |
| `vanilla_long_prompt` | Filler preamble + 41× filler paragraph + Advisor prompt | 5482 | `94b3133ba47bb8d5` | 104 |
| `optional_local_model` | Advisor prompt only (byte-identical to `vanilla`) | 307 | `1a462aef8cb5e7dd` | 105 |

Full hashes: `vanilla`/`optional_local_model` `1a462aef8cb5e7dd7315530870829df5c6c937623126a82e5c2ed439f0af02dd`; `famous_sources_supplied` `627ef43885c9841ec4ecb297c5a51dd20a3dec2513424cf0bc032fd5f8a35319`; `substrate_workflow` `89425b11beb871304fa5229124609718a8778595567261222d8daf58bbf90e84`; `vanilla_long_prompt` `94b3133ba47bb8d500ee8565a5568dbc8ad1524de87bd5fc45c8dfd41877ca64`.

The `substrate_workflow` packet (5348 words) and the equal-length control `vanilla_long_prompt` (5482 words) are token-matched within ~2.5%, so a `substrate_workflow` advantage over the control would not be a mere prompt-length effect.

### Packet recipes (for reproducibility)

- **`vanilla`** and **`optional_local_model`**: the Advisor prompt verbatim, nothing else. The two packets are byte-identical; `optional_local_model` is, by the case design, "a real local-model run on the Advisor prompt only (the same packet as `vanilla`)".
- **`famous_sources_supplied`**: the following preamble, then a blank line, then the Advisor prompt:
  > You are an experienced competitive-strategy advisor. As background, you are aware of two well-known and widely used bodies of strategy thinking, at a general level:
  >
  > 1. One influential idea holds that good strategy begins by diagnosing the single most critical challenge a specific organisation faces — cutting through a confusing situation to name the few factors that genuinely matter — and then building a focused, coherent response around that diagnosis.
  >
  > 2. Another influential idea holds that the long-run profitability of an industry is governed by the structure of its competitive forces — the bargaining power of buyers and of suppliers, the threat of new entrants and of substitute products, and the intensity of rivalry among existing firms — and that competitive strategy should begin from an analysis of that industry structure.
  >
  > Draw on your general knowledge of these and any other strategy ideas as you see fit. Now consider the following request from a business owner and answer it.

  Name-level awareness only — no source cards, no claim/tension card, no card text.
- **`substrate_workflow`**: a preamble naming the artifacts and their authority levels (source cards are evidence-level, the claim/tension card synthesis-level, none of it canon, the tension explicitly open), then the three reviewed artifacts supplied verbatim in order — (1) `corpus/claim-tension-cards/strategy-diagnosis-vs-structural-positioning.md`, (2) `corpus/source-cards/BK-0001-card-001.md`, (3) `corpus/source-cards/BK-0023-card-001.md` — each behind an `--- ARTIFACT n of 3 ---` separator, then a transition line, then the Advisor prompt. The artifact files are the committed public versions at their head as of the freeze.
- **`vanilla_long_prompt`**: a one-line note that unrelated background follows, then 41 numbered repetitions ("Facilities note N.") of the following neutral, unrelated filler paragraph, then a transition line, then the Advisor prompt:
  > The facilities team reviews the building's general maintenance schedule on a regular cycle. Routine tasks include checking that meeting rooms are stocked with basic supplies, confirming that shared printers have paper and toner, testing that the visitor sign-in tablets are charged, and noting which light fixtures in common corridors need a replacement bulb. Heating and ventilation settings are adjusted seasonally, and the team keeps a simple log of when air filters were last changed. Recycling and waste-collection points are emptied on a fixed weekday rotation, and the team confirms that fire-exit routes are clear. None of this work is urgent on any given day, but keeping the log current makes the quarterly facilities review straightforward and avoids small tasks piling up unnoticed.

  The repetition count (41) was chosen by the runner to match the substrate packet's added-material word count.

## Decoding parameters

Model `qwen3.5:latest` run via the Ollama HTTP API (server version 0.24.0), endpoint `/api/chat`, `stream: false`. Decoding: `temperature 0.7`, `top_p 0.9`, per-condition `seed` as in the table above. Per-call timeout 900s.

## Run outcome — first real-run pass, 2026-05-21

Every condition was attempted as a **real local-model run** against `qwen3.5:latest`. **No condition was simulated**; no output was fabricated.

| Condition | Outcome | Generation | Tokens (prompt_eval / output) |
|---|---|---|---|
| `vanilla` | real run — OK | 106.7s | 366 / 5361 |
| `famous_sources_supplied` | real run — OK | 95.9s | 548 / 4418 |
| `substrate_workflow` | real run — OK | 147.2s | 7593 / 6072 |
| `vanilla_long_prompt` | **deferred** — timed out at 900s | — | — |
| `optional_local_model` | **deferred** — timed out at 900s | — | — |

Three conditions produced real outputs and have model-output files in `model-outputs/` (`vanilla.md`, `famous_sources_supplied.md`, `substrate_workflow.md`). Two conditions are deferred and have **no** model-output file — they were not fabricated:

- **`vanilla_long_prompt`** — the call timed out at 900s (Ollama returned HTTP 500 after 15m). The 41× repeated filler paragraph appears to have driven the local model into a degenerate generation/repetition loop. The condition is deferred for this pass. A future pass should build the equal-length control from *non-repetitive* neutral filler (distinct paragraphs rather than one repeated paragraph) so the control is executable on this model; the case design (`case.md`) is unaffected — only the runner's filler construction needs to change.
- **`optional_local_model`** — the call timed out at 900s the same way (HTTP 500 after 15m), on `seed 105` of the small Advisor-prompt-only packet; this looks like a seed-specific generation loop, since the byte-identical `vanilla` packet completed normally on `seed 101` in 106.7s. The condition is deferred for this pass. Its role is not lost: `optional_local_model` exists to record "a real local-model run on the Advisor prompt only", and in this pass every condition's generator was the local model — so the `vanilla` run is itself a real local-model run on exactly that packet. The deferral leaves no gap in the real-local-model baseline.

## v2 pass — distinct-filler equal-length control and optional_local_model retry, 2026-05-21

The two conditions deferred in the first pass were re-attempted as real local-model runs. The case design (`case.md`) — scenario, Advisor prompt, rubric, Positive result, Falsifier, Lineage — was not changed; only the runner's construction of the `vanilla_long_prompt` filler was fixed, and `optional_local_model` was retried on a fresh seed.

Frozen at `2026-05-21T16:18:45Z` (v2). Decoding unchanged — `temperature 0.7`, `top_p 0.9`; per-call timeout 420s.

| Condition | Packet | Words | sha256 (first 16) | Seed | Outcome | Generation | Tokens (prompt_eval / output) | Output file |
|---|---|---|---|---|---|---|---|---|
| `vanilla_long_prompt` (v2) | Distinct-filler preamble + 30 distinct filler paragraphs + Advisor prompt | 4889 | `8cc61ae2c0390ae4` | 104 | real run — OK | 278.3s | 5815 / 10697 | `model-outputs/vanilla_long_prompt.md` |
| `optional_local_model` (retry) | Advisor prompt only (byte-identical to `vanilla`) | 307 | `1a462aef8cb5e7dd` | 205 | real run — OK | 131.3s | 366 / 5241 | `model-outputs/optional_local_model.md` |

Full hashes: `vanilla_long_prompt` (v2) `8cc61ae2c0390ae46a94b4948b870a846a0de84bd53320d88128784de344b8c4`; `optional_local_model` `1a462aef8cb5e7dd7315530870829df5c6c937623126a82e5c2ed439f0af02dd` (the Advisor-prompt-only packet, unchanged from the frozen `vanilla` packet).

**`vanilla_long_prompt` v2 packet recipe.** The v1 control packet — 41 repetitions of one identical filler paragraph — drove the local model into a generation loop and timed out. The v2 packet replaces it with **30 distinct neutral filler paragraphs**, one per everyday topic, none repeated: clouds, rivers, bread baking, brewing tea, coastal-path walking, moon phases, tending a vegetable patch, autumn leaves, snow, tides, morning birdsong, stargazing, pottery, a rainy afternoon, mountain weather, a quiet beach, cycling a country lane, reading paper maps, hand-brewed coffee, woodworking, knitting, a lake at dawn, deserts, a forest floor, kite flying, sandcastles, paper folding, jigsaw puzzles, beekeeping, and shells and pebbles. The filler is unrelated to strategy, competition, markets, organisations, diagnosis, industry structure, lighting, pricing, buyers, suppliers, and management, and contains no source names, book titles, card IDs, or framework labels. The packet is a short preamble noting that unrelated background follows, the 30 numbered paragraphs, a transition line, and the Advisor prompt. The v2 control packet is 4889 words against the `substrate_workflow` packet's 5348 — reasonably length-matched (~91%). The v2 distinct filler completed cleanly in 278.3s with no loop.

**`optional_local_model` retry.** The first attempt (`seed 105`) timed out at 900s on a seed-specific generation loop. The retry on `seed 205` of the same byte-identical Advisor-prompt-only packet completed normally in 131.3s.

Both v2 runs are real local-model runs against `qwen3.5:latest` via Ollama (server 0.24.0); neither was simulated and no output was fabricated. With this pass all five `model_conditions` have a real model-output file.

## Judge separation

Generator: `qwen3.5:latest` (local, via Ollama). Judge: Claude Opus 4.7 (`claude-opus-4-7`) — a different model family and provider from the generator, so generation and scoring are performed by separate models. **Limitation:** the judge is the same agent orchestrating these passes; this is model-family separation, not an independent third-party or human judge. A benchmark pass should add an independent judge per `docs/eval-benchmark-upgrade.md`.

## Status

This is **not** a benchmark pass and does not move the case to `benchmark_supported`. With the v2 pass, all five `model_conditions` have completed as **real local-model runs** — there are no in-session simulations anywhere in the case. The `score-sheet.md` `## Result` stays **`partial`**:

- the runs are single — one real run per condition — and a benchmark pass needs at least three repeats per condition (`docs/eval-benchmark-upgrade.md`);
- the judge is model-family-separated from the generator but is not an independent third-party judge;
- `dry_run_supported` does not fit either, since that status is defined by in-session simulated outputs and this case has none — the evidence is all-real but single-run, which is mid-evaluation toward a benchmark, i.e. `partial`.

`substrate_workflow` (5/5) beats every baseline, including the equal-length control `vanilla_long_prompt` (3/5) by two points, so the substrate advantage on this pass is not explained by prompt length. Per `docs/eval-result-status-policy.md` a `partial` result informs methodology only and is **not** eligible to support a canon candidate or any "the substrate produces better advice" claim.
