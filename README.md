# Anti-Slop

**Make AI coding agents cite receipts, not vibes.**

Anti-Slop is deterministic **agent claim verification** for AI coding agents. It
checks whether the references and receipts an agent cites resolve against repo
state, so a reviewer can separate "this exists" from "the agent said it exists."

The contract is intentionally narrow: Anti-Slop verifies **resolution of
references and receipts**. It does **not** verify correctness, relevance, source
truth, support, advice quality, reasoning, safety, or canon.

## Objective

Make AI coding agents cite concrete receipts, then deterministically resolve
those references against repo state. Start with PR bodies, keep report-mode
adoption easy, and keep enforcement limited to claims a resolver can actually
check.

## Surface #1: PR Bodies

PR descriptions are the first shipped surface, not the whole category.

`anti-slop-pr` checks the file / test / source-card / issue / commit references
an AI-written PR body cites. `anti-slop-pr-event` runs the same check from a
GitHub Actions `pull_request` event payload without a GitHub API call or token.
Both are stdlib-only and run offline against the checked-out repo.

Start in report mode: findings are printed, but the check exits 0. Enforcement
is explicit opt-in once a repo is ready.

## Generic Artifacts

`anti-slop-claims` is the generic artifact-checking entrypoint. It accepts a
Markdown/text artifact such as `AGENT_FINAL_REPORT.md` and uses the same
reference resolver engine as `anti-slop-pr`.

This is a packaging/API shape change, not a semantic expansion. The generic
entrypoint still resolves references only; it does not add diff-aware changed-file
checks, command-receipt validation, benchmark-receipt validation, or a new JSON
receipt schema.

## Install It

Point a coding agent at [`INSTALL_FOR_AGENTS.md`](INSTALL_FOR_AGENTS.md) (short
entrypoint: [`llms.txt`](llms.txt)) with this prompt:

> **"Install anti-slop-pr in this repo, run the smoke, add report-mode CI, and open a PR."**

The core commands are:

```sh
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop"
anti-slop-pr --self-test
anti-slop-pr-event --self-test
anti-slop-claims --self-test
anti-slop-claims --root . AGENT_FINAL_REPORT.md --report
anti-slop-pr --root . <pr-body.md> --report
```

See [`docs/pr-provenance.md`](docs/pr-provenance.md) for usage and
[`docs/agent-claim-verification.md`](docs/agent-claim-verification.md) for the
supported-claims matrix.

## What It Checks

The supported-claims matrix is load-bearing:

- Hard resolution: path-like file refs, test nodes, source/card refs.
- Registry-backed resolution: issue refs when a numbers-only registry is
  supplied.
- Advisory refs: commit refs; issue refs without a registry.
- Path-only resolution can be used for cited docs or receipt artifact paths, but
  this tranche does not implement diff-aware changed-file checks,
  command-receipt validation, or benchmark-receipt validation.
- Out of scope: "fixed", "safe", "supported", "correct", and similar claims
  whose truth cannot be mechanically proven by reference resolution.

A PASS means cited artifacts resolved. It is not a quality verdict.

## Why

AI coding agents can write confident change summaries while quietly inventing
files, tests, issues, commits, commands, benchmark receipts, or source-card
references. Anti-Slop turns those claims into checkable references before merge.

The point is not to make AI sound more informed. The point is to make its claims
inspectable: what was cited, what resolved, what was advisory, and what remains
outside the resolver's authority.

## What This Is Not

- Not a model, hosted service, API integration, RAG layer, vector store, or agent
  runtime.
- Not a correctness checker.
- Not a relevance, support, safety, advice-quality, reasoning, or source-truth
  judge.
- Not a canon or authority-promotion mechanism.
- Not a public archive of copyrighted source text.

## Publication Rule

Raw copyrighted source text must never be committed.

No PDFs, EPUBs, MOBIs, AZW files, OCR dumps, extracted text, copied chapters,
long excerpts, public raw-text prompts, or public embeddings of copyrighted
source text.

Public artifacts are receipts: metadata, locators, short conservative excerpts
when necessary, paraphrases, cards, evals, gate logs, model-output metadata,
decisions, and methodology notes.

## Authority Order

- Book maps are discovery aids, not canon.
- Source cards are evidence units, not canon.
- Claim/tension cards are synthesis units, not canon.
- Canon candidates are proposals.
- Canon requires operator approval.

Machine-generated maps or summaries must never become hidden canon.

## Evidence History

Anti-Slop came out of `Anti-Slop books-kb`: a governed Markdown knowledgebase
and eval lab for making AI-assisted advice inspectable before it becomes
operational. The older 200-book corpus work remains in this repo as history,
evidence, and receipts, not as the public product category.

### Program hypothesis (under test, not yet proven)

> A maintained knowledgebase with source lineage, contradiction handling,
> deterministic gates, and operator approval can reduce slop compared with
> vanilla model use and vanilla model use with famous manually supplied sources.

This hypothesis is **not** established. Most of the broad "reduce slop" /
"improve advice" surface is still unproven, and at least one careful baseline
(a well-written `criteria_prompted_no_sources` prompt) is a documented ceiling
on general reasoning-disposition tasks.

### What is benchmark-supported so far (the narrow result)

One narrow, mechanical claim is benchmark-supported, under a frozen,
pre-registered rule, by two independent different-family hosted judges
(`evals/bibliographic-adversary/locator-accuracy-v4/`, `benchmark_supported`):

> Under adversarial citation pressure, the substrate workflow adds **inspectable
> reviewed public-KB lineage** - the correct card ID, the reviewed locator at the
> granularity the card carries, and the supported claim, while refusing
> unsupported card IDs, pages, quotes, false source relations, book-map evidence
> moves, and standing-canon claims - where source-free prompting (including a
> careful criteria prompt and famous-source awareness) cannot.

This is a claim about *mechanical lineage*, not about advice quality or source
truth. It does not say the substrate gives better recommendations; it says the
substrate supplies citations that resolve to reviewed evidence and that
controls, lacking the reviewed cards, cannot reproduce. The earlier `v3-v1`
attempt recorded `do_not_promote`; `v4-v1` carries the supported result after a
scoring-surface repair, with `v3-v1` left frozen as history.

## Proof Surface

The gates fall into two tiers, and the distinction is load-bearing:

**Deterministic gates** — a reference either resolves or it does not; the check
is mechanical and reproducible:

- `citation-lineage` (`scripts/gate_citation_lineage.py`) — *implemented*: every
  cited source ID, source-card ID, claim/tension-card ID, or card path must
  resolve in the public KB; with `--require-reviewed`, every source-card
  reference must resolve to a *reviewed* card. This is the operational form of
  the **benchmark-supported** mechanical-lineage primitive (locator-accuracy-v4).
  It is self-tested (`make gate-citation-lineage-self-test`), dogfooded over the
  KB's own lineage artifacts (`make citation-dogfood`), demonstrated end-to-end
  (`make demo`), run in CI (`.github/workflows/ci.yml`), and installable as the
  stdlib-only `anti-slop-lineage` CLI (`pip install .`; isolated-install smoke
  `make package-smoke`) — packaging adds distribution, not capability. Usage:
  [`docs/citation-lineage-gate.md`](docs/citation-lineage-gate.md).
- `claims` (`scripts/gate_claims.py`, `anti-slop-claims`) - *implemented*:
  generic artifact-checking entrypoint for deterministic agent claim
  verification. It accepts Markdown/text artifacts such as
  `AGENT_FINAL_REPORT.md` and reuses the `anti-slop-pr` resolver engine for
  file / test / source-card / issue / commit references. This is packaging/API
  shape only; it does not add diff-aware changed-file checks, command receipts,
  benchmark receipts, or a new JSON receipt schema. Self-tested
  (`make claims-self-test`) and package-smoked (`make package-smoke`).
- `pr-provenance` (`scripts/gate_pr_provenance.py`, `anti-slop-pr`) -
  *implemented*: surface #1 PR-body preset for deterministic agent claim
  verification. It
  resolves the issue / file / test / source-card / commit references a PR body
  cites against a repo or fixture root, failing on
  unresolved references. The card check reuses the citation-lineage resolver
  unchanged; stdlib-only, no GitHub API / model / network (commit refs use only
  local git). It resolves references, it does not judge relevance, correctness,
  support, safety, advice quality, reasoning, source truth, or canon. File refs
  must be path-like; issue refs are deterministic only against a supplied
  registry (advisory otherwise); commit refs are advisory.
  `--report` gives an advisory (exit-0) mode, and explicit, auditable
  `<!-- anti-slop-pr: ignore-next-line -->` / `ignore-start`…`ignore-end`
  directives let docs PRs suppress intentionally-fabricated example refs
  line-scoped (an unclosed directive is a fail-safe no-op). Self-tested
  (`make pr-provenance-self-test`, 22 checks), demonstrated incl. the escape hatch
  (`make pr-provenance-demo`), and
  [dogfooded on this repo's own PRs](docs/pr-provenance-dogfood-memo.md)
  (`make pr-provenance-dogfood`). Adopt it as a GitHub PR check with the event
  wrapper `anti-slop-pr-event` (`scripts/pr_provenance_from_github_event.py`),
  which reads the PR body from the pull_request event payload — no GitHub API;
  non-PR events SKIP — report mode by default, enforcement opt-in
  (`make pr-provenance-event-demo`). Usage: [`docs/pr-provenance.md`](docs/pr-provenance.md).
- raw-text / quote check (`scripts/check_no_raw_text.py`, `make check-raw`) —
  *implemented*: a mechanical scan for committed raw copyrighted text.
- quote-limit, authority-order — *scaffold-only* (`gates/gate-specs.yaml`):
  mechanical in principle, specified but not yet implemented as scripts; the
  authority ladder is currently enforced by `AGENTS.md` / `CLAUDE.md` review, not
  by a gate.

**Heuristic gates** — a conservative pattern check that flags a likely failure
but does not prove correctness, and is not benchmark-backed:

- `no-universalization` (`scripts/gate_no_universalization.py`) — *implemented*:
  flags broad advice stated without nearby scope language. Advisory only — it
  catches a simple failure shape, not a proof that a scoped claim is right.
- source-diversity, canon-duplication, contradiction — *scaffold-only* design
  targets, advisory.

Positive evidence requires more than a better-sounding answer. For the broad
advisory claim it requires fewer critical failures, better source fit, better
contradiction preservation, and better gate compliance than baselines — a bar
not yet cleared. Only the narrow mechanical-lineage claim is benchmark-supported
so far.

See [proof/README.md](proof/README.md).

## Start

Current status: Phase 0 (scaffold + rules) and Phase 1 (manifest + acquisition registry) closed. `corpus/manifests/books-200.yaml` carries the operator-provided 200-book corpus. `corpus/manifests/source-id-registry.yaml` locks wave-1 at BK-0001 through BK-0050. `corpus/manifests/acquisition-registry.yaml` carries the public-safe rights/access view.

Run:

```sh
make validate
make check-raw
make kb-lint
make report
```

Create artifacts:

```sh
python3 scripts/new_book_map.py <source_id>
python3 scripts/new_source_card.py <source_id>
python3 scripts/new_claim_tension_card.py <slug>
python3 scripts/new_canon_candidate.py <slug>
python3 scripts/new_eval_case.py <eval_type> <case_id>
python3 scripts/new_gate_log.py <run_id>
```

Next useful path:

1. Verify rights/access for BK-0020 and BK-0046 (currently `raw_source_status: metadata_only`).
2. Verify edition / publisher / ISBN / year for the wave-1 books with local filename evidence; lift `edition_verified` in the acquisition registry.
3. Pick a locator scheme per source; lift `locator_confidence` from `none` only on verification.
4. Create the first public-safe book map (start with a wave-1 map candidate).
5. Run gates.
6. Log the result in `kb/log.md`.

## Repo Map

- `kb/`: maintained Markdown KB, index, log, question and synthesis templates.
- `corpus/`: manifests, maps, source cards, tension cards, canon candidates.
- `canon/`: operator-approved concepts, patterns, guardrails, and playbooks.
- `evals/`: proof-surface cases.
- `gates/`: gate definitions.
- `proof/`: claims, baselines, proof thresholds, and falsifiers.
- `runs/`: model-output metadata, gate logs, and score sheets.
- `registry/`: accepted, rejected, deferred, and retired decisions.
- `scripts/`: local validation and artifact helpers.

## Claim Boundary

This project does not prove that Anti-Slop improves advice. One narrow,
mechanical claim is benchmark-supported (the substrate adds inspectable reviewed
public-KB lineage that source-free prompting cannot — locator-accuracy-v4); the
broad "reduce slop / improve advice" claim is not, and a careful criteria prompt
remains a documented ceiling on general reasoning-disposition tasks.

A benchmark-supported eval decision is evidence about scoring behavior under a
frozen rubric, never source truth, never an advice claim, and never canon; canon
still requires a separate, explicit operator decision.

If evals show no meaningful delta over simpler baselines, the method should
narrow or reset.
