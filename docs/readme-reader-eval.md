# README Reader Eval

Date: 2026-05-19

## Eval Question

Fast forward one year. If different readers land on the README, do they know what Anti-Slop books-kb is, why it matters, and how to try or evaluate it?

## Current README Score Before Revision

Overall: 6 / 10

## Persona Scores Before Revision

| Reader | Score | Why |
| --- | ---: | --- |
| New reader | 5 | The README explained artifacts but did not quickly explain why someone should care or what they can try. |
| Executive evaluator | 6 | The governance posture was strong, but the leadership/business relevance was implicit. |
| Consulting customer | 5 | The method sounded careful, but the customer path and deliverable were unclear. |
| AI frontier lab | 7 | The eval/gate idea was interesting, but the persistent-KB research claim and baselines were underdeveloped. |

## Why It Was Not A 10

- The objective was accurate but too internal.
- The README described scaffolding more than outcomes.
- The Karpathy-style KB requirement was not visible enough.
- There was no simple explanation of what changes in a recommendation.
- There was no explicit audience map.
- There was no proof threshold or decision rule near the top.
- There was no repo-level `kb/` front door with index/log conventions.
- There was no `proof/` layer separating claims from evidence.
- The try-it path was command-heavy and not framed as a first workflow.

## Revision Goals

- Lead with the problem and testable bet.
- Make the persistent Markdown KB the product shape.
- Explain the value for new readers, executives, customers, and research partners.
- Add an obvious first workflow.
- Add a proof plan that says what would falsify or narrow the claim.
- Add `kb/index.md` and `kb/log.md`.
- Add KB linting so the shape is operational.

## Projected Score After Revision

Overall: 9 / 10

| Reader | Score | Why |
| --- | ---: | --- |
| New reader | 9 | The README now explains the problem, the product shape, what is safe to inspect, and a first workflow. |
| Executive evaluator | 9 | The README now frames the project as practical AI governance and decision-quality infrastructure. |
| Consulting customer | 8 | The README now explains the workbench and deliverable, but real examples are still needed to create buying confidence. |
| AI frontier lab | 9 | The README now states the persistent-KB hypothesis, baselines, gates, and falsification posture. |

## Remaining Gap

The missing point depends on real receipts: populated corpus, reviewed cards, failed gates, eval outputs, and examples of before/after advisory quality. Copy and structure can make the project legible, but only evidence can make it fully compelling.

## Implemented Shape Changes

- Rewrote the README around problem, objective, proof surface, audience value, and try-it path.
- Added `kb/` as the maintained Markdown knowledgebase front door.
- Added `kb/index.md` and `kb/log.md`.
- Added KB question and synthesis templates.
- Added `proof/README.md` to separate evidence standards from project ambition.
- Added `scripts/kb_lint.py`.
- Added `make kb-lint`.
