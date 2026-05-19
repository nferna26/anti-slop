# Phase 0 Closeout

Phase 0 was the scaffold-and-rules phase: stand up the substrate's structure, publication policy, contracts, and front-door discipline before any substrate content lands. This doc records what closed and what remains manual.

## What is closed

### Structural

- Five-layer repo present: `kb/`, `corpus/`, `canon/`, `evals/`, `gates/`, `proof/`, `runs/`, `registry/`.
- Local-only shelf convention: `local-only/` and the `.gitignore` defensive rules.
- README is punchy and aligned to current product shape; not regrown.
- AGENTS.md maintenance contract present at repo root.

### Policy

- `legal-publication-policy.md` — no raw copyrighted text in the public repo.
- `local-source-shelf.md` — local-only conventions, locator-not-path rule, lawful access only.
- `public-writing-rules.md` — receipts before claims, no overclaiming, negative-evidence format, claim boundary.
- `source-authority-levels.md` — authority signaling per artifact.

### Contracts

- `AGENTS.md` — three-layer mental model, three loops, authority order, eight rules for future agents.
- `kb-maintenance-contract.md` — operational expansion of AGENTS.md.
- `front-door-quality-gate.md` — what `make kb-lint` enforces and why.

### Glossary and discipline

- `artifact-definitions.md` — every public-safe artifact, with authority level and home directory.
- `operator-roles.md` — the six roles (GM, source owner, judge, editor, canon owner, eval owner).
- `wip-limits.md` — caps at every layer of the artifact ladder.

### Walkthrough

- `end-to-end-walkthrough-template.md` — fill-in-the-blanks skeleton from source candidate through log entry.

### Gates

- `make validate` — manifest schema.
- `make check-raw` — defensive heuristic for raw-text leakage.
- `make kb-lint` — front-door structural lint (kb/index.md, kb/log.md, AGENTS.md, README sections, broken links, raw-source extensions).
- `python3 -m py_compile scripts/*.py` — script syntax.

### Front-door files

- `kb/index.md` — navigation layer including Start Here, Operator and Agent Reference, Active Corpus, Artifact Templates, Proof Surface, Open Questions, Authority Reminder.
- `kb/log.md` — chronological log with dated entries and the log entry template at the bottom.

## What remains manual

These are not engineering gaps. They are decisions only the operator can make.

- Choosing which roles are vacant vs filled for the current solo phase.
- Adjusting WIP caps if the substrate's actual work rate diverges from the defaults.
- Deciding when an additional contributor needs explicit role assignment.
- Choosing the next eval family to seed once Phase 1 acquisition produces enough source cards.

## What is explicitly NOT in scope for Phase 0

- Building book maps. (Phase 2.)
- Drafting source cards from book content. (Phase 2.)
- Authoring claim or tension cards. (Phase 2.)
- Promoting anything to canon. (Phase 3+.)
- Running model evals. (Phase 3+.)

## How to verify Phase 0 closeout locally

```sh
make validate
make check-raw
make kb-lint
python3 -m py_compile scripts/*.py
```

All four should pass. `make check-raw` will emit informational warnings on the two structured manifests:

- `corpus/manifests/books-200.yaml`
- `corpus/manifests/acquisition-registry.yaml`

Both files are curated metadata (not raw source text) and legitimately exceed the size heuristic. The warning text identifies them as such. Documented further in `front-door-quality-gate.md` and `legal-publication-policy.md`.
