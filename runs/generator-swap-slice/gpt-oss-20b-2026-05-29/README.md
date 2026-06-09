# Generator-Swap Slice — gpt-oss:20b (status: `generated_not_judged`)

**`generator_swap_slice_not_benchmark` — not canon, not source truth, not a
benchmark result.** This is a public-safe receipt of a generation-only slice. It
does **not** answer the portability question (that needs the frozen two-route
judge, which is unavailable) and makes **no** claim about advice quality, slop,
reasoning, source truth, or model improvement.

## Question (Days 8–14)

Does `locator-accuracy-v4`'s substrate separation survive a **non-Gemma**
generator? v4 generated with Gemma (`gemma-4-31b-it-mlx`); the result is a
single-generator finding. This slice swaps **only the generator** and keeps the
frozen v4 condition packets and rule unchanged.

## What was done

- **Generator swapped to a non-Gemma model:** `gpt-oss:20b` served by a local
  Ollama OpenAI-compatible endpoint (Gemma was **not** substituted into this
  role; it remains v4's generator and was not used here). Decoding mirrors v4
  where applicable: `temperature 0.1`, `top_p 0.9`, `num_predict 800`,
  `seed 7` (deterministic).
- **Frozen packets, unchanged:** the 30 frozen `locator-accuracy-v4-v1`
  condition packets (6 conditions × 5 cases) were used **verbatim**. All 30 were
  `sha256`-verified against the published **Condition-Packet Hashes** table in
  [`run-packet.md`](../../../evals/bibliographic-adversary/locator-accuracy-v4/run-packet.md)
  before generation: **30/30 match, 0 mismatches.** No frozen v4 file
  (`case.md`, `run-packet.md`, model outputs, judge packet, decision) was edited.
- **Outputs:** 30/30 generated, 30/30 non-empty final answers. Mean latency
  ~5.3 s/output, ~158 s total. The raw model outputs and the model's `thinking`
  are kept **local-only** (not committed), per the repo's harness/raw-output
  rule; this receipt commits aggregates only.

## What was NOT done — judging blocked

v4's frozen rule requires **two different-family hosted judge routes**
(Anthropic + OpenAI), each passing exact A–L calibration. Only **one** hosted
route's credential is present (`ANTHROPIC_API_KEY` present; `OPENAI_API_KEY`
absent — checked as booleans only, values not inspected or hunted). One route
cannot satisfy the frozen rule. Judging was **not faked**, the frozen rule was
**not changed**, and no local model was substituted as a second judge.

**Therefore: `generated_not_judged`.** The substrate-vs-control separation is a
*scored* quantity, so portability remains **UNANSWERED** — this slice stages it
for the moment a second different-family hosted route is available.

## Aggregate (no per-output condition map, no raw text)

| field | value |
|---|---|
| status | `generated_not_judged` |
| generator | `gpt-oss:20b` (non-Gemma), Ollama local |
| decoding | temp 0.1, top_p 0.9, num_predict 800, seed 7 |
| packets | 30 (6 conditions × 5 cases), frozen, unchanged |
| hash-verified | 30 / 30 (0 mismatches) |
| outputs generated | 30 / 30 (30 non-empty) |
| judging | blocked — 1 of 2 required hosted routes |
| answers portability? | no — staged, not measured |

## Rerun / check (deterministic, public-safe)

The packet-integrity check anyone can reproduce (proves the frozen packets were
used unchanged): recompute the `sha256` of each `locator-accuracy-v4-v1`
condition packet and compare to the published Condition-Packet Hashes table in
`run-packet.md` — expect 30/30 match. Generation itself is operator-local (needs
a local Ollama `gpt-oss:20b` endpoint and the frozen v4 packets, which live in
the local-only shelf); the local runner and raw outputs are local-only by
policy. To complete the slice, run the frozen v4 judge once a second
different-family hosted route is available — without changing the frozen packets
or rule.
