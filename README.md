# Anti-Slop books-kb

Anti-Slop books-kb is a governed Markdown knowledgebase for making AI-assisted advice inspectable before it becomes operational.

## Objective

Build a citation-traceable, contradiction-aware advisory substrate from a sourced 200-book corpus.

### Program hypothesis (under test, not yet proven)

> A maintained knowledgebase with source lineage, contradiction handling, deterministic gates, and operator approval can reduce slop compared with vanilla model use and vanilla model use with famous manually supplied sources.

This is the hypothesis the eval lab tests. It is **not** established. Most of the
broad "reduce slop" / "improve advice" surface is still unproven, and at least
one careful baseline (a well-written `criteria_prompted_no_sources` prompt) is a
documented ceiling on general reasoning-disposition tasks.

### What is benchmark-supported so far (the narrow result)

One narrow, mechanical claim is benchmark-supported, under a frozen,
pre-registered rule, by two independent different-family hosted judges
(`evals/bibliographic-adversary/locator-accuracy-v4/`, `benchmark_supported`):

> Under adversarial citation pressure, the substrate workflow adds **inspectable
> reviewed public-KB lineage** — the correct card ID, the reviewed locator at the
> granularity the card carries, and the supported claim, while refusing
> unsupported card IDs, pages, quotes, false source relations, book-map evidence
> moves, and standing-canon claims — where source-free prompting (including a
> careful criteria prompt and famous-source awareness) cannot.

This is a claim about *mechanical lineage*, not about advice quality or source
truth. It does not say the substrate gives better recommendations; it says the
substrate supplies citations that resolve to reviewed evidence and that
controls, lacking the reviewed cards, cannot reproduce. The earlier `v3-v1`
attempt recorded `do_not_promote`; `v4-v1` carries the supported result after a
scoring-surface repair, with `v3-v1` left frozen as history.

This repo tests the method and ships its receipts; it is not a possession of
books.

## Why

AI can sound strategic while quietly failing at the parts that matter: fabricated lineage, famous-source defaults, flattened contradictions, universal advice from narrow cases, and no audit trail for what changed the recommendation.

Anti-Slop turns that into a workflow:

```text
source -> map -> card -> preserve tension -> propose canon -> test -> publish receipts
```

The point is not to make AI sound more informed. The point is to make advice accountable: what sources were allowed, what claims were rejected, what contradictions remained unresolved, what gates failed, and what changed in the KB.

## What This Is

This is a Karpathy-style persistent Markdown knowledgebase, not a prompt pack and not query-time RAG.

- Raw sources stay local-only.
- Public-safe Markdown pages compound over time.
- Maps and cards organize source lineage.
- Tension cards preserve disagreement instead of smoothing it away.
- Canon requires explicit operator approval.
- Evals and gates test whether the method beats simpler baselines.

## What This Is Not

- Not a public archive of copyrighted book text.
- Not a raw document dump.
- Not a vector store of book contents.
- Not a replacement for the books.
- Not a claim that 200 books automatically make AI advice better.

Canon Patch Trial is prior context only. It is not the active workstream and not a gate.

## Publication Rule

Raw copyrighted book text must never be committed.

No PDFs, EPUBs, MOBIs, AZW files, OCR dumps, extracted text, copied chapters, long excerpts, public raw-text prompts, or public embeddings of copyrighted source text.

Public artifacts are receipts: metadata, locators, short conservative excerpts when necessary, paraphrases, cards, evals, gate logs, model-output metadata, decisions, and methodology notes.

## Authority Order

- Book maps are discovery aids, not canon.
- Source cards are evidence units, not canon.
- Claim/tension cards are synthesis units, not canon.
- Canon candidates are proposals.
- Canon requires operator approval.

Machine-generated maps or summaries must never become hidden canon.

## Proof Surface

The first eval families:

- bibliographic adversary
- contradiction preservation
- canon promotion tournament
- long-tail transfer
- source-lineage hostile

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
- `pr-provenance` (`scripts/gate_pr_provenance.py`, `anti-slop-pr`) —
  *implemented*: resolves the issue / file / test / source-card / commit
  references a PR description cites against a repo or fixture root, failing on
  unresolved references. The card check reuses the citation-lineage resolver
  unchanged; stdlib-only, no GitHub API / model / network (commit refs use only
  local git). It resolves references, it does not judge relevance, correctness,
  or support. File refs must be path-like; issue refs are deterministic only
  against a supplied registry (advisory otherwise); commit refs are advisory.
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
