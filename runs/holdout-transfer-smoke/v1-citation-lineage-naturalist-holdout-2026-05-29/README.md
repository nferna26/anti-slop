# Holdout-Transfer Smoke — citation-lineage primitive

**status: `holdout_smoke_not_benchmark` — not canon, not source truth, not a
benchmark.** This packet does not measure any model, does not promote canon, and
makes no claim about advice quality, slop reduction, reasoning, or source truth.

## The question

`locator-accuracy-v4` is `benchmark_supported` for one narrow, mechanical claim
over the business-strategy corpus (reviewed card ID + reviewed locator +
supported claim). This smoke asks a smaller, separate question:

> Does the **deterministic** citation-lineage primitive — *a cited card ID
> resolves to a reviewed card in the corpus, and fabricated /
> unreviewed-as-reviewed citations are caught* — still work when the corpus is
> **not** the benchmark-shaped business corpus?

It is a transfer probe for the *mechanism*, run with the **same unmodified**
`scripts/gate_citation_lineage.py` via its existing `--root` injection point. It
is **not** a model run and **not** a re-run of the v4 benchmark.

## Why this corpus is not v4-shaped

The fixtures are a **synthetic field-naturalism** corpus (bird-behaviour
observation logs, specimen-locality precision, seasonal plant-count confounds,
inter-observer agreement) on a reserved **`BK-79##`** ID band that does not exist
in the real `corpus/manifests/books-200.yaml` (`BK-0001..BK-0200`). None of v4's
business content (halo effect, strategy kernel, five forces, validated learning)
appears here. The only structural inheritance is the public
`proof/citation-lineage-demo/` pattern (a good sample that passes + a slop sample
that fails), generalised to a new corpus root and a new domain.

## Contents

- `corpus/source-cards/` — four synthetic fixture cards: three `reviewed`
  (`BK-7901-card-001`, `BK-7901-card-002`, `BK-7902-card-001`) and one
  deliberately `unreviewed` (`BK-7902-card-002`) so `--require-reviewed` is
  exercised. Paraphrase + locator only; no raw text. "reviewed" here is a
  fixture flag for the smoke, not a real operator review.
- `corpus/manifests/books-200.yaml` — holdout manifest (`BK-7901`, `BK-7902`).
- `outputs/brief-assisted-note.md` — static stand-in (NOT a model run) that
  cites only resolving reviewed cards at their carried locators and refuses
  unsupported excess. Expected: gate **PASS** in both modes.
- `outputs/source-free-note.md` — static stand-in (NOT a model run) that
  fabricates a card/source ID and cites the unreviewed draft as reviewed
  lineage. Expected: gate **FAIL** in both modes.
- `example-receipt.md` — sample of the receipt the runner writes (transient).

## Run it (deterministic; no API key, network, model, or raw book)

```sh
python3 scripts/holdout_smoke.py          # deterministic rerun
python3 scripts/holdout_smoke.py --self-test   # alias
```

The runner compiles a `compile_brief`-equivalent fixture brief over the holdout
root (the real `compile_brief.py` has no `--root`, so it reads the real corpus),
then gates the two static notes with `gate_citation_lineage.py --root <packet>`
in both modes, and exits 0 only when all four gate behaviours hold. Equivalent
manual calls (note: `--root` points at the **packet dir**, which contains
`corpus/`):

```sh
P=runs/holdout-transfer-smoke/v1-citation-lineage-naturalist-holdout-2026-05-29
python3 scripts/gate_citation_lineage.py --root $P --require-reviewed $P/outputs/brief-assisted-note.md   # PASS
python3 scripts/gate_citation_lineage.py --root $P --require-reviewed $P/outputs/source-free-note.md       # FAIL
```

## Countable lineage outcomes (observed)

Both notes carry 17 detected references. Gate-enforced counts:

| mode | note | unresolved refs | gate |
|---|---|---|---|
| existence (default) | brief-assisted | 0 | PASS (exit 0) |
| existence (default) | source-free | 8 (fabricated `BK-7999-card-001` / `BK-7999`) | FAIL (exit 1) |
| `--require-reviewed` | brief-assisted | 0 | PASS (exit 0) |
| `--require-reviewed` | source-free | 11 (8 fabricated + 3 unreviewed-as-reviewed `BK-7902-card-002`) | FAIL (exit 1) |

Only the **fabricated-ID** and **unreviewed-as-reviewed** findings above are
gate-caught. The source-free note's invented grid reference and
population-decline over-claim are **not** gate-detectable — they are
human-inspected only (see the next section), so do not read "source-free FAILED"
as the gate catching a wrong locator or an over-claim.

The **+3** findings that appear only under `--require-reviewed` are exactly the
reviewed-lineage discipline the gate adds (an existing but unreviewed card cited
as reviewed lineage).

## What the gate enforces vs. what it does not

- **Gate-enforced (deterministic):** card-ID / source-ID **resolution** against
  the corpus, and **reviewed-lineage discipline** under `--require-reviewed`.
  These are the countable outcomes above and they transferred cleanly to the
  holdout corpus.
- **NOT gate-enforced (human-inspected, illustrative only):** locator-text
  correctness, claim anchoring, and whether a refusal happened. The source-free
  note's invented grid reference and population-decline over-claim are visible to
  a human reviewer but the gate does **not** catch them — it is a lineage
  resolver, not a fact checker. Do not read this smoke as evidence about source
  truth, advice quality, or reasoning.

## Public-safety

Synthetic paraphrases only (`Short excerpt: None.`); no raw copyrighted text, no
private paths (all paths repo-relative; the runner writes only to a transient
temp dir), no answer keys or per-output condition mappings (the two notes are
static placeholders, and their expected gate exits are stated here as the smoke's
assertion, not a hidden key). The holdout corpus is self-contained under
`corpus/` and is reached only via `--root`, so resolution never touches the real
corpus; the `BK-79##` band cannot collide with real `BK-####` IDs.
