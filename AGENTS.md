# AGENTS.md — Maintenance Contract for books-kb

This file is the authoritative maintenance contract for any agent — human or LLM — that touches the Anti-Slop books-kb repo. Read it before editing anything in the public tree.

## What this repo is

Anti-Slop books-kb is a Karpathy-style maintained Markdown knowledgebase for making AI-assisted advice inspectable before it becomes operational. It is not a raw book archive, not a prompt pack, not query-time RAG, and not the prior Canon Patch Trial workstream.

The repo is a maintained KB plus a receipt trail. Public Markdown pages compound over time; raw copyrighted sources never leave local-only storage.

## Three-layer mental model

1. **Raw sources** — local-only book files, OCR dumps, extracted text. Excluded from git by `.gitignore` and `scripts/check_no_raw_text.py`. Never read into repo artifacts.
2. **Public-safe KB** — Markdown pages in `kb/`, `corpus/`, `canon/`, `evals/`, `gates/`, `proof/`, `runs/`, `registry/`. Receipts only: metadata, locators, paraphrases, short conservative excerpts when necessary, cards, evals, gate logs, decisions.
3. **Schema and playbook layers** — `docs/` holds methodology, workflows, and policies. `scripts/` holds local validation and artifact helpers. These describe how the KB is operated.

## The three loops

**Ingest.** Add or update manifest/acquisition metadata. Create public-safe maps or cards. Update relevant index entries and cross-links. Append a log entry.

**Query.** Answer from approved KB artifacts. Name source lineage and uncertainty. Preserve contradictions instead of smoothing them away. File useful public-safe outputs back into the KB when appropriate.

**Lint.** Run `make validate`, `make check-raw`, `make kb-lint`. Fix failures before opening a PR or committing.

## index.md and log.md conventions

- `kb/index.md` is the content-oriented navigation layer. Updated whenever a new doc, template, or artifact category lands.
- `kb/log.md` is the chronological memory layer. Updated whenever the KB's public surface changes — new doc, new template, new policy, schema migration, decision.
- Log entries use the dated template at the bottom of `kb/log.md`. Empty fields are acceptable; silent omission is not. Write `Decision: —` rather than dropping the field.

## Authority order

Strictly enforced:

- Book maps are discovery aids, not canon.
- Source cards are evidence units, not canon.
- Claim/tension cards are synthesis units, not canon.
- Canon candidates are proposals.
- Canon requires operator approval.

Machine-generated maps or summaries must never become hidden canon. Promotion goes through the workflow at `docs/canon-promotion-workflow.md` with operator sign-off, recorded in `registry/`.

## No raw copyrighted text

Hard rule. See `docs/legal-publication-policy.md`. Do not commit:

- PDFs, EPUBs, MOBIs, AZW/AZW3 files, DJVU, CBZ/CBR.
- OCR dumps, extracted text, copied chapters, long excerpts.
- Public raw-text prompts or public embeddings of copyrighted source text.

Public artifacts are receipts. When in doubt, use locator plus paraphrase. The operator is responsible for final review; `.gitignore` and `scripts/check_no_raw_text.py` are defensive aids, not legal guarantees.

## No hidden canon drift

Canon changes only through the candidate → approval → registry path. Do not:

- Edit `canon/` files outside an approved promotion.
- Write a "synthesis" or "framework" page that functionally acts as canon without going through the workflow.
- Add an advisory claim to a non-canon page that quietly establishes a rule.

If a machine-generated map or card states an advisory claim, mark its authority level explicitly per `docs/source-authority-levels.md`.

## How future agents should update KB pages safely

1. **Read first.** `README.md`, this file, `kb/index.md`, `kb/log.md`, and the workflow doc relevant to the artifact type.
2. **Stay in scope.** Touch only the layer the task names. Do not refactor adjacent layers as a side effect.
3. **Use the helpers.** `scripts/new_*.py` create well-formed artifact skeletons; prefer those over hand-rolled files.
4. **Cross-link forward and back.** A new doc gets a link from `kb/index.md` and — if it changes the public surface — a `kb/log.md` entry.
5. **Run the gates locally.** `make validate && make check-raw && make kb-lint` before commit.
6. **Preserve the README.** Do not regrow archive/scaffold sections. Internal detail belongs in `docs/`, not in the README.
7. **Do not introduce model or API integrations.** This repo is an inspectable substrate, not a runtime.
8. **Never read or commit raw book content.** The substrate is locators plus paraphrases, not the books themselves.

## Acceptance gates

A change is accepted only if:

- `make validate` passes.
- `make check-raw` passes.
- `make kb-lint` passes.
- `python3 -m py_compile scripts/*.py` passes.
- No raw copyrighted text or raw book files are introduced.
- The README has not regained archive/scaffold clutter.
- Any new advisory claim has its authority level named.

If a check fails, fix it before commit. Do not skip hooks or bypass the gates.

## Related docs

- [docs/kb-maintenance-contract.md](docs/kb-maintenance-contract.md) — operational detail behind this contract.
- [docs/front-door-quality-gate.md](docs/front-door-quality-gate.md) — what `make kb-lint` enforces and why.
- [docs/end-to-end-walkthrough-template.md](docs/end-to-end-walkthrough-template.md) — full source-to-eval walkthrough skeleton.
- [docs/methodology.md](docs/methodology.md) — seven-layer substrate.
- [docs/legal-publication-policy.md](docs/legal-publication-policy.md) — the no-raw-text rule.
- [docs/source-authority-levels.md](docs/source-authority-levels.md) — how authority is named on advisory claims.
