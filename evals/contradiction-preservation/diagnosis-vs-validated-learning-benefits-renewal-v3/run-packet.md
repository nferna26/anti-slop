---
case_id: diagnosis-vs-validated-learning-benefits-renewal-v3
artifact: run-packet
eval_type: contradiction-preservation
benchmark_version: diagnosis-vs-validated-learning-benefits-renewal-v3-v1
status: frozen_run_complete
created: 2026-05-22
---

# Run Packet — diagnosis-vs-validated-learning-benefits-renewal-v3-v1

A run packet for the eval case in this folder. It records the condition packet
recipes, the exact packet hashes, the equal-length filler recipe and scan, the
run parameters, the output / anonymisation / answer-key rules, and the
judge-packet structure — the frozen inputs the benchmark pass was run against.

**The inputs were frozen first; the benchmark pass has now been run.** Forty real
model outputs exist under `model-outputs/` — eight per condition — and the
condition-blind judge packet has been built under `judge-packet/`; see
`## Status` and `## Run`. **One blind-judge calibration attempt is on record —
`gpt-oss:20b` failed the calibration gate — so zero `OUT-NN` outputs have been
scored, and nothing has been reconciled:** `score-sheet.md` stays
`scoring_status: unscored` and `## Result` stays `partial`. A model output is a
test artifact — never an authority, never citable as a source.

**This run packet is operator-facing.** It names the model conditions because it
is the operator's run specification; it is **not** part of the blind judge
packet, and a judge never sees it.

## Status

**Frozen, run, and judge-packet built — not scored.** The five condition packets
were assembled and hashed, the `vanilla_long_prompt` filler built and scanned,
and the Advisor prompt derived and hashed (see `## Freeze checklist`); the
benchmark pass has since been **run** — see `## Run`. Forty real `gemma4:31b`
outputs (eight per condition) are recorded under `model-outputs/`, with zero
simulated outputs and zero deferrals. The outputs were anonymised and a
condition-blind judge packet was built under `judge-packet/`. **One blind-judge
calibration attempt is on record — `gpt-oss:20b` failed the calibration gate, so
zero `OUT-NN` outputs have been scored, no eligible judge exists yet, and no
reconciliation has occurred** (see `## Run`). `score-sheet.md` stays
`scoring_status: unscored` and `## Result` stays `partial`. The run promotes
nothing and lifts no status.

The byte-exact assembled condition packets, the filler, the runner, and the raw
interactions are held in the case's git-ignored local-only run folder. The
committed record of the freeze is the recipes and the `sha256` table in this
file; before each call the runner verified the frozen packet file's `sha256`
against the table in `## Freeze checklist`.

## Frozen inputs

The benchmark pass freezes, and does not edit during the run: `case.md` —
`## Scenario`, `## Advisor prompt`, `## Expected reasoning`, `## Failure modes`,
`## Scoring rubric`, `## Criterion dependency rule`, `## Positive result`,
`## Falsifier`, `## Judge protocol`, `## Anti-overfitting safeguards`, and the
`model_conditions` list — the three reviewed lineage artifacts named in
`case.md` → `## Lineage`, and the operator-accepted calibration anchors
(`judge-packet/calibration-anchors.md`, `status: filled_pre_run`). Any edit to a
frozen input starts a new benchmark version (`…-v3-v2`); it does not silently
re-base `…-v3-v1`.

Frozen lineage artifact `sha256` (committed head as of freeze):

| Artifact | `sha256` |
|---|---|
| `corpus/claim-tension-cards/strategy-diagnosis-vs-validated-learning.md` | `adbc27e7b1d8eb59731abf8e0403bc675107a32961b3a7fb02f3b816b85ad4b6` |
| `corpus/source-cards/BK-0001-card-001.md` | `1535ee5be11481217f9731d0851b2ffe23f9f61ae1b8b978added09026a9730b` |
| `corpus/source-cards/BK-0007-card-001.md` | `8d7bb540f96f0cc51fd77173c8e02988bdf8ca500fa2507c8f25875bc466251f` |

## Advisor prompt

The Advisor prompt is derived deterministically from `case.md` → `## Advisor
prompt`: take the block-quote lines, remove a leading `> ` from each (a line that
is exactly `>` becomes an empty line), join with newlines, strip
leading/trailing whitespace, append a single trailing newline.

- **Words:** 303. **Characters:** 1904.
- **`advisor_prompt_sha256`:** `17cdf26f6cea2e87242727908093b48a47b0394671f519ff51b156a53541220a`

At run time this hash is recomputed and must match; if `case.md`'s Advisor
prompt has changed, the run stops and a new benchmark version is opened.

## Condition packets

Five conditions. Each packet is the named added material followed by the
**verbatim Advisor prompt**. The Advisor prompt is byte-identical across all
five; the condition is the only deliberate variable.

| Condition | Added material before the Advisor prompt |
|---|---|
| `vanilla` | None. The Advisor prompt alone. |
| `famous_sources_supplied` | A name-level list of famous book titles + authors; no claims, no summaries. |
| `substrate_workflow` | A substrate preamble + the three reviewed artifacts, verbatim. |
| `vanilla_long_prompt` | A one-line note + the equal-length filler + a one-line transition. |
| `generic_advice_prompted` | A short generic advice-quality request; no rubric, no sources. |

### Packet recipes (deterministic)

Each non-`vanilla` packet is `added material` + one blank line + the verbatim
Advisor prompt. The exact preamble texts are frozen below so the packets are
reproducible from this file, `case.md`, and the `corpus/` artifacts.

- **`vanilla`** — the Advisor prompt verbatim, nothing else.

- **`famous_sources_supplied`** — the frozen preamble below, then a blank line,
  then the Advisor prompt verbatim. The list contains the two famous books
  behind this case's substrate — *Good Strategy Bad Strategy* (Richard Rumelt,
  BK-0001) and *The Lean Startup* (Eric Ries, BK-0007) — mixed with three
  unrelated famous decoys, in a fixed order set at freeze. The preamble makes no
  claim about what any book argues, supplies no source-card or tension-card
  content, and marks no book as authoritative.

  ```
  The list below names some widely known books on business, strategy, and
  decision-making that are sometimes mentioned in connection with questions
  like the one that follows. They are given by title and author only. Nothing
  here states or summarises what any book argues, and nothing here marks any
  title as relevant to, or authoritative for, the question below.

  - Thinking, Fast and Slow — Daniel Kahneman
  - Good Strategy Bad Strategy — Richard Rumelt
  - The Innovator's Dilemma — Clayton Christensen
  - The Lean Startup — Eric Ries
  - Competitive Strategy — Michael Porter

  The question follows.
  ```

- **`substrate_workflow`** — the frozen preamble below, then a blank line, then
  the three reviewed artifacts supplied verbatim (each artifact's full committed
  file content) behind `--- ARTIFACT n of 3 ---` separators in order — (1)
  `corpus/claim-tension-cards/strategy-diagnosis-vs-validated-learning.md`, (2)
  `corpus/source-cards/BK-0001-card-001.md`, (3)
  `corpus/source-cards/BK-0007-card-001.md` — then the one-line transition, then
  the Advisor prompt verbatim.

  Preamble:
  ```
  The three reviewed artifacts below come from a knowledge base and may be
  useful background for the question that follows. Two of them are source
  cards: each is an evidence-level note that records a single claim drawn from
  one book, with a locator, a paraphrase, and scope conditions. The third is a
  claim/tension card: a synthesis-level note that relates the two source-card
  claims and holds the tension between them open. None of these artifacts is
  canon, none is authoritative, and none settles the question; the tension
  they describe is explicitly unresolved. They are reproduced verbatim below,
  and the question follows after them.
  ```
  Transition line: `That is the end of the reviewed artifacts. The question follows.`

- **`vanilla_long_prompt`** — the one-line note below, then a blank line, then
  the equal-length filler (see `## Equal-length filler recipe`), then the
  one-line transition, then the Advisor prompt verbatim. No reviewed substrate
  artifact, no claim/tension card, no source card.

  Note line: `The text below is unrelated background reading on a range of everyday subjects. It has no connection to the question that follows; it is included only as reading material. The question comes after it.`
  Transition line: `That is the end of the unrelated background reading. The question follows.`

- **`generic_advice_prompted`** — the frozen preamble below, then a blank line,
  then the Advisor prompt verbatim. It conveys advice-quality expectations only;
  it enumerates no rubric criterion, names no reading, mentions no "flattening",
  asks for no disconfirming evidence, and supplies no source. This control
  isolates a substrate effect from a mere being-asked-for-good-advice effect.

  ```
  Please give thorough, balanced, and well-reasoned advice on the question
  below. Take the situation's tradeoffs seriously, and be honest about what is
  uncertain. The question follows.
  ```

## Equal-length filler recipe

The `vanilla_long_prompt` filler is a neutral, topic-free body that matches the
length of the `substrate_workflow` added material so a substrate advantage
cannot be a more-tokens effect.

- **Structure.** Distinct, non-repetitive neutral paragraphs — one per everyday
  topic, no two paragraphs alike (repetition triggered a generation loop in an
  earlier case). The frozen filler is **44 distinct everyday-topic paragraphs**.
- **Topic set** (everyday, sensory, non-topical): valley mist, a river bend,
  the turning tide, baking bread, steeping tea, hand-poured coffee, a cliff
  path, moon phases, a vegetable patch, autumn leaves, fresh snow, the dawn
  chorus, stargazing, a potter's wheel, a rainy afternoon, ridge weather, a
  low-water beach, a country lane, a paper map, working oak, knitting a scarf,
  a still lake, a desert at noon, an old wood floor, kite flying, a sandcastle,
  paper folding, a jigsaw, a beehive, shells and pebbles, frost on a window,
  dipping candles, watercolour, a campfire, a winter night sky, sand dunes,
  river stones, a hedgerow, an orchard in bloom, a frame loom, whittling, rain
  on dry ground, a garden pond, picking blackberries.
- **Forbidden vocabulary.** The assembled filler was scanned and must contain
  **zero** occurrences of these stems and their close variants: `strateg`,
  `learn`, `startup`, `organi`, `manage`, `diagnos`, `experiment`, `benefit`,
  `budget`, `pilot`, `decid`, `decis`, `advic`, `advis`, `recommend`. A nonzero
  scan stops the freeze.
- **Length rule.** The filler's word count matches the `substrate_workflow`
  **added-material** word count (the substrate preamble plus the three artifacts
  plus separators and transition — everything in that packet beyond the Advisor
  prompt) within **±8%**.

Filler scan and length, computed at freeze:

- Filler word count: **4696**.
- `substrate_workflow` added-material word count: **4670**.
- Ratio: **100.6%** — within the 92.0%–108.0% band.
- Forbidden-vocabulary scan: **CLEAN — zero hits** across all fifteen stems.

## Run parameters

The pre-registered run parameters the benchmark pass was run under; the run
record itself is in `## Run`.

- **Run count.** **Eight** real runs per condition **minimum** for the
  `…-v3-v1` benchmark pass — five conditions × 8 = **40 outputs** minimum; **ten**
  runs per condition (50 outputs) preferred if later feasible. Single-run results
  are not a benchmark pass.
- **Seeds (deterministic).** Condition index 1–5 in the declared
  `model_conditions` order: `vanilla` (1), `famous_sources_supplied` (2),
  `substrate_workflow` (3), `vanilla_long_prompt` (4), `generic_advice_prompted`
  (5). Run *r*, condition *i* → seed `r*100 + i`: run 1 = 101–105, run 2 =
  201–205, run 3 = 301–305, run 4 = 401–405, run 5 = 501–505, run 6 = 601–605,
  run 7 = 701–705, run 8 = 801–805 (runs 9–10 = 901–905 and 1001–1005 if used).
  A call that times out is re-attempted on a fresh deterministic seed
  (`seed + 10`), recorded as such, never fabricated.
- **Decoding (frozen).** Generation `temperature 0.7`, `top_p 0.9`,
  `num_ctx 32768`, held constant across all conditions and runs. Per-call
  timeout 600 s. These match the `…-v2-v1` decoding parameters for
  cross-version comparability.
- **Generator model.** **`gemma4:31b`** (Gemma family) — one fixed real model,
  held constant across every condition and run, so the model condition is the
  only deliberate variable. Selected at run time from the installed local Ollama
  models, carrying forward the `…-v2-v1` choice; Ollama model ID `6316f0629137`,
  local Ollama server 0.24.0. See `## Run` for the run record and the
  `## Freeze checklist` generator row. Because the generator is Gemma-family,
  every blind judge must be a non-Gemma family.

## Output, anonymisation, and answer key

- **Output naming.** One file per run under `model-outputs/`, named
  `<condition>` for run 1 and `<condition>-NN` for later runs (`-02`, `-03`).
  Each file records full provenance per `runs/model-outputs/_metadata-template.yaml`
  — provider/runtime, model ID and snapshot, decoding params, per-run seed,
  prompt and condition-packet `sha256`, output path, and the real-run status.
  Real runs only; no simulated outputs. Forty such receipts are now committed —
  see `## Run`.
- **Anonymisation rule.** After all outputs exist and **before any judge sees
  them**, each output body is hashed with `sha256` and the outputs are sorted in
  ascending hash order; labels `OUT-01 … OUT-NN` are assigned in that order. The
  hash-sorted order carries no condition information.
- **Answer-key locality.** The `OUT-NN` → condition map is written **only** to
  the case's local-only run folder (git-ignored). It is **never** committed and
  is not read until after blind scoring is complete (see `score-sheet.md` →
  `## Post-reconciliation condition aggregate`).

## Judge-packet structure

At run time a **condition-blind** judge packet is built (committed, public-safe).
The judge-facing packet will contain, and only contain:

- condition-neutral judge instructions naming no condition;
- condition-neutral case-context excerpts;
- a condition-neutral copy of the `## Scoring rubric` and `## Criterion
  dependency rule`;
- the calibration **Surface 1** only — the three anchor texts and the blank
  scoring grid from `judge-packet/calibration-anchors.md` — for the pre-scoring
  calibration exercise;
- the anonymised `OUT-NN` outputs (added **only after** generation and
  anonymisation);
- an output-hash manifest (`OUT-NN` → body `sha256`);
- a blank score sheet (`OUT-NN` rows × C1–C6).

The calibration **Surface 2** reference verdicts in `calibration-anchors.md`
stay operator-only and are withheld from a judge until that judge has completed
the Surface 1 exercise. The `OUT-NN` → condition answer key stays local-only and
is **never** committed. No judge-facing file carries a condition label.

Per `case.md` → `## Judge protocol`: each judge first completes the
calibration-anchor step and must clear the eligibility threshold; at least two
eligible blind judges from different model families score the packet; at least
one eligible judge must be independent of the orchestrating agent before any
Result lift above `partial`; criterion-level pass/fail scoring on every `OUT-NN`
with the dependency rule applied; a third eligible judge is triggered on the
pre-registered C5/C6 or margin disagreement; a judge-sensitive outcome stays
`partial`.

## Freeze checklist

Completed at freeze-prep time, **before any output was generated**.

- [x] Generator model ID and snapshot recorded — `gemma4:31b`, Ollama model ID
      `6316f0629137` (local Ollama server 0.24.0); see `## Run`.
- [x] All five condition packets assembled per `## Condition packets`; each
      packet's word count and `sha256` recorded in the table below.
- [x] `vanilla_long_prompt` filler assembled; forbidden-vocabulary scan returned
      **zero** hits; filler is **4696** words against the `substrate_workflow`
      added material of **4670** words — **100.6%**, within the ±8% band (44
      distinct everyday-topic paragraphs).
- [x] `advisor_prompt_sha256` computed as
      `17cdf26f6cea2e87242727908093b48a47b0394671f519ff51b156a53541220a`
      (303 words, 1904 characters).
- [x] `case.md` frozen inputs (see `## Frozen inputs`) and the operator-accepted
      `judge-packet/calibration-anchors.md` (`filled_pre_run`) confirmed.
- [x] Frozen lineage artifact `sha256` recorded (see `## Frozen inputs`).
- [x] Freeze-prep timestamp recorded.

| Condition | Packet word count | Packet `sha256` | Seeds (runs 1–8) |
|---|---|---|---|
| `vanilla` | 303 | `17cdf26f6cea2e87242727908093b48a47b0394671f519ff51b156a53541220a` | 101 / 201 / 301 / 401 / 501 / 601 / 701 / 801 |
| `famous_sources_supplied` | 400 | `2613102cf0154476f96c891d5054f2cf57cff28a7bdfc2f9168ac7f7f11b0ef9` | 102 / 202 / 302 / 402 / 502 / 602 / 702 / 802 |
| `substrate_workflow` | 4973 | `58b50ce099b2f287a38d0a5b95cd0e640069db62a712813a3ee87f644f421173` | 103 / 203 / 303 / 403 / 503 / 603 / 703 / 803 |
| `vanilla_long_prompt` | 5045 | `9862f544d24f017f14df21b639ca4b0b8d012042821d914f530cbe775f332273` | 104 / 204 / 304 / 404 / 504 / 604 / 704 / 804 |
| `generic_advice_prompted` | 329 | `e3027cc78dfb2ff088a59d0b1ed85e19b08f812692dceba3fd97e50cb0b38806` | 105 / 205 / 305 / 405 / 505 / 605 / 705 / 805 |

The `vanilla` packet is the Advisor prompt alone, so its `sha256` equals
`advisor_prompt_sha256`. Runs 9–10 (seeds 901–905, 1001–1005) are used only if
the operator opts for the ten-run pass.

## Run

The benchmark pass was run on 2026-05-22 — UTC start `2026-05-22T14:55:16Z`,
completion `2026-05-22T15:47:24Z`. Generator: **`gemma4:31b`** (Gemma family),
Ollama model ID `6316f0629137`, via local Ollama (server 0.24.0); decoding
`temperature 0.7`, `top_p 0.9`, `num_ctx 32768`, on the pre-registered seeds.

**Forty real model outputs — eight runs for each of the five conditions.** Zero
simulated outputs. **Zero deferrals**: every call completed within the 600 s
timeout on its first attempt with `done_reason: stop`, so the `seed + 10`
timeout-retry rule was not exercised. Before each call the frozen condition
packet's `sha256` was verified against the `## Freeze checklist` table; all forty
verifications matched. Per-call wall time ranged 46.5 s to 161.3 s (about 52 min
total). One public-safe model-output receipt per run is committed under
`model-outputs/` (`<condition>.md`, `<condition>-02.md` …) with full benchmark
provenance: benchmark version, condition, run number, seed, model ID/snapshot,
runtime, decoding parameters, condition-packet and advisor `sha256`, the real-run
classification, and the verbatim answer. `gemma4:31b` emitted no separate
reasoning/thinking block, so each receipt carries the final answer only; the raw
interactions stay in the git-ignored local-only run folder.

The forty output bodies were then anonymised — each hashed with `sha256`, sorted
in ascending hash order, labelled `OUT-01 … OUT-40` (all forty bodies distinct).
A condition-blind judge packet was built under `judge-packet/`: `README.md`,
`judge-instructions.md`, `case-context.md`, `rubric.md`, `calibration-exercise.md`
(calibration Surface 1 only — anchor texts and a blank grid, no reference
verdicts), `output-manifest.yaml`, `blank-score-sheet.md`, and
`outputs/OUT-01.md … OUT-40.md`. No judge-facing file carries a condition label,
seed, run number, or the answer key. The Surface 2 reference verdicts stay
operator-only in `judge-packet/calibration-anchors.md` and were not copied into
any judge-facing file. The `OUT-NN` → condition answer key is in the local-only
run folder, git-ignored, **not committed**.

Some `substrate_workflow` outputs refer to the artifacts supplied to that
condition, and a few answers name a well-known author from the model's own
memory. These are verbatim model output and were not edited; the packet is
label-blind — no `OUT-NN` → condition map is committed — consistent with the v2
pass.

**No reconciliation.** `score-sheet.md` stays `scoring_status: unscored`;
`## Result` stays `partial`; no `eval-decision.md`, no canon. Two blind-judge
attempts have since been recorded: `gpt-oss:20b` failed the pre-registered
calibration gate and scored no `OUT-NN`
(`judge-packet/judge-calibration-gpt-oss-20b.md`); Claude Opus 4.7 scored all 40
`OUT-NN` (`judge-packet/judge-score-claude-opus.md`) but is the orchestrating
agent with a circular calibration — a judge-variance data point only, not an
eligible independent pass. No eligible, independent judge pass exists yet.

## Discipline note

This packet froze the v3 inputs and recorded the benchmark run; it scored
nothing. Forty model outputs now exist as test artifacts under `model-outputs/`.
No score exists, `## Result` stays `partial`, `scoring_status` stays `unscored`,
and no canon or authority follows from this file. A model output is a test
artifact — never an authority, never citable as a source.
