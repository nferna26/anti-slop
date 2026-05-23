---
case_id: normalization-vs-latent-errors-runway-lighting-v5
artifact: run-packet
eval_type: contradiction-preservation
benchmark_version: normalization-vs-latent-errors-runway-lighting-v5-v1
status: prepared_not_frozen_not_run
created: 2026-05-23
---

# Run Packet - normalization-vs-latent-errors-runway-lighting-v5-v1

This is the prepared, not frozen, run packet for the v5 runway-lighting
contradiction-preservation case. It records the intended condition recipes, run
parameters, filler constraints, anonymisation rules, and external-judge plan for
benchmark version `normalization-vs-latent-errors-runway-lighting-v5-v1`.

**Status: prepared, not frozen, not run.** The v5 case and calibration anchors
are drafted, but `judge-packet/calibration-anchors.md` is still
`status: proposed_unreviewed`. Operator approval is required before this packet
may be frozen. No condition packets have been frozen by hash, no model outputs
exist, no judge packet has been built, no judging has occurred, and no
reconciliation or eval decision exists.

This file is operator-facing. It names model conditions and run mechanics. It
must not be shown to blind judges.

## Freeze prerequisites

The following must be satisfied before `status` can change to a frozen state:

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

Lineage artifacts to hash at freeze:

| Artifact |
| --- |
| `corpus/claim-tension-cards/normalization-of-deviance-vs-latent-errors.md` |
| `corpus/source-cards/BK-0042-card-001.md` |
| `corpus/source-cards/BK-0044-card-001.md` |
| `corpus/source-cards/BK-0044-card-002.md` |

## Advisor prompt

The Advisor prompt is derived deterministically from `case.md` -> `## Advisor
prompt`: take the block-quote lines, remove a leading `> ` from each line, turn
a line that is exactly `>` into an empty line, join with newlines, strip
leading/trailing whitespace, and append one trailing newline.

The exact word count, character count, and `advisor_prompt_sha256` must be filled
at freeze. A change opens a new benchmark version; it must not silently rebase
v5-v1.

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
- Planned generator: `gemma4:31b`, unless the freeze checklist records a
  different fixed model before generation.

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

Fill these fields before changing `status` to frozen:

| Item | Value |
| --- | --- |
| Calibration-anchor status | TODO - must be `filled_pre_run` before freeze |
| Calibration-anchor `sha256` | TODO |
| Advisor prompt words / characters / `sha256` | TODO |
| Generator model and snapshot | TODO |
| Judge route A | hosted OpenAI API judge, exact model/settings TODO |
| Judge route B | hosted Anthropic API judge, exact model/settings TODO |
| `vanilla` packet words / `sha256` | TODO |
| `famous_sources_supplied` packet words / `sha256` | TODO |
| `substrate_workflow` packet words / `sha256` | TODO |
| `vanilla_long_prompt` packet words / `sha256` | TODO |
| `generic_advice_prompted` packet words / `sha256` | TODO |
| Filler word count and ratio | TODO |
| Filler forbidden-vocabulary scan | TODO |

## Current state

The v5 case is drafted and prepared, but not frozen and not run. The next step
is operator review of `judge-packet/calibration-anchors.md`. If approved, the
anchors can be set to `filled_pre_run` and the freeze/run pipeline can continue.
