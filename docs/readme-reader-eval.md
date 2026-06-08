# README Reader Eval

Date: 2026-05-19; launch-hardening note added 2026-06-08

## Eval Question

Fast forward one year. If different readers land on the README, do they know
what Anti-Slop Receipts is, why it matters, how to install report mode, how to
read receipt artifacts, and what the tool explicitly does not prove?

Historical note: the original May 2026 reader eval targeted the older
books-KB/eval-lab front door. That history is now preserved under
[`history/books-kb-eval-lab.md`](history/books-kb-eval-lab.md); the public
README is the launch front door for deterministic agent report reference/receipt
resolution.

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

- Lead with the agent-report receipt problem.
- Make `anti-slop-claims` the canonical checker, `anti-slop-run` the receipt
  producer, and `anti-slop-pr-event` the GitHub PR-body preset.
- Add an obvious install path, 60-second demo, and report-mode workflow.
- Keep non-goals and privacy/security constraints above the fold.
- Tie README proof numbers to committed summary JSON.
- Preserve the books-KB/eval-lab history without making it the product category.

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

- Rewrote the README around the receipt-first product surface: problem,
  install, demo, GitHub Action, supported claim types, non-goals,
  privacy/security, and smoke-checked proof metrics.
- Added `docs/agent-report-contract.md` for copyable `AGENT_FINAL_REPORT.md`
  structure and command receipt examples.
- Moved books-KB/eval-lab/canon history to `docs/history/books-kb-eval-lab.md`.
- Updated `make kb-lint` to enforce the new receipt-first launch sections.
