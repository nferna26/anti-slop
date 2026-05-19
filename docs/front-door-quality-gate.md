# Front-Door Quality Gate

`make kb-lint` is the local pre-commit gate for the public front door of books-kb: `README.md`, `AGENTS.md`, `kb/index.md`, `kb/log.md`. It catches the structural failure modes that erode the repo's claim to be a maintained KB rather than a scratch pad.

## What it checks

1. **`kb/index.md` exists.** The navigation layer must always be present. A KB without an index is a dump.
2. **`kb/log.md` exists.** The chronological memory layer must always be present. A KB without a log loses provenance.
3. **`AGENTS.md` exists at the repo root.** The maintenance contract must be discoverable from the top of the tree.
4. **`README.md` has no "Archived Legacy Work" section.** Archive content lives in `_archive/`, not on the front door. A regrown archive section is the lint-detectable symptom of scope drift.
5. **`README.md` contains "Objective", "Publication Rule", "Proof Surface", and "Start" sections.** These are the four anchors a first-time reader needs in order to understand the claim, the rule, the test, and the next action.
6. **Local Markdown links are not broken.** A relative link to a path that does not exist on disk is an error. Broken links inside the KB compound silently.
7. **Public Markdown files do not name raw-source filename extensions.** Filename extensions for EPUB, PDF, MOBI, AZW, AZW3, DJVU, CBZ, and CBR formats appearing inside a Markdown file are a smell — either we are about to commit raw content, or we are sloppily naming files in advisory prose. See `scripts/kb_lint.py` for the exact regex. Allowed exceptions:
   - the repo's `.gitignore` — that file's job is to list extensions.
   - `docs/legal-publication-policy.md` — that file's job is to state the rule.
   - `README.md` inside the Publication Rule section — bounded to the publication-rule statement.

## What it does not check

- Card content quality — that is the source-card workflow's job.
- Quote-limit compliance — that is `scripts/check_no_raw_text.py`'s job (`make check-raw`).
- Manifest schema — that is `scripts/validate_manifest.py`'s job (`make validate`).
- Canon-promotion correctness — that is the operator's job, recorded in `registry/`.

## How to fix common failures

| Failure | Fix |
|---|---|
| `AGENTS.md` missing | Add the file at repo root with the maintenance contract. |
| README missing one of the four sections | Add the section. Do not rename existing sections to satisfy the lint — they are named what they are named on purpose. |
| README has "Archived Legacy Work" section | Move the content to `../_archive/` and remove from README. |
| Broken local link | Fix the link or move/restore the target. |
| Raw extension in public Markdown | If the reference is unavoidable, move it to an allowed location or rewrite to reference the locator (book + chapter + page) instead. |

## Standard-library only

`scripts/kb_lint.py` is intentionally Python standard-library only. Anyone with Python 3 can run the gate. No `pip install` required. If a check requires a third-party dependency, it does not belong in this script — it belongs in a separate tool with its own setup story.

## Relationship to the other gates

- `make validate` — manifest schema validation plus acquisition registry validation when present. Structural.
- `make check-raw` — defensive heuristic for raw text leaking into the public tree. Content-shaped.
- `make kb-lint` — front-door structural lint. Cross-cutting.
- `make report` — public-safe status report on the 200-book manifest and wave-1 progress. Read-only.

All three checks (validate / check-raw / kb-lint) run before commit. None of them is a legal guarantee; they are defensive aids, not substitutes for operator review.

## Large structured manifests

`scripts/check_no_raw_text.py` warns on any text-like file over the size threshold (default 75,000 bytes). The 200-entry manifest and the acquisition registry legitimately exceed that threshold — they are curated metadata, not raw source text. The script recognizes those two paths (`corpus/manifests/books-200.yaml`, `corpus/manifests/acquisition-registry.yaml`) and emits a clearer informational warning for them. The threshold is intentionally left in place so a third large file would still raise a question.

The script's exit code is 0 in either case; the warning is signal, not failure.
