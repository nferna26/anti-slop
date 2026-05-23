---
case_id: normalization-vs-latent-errors-print-vault-v6
artifact: run-packet
eval_type: contradiction-preservation
benchmark_version: normalization-vs-latent-errors-print-vault-v6-v1
status: frozen_run_complete_scored
created: 2026-05-23
---

# Run Packet - normalization-vs-latent-errors-print-vault-v6-v1

This is the frozen run packet for the v6 print-vault contradiction-preservation
case. It records the condition recipes, run parameters, filler constraints,
anonymisation rules, and external-judge plan for benchmark version
`normalization-vs-latent-errors-print-vault-v6-v1`.

**Status: frozen run complete and scored.** The operator directed Codex to
design and execute v6 without stopping for a separate approval turn. Under that
active directive, `judge-packet/calibration-anchors.md` was filled pre-run with
`status: filled_pre_run`. All five condition packets were assembled and frozen
by hash. Forty real `gemma4:31b` outputs were generated, the condition-blind
judge packet was built, OpenAI and Anthropic API routes calibrated, Anthropic
scored all forty blinded outputs after passing calibration, aggregate-only
reconciliation is complete, and `eval-decision.md` records `do_not_promote`.
OpenAI failed calibration and scored zero real outputs.

This file is operator-facing. It names model conditions and run mechanics. It
must not be shown to blind judges.

## Freeze prerequisites

The following were satisfied before `status` changed to `frozen_inputs_no_run`:

- `judge-packet/calibration-anchors.md` is filled pre-run under the operator's
  active no-stop v6 execution directive.
- At least two external eligible hosted API judge routes are named before
  generation: OpenAI and Anthropic.
- The `vanilla_long_prompt` filler is generated, scanned, length-matched to the
  `substrate_workflow` added material, and frozen by hash.
- All five condition packets are assembled and frozen by hash.
- The generator model and runtime snapshot are recorded.

## Planned frozen inputs

The frozen pass will cover the case sections in `case.md` from `## Scenario`
through `## Anti-overfitting safeguards`, the declared `model_conditions`, the
reviewed lineage artifacts below, and the filled calibration anchors.

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

Frozen Advisor prompt: 454 words, 2866 characters, sha256
`47e70d50741535d08f44f13a5a4d15abdbe7d15b552678359c585331cabff5c6`. A change
opens a new benchmark version; it must not silently rebase v6-v1.

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

- **`famous_sources_supplied`** - a name-level list of famous source titles and
  authors only, then a blank line, then the Advisor prompt verbatim. The list
  states no claim about what any source argues, supplies no source-card or
  tension-card content, marks no source as authoritative, and includes decoys.

- **`substrate_workflow`** - a substrate preamble, then the four reviewed
  artifacts supplied as their full committed file content behind
  `--- ARTIFACT n of 4 ---` separators in this order: (1)
  `corpus/claim-tension-cards/normalization-of-deviance-vs-latent-errors.md`,
  (2) `corpus/source-cards/BK-0042-card-001.md`, (3)
  `corpus/source-cards/BK-0044-card-001.md`, (4)
  `corpus/source-cards/BK-0044-card-002.md`; then a transition line, then the
  Advisor prompt verbatim.

- **`vanilla_long_prompt`** - a note that the following text is unrelated
  background reading, then neutral equal-length filler, then a transition, then
  the Advisor prompt verbatim. The filler contains no substrate artifacts, no
  source names, and no museum, collections, humidity, storage, safety, accident,
  risk, operations, management, diagnosis, or decision-advice content.

- **`generic_advice_prompted`** - a short generic advice-quality request, then a
  blank line, then the Advisor prompt verbatim. It does not enumerate the rubric,
  name the two mechanisms, mention contradiction preservation, ask for source
  lineage, or leak the answer key.

## Equal-length filler requirements

The `vanilla_long_prompt` filler was generated under the git-ignored local-only
run folder and is not committed. It must meet these requirements:

- Distinct, non-repetitive everyday-topic paragraphs.
- Word count matches the `substrate_workflow` added-material word count within
  +/- 8%.
- Zero occurrences of these stems or close variants in the filler body:
  `safe`, `risk`, `accident`, `hazard`, `museum`, `vault`, `print`,
  `collection`, `gallery`, `humid`, `dry`, `moist`, `mold`, `foxing`, `paper`,
  `storage`, `cart`, `door`, `vestibule`, `curtain`, `dehumid`, `pump`,
  `damper`, `actuator`, `pressure`, `sensor`, `dashboard`, `notice`,
  `exception`, `hygrometer`, `registrar`, `conservator`, `operator`, `manage`,
  `organis`, `normal`, `deviance`, `latent`, `defence`, `defense`, `error`,
  `diagnos`, `decid`, `decision`, `advice`, `advise`, `recommend`.
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

The v6 pass requires at least two eligible external blind judges from different
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
| Calibration-anchor status | `filled_pre_run`, filled under operator no-stop v6 execution directive on 2026-05-23 |
| Calibration-anchor `sha256` | `208c45a5961334b6d714238f0914f57adee1938b20551adc4da8b78ab1ecacb9` |
| Advisor prompt words / characters / `sha256` | 454 / 2866 / `47e70d50741535d08f44f13a5a4d15abdbe7d15b552678359c585331cabff5c6` |
| Generator model and snapshot | `gemma4:31b`; Ollama model ID `6316f0629137`; Ollama server `0.24.0` |
| Judge route A | hosted OpenAI API judge, planned model `gpt-5.4-mini`, reasoning effort `medium`, text verbosity `medium`, calibration first |
| Judge route B | hosted Anthropic API judge, planned Claude Opus-family model selected from API availability at judge time, calibration first |
| `vanilla` packet words / `sha256` | 454 / `47e70d50741535d08f44f13a5a4d15abdbe7d15b552678359c585331cabff5c6` |
| `famous_sources_supplied` packet words / `sha256` | 555 / `76c827939fa297044d41ed9ebff1ab53363f17610571462300b106af9bfd0920` |
| `substrate_workflow` packet words / `sha256` | 8028 / `696c48f58ac6f8edf50c0e3441f963839db307f754ea8d669c5e0ccf4d231883` |
| `vanilla_long_prompt` packet words / `sha256` | 8071 / `de266b7f5dfe7ec59a92f10a3da81f4258de16e22769c3307549ad4c0452ed97` |
| `generic_advice_prompted` packet words / `sha256` | 478 / `c86420e546f8f0094fa8751fe984a1e420ee23251d0d6fa80216df4133941093` |
| Filler word count and ratio | 7574 words; ratio 1.000 to `substrate_workflow` added material |
| Filler forbidden-vocabulary scan | `{}`; zero forbidden-stem hits |

## Run

The v6-v1 generation pass completed with forty real local-model outputs: eight
runs for each of the five frozen conditions, zero simulated outputs, zero
deferred outputs, and zero `seed + 10` retries. Each public-safe model-output
receipt under `model-outputs/` records the condition, run number, seed,
generator identity, decoding settings, advisor prompt hash, condition packet
hash, and output body. `receipt-index.yaml` indexes the forty receipts.

The condition-blind judge packet was built after generation. Output bodies were
hashed, sorted by `sha256`, and assigned `OUT-01` through `OUT-40`. The
`OUT-NN` to condition/run answer key remains local-only and git-ignored. The
committed judge packet contains no condition labels, seeds, run numbers,
model-output receipt paths, or answer key.

## Judge and reconciliation

Hosted OpenAI `gpt-5.4-mini` failed calibration with 7 criteria differences and
an Anchor C C5/C6 disagreement, so it scored zero real outputs. Hosted
Anthropic `claude-opus-4-7` passed calibration with 1 criteria difference and
no Anchor C C5/C6 disagreement, then scored all forty blinded `OUT-NN` outputs.

Aggregate-only reconciliation was reconstructed from committed hashes:
`judge-packet/output-manifest.yaml` output hashes joined to committed
`model-outputs/` receipt bodies and `model_condition` frontmatter. All forty
rows matched; the local-only answer key was not read. No per-`OUT-NN` to
condition mapping is committed.

## Current state

The v6-v1 run is complete, scored, and reconciled aggregate-only.
`score-sheet.md` records `## Result: partial`; `eval-decision.md` records
`eval_decision: do_not_promote` / `decision_class:
insufficient_external_judges`. The positive rule is not met: fewer than two
eligible scored judges, the critical-criterion margin fails against
`generic_advice_prompted`, and generic-advice C3/C4 still saturate at 1.00.
No `benchmark_supported` promotion, canon candidate, public advice claim, or
per-`OUT-NN` mapping is created.
