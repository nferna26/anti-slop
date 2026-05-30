# anti-slop-pr Dogfood Memo

Public-safe record of dogfooding `anti-slop-pr` on this repo's own PR
descriptions. Not canon, not a benchmark. The goal: does the checker work on
real PR bodies, what does it catch, and what false-positives does it produce.

## Method

- Collected **8** public-safe PR-body copies (`proof/pr-provenance-dogfood/bodies/pr-*.txt`,
  read from this repo's public PR metadata via `gh` — a mix of clean feature/
  benchmark PRs and two "meta" tooling PRs). No credentials, private paths, or
  raw API JSON were saved.
- Built a public-safe **issue registry** of valid PR/issue numbers
  (`proof/pr-provenance-dogfood/issue-registry.txt`, numbers only — no titles or
  bodies), so issue refs resolve deterministically.
- Ran `gate_pr_provenance` against the **repo root**. Reproduce:
  `make pr-provenance-dogfood` (offline, always exit 0 — a report, not a gate).

## Key finding: bare-basename false positives (found and fixed)

Over the 8 committed bodies, the checker first **failed 6 of the 8**. Almost
every failure was a **bare basename cited in backticks** — a real file referenced
by name without a path, e.g. `` `gate_citation_lineage.py` ``, `` `case.md` ``,
`` `run-packet.md` ``. The checker resolved them at the repo root (where they
don't exist — they live under `scripts/`, `evals/…`) and failed.

Fix (this tranche): **a file ref must be path-like (contain a `/`)**. A bare
basename — even backticked — is a name, not a locatable path claim, and is
ignored (`Express.js`, `README.md`, `main.go` likewise). Effect on the dogfood
(reproducible over the 8 committed bodies — "after" is `make pr-provenance-dogfood`;
"before" toggles the path-like filter off over the same bodies):

| metric | before (no path-like rule) | after |
|---|---|---|
| file refs unresolved | 22 | 3 |
| PR bodies passing | 2 / 8 | 6 / 8 |

## Snapshot after the fix (8 saved bodies)

| body | pass | file (u) | test (u) | issue (u) | card (u) | commit (adv) |
|---|---|---|---|---|---|---|
| pr-11 | PASS | 8/0 | 0/0 | 0/0 | 0/0 | 0 |
| pr-19 | PASS | 3/0 | 0/0 | 0/0 | 0/0 | 0 |
| pr-21 | FAIL | 4/0 | 0/0 | 0/0 | 17/3 | 0 |
| pr-22 | PASS | 6/0 | 0/0 | 0/0 | 18/0 | 0 |
| pr-24 | PASS | 7/0 | 0/0 | 3/0 | 0/0 | 2 |
| pr-25 | PASS | 2/0 | 0/0 | 2/0 | 0/0 | 2 |
| pr-26 | PASS | 4/0 | 0/0 | 3/0 | 0/0 | 2 |
| pr-27 | FAIL | 11/3 | 1/1 | 3/2 | 4/4 | 1 |

Totals: file 45 (3 unresolved), test 1 (1), issue 11 (2), card 39 (7), commit 7
(0 advisory — all resolved).

## Remaining false positives are META PRs

The only two failing bodies are the tool's own meta PRs:

- **pr-27** (the `anti-slop-pr` PR): its unresolved refs are all **documentation
  examples** — `docs/foo.md`, `tests/x.py::…`, `#123`, `#9999`, `BK-1234-card-001`,
  `BK-7099-card-001`. The PR body *documents the checker*, so it necessarily
  contains fabricated example references.
- **pr-21** (the citation-lineage tool PR): unresolved `BK-9999-card-001` (the
  demo slop ID) and a literal `x-vs-y` placeholder.

This is an **inherent limitation**, not a defect: a PR that documents fabricated
example references will flag those examples. Ordinary feature/benchmark PRs
(pr-11, pr-19, pr-22, pr-24, pr-25, pr-26 — 6/6) resolve cleanly.

## Per-category usefulness

- **file** — rich and useful after the path-like fix (45 refs across 8 bodies);
  it would catch a genuinely fabricated path. Bare-basename mentions are now
  ignored (small false-negative, large false-positive reduction).
- **card / source** — rich (39 refs); the reused `anti-slop-lineage` resolver is
  the strongest signal, but meta PRs flag documented example IDs.
- **issue** — present (11), resolved against the public-number registry.
- **test** — **sparse** here: this repo has no `pytest` suite (its "tests" are
  `make` self-tests), so test-node refs barely appear. Valuable for repos that
  have a real test suite; low signal in this one.
- **commit** — present in ~half the recent bodies (7 refs), **all resolved**
  cleanly via local git, **zero** false positives. See decision below.

## Commit-ref decision: ADDED, advisory

Real PR bodies cite commit SHAs often enough to matter (each recent PR cites the
prior merge commit; 7 refs across the 8 bodies, all real commits). Implemented
commit resolution via **local `git cat-file`** (offline, no network/API),
**advisory by default** — a 7-40 hex token is ambiguous (commit SHA vs. a
non-commit hash such as a sha256 fragment), so it reports rather than fails, and
degrades gracefully when the root is not a git repo. Self-test + the
fixture/demo cover it. (The feared sha256 false-positives did not appear in the
PR *bodies* — long hashes live in committed docs, not descriptions — but the
advisory tier guards against them regardless.)

## Usefulness verdict

**Useful, with a known boundary.** On ordinary feature/benchmark PRs the checker
is clean and would catch a fabricated path, card, or issue before merge (and
flag a fabricated commit as advisory).
Its false positives are concentrated in PRs that *document* fabricated examples
(meta/tooling PRs). Launch recommendation: adopt **advisory-first** with the
`--report` flag (prints findings, never fails), then enforce on
non-documentation PRs once teams are comfortable. The tool resolves references;
it does not judge relevance, correctness, or support.

## Update: ignore directives close the meta-PR boundary

The two failing bodies in the snapshot (pr-21, pr-27) are exactly the meta-PR
class — PRs that cite fabricated example IDs on purpose. The follow-up tranche
added **explicit, auditable ignore directives** so such a PR can suppress its
documented examples line-by-line without weakening the checker:
`<!-- anti-slop-pr: ignore-next-line -->` and an
`<!-- anti-slop-pr: ignore-start --> … <!-- anti-slop-pr: ignore-end -->` block.

What changes on the boundary: a meta PR wraps only its example references and
**passes**, while every real reference outside the block is still checked
(demonstrated by `proof/pr-provenance-demo/meta-pr.md` — FAILs — vs.
`meta-pr-ignored.md` — PASSes; `make pr-provenance-demo` asserts both). The
directives are fail-safe (an unclosed `ignore-start` hides nothing and warns) and
the receipt records how many lines were ignored, so suppression stays auditable.
Prefer `ignore` (line-scoped, in the PR body) over `--report` (whole-PR advisory)
when only a few example refs need suppressing.
