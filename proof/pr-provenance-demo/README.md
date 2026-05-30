# anti-slop-pr Demo

A stranger-reproducible demo of the deterministic PR-description provenance
checker. Fully offline — **no GitHub API, no model, no network, no credential**.
Not canon, not source truth.

## Run it

```sh
make pr-provenance-demo
# or: python3 scripts/demo_pr_provenance.py
```

## Pipeline

The demo resolves two committed sample PR bodies against a self-contained
`fixture-root/` (so a stranger needs no GitHub access):

- `fixture-root/` — a tiny fake repo: `docs/example.md`, `tests/test_example.py`
  (defining `test_widget` / `test_locator`), a reviewed fixture card
  `corpus/source-cards/BK-7001-card-001.md` (+ manifest), and
  `issue-registry.txt` (valid issue numbers, produced offline).
- `pass-pr.md` — cites only resolvable references (`#42`, `docs/example.md`,
  `tests/test_example.py::test_widget`, `BK-7001-card-001`). Expected: **PASS**
  (exit 0).
- `fail-pr.md` — plants five fabrications: a fake issue (`#9999`), a missing doc
  (`docs/missing.md`), a bad test node (`::test_nope`), a fabricated card
  (`BK-7099-card-001`), and an out-of-range line ref (`docs/example.md:L99`).
  Expected: **FAIL** (exit 1).

`make pr-provenance-demo` exits 0 only when the checker PASSES the good body and
FAILS the slop body — proving it both accepts resolvable references and rejects
fabricated ones.

## Expected result (observed)

- `pass-pr.md`: PASS — file 2/0, test 2/0, issue 2/0, card 3/0 (checked/unresolved).
- `fail-pr.md`: FAIL — file 2 unresolved (missing doc + line overflow), test 1
  (undefined node), issue 1 (`#9999`), card 3 (the one fabricated `BK-7099`
  detected as source-card + source-id + card-id). The single fabricated card
  shows up as three resolver findings; the receipt lists each.

See `example-receipt.md` for the receipt shape.

## What this is and is not

The checker resolves references; it does not judge relevance, correctness, or
support, and proves nothing about advice quality, source truth, or canon. The
card/source check reuses the `anti-slop-lineage` resolver unchanged. See
[`docs/pr-provenance.md`](../../docs/pr-provenance.md).
