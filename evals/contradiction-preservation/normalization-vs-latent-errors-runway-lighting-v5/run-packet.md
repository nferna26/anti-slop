---
case_id: normalization-vs-latent-errors-runway-lighting-v5
artifact: run-packet
eval_type: contradiction-preservation
benchmark_version: normalization-vs-latent-errors-runway-lighting-v5-v1
status: frozen_run_complete_scored
created: 2026-05-23
---

# Run Packet - normalization-vs-latent-errors-runway-lighting-v5-v1

This is the frozen, completed run packet for the v5 runway-lighting
contradiction-preservation case. It records the condition recipes, run
parameters, filler constraints, anonymisation rules, and external-judge plan for
benchmark version `normalization-vs-latent-errors-runway-lighting-v5-v1`.

**Status: frozen run complete and scored.** The operator approved
`judge-packet/calibration-anchors.md` as written and it is now
`status: filled_pre_run`. All five condition packets are assembled and frozen by
hash. Forty real `gemma4:31b` outputs were generated, the condition-blind judge
packet was built, OpenAI and Anthropic API routes calibrated, Anthropic scored
all forty blinded outputs after passing calibration, aggregate-only
reconciliation is complete, and `eval-decision.md` records `do_not_promote`.
OpenAI failed calibration and scored zero real outputs.

This file is operator-facing. It names model conditions and run mechanics. It
must not be shown to blind judges.

## Freeze prerequisites

The following were satisfied before `status` changed to `frozen_inputs_no_run`:

- `judge-packet/calibration-anchors.md` is operator-reviewed and set to
  `status: filled_pre_run`.
- At least two external eligible hosted API judge routes are named before
  generation: OpenAI and Anthropic.
- The `vanilla_long_prompt` filler is generated, scanned, length-matched to the
  `substrate_workflow` added material, and frozen by hash.
- All five condition packets are assembled and frozen by hash.
- The generator model and runtime snapshot are recorded.

## Planned frozen inputs

The frozen pass will cover the case sections in `case.md` from `## Scenario`
through `## Anti-overfitting safeguards`, the declared `model_conditions`, the
reviewed lineage artifacts below, and the operator-accepted calibration anchors.

Lineage artifacts hashed at freeze:

| Artifact | sha256 |
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

Frozen Advisor prompt: 388 words, 2431 characters, sha256
`d2eca36cfadf8d529091720a6374363b1aae6333f637fcb04813fc86790d38c0`. A change
opens a new benchmark version; it must not silently rebase v5-v1.

## Condition packets

Five conditions are declared in `case.md`. Each packet is the named added
material followed by one blank line and the verbatim Advisor prompt. The Advisor
prompt must be byte-identical across conditions.

| Condition | Added material before the Advisor prompt |
| --- | --- |
| `vanilla` | None. Advisor prompt only. |
| `famous_sources_supplied` | Name-level list of relevant famous sources and decoys only; no claims or summaries. |
| `substrate_workflow` | Substrate preamble plus the reviewed tension card and three reviewed source cards. |
| `vanilla_long_prompt` | One-line note plus neutral equal-length filler plus transition. |
| `generic_advice_prompted` | Short generic advice-quality request; no rubric or source content. |

### Packet recipes

- **`vanilla`** - the Advisor prompt verbatim, nothing else.

- **`famous_sources_supplied`** - the frozen preamble below, then a blank line,
  then the Advisor prompt verbatim. The list supplies titles and authors only.
  It states no claim about what any source argues, supplies no source-card or
  tension-card content, marks no source as authoritative, and includes decoys.

  ```text
  The list below names some widely known works on safety, accidents, and
  organisational risk that are sometimes mentioned near questions like the one
  that follows. They are given by title and author only. Nothing here states or
  summarises what any work argues, and nothing here marks any title as relevant
  to, or authoritative for, the question below.

  - The Challenger Launch Decision - Diane Vaughan
  - Human Error - James Reason
  - Normal Accidents - Charles Perrow
  - Managing the Unexpected - Karl Weick and Kathleen Sutcliffe
  - The Field Guide to Understanding Human Error - Sidney Dekker

  The question follows.
  ```

- **`substrate_workflow`** - the frozen preamble below, then a blank line, then
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

- **`vanilla_long_prompt`** - the note below, then a blank line, then neutral
  equal-length filler, then the transition below, then the Advisor prompt
  verbatim. The filler must contain no substrate artifacts, no source names, no
  aviation, safety, accident, risk, runway, airport, lighting, operations,
  management, diagnosis, or decision-advice content.

  Note line: `The text below is unrelated background reading on everyday subjects. It has no connection to the question that follows; it is included only as reading material. The question comes after it.`

  Transition line: `That is the end of the unrelated background reading. The question follows.`

- **`generic_advice_prompted`** - the frozen preamble below, then a blank line,
  then the Advisor prompt verbatim. It must not enumerate the rubric, name the
  two mechanisms, mention contradiction preservation, ask for source lineage, or
  leak the answer key.

  ```text
  Please give careful, practical advice on the question below. Take the
  tradeoffs seriously, explain your reasoning, and be honest about uncertainty.
  The question follows.
  ```

## Equal-length filler requirements

The `vanilla_long_prompt` filler must be generated under the git-ignored
local-only run folder and not committed. It must meet these requirements:

- Distinct, non-repetitive everyday-topic paragraphs.
- Word count matches the `substrate_workflow` added-material word count within
  +/- 8%.
- Zero occurrences of these stems or close variants in the filler body:
  `safe`, `risk`, `accident`, `hazard`, `airport`, `runway`, `taxiway`,
  `crossing`, `tower`, `light`, `stop`, `bar`, `panel`, `ticket`, `relay`,
  `battery`, `voltage`, `operator`, `manage`, `organis`, `normal`, `deviance`,
  `latent`, `defence`, `defense`, `error`, `diagnos`, `decid`, `decision`,
  `advice`, `advise`, `recommend`.
- If the scan is nonzero, discard the filler and regenerate before freeze.

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
  server version `0.24.0`.

## External judge routes

The v5 pass requires at least two eligible external blind judges from different
families/providers. Planned routes:

- Judge A: hosted OpenAI model through the operator-provided OpenAI API key,
  operated by Codex as an accepted hosted API judge route. Planned candidate:
  `gpt-5.4-mini`; the exact model ID, API settings, calibration result, and
  judge independence must be recorded in the judge receipt.
- Judge B: hosted Anthropic model through the operator-provided Anthropic API
  key, operated by Codex as an accepted hosted API judge route. Planned
  candidate: Claude Opus-family hosted model available at judge time; the exact
  model ID, API settings, calibration result, and judge independence must be
  recorded in the judge receipt.

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
- The `OUT-NN` to condition answer key stays local-only and git-ignored.
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
judge-facing files.

## Freeze checklist

These fields were filled before changing `status` to frozen:

| Item | Value |
| --- | --- |
| Calibration-anchor status | `filled_pre_run`, operator-approved as written on 2026-05-23 |
| Calibration-anchor `sha256` | `d0c5f271b79fd052f75e977fc8814dbc9048fff11f246f9114cdfa4e687c16de` |
| Advisor prompt words / characters / `sha256` | 388 / 2431 / `d2eca36cfadf8d529091720a6374363b1aae6333f637fcb04813fc86790d38c0` |
| Generator model and snapshot | `gemma4:31b`; Ollama model ID `6316f0629137`; Ollama server `0.24.0` |
| Judge route A | hosted OpenAI API judge, planned model `gpt-5.4-mini`, reasoning effort `medium`, text verbosity `medium`, calibration first |
| Judge route B | hosted Anthropic API judge, planned Claude Opus-family model selected from API availability at judge time, calibration first |
| `vanilla` packet words / `sha256` | 388 / `d2eca36cfadf8d529091720a6374363b1aae6333f637fcb04813fc86790d38c0` |
| `famous_sources_supplied` packet words / `sha256` | 489 / `7d4f9ec002f539b85219f06e204c6cbd48eb7ee6a6eb3d529f8507892b316c81` |
| `substrate_workflow` packet words / `sha256` | 7962 / `4183c7a2d770b7b6958884bae14efbc50d8718025d071c045a0a61df19013e78` |
| `vanilla_long_prompt` packet words / `sha256` | 8005 / `b6518476357c9997e0d258f69d358af5013b800062ee397caf0af6b92a6aba14` |
| `generic_advice_prompted` packet words / `sha256` | 412 / `8698229be7cd409154cf9d7e1a6a69017e7056b1ba09e5833d88ea8addb37bae` |
| Filler word count and ratio | 7574 words; ratio 1.000 to `substrate_workflow` added material |
| Filler forbidden-vocabulary scan | `{}`; zero forbidden-stem hits |

## Current state

The v5-v1 run is complete and scored. Forty real local generator outputs exist,
eight per frozen condition, with zero deferred outputs and no seed+10 retries.
`judge-packet/output-manifest.yaml` anonymises outputs by body hash and withholds
condition labels. OpenAI `gpt-5.4-mini` failed calibration and has a
calibration-only receipt. Anthropic `claude-opus-4-7` passed calibration, scored
all forty blinded outputs, and has a judge-score receipt. Aggregate-only
reconciliation from committed hashes is recorded in `score-sheet.md`; no
per-`OUT-NN` to condition mapping is committed. `eval-decision.md` records
`eval_decision: do_not_promote` because the Positive-result rule is not met.

## Run completion

| Item | Value |
| --- | --- |
| Output count | 40 real local-model outputs |
| Runs per condition | 8 each for `vanilla`, `famous_sources_supplied`, `substrate_workflow`, `vanilla_long_prompt`, `generic_advice_prompted` |
| Deferred outputs | 0 |
| seed+10 retries | 0 |
| Public receipts | `model-outputs/` and `receipt-index.yaml` |
| Blind packet | `judge-packet/` with `OUT-01` through `OUT-40` and output-body hashes only |

## Judge outcome

| Route | Outcome |
| --- | --- |
| OpenAI API `gpt-5.4-mini` | Calibration failed: 7 criteria differences and Anchor C C5/C6 disagreement; scored zero real outputs. |
| Anthropic API `claude-opus-4-7` | Calibration passed: 1 criteria difference and no Anchor C C5/C6 disagreement; scored all 40 real outputs. |

## Reconciliation outcome

`score-sheet.md` records `Result: partial`. `eval-decision.md` records
`eval_decision: do_not_promote` / `decision_class: insufficient_external_judges`.
The positive rule also fails total-score margin, critical-criterion margin,
judge-level stability, and no-critical-saturation clauses under the eligible
Anthropic scored pass.
