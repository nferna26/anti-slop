# Citation-Lineage Transfer Memo (post-v4)

Public-safe decision memo for the transfer tranche that followed PR #22. It
records what was done, what transferred, what did not, and the next-step
recommendation. It is **not** canon, **not** a benchmark result, and makes
**no** claim about advice quality, slop, reasoning, or source truth.

## 1. PR #22 merged

`OSS-readiness: CI dogfood, citation-lineage docs, BK-0023 stale-clause
reconcile` merged into the integration branch `codex/locator-accuracy-v1-
benchmark-run` (two-parent merge commit `b275dcf`, merging `d7cd5df` into the
base `72e1db6`; the local base was then fast-forwarded to `b275dcf`). Six files:
`.github/workflows/ci.yml`, `README.md`, `corpus/source-cards/BK-0023-card-001.md`,
`docs/citation-lineage-gate.md`, `kb/index.md`, `kb/log.md`. No frozen v2/v3/v4
eval artifact was touched (verified by diff grep against the on-disk frozen
dirs); no canon promotion, review-status lift, or registry decision. CI `gates`
checks were green on PR #22 before merge (verified via `gh pr checks`); the
local acceptance suite was re-run green on the pre-merge tip.

## 2. Holdout-transfer smoke — result

**Question (narrow):** does the *deterministic* citation-lineage primitive — a
cited card ID resolves to a reviewed card, and fabricated / unreviewed-as-
reviewed citations are caught — still work on a corpus that is **not** the
benchmark-shaped business corpus v4 was run over?

**Design:** a self-contained synthetic **field-naturalism** fixture corpus
(reserved `BK-79##` band; 3 reviewed + 1 deliberately unreviewed card) under
`runs/holdout-transfer-smoke/v1-citation-lineage-naturalist-holdout-2026-05-29/`,
gated by the **same unmodified** `scripts/gate_citation_lineage.py` via its
existing `--root` injection point. Two static, hand-written stand-in notes
(explicitly **not** model runs) play the role of model output. status:
`holdout_smoke_not_benchmark` — not canon, not source truth. Rerun:
`python3 scripts/holdout_smoke.py` (also `make holdout-smoke`; deterministic, no
API key / network / model / raw book).

**Result (countable, gate-enforced):**

| mode | brief-assisted | source-free |
|---|---|---|
| existence (default) | PASS — 0 unresolved | FAIL — 8 unresolved (fabricated `BK-7999-card-001`/`BK-7999`) |
| `--require-reviewed` | PASS — 0 unresolved | FAIL — 11 unresolved (8 fabricated + 3 unreviewed-as-reviewed `BK-7902-card-002`) |

The gate resolved a fresh, different-domain corpus and discriminated good lineage
from fabricated/unreviewed lineage, with the reviewed-lineage discipline (+3
findings) firing only under `--require-reviewed`.

## 3. Generator-swap replication — `blocked_generator_unavailable`

Attempted: a small pre-registered v4 slice (1 run × 6 conditions × 5 cases) with
a **non-Gemma** generator, frozen condition packets unchanged. **Blocked, with
evidence:**

- Non-Gemma local generators *do* exist (Ollama serves `gpt-oss:20b`,
  `qwen3.5`), but the frozen v4 harness pins the Gemma generator
  (`gemma-4-31b-it-mlx` via the LM Studio local endpoint) with **no swap flag** —
  running a different generator would require editing the frozen run recipe,
  which is out of scope.
- Independently, scoring is blocked: the frozen v4 rule requires **two
  different-family hosted judge routes**, but only one hosted credential is
  present (`ANTHROPIC_API_KEY` present; `OPENAI_API_KEY` absent — booleans only,
  no values inspected). A single route cannot satisfy the frozen rule, and the
  missing credential is treated as a hard unavailability (not hunted for).

Per the tranche constraints, the negative is recorded as-is: **Gemma was not
substituted, the v4 recipe was not revised, and no result was rescued or
fabricated.** Generator portability of the substrate effect therefore remains
**untested**.

## 4. What transferred, what did not

**Transferred (mechanical only):** the deterministic citation-lineage primitive
is **corpus-agnostic** — the same gate, via `--root`, resolves reviewed-card
lineage and rejects fabricated and unreviewed-as-reviewed citations on a
new-domain corpus it was never tuned for. This is consistent with v4's narrow
mechanical-lineage claim and extends only its *mechanical* portability.

**Did NOT transfer / still unproven:**

- **Generator portability** — untested (§3 blocked). The v4 separation result
  remains a single-generator (Gemma) finding.
- **Anything beyond mechanical lineage** — the gate enforces ID resolution +
  reviewed-lineage discipline only. Locator-text correctness, claim anchoring,
  and refusal-of-excess are human-inspected in the smoke, **not** gate-enforced.
- No claim about advice quality, slop, reasoning, or source truth; no canon, no
  registry decision; no model was measured.

## 5. Is packaging / MCP justified next?

- **Packaging the deterministic gate** as a small, corpus-agnostic
  citation-lineage checker (it already takes `--root`; offline; stdlib-only) is
  the *most* defensible next step — the holdout shows the mechanism is not tied
  to the benchmark corpus. Scope it as an inspectable tool, not a runtime.
- **MCP / runtime / RAG integration is NOT justified yet.** It would cross the
  substrate-not-runtime line (`AGENTS.md`), and the one open portability
  question (generator-swap) is still blocked. Building a product surface on an
  effect demonstrated for a single generator family would outrun the evidence.

## 6. Single best next PR

Unblock and run the **generator-swap slice** the moment a second different-family
hosted judge route is available (`OPENAI_API_KEY` present), keeping the frozen v4
packets and rule unchanged and committing aggregate-only, public-safe receipts.
That directly tests the one thing this tranche could not: whether the substrate
separation is generator-portable or a Gemma artifact. Packaging the deterministic
gate can follow, but the portability question is the higher-value unknown.
