# KB Maintenance Contract

This doc expands on the maintenance contract stated in `../AGENTS.md`. It is the operational reference for keeping the public KB internally consistent as the corpus grows.

## What the KB owes its readers

- **Lineage.** Every advisory claim cites the source card(s) supporting it. Source cards cite the source's locator (book + chapter + page or section). No claim without lineage.
- **Contradiction.** When two cards disagree, both are preserved as a tension card. The KB does not pick a winner without going through canon promotion.
- **Uncertainty.** Open questions live in `../kb/index.md` under "Current Open Questions" and in the question template in `../kb/questions/`. Silent omission is not acceptable — a known unknown is recorded as a known unknown.
- **Authority level.** Each advisory claim states its authority on the page that carries it (source / synthesis / canon-candidate / canon). See [source-authority-levels.md](source-authority-levels.md).

## Lifecycle of an artifact

| Stage | Lives in | Authority | Approval required |
|---|---|---|---|
| Manifest entry | `corpus/manifests/` | metadata | none beyond manifest schema |
| Book map | `corpus/book-maps/` | discovery aid | none |
| Source card | `corpus/source-cards/` | evidence | operator verification per source-card workflow |
| Claim/tension card | `corpus/claim-tension-cards/` | synthesis | operator review |
| Canon candidate | `corpus/canon-candidates/` | proposal | none to draft; explicit approval to promote |
| Canon | `canon/` | advisory | explicit operator approval, recorded in `registry/` |

## Cross-link conventions

- `../kb/index.md` lists every public-surface category. New docs, templates, or workflow files get a link.
- `../kb/log.md` records what changed and when. Dated entries follow the template at the bottom of that file.
- Public Markdown files link with relative paths (`../docs/foo.md`), not absolute. `scripts/kb_lint.py` verifies links are not broken.

## What to do when something is off

- **Stale page** — open a tension card or an open question in `../kb/index.md`. Do not silently rewrite.
- **Broken link** — fix at the source, not by removing the link.
- **Drifted authority** — flag in `../kb/log.md` under "Decision" and walk it back through the workflow.
- **Missing log entry** — add it. Date-stamp. Note the back-fill.

## See also

- `../AGENTS.md` — the maintenance contract.
- [methodology.md](methodology.md) — the seven-layer substrate.
- [canon-promotion-workflow.md](canon-promotion-workflow.md) — how a candidate becomes canon.
- [source-authority-levels.md](source-authority-levels.md) — naming authority on advisory pages.
- [front-door-quality-gate.md](front-door-quality-gate.md) — what the kb-lint script enforces.
