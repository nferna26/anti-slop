# anti-slop-pr — PR-description provenance checker

`scripts/gate_pr_provenance.py` (`anti-slop-pr`) is a **deterministic**,
stdlib-only checker for the references an AI-written PR description cites. It
catches the cheap, common failure — a fabricated issue number, a doc/file path
that was never added, a test node that is not defined, a source-card ID that does
not resolve — **before merge**. No GitHub API, no model, no network, no runtime.

It is a *resolver*, not a judge. See "What it cannot catch".

## Why this matters

An AI agent opens a PR with a confident description:

> Fixes #4123. Adds `docs/rate-limiting.md` and is covered by
> `tests/test_limiter.py::test_burst`. Lands on commit `9f3a2b1`.

…but issue #4123 doesn't exist, `docs/rate-limiting.md` was never added,
`test_burst` isn't defined, and `9f3a2b1` isn't a real commit. `anti-slop-pr`
resolves each reference against the repo and fails before merge — turning a
plausible-sounding description into a checkable one. It says nothing about
whether the change is *good*; only whether what the PR *cites* is real.

This was [dogfooded on this repo's own PR bodies](pr-provenance-dogfood-memo.md).

## Install / run

```sh
# Checkout mode (no install):
python3 scripts/gate_pr_provenance.py --root . path/to/pr-body.md
python3 scripts/gate_pr_provenance.py --self-test

# Package mode (installed alongside anti-slop-lineage):
pip install .
anti-slop-pr --root . --issue-registry .known-issues.txt path/to/pr-body.md

# Advisory adoption: print findings but always exit 0 (don't block yet):
anti-slop-pr --root . --report path/to/pr-body.md

# Make targets:
make pr-provenance ROOT=. PR=path/to/pr-body.md [ISSUES=known-issues.txt]
make pr-provenance-self-test
make pr-provenance-demo        # passing + failing sample bodies vs a fixture root
make pr-provenance-dogfood     # report over this repo's own saved PR bodies
```

Exit `0` when every hard reference resolves, `1` when any hard reference is
unresolved, `2` on usage error. `--report` forces exit 0 (advisory mode). With
`--json OUT` it also writes a JSON receipt.

## What it checks (tiers — deterministic vs advisory)

**Deterministic (hard; unresolved → exit 1), resolved against `--root`:**

- **file refs** — `docs/foo.md`, `path/to/x.py`, optionally `path.py:L10` (the
  file must exist; with a line number it must have at least that many lines). A
  token is a file ref only when it is **path-like** (contains a `/`); a bare
  basename — even in backticks (`README.md`, `gate.py`, `Express.js`) — is a
  *name*, not a locatable path, and is ignored. (Dogfooding real PR bodies showed
  bare backtick basenames were the dominant false positive; see the memo.)
- **test refs** — `tests/test_x.py::test_name` (the file must exist **and**
  define `def test_name` / `async def test_name` / `class test_name`).
- **card / source refs** — `BK-1234` / `BK-1234-card-001`, delegated to the
  `anti-slop-lineage` resolver (`gate_citation_lineage`); with
  `--require-reviewed-cards`, a cited card must resolve to a **reviewed** source
  card.

**Deterministic against a registry (hard only with `--issue-registry`, else
ADVISORY):**

- **issue refs** — `#123`. Offline there is no way to know an issue's state
  without a credential, and this tool adds **no** GitHub API. With a registry of
  valid issue numbers (produced offline) unresolved issues fail; without one they
  are reported as advisory and never fail the build.

**Advisory (always reported, never fails):**

- **commit refs** — 7–40 hex tokens (with at least one `a–f`) resolved against
  the **local git** repo at `--root` (`git cat-file`). A hex token is ambiguous
  (a commit SHA vs. a non-commit hash), so commit refs are advisory by default
  and degrade gracefully when `--root` is not a git repo. Local git only — no
  network or GitHub API.

HTML comments (`<!-- ... -->`) are ignored — GitHub hides them, so they are not
part of the PR's visible claim.

## What it cannot catch

A passing check means the cited references **resolve**, nothing more. It does
**not** verify:

- **Relevance** — a resolvable `docs/foo.md` or test node might be the *wrong*
  one for the change. The tool checks existence, not aptness.
- **Correctness / support** — it does not run the cited test, does not check the
  PR does what it says, and does not judge whether a cited card actually supports
  the claim (that is the difference between resolution and the benchmark — see
  `docs/citation-lineage-gate.md`).
- **Issue state** without a registry; **renamed-but-present** files cited at an
  old path; references written in prose that do not match the reference patterns.
  A real file mentioned only by **bare basename** (no `/`) is not checked — the
  path-like rule trades that miss for not failing on the bare basenames real PR
  bodies use constantly.
- **Meta / documentation PRs** that *cite fabricated example references on
  purpose* (e.g. a PR documenting this very tool) will flag those examples. Use
  `--report` (advisory) for such PRs. This is inherent to checking citations.
- Anything about advice quality, source truth, reasoning, slop, or canon. It
  promotes no canon and lifts no status.

## Relation to `anti-slop-lineage`

The **card/source** portion of `anti-slop-pr` *is* `anti-slop-lineage`: it reuses
the same `build_index` + `check_paths` resolver **unchanged** (no fork). The
benchmark result (locator-accuracy-v4) backs **only** that card/source
mechanical-lineage resolution — *does a cited card/source reference resolve to
real public-KB lineage* (and, under `--require-reviewed-cards`, to a reviewed
source card).

The **file / test / issue** checks are new stdlib resolution added by
`anti-slop-pr`. They apply the same idea — *does a cited reference resolve?* — but
are **not** benchmark-backed and carry no benchmark claim. Same deterministic,
stdlib-only, no-model posture; same narrow "resolves, does not judge" claim. It
is a checker, not an advisor.
