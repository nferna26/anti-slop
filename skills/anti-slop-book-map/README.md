# anti-slop-book-map

Judgment rails for the books-kb book-map workflow. Encodes the hand-rolled process used for BK-0001 (Rumelt) and BK-0003 (Bryar & Carr) so future books and batches follow the same public-safe discipline, with map-lite for breadth and deep maps for anchors.

## What is in this skill

- `SKILL.md` — six workflows, shared contract, map-class policy, review checklist, batch rules, closing-gate commands. Open this first.
- `templates/` — seven short textual scaffolds for the artifacts the workflows produce.
- (no `.py` scripts, no automation — v1 is judgment rails only)

## Workflows

| Workflow | Purpose |
|---|---|
| `prepare-operator-approval` | Build a 4-file operator-approval packet for one source |
| `apply-verified-metadata` | After operator sign-off, apply the proposal to public manifests and the log |
| `draft-book-map` | Draft a public-safe map-lite or deep book map from verified metadata + heading structure |
| `review-book-map` | Run the 10-check review on an existing map; produce a local-only report |
| `batch-metadata-verify` | Run `prepare-operator-approval` across 3–5 sources |
| `batch-map-draft` | Run `draft-book-map` across a small compatible batch of verified sources |

## Invocation

The operator names a workflow and (where relevant) a `source_id` or list of `source_ids`. Claude opens `SKILL.md`, reads the matching `## Workflow N` section, follows the steps, and runs the closing-gate suite if public files are touched.

## v1 posture

Judgment rails, not a tooling framework. Helper scripts (gate runners, YAML patchers, metadata extractors) are deferred to v2 once batch failures teach which patterns are worth automating. The skill's first job is keeping Claude's behavior consistent across batches.
