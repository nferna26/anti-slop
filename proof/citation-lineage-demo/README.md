# Citation-Lineage Demo

A stranger-reproducible demonstration of Anti-Slop's one benchmark-supported
primitive: a deterministic **citation-lineage gate** that checks whether the
source cards and source IDs an output cites resolve to *reviewed* public-KB
artifacts.

This demo runs fully offline. It needs **no API key, no network, no model
runtime, and no raw book** — it compiles a brief from public-safe reviewed
source cards (paraphrases + locators only) and checks static sample notes.

## Run it

```sh
make demo
```

or directly:

```sh
python3 scripts/demo_citation_lineage.py
```

## Pipeline

1. `compile_brief.py` compiles a non-canon decision brief from five reviewed
   source cards (`BK-0048-card-001`, `BK-0001-card-001`, `BK-0002-card-001`,
   `BK-0042-card-001`, `BK-0044-card-002`) — public paraphrases and locators
   only.
2. A static, committed sample stands in for a model output (no model is run):
   - `sample-corrected-note.md` cites only reviewed cards at reviewed locators
     and refuses an unsupported page/quote request.
   - `sample-slop-note.md` cites `BK-9999-card-001`, a card ID that does not
     exist.
3. `gate_citation_lineage.py --require-reviewed` checks each sample.
4. A receipt is written to a transient temp dir (path printed at the end).

## Expected result

- The gate **PASSES** the good sample (every cited card resolves to a reviewed
  source card at a reviewed locator).
- The gate **FAILS** the slop sample (the fabricated `BK-9999-card-001` is an
  unresolved reference).
- `make demo` exits 0 only when both behaviours hold — it proves the tool both
  accepts real reviewed lineage and rejects a fabricated citation.

See `example-receipt.md` for a sample of the receipt format (the compiled brief
sha256 varies because the brief carries a compile date).

## What this is and is not

The gate is **deterministic** and is the operational form of the narrow,
benchmark-supported claim (see `evals/bibliographic-adversary/locator-accuracy-v4/`):
the substrate adds inspectable reviewed public-KB lineage that source-free
prompting does not. It is **not** evidence about source truth or advice quality,
and it does not promote canon. A model output is a test artifact, never an
authority.

The `sample-slop-note.md` fixture deliberately cites a nonexistent card; it lives
under `proof/` and is intentionally outside the `corpus/` + `evals/`
`make citation-dogfood` scope.
