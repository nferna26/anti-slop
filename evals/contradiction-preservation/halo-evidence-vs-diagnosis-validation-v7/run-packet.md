---
case_id: halo-evidence-vs-diagnosis-validation-v7
artifact: run-packet
eval_type: contradiction-preservation
benchmark_version: halo-evidence-vs-diagnosis-validation-v7-v1
status: frozen_run_complete_calibration_failed
created: 2026-05-23
---

# Run Packet - halo-evidence-vs-diagnosis-validation-v7-v1

This is the frozen run packet for the v7 evidence-quality pivot case. It records
the condition recipes, run parameters, filler constraints, anonymisation rules,
and judge plan for benchmark version
`halo-evidence-vs-diagnosis-validation-v7-v1`.

**Status: frozen run complete; judge calibration failed.** The active thread
goal directed Codex to design and execute the v7 pivot plan. Under that directive,
`judge-packet/calibration-anchors.md` was filled pre-run with `status:
filled_pre_run`. All five condition packets were assembled and frozen by hash.
Forty real `gemma4:31b` outputs were generated, public-safe receipts and a
condition-blind `OUT-NN` judge packet were built, and three pre-registered judge
routes calibrated. All three judge routes failed the stricter v7 calibration
gate, so no OUT-NN answers were scored and no aggregate reconciliation was
performed. `eval-decision.md` records `do_not_promote`. No result lift, canon
candidate, public advice claim, or per-`OUT-NN` mapping was created.

This file is operator-facing. It names model conditions and run mechanics. It
must not be shown to blind judges.

## Freeze prerequisites

The following were satisfied before `status` changed to `frozen_inputs_no_run`:

- `judge-packet/calibration-anchors.md` is filled pre-run under the active v7
  execution goal.
- Three judge routes are named before generation: hosted OpenAI, hosted
  Anthropic, and local `gpt-oss:20b` as a non-generator backstop.
- The `vanilla_long_prompt` filler is generated, scanned, length-matched to the
  `substrate_workflow` added material, and frozen by hash.
- All five condition packets are assembled and frozen by hash.
- The generator model and runtime snapshot are recorded.

## Planned frozen inputs

The frozen pass covers the case sections in `case.md` from `## Scenario`
through `## Anti-overfitting safeguards`, the declared `model_conditions`, the
reviewed lineage artifacts below, and the filled calibration anchors.

Lineage artifacts hashed at freeze:

| Artifact | sha256 |
| --- | --- |
| `corpus/source-cards/BK-0048-card-001.md` | `2f11b5e74182d50dbbff87d26f43dd9376e22a6d4aa316a264fd9e2ecf5b476d` |
| `corpus/source-cards/BK-0001-card-001.md` | `1535ee5be11481217f9731d0851b2ffe23f9f61ae1b8b978added09026a9730b` |
| `corpus/source-cards/BK-0007-card-001.md` | `8d7bb540f96f0cc51fd77173c8e02988bdf8ca500fa2507c8f25875bc466251f` |

The draft v7 claim/tension card is pre-work only. It is not in the frozen
lineage packet because it remains `operator_review_status: unreviewed`.

## Advisor prompt

The Advisor prompt is derived deterministically from `case.md` -> `## Advisor
prompt`: take the block-quote lines, remove a leading `> ` from each line, turn
a line that is exactly `>` into an empty line, join with newlines, strip
leading/trailing whitespace, and append one trailing newline.

Frozen Advisor prompt: 391 words, 2636 characters, sha256
`5a42e17859b4a23ae36d2682474f8d0369ffc492c200375fd79a14bf3b322262`. A change
opens a new benchmark version; it must not silently rebase v7-v1.

## Condition packets

Five conditions are declared in `case.md`. Each packet is the named added
material followed by one blank line and the verbatim Advisor prompt. The Advisor
prompt must be byte-identical across conditions.

| Condition | Added material before the Advisor prompt |
| --- | --- |
| `vanilla` | None. Advisor prompt only. |
| `famous_sources_supplied` | Name-level list of relevant famous sources and decoys only; no claims or summaries. |
| `substrate_workflow` | Substrate preamble plus three reviewed source cards. No unreviewed claim/tension card. |
| `vanilla_long_prompt` | One-line note plus neutral equal-length filler plus transition. |
| `generic_advice_prompted` | Short generic advice-quality request; no rubric or source content. |

### Packet recipes

- **`vanilla`** - the Advisor prompt verbatim, nothing else.

- **`famous_sources_supplied`** - a name-level list of famous source titles and
  authors only, then a blank line, then the Advisor prompt verbatim. The list
  states no claim about what any source argues, supplies no source-card content,
  marks no source as authoritative, and includes decoys.

- **`substrate_workflow`** - a substrate preamble, then the three reviewed
  source-card artifacts supplied as their full committed file content behind
  `--- ARTIFACT n of 3 ---` separators in this order: (1)
  `corpus/source-cards/BK-0048-card-001.md`, (2)
  `corpus/source-cards/BK-0001-card-001.md`, (3)
  `corpus/source-cards/BK-0007-card-001.md`; then a transition line, then the
  Advisor prompt verbatim.

- **`vanilla_long_prompt`** - a note that the following text is unrelated
  background reading, then neutral equal-length filler, then a transition, then
  the Advisor prompt verbatim. The filler contains no substrate artifacts, no
  source names, and no business, product, evidence, strategy, customer, revenue,
  sales, support, compliance, auditor, segment, validation, recommendation, or
  decision-advice content.

- **`generic_advice_prompted`** - a short generic advice-quality request, then a
  blank line, then the Advisor prompt verbatim. It does not enumerate the
  rubric, name the target distinction, mention contradiction preservation,
  request source lineage, or leak the answer key.

## Equal-length filler requirements

The `vanilla_long_prompt` filler was generated under the git-ignored local-only
run folder and is not committed. It must meet these requirements:

- Distinct, non-repetitive everyday-topic paragraphs.
- Word count matches the `substrate_workflow` added-material word count within
  +/- 8%.
- Zero occurrences of the forbidden stems recorded in
  `local-only/eval-runs/halo-evidence-vs-diagnosis-validation-v7/v7_pipeline.py`.
- If the scan is nonzero, discard the filler and regenerate before freeze.

## Run parameters

- Run count: eight real runs per condition minimum, five conditions x 8 = 40
  outputs.
- Seeds: condition index follows the declared `model_conditions` order:
  `vanilla` (1), `famous_sources_supplied` (2), `substrate_workflow` (3),
  `vanilla_long_prompt` (4), `generic_advice_prompted` (5). Run `r`, condition
  `i` -> seed `r*100 + i`: 101-105 through 801-805 for the required eight runs.
  A timeout retry uses `seed + 10` and is recorded; no output is fabricated.
- Decoding: generation `temperature 0.7`, `top_p 0.9`, `num_ctx 32768`,
  timeout 600 s, held constant across all conditions and runs.
- Frozen generator: `gemma4:31b`, Ollama model ID `6316f0629137`, local Ollama
  server version `0.24.0`.

## Judge routes

The v7 pass pre-registers three condition-blind judge routes before generation:

- Judge A: hosted OpenAI model through the operator-provided OpenAI API key,
  operated by Codex as an accepted hosted API judge route. Planned candidate:
  `gpt-5.4-mini`; exact model ID, API settings, calibration result, and judge
  independence must be recorded in the judge receipt.
- Judge B: hosted Anthropic model through the operator-provided Anthropic API
  key, operated by Codex as an accepted hosted API judge route. Planned
  candidate: Claude Opus-family hosted model available at judge time; exact
  model ID, API settings, calibration result, and judge independence must be
  recorded in the judge receipt.
- Judge C: local `gpt-oss:20b` through Ollama, operated as a non-generator
  third-family backstop. It is not a hosted API judge and must be recorded as
  such; it counts only if it passes the same calibration gate.

A judge route is not eligible if it is in-session self-judging, authored the
anchors/reference verdicts, saw condition labels or the answer key before
scoring, failed calibration, or belongs to the generator family in a way that
violates the frozen judge protocol.

## Frozen packet hashes

| Item | Value |
| --- | --- |
| Calibration-anchor status | `filled_pre_run`, filled under active v7 execution goal on 2026-05-23 |
| Calibration-anchor `sha256` | `21791726d237b5c518fca6a7205a8803e75a82614039bbf80da78848b2b90511` |
| Advisor prompt words / characters / `sha256` | 391 / 2636 / `5a42e17859b4a23ae36d2682474f8d0369ffc492c200375fd79a14bf3b322262` |
| Generator model and snapshot | `gemma4:31b`; Ollama model ID `6316f0629137`; Ollama server `0.24.0` |
| Judge route A | hosted OpenAI API judge, planned model `gpt-5.4-mini`, reasoning effort `medium`, text verbosity `medium`, calibration first |
| Judge route B | hosted Anthropic API judge, planned Claude Opus-family model selected from API availability at judge time, calibration first |
| Judge route C | local `gpt-oss:20b`, Ollama model ID `17052f91a42e`, calibration first |
| `vanilla` packet words / `sha256` | 391 / `5a42e17859b4a23ae36d2682474f8d0369ffc492c200375fd79a14bf3b322262` |
| `famous_sources_supplied` packet words / `sha256` | 520 / `a8f837584b6b87efa42fb92f178885d67f9a6373379ee1ede9671b0a54d4d2f8` |
| `substrate_workflow` packet words / `sha256` | 4725 / `86235e082879e8119f7adb956d7b870675e03f798daf72f80f32353376157508` |
| `vanilla_long_prompt` packet words / `sha256` | 4768 / `4534e171b8d6f32b6e7785827b181c32158796a35e8ccccf057086ac0f0e43d5` |
| `generic_advice_prompted` packet words / `sha256` | 415 / `5e94f3c66f0dff57d38dd5c747b6fa04e65a3365ab875d68633add0ce68b4ce2` |
| Filler word count and ratio | 4334 words; ratio 1.000 to `substrate_workflow` added material |
| Filler forbidden-vocabulary scan | `{}`; zero forbidden-stem hits |

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

## Run

The v7-v1 generation pass completed with forty real local-model outputs: eight
runs for each of the five frozen conditions, zero simulated outputs, zero
deferred outputs, and zero `seed + 10` retries. Each public-safe model-output
receipt under `model-outputs/` records the condition, run number, seed,
generator identity, decoding settings, Advisor prompt hash, condition packet
hash, and output body. `receipt-index.yaml` indexes the forty receipts.

The condition-blind judge packet was built after generation. Output bodies were
hashed, sorted by `sha256`, and assigned `OUT-01` through `OUT-40`. The
`OUT-NN` to condition/run answer key remains local-only and git-ignored. The
committed judge packet contains no condition labels, seeds, run numbers,
model-output receipt paths, or answer key.

## Judge and reconciliation

All three pre-registered judge routes failed calibration and scored zero real
outputs:

| Judge route | Calibration differences | Critical C3-C6 differences | Noncritical C1/C2 differences | Eligible? | Receipt |
| --- | ---: | ---: | ---: | --- | --- |
| Hosted OpenAI `gpt-5.4-mini` | 6 | 1 | 5 | No | `judge-packet/judge-calibration-openai-gpt-5.4-mini-api.md` |
| Hosted Anthropic `claude-opus-4-7` | 5 | 0 | 5 | No | `judge-packet/judge-calibration-anthropic-claude-opus-4-7-api.md` |
| Local `gpt-oss:20b` | 6 | 1 | 5 | No | `judge-packet/judge-calibration-local-gpt-oss-20b.md` |

No aggregate reconciliation was performed because no eligible judge-score
receipt exists. The positive result cannot be evaluated. The result is
`partial`; `eval-decision.md` records `eval_decision: do_not_promote` /
`decision_class: judge_calibration_failed`.

## Current state

The v7-v1 run is complete through generation and calibration. `score-sheet.md`
records `## Result: partial`; `eval-decision.md` records `do_not_promote` after
all three pre-registered judge routes failed calibration. No OUT-NN answers
were scored, no aggregate condition table was computed, and no
`benchmark_supported` promotion, canon candidate, public advice claim, or
per-`OUT-NN` mapping was created.
