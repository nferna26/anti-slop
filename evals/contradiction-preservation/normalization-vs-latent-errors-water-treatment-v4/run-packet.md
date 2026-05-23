---
case_id: normalization-vs-latent-errors-water-treatment-v4
artifact: run-packet
eval_type: contradiction-preservation
benchmark_version: normalization-vs-latent-errors-water-treatment-v4-v1
status: frozen_inputs_no_run
created: 2026-05-22
---

# Run Packet — normalization-vs-latent-errors-water-treatment-v4-v1

This is the frozen run packet for the v4 water-treatment contradiction
preservation case. It records the condition recipes, run parameters, filler
constraints, anonymisation rules, and external-judge plan for benchmark version
`normalization-vs-latent-errors-water-treatment-v4-v1`.

**Status: frozen inputs — not run.** The calibration anchors are
operator-accepted (`status: filled_pre_run`), the condition packets and
equal-length filler are frozen by hash, the generator/runtime snapshot is
recorded, and two external judge routes are named before generation. Output
generation may begin against this frozen packet, but no v4 model output, judge
score, reconciliation, eval decision, `## Result` lift, or canon claim exists
yet.

This file is operator-facing. It names model conditions and run mechanics. It
must not be shown to blind judges.

## Freeze prerequisites

The following were satisfied before `status` changed to `frozen_inputs_no_run`:

- `judge-packet/calibration-anchors.md` is operator-reviewed and set to
  `status: filled_pre_run`.
- At least two external eligible judge routes are named before generation. A
  judge route counts only if it is external to the orchestrating agent and did
  not author the v4 scenario, rubric, anchors, condition packets, or judge
  packet.
- The `vanilla_long_prompt` filler and condition packets below were
  accepted unchanged at freeze and reverified.
- The generator model and runtime snapshot are recorded.

## Frozen inputs

The frozen pass covers the case sections in `case.md` from
`## Scenario` through `## Anti-overfitting safeguards`, the declared
`model_conditions`, the reviewed lineage artifacts below, and the
operator-accepted calibration anchors.

Frozen lineage artifact `sha256`:

| Artifact | `sha256` |
| --- | --- |
| `corpus/claim-tension-cards/normalization-of-deviance-vs-latent-errors.md` | `f2741f834d5f7b3f21030339821040720b5d38a09a551603fcdc6004a1263dc1` |
| `corpus/source-cards/BK-0042-card-001.md` | `4b747866b13911b347d1a3acde4f98f7ba3577be978345818b7279464aad57c2` |
| `corpus/source-cards/BK-0044-card-001.md` | `e2a9014d3668ecf18ff3a82a685bf6d441a4ebb37f43e3500fe74900ba08c597` |
| `corpus/source-cards/BK-0044-card-002.md` | `20d496fec3e4aecf9ed38504bfedd82818da5f3a5d4704992f8d4c43fde9284f` |

## Advisor prompt

The Advisor prompt is derived deterministically from `case.md` -> `## Advisor
prompt`: take the block-quote lines, remove a leading `> ` from each line, turn
a line that is exactly `>` into an empty line, join with newlines, strip
leading/trailing whitespace, and append one trailing newline.

- Words: 311.
- Characters: 2024.
- `advisor_prompt_sha256`: `6844cf29154c9f73180d42ea5b7b83f475a0bada9ac7661eec61fbacfce5658f`.

At freeze and before every generation call, this hash must be recomputed. A
change opens a new benchmark version; it must not silently rebase v4-v1.

## Condition packets

Five conditions are declared in `case.md`. Each packet is the named added
material followed by one blank line and the verbatim Advisor prompt. The Advisor
prompt is byte-identical across conditions.

| Condition | Added material before the Advisor prompt |
| --- | --- |
| `vanilla` | None. Advisor prompt only. |
| `famous_sources_supplied` | Name-level list of relevant famous sources and decoys only; no claims or summaries. |
| `substrate_workflow` | Substrate preamble plus the reviewed tension card and three reviewed source cards. |
| `vanilla_long_prompt` | One-line note plus neutral equal-length filler plus transition. |
| `generic_advice_prompted` | Short generic advice-quality request; no rubric or source content. |

### Packet recipes

- **`vanilla`** — the Advisor prompt verbatim, nothing else.

- **`famous_sources_supplied`** — the frozen preamble below, then a blank line,
  then the Advisor prompt verbatim. The list supplies titles and authors only.
  It states no claim about what any source argues, supplies no source-card or
  tension-card content, marks no source as authoritative, and includes decoys.

  ```text
  The list below names some widely known works on safety, accidents, and
  organisational risk that are sometimes mentioned near questions like the one
  that follows. They are given by title and author only. Nothing here states or
  summarises what any work argues, and nothing here marks any title as relevant
  to, or authoritative for, the question below.

  - The Challenger Launch Decision — Diane Vaughan
  - Normal Accidents — Charles Perrow
  - Human Error — James Reason
  - Managing the Unexpected — Karl Weick and Kathleen Sutcliffe
  - The Field Guide to Understanding Human Error — Sidney Dekker

  The question follows.
  ```

- **`substrate_workflow`** — the frozen preamble below, then a blank line, then
  the four reviewed artifacts supplied as their full committed file content
  behind `--- ARTIFACT n of 4 ---` separators in this order: (1)
  `corpus/claim-tension-cards/normalization-of-deviance-vs-latent-errors.md`,
  (2) `corpus/source-cards/BK-0042-card-001.md`, (3)
  `corpus/source-cards/BK-0044-card-001.md`, (4)
  `corpus/source-cards/BK-0044-card-002.md`; then the transition line below;
  then the Advisor prompt verbatim.

  Preamble:
  ```text
  The reviewed artifacts below come from a public-safe knowledge base and may be
  useful background for the question that follows. Three are source cards:
  each is an evidence-level note that records one reviewed claim with a locator,
  paraphrase, scope conditions, and misuse risks. One is a claim/tension card:
  a synthesis-level note that relates reviewed source-card claims while keeping
  the tension open. None of these artifacts is canon, none is authoritative, and
  none settles the operational decision. Use them as evidence aids only. The
  question follows after the artifacts.
  ```

  Transition line: `That is the end of the reviewed artifacts. The question follows.`

- **`vanilla_long_prompt`** — the note below, then a blank line, then neutral
  equal-length filler, then the transition below, then the Advisor prompt
  verbatim. The filler must contain no substrate artifacts, no source names, no
  safety/water/utility/accident/risk content, and no advice-like content.

  Note line: `The text below is unrelated background reading on everyday subjects. It has no connection to the question that follows; it is included only as reading material. The question comes after it.`

  Transition line: `That is the end of the unrelated background reading. The question follows.`

- **`generic_advice_prompted`** — the frozen preamble below, then a blank line,
  then the Advisor prompt verbatim. It must not enumerate the rubric, name the
  two mechanisms, mention contradiction preservation, ask for source lineage, or
  leak the answer key.

  ```text
  Please give careful, practical advice on the question below. Take the
  tradeoffs seriously, explain your reasoning, and be honest about uncertainty.
  The question follows.
  ```

## Equal-length filler requirements

The `vanilla_long_prompt` filler is held in the git-ignored local-only run
folder and is not committed. It must meet these requirements:

- Distinct, non-repetitive everyday-topic paragraphs.
- Word count matches the `substrate_workflow` added-material word count within
  ±8%.
- Zero occurrences of these stems or close variants in the filler body:
  `safe`, `risk`, `accident`, `hazard`, `water`, `plant`, `utility`, `alarm`,
  `signal`, `filter`, `operator`, `manage`, `organis`, `normal`, `deviance`,
  `latent`, `defence`, `defense`, `error`, `diagnos`, `decid`, `decision`,
  `advice`, `advise`, `recommend`.
- If the scan is nonzero, discard the filler and regenerate before freeze.

Frozen filler:

- Filler word count: 7570.
- `substrate_workflow` added-material word count: 7570.
- Ratio: 100.0% — within the 92.0% to 108.0% band.
- Forbidden-vocabulary scan: clean — zero hits across all listed stems.
- Filler `sha256`: `5e5f576b7880948cf7b3deffe971e0267df2b78ac3298242ec129b0bbe7c1e2c`.

The frozen filler and assembled condition packets are stored under the
git-ignored local-only run folder. The public freeze record is the recipe plus
hashes in this run packet.

## Frozen packet hashes

The packets were assembled from this run packet's recipes, the current
`case.md`, the current reviewed lineage artifacts, and the local-only
equal-length filler. These are the frozen benchmark hashes for v4-v1. The
generation harness must reverify each hash before every model call.

| Condition | Words | Frozen `sha256` |
| --- | ---: | --- |
| `vanilla` | 311 | `6844cf29154c9f73180d42ea5b7b83f475a0bada9ac7661eec61fbacfce5658f` |
| `famous_sources_supplied` | 412 | `606153e13082e1c83c12be2e8160f7709dbc3524688ae6ca06a679348ff639e1` |
| `substrate_workflow` | 7881 | `ea7aaa8b6ca603d18e000a32d4f9bbda8422d472ea0b17fcb596763d4d014ead` |
| `vanilla_long_prompt` | 7924 | `ec7a3a322a052431322b28c217f06fe749c1e6a477fcf781564f058e32b8a441` |
| `generic_advice_prompted` | 335 | `09689f074da86aacaebe20292d529da17dd8ccda9f7a7d28caac79dbed0c1778` |

## Run parameters

- Run count: eight real runs per condition minimum, five conditions x 8 = 40
  outputs. Ten runs per condition may be used only if recorded before freeze.
- Seeds: condition index follows the declared `model_conditions` order:
  `vanilla` (1), `famous_sources_supplied` (2), `substrate_workflow` (3),
  `vanilla_long_prompt` (4), `generic_advice_prompted` (5). Run `r`, condition
  `i` -> seed `r*100 + i`: 101-105 through 801-805 for the required eight runs.
  A timeout retry uses `seed + 10` and is recorded; no output is fabricated.
- Decoding: generation `temperature 0.7`, `top_p 0.9`, `num_ctx 32768`,
  timeout 600 s, held constant across all conditions and runs.
- Frozen generator: `gemma4:31b`, Ollama model ID `6316f0629137`, local Ollama
  server version `0.24.0` (CLI client reported `0.19.0`). This generator is held
  constant across all conditions for v4-v1.

## External judge routes

The v4 pass requires at least two eligible external blind judges from different
families/providers. Frozen routes named before generation:

- Judge A: hosted OpenAI model, operated by the human operator outside the
  orchestration session. Planned candidate: `gpt-5.4-mini`; the exact model ID,
  API/workbench settings, calibration result, and judge independence must be
  recorded in the judge receipt.
- Judge B: hosted Anthropic model, operated by the human operator outside the
  orchestration session and not as an in-session Claude Code self-judge. Planned
  candidate: Claude Opus-family hosted model available at judge time; the exact
  model ID, API/workbench settings, calibration result, and judge independence
  must be recorded in the judge receipt.

A judge route is not eligible if it is in-session self-judging, authored the
anchors/reference verdicts, saw condition labels or the answer key before
scoring, failed calibration, or belongs to the generator family in a way that
violates the frozen judge protocol.

## Output, anonymisation, and answer key

- One public-safe model-output receipt per run under `model-outputs/`, with full
  benchmark provenance per `runs/model-outputs/_metadata-template.yaml`.
- Real outputs only; no simulations in the comparison set.
- After all outputs exist and before any judge sees them, hash each output body
  with `sha256`, sort ascending, and assign `OUT-01` through `OUT-NN`.
- The `OUT-NN` to condition answer key stays local-only and git-ignored. It is
  read only after all blind scoring is complete.
- Committed reconciliation is aggregate-only; no per-`OUT-NN` to condition
  mapping is committed.

## Judge-packet structure

After outputs are generated and anonymised, build a condition-blind
`judge-packet/` containing:

- `README.md`;
- `judge-instructions.md`;
- `case-context.md`;
- `rubric.md`;
- `calibration-exercise.md` containing only Surface 1 anchors;
- `output-manifest.yaml` with `OUT-NN` hashes but no conditions;
- `blank-score-sheet.md`;
- `outputs/OUT-01.md` through `outputs/OUT-NN.md`.

Do not copy Surface 2 reference verdicts, condition labels, seeds, run numbers,
model-output receipt paths, source-card IDs as metadata, or the answer key into
judge-facing files. If a model output body itself mentions a source ID, leave
the body unchanged and record that it is output text, not packet metadata.

## Freeze checklist

Fill these fields before changing `status` to frozen:

| Item | Value |
| --- | --- |
| Calibration-anchor status | `filled_pre_run`, operator-approved on 2026-05-22 |
| Calibration-anchor `sha256` | `99a624bd7186b8a2f9918045becc245f9ff5c01db18662ce50bf158464a41923` |
| Generator model and snapshot | `gemma4:31b`, Ollama model ID `6316f0629137`, local Ollama server `0.24.0` |
| Judge route A | hosted OpenAI `gpt-5.4-mini` candidate, human-operator run outside orchestration; exact model/settings recorded in judge receipt |
| Judge route B | hosted Anthropic Claude Opus-family candidate, human-operator run outside orchestration and not in-session self-judging; exact model/settings recorded in judge receipt |
| `vanilla` packet words / `sha256` | frozen 311 / `6844cf29154c9f73180d42ea5b7b83f475a0bada9ac7661eec61fbacfce5658f` |
| `famous_sources_supplied` packet words / `sha256` | frozen 412 / `606153e13082e1c83c12be2e8160f7709dbc3524688ae6ca06a679348ff639e1` |
| `substrate_workflow` packet words / `sha256` | frozen 7881 / `ea7aaa8b6ca603d18e000a32d4f9bbda8422d472ea0b17fcb596763d4d014ead` |
| `vanilla_long_prompt` packet words / `sha256` | frozen 7924 / `ec7a3a322a052431322b28c217f06fe749c1e6a477fcf781564f058e32b8a441` |
| `generic_advice_prompted` packet words / `sha256` | frozen 335 / `09689f074da86aacaebe20292d529da17dd8ccda9f7a7d28caac79dbed0c1778` |
| Filler word count and ratio | frozen 7570 vs 7570, 100.0% |
| Filler forbidden-vocabulary scan | frozen clean, zero hits |

## Current state

The v4-v1 inputs are frozen and local packet verification passes. The next step
is to generate forty real model outputs using the frozen generator and packet
hashes, then build the condition-blind judge packet. No output has been generated
yet, and no judging, scoring, reconciliation, eval decision, `## Result` lift,
canon candidate, or public claim exists.
