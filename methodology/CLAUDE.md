> Template — adapt to your domain. This is the rules layer for the schema described in methodology/schema.md. Drop at the root of your KB.

# CLAUDE.md — Session Rules

You are working inside the **<your-kb-name>** knowledge base. <!-- e.g. engineering-kb, design-kb, ops-kb --> This repo binds to the schema described at `anti-slop/methodology/schema.md`. (Operators with their own shared-kernel SCHEMA can swap the path; the rules below are unchanged.) Quality over speed.

## Architecture

Five-layer repo: `raw/` → `cards/` → `canon/` → `execution/` → `registry/`. Source of truth is the repo, not the model.

## Session rules

### Plan mode

Use plan mode BEFORE:
- Designing a new page type (even "just a small one" — it ripples)
- Writing any script that touches `registry/kb.sqlite`
- Adding any playbook or significantly editing an existing one
- Any step where you're unsure about the right structure

Do NOT use plan mode for:
- Creating directories and `.gitkeep` files
- Writing pages against existing templates where the structure is clear
- Mechanical file moves or renames

### Commits

Commit after EVERY completed step. Conventional commit messages:
- `feat: <what>` — new content or capability
- `fix: <what>` — correction to existing content
- `docs: <what>` — documentation-only

Never batch multiple logical steps into one commit. The git history IS the audit trail.

### Quality bar

- Every `.md` file in `cards/`, `canon/`, or `execution/` MUST have valid YAML frontmatter. Parse-test it.
- Every guardrail checklist item must be a concrete, testable rule — never vague advice.
- This file is a resolver, not a bible. Keep it ≤ 250 lines.
- Python scripts: executable, shebanged, `sqlite-utils` for DB work (no raw DDL).
- Every canon page cites ≥ 2 source cards via `source_refs`.

### Do not

- Create files outside the <your-kb-name> repo
- Install global packages without asking
- Skip frontmatter on any page in `cards/`, `canon/`, `execution/`
- Write playbook content into this file — it goes in `canon/playbooks/`

### Owners

Primary owner for this KB: <your-owner>. <!-- e.g. founder, platform-lead, head-of-research -->

### Domains

<your-kb-name> covers: <your-domain-list>. <!-- comma-separated, e.g. product,design,ux,research  or  finance,ops,people,m-and-a  or  architecture,security,data -->

## Playbooks

Operational playbooks live under `canon/playbooks/playbook-*.md` — one per repeatable task. The anti-slop pack will ship universal playbooks (book ingestion, query writeback, skill improvement, KB health check) as those layers come online; until those land, define your own and link them here. On first use, rewrite each Worked Example with content from your own domain.

## Verification

After any non-trivial edit:
1. Run the KB lint Skill — must report no CRITICAL findings.
2. Rebuild the registry index — should be idempotent.
3. `git log --oneline` — confirm one commit per logical step.

These steps will be backed by lint and index Skills in `skills/lint/` and `skills/index/` as those Skills ship. Operators using their own shared kernel can substitute kernel scripts.

## Kernel-level changes

If you find a genuine improvement to the schema (`methodology/schema.md`), the lint Skill, or the universal playbooks, do NOT modify the methodology from inside this KB's session. Log the idea in a local `IMPROVEMENTS.md` with a dated entry, or open an issue on the upstream anti-slop repository, and address it in a separate session. Methodology changes are cross-cutting and need their own audit trail.
