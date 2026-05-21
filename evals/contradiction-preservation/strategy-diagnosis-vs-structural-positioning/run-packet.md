---
case_id: strategy-diagnosis-vs-structural-positioning
artifact: run-packet
eval_type: contradiction-preservation
frozen: 2026-05-21
---

# Run Packet — strategy-diagnosis-vs-structural-positioning

Public-safe freeze and run receipt for the contradiction-preservation eval case in this folder. It records the condition packets, their `sha256` hashes, the decoding parameters, and the outcome of the first real-run pass. A model output is a test artifact — never an authority and never citable as a source.

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

## Judge separation

Generator: `qwen3.5:latest` (local, via Ollama). Judge: Claude Opus 4.7 (`claude-opus-4-7`) — a different model family and provider from the generator, so generation and scoring are performed by separate models. **Limitation:** the judge is the same agent orchestrating this pass; this is model-family separation, not an independent third-party or human judge. A benchmark pass should add an independent judge per `docs/eval-benchmark-upgrade.md`.

## Status

This pass is **not** a benchmark pass and does not move the case toward `benchmark_supported`. The `score-sheet.md` `## Result` stays **`partial`**:

- only 3 of 5 conditions produced real outputs (the equal-length control `vanilla_long_prompt` is deferred, so a `substrate_workflow` advantage cannot yet be separated from a prompt-length effect — see `case.md` → `## Falsifier`);
- the runs are single (a benchmark pass needs at least three repeats per condition);
- the packet is frozen here, but real outputs, repeat runs, an independent judge, and the equal-length control are still required.

The three real outputs are all genuine local-model runs (no in-session simulations); per `docs/eval-result-status-policy.md` the evidence informs methodology only and is **not** eligible to support a canon candidate or any "the substrate produces better advice" claim.
