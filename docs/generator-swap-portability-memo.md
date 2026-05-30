# Generator-Swap Portability Memo (Days 1–14)

Public-safe decision memo. Not canon, not a benchmark, makes no advice / slop /
reasoning / source-truth / model-improvement claim.

## Part A — Days 1–7 closeout (package the deterministic tool)

**Done.** PR #24 merged into `codex/locator-accuracy-v1-benchmark-run` (merge
commit `3e8f6b1`). Success criterion met:

- **CLI installable** — `anti-slop-lineage` (`pip install .`); its entry point
  is the existing gate's own `main()` (zero behaviour fork; gate module
  byte-identical to base), stdlib-only, no model/API/network.
- **Package smoke exists and is hardened for CI** — `make package-smoke` installs
  into a throwaway venv (isolated install, with an offline `--no-build-isolation`
  fallback), runs the installed `--self-test`, and audits the holdout fixture
  (`--root --require-reviewed`: brief-assisted PASS, source-free FAIL). It is now
  wired into CI as a **separate `package` job** (uses pip's package-index network,
  so it is kept out of the offline `gates` job; still no model/API/credential).
- **Docs narrow** — `docs/citation-lineage-gate.md` "Install as a CLI" states
  packaging adds *distribution, not capability*; benchmark-backed only for
  lineage resolution + reviewed-lineage checks.
- **MCP deferred** — `docs/citation-lineage-mcp-deferred.md`: substrate-not-runtime;
  thin dependency-free sketch documented, no runtime committed.

## Part B — Days 8–14 generator-swap slice → `generated_not_judged`

**Question:** does v4's substrate separation survive a **non-Gemma** generator,
or is it a Gemma artifact? v4's result is a single-generator (Gemma) finding.

**Setup (credentials reported as booleans only; never values, never hunted):**

- Non-Gemma local generators available via Ollama: `gpt-oss:20b`, `qwen3.5`.
  Chose **`gpt-oss:20b`** — it returns clean, bounded final answers; `qwen3.5`
  over-thinks and did not reach a final answer within the token budget. Gemma
  (`gemma-4-31b-it-mlx`) was **not** used as the generator here and **not**
  substituted into any role.
- Hosted judge routes: `ANTHROPIC_API_KEY` present; `OPENAI_API_KEY` absent.
  Only **one** of the two different-family hosted routes the frozen v4 rule
  requires.

**Slice recipe (frozen packets unchanged):**

- Inputs: the 30 frozen `locator-accuracy-v4-v1` condition packets
  (6 conditions × 5 cases). All 30 `sha256`-verified against the published
  Condition-Packet Hashes table in `run-packet.md` — **30/30 match, 0
  mismatches**. No frozen v4 file edited.
- Generator: `gpt-oss:20b` (Ollama local), decoding mirrors v4 where applicable:
  `temperature 0.1`, `top_p 0.9`, `num_predict 800`, `seed 7` (deterministic).
- Outputs: **30/30 generated, 30 non-empty**, ~5.3 s/output, ~158 s total. Raw
  outputs and model `thinking` kept **local-only** (not committed). Public-safe
  aggregate receipt: `runs/generator-swap-slice/gpt-oss-20b-2026-05-29/`.

**Why judging did not happen:** the frozen rule requires **two** different-family
hosted judge routes, each passing exact A–L calibration. With one route present,
the rule cannot be met. Judging was **not faked**, the rule was **not changed**,
Gemma was **not** substituted, and no local model was used as a second judge.

**Status: `generated_not_judged`.**

## What is — and is not — supported

- **Supported (mechanical only):** a non-Gemma generator (`gpt-oss:20b`) runs on
  the byte-identical frozen v4 packets and produces 30 bounded final answers; the
  generator swap executed mechanically; the slice is staged for judging.
- **NOT supported / UNANSWERED:** generator portability of the substrate
  separation. That separation is a *scored* quantity (SO/F surface under two
  calibrated judges); without judging, nothing is measured. This slice is **not**
  a portability result, **not** a benchmark, and says nothing about advice
  quality, source truth, or reasoning.

## Next

Complete the judge pass the moment a second different-family hosted route is
available (`OPENAI_API_KEY`), scoring the already-generated 30 outputs against the
frozen rubric/rule unchanged, aggregate-only — yielding `portable_signal` or
`failed_signal`. (A calibrated local non-Gemma backup judge is permitted by the
frozen rule only if it passes the identical exact A–L calibration; that is a
heavier, separate step and was not attempted here.)
