---
name: anti-slop-artifact-packet
description: "Six-workflow orchestration layer for the books-kb control plane: build-first50-queue, prepare-source-packet, batch-plan-card-targets, run-one-artifact-pass, receipt-reconcile, and weekly-operator-review-board. Coordinates existing book-map, source-card, claim/tension, and eval-run skills without replacing their operator gates."
---

# anti-slop-artifact-packet

This skill coordinates the books-kb artifact ladder. It is an orchestration layer, not an authority layer: it plans packets, queues, and receipts, then hands one artifact at a time to the existing specialized workflows.

It exists to remove repeated handoff friction while preserving the review discipline that keeps the substrate public-safe and useful.

## When to invoke

Invoke this skill when the operator asks to plan the next rung, build a first-50 queue, prepare an artifact packet, batch-plan card targets, reconcile receipts/status, or produce a weekly operator review board.

Do not use this skill to bypass `anti-slop-book-map`, `anti-slop-source-card`, `docs/claim-tension-card-workflow.md`, or `anti-slop-eval-run`. Use it to decide what should run next and what evidence is ready for review.

## Workflow selector

| Workflow | Section | Writes public? |
|---|---|---|
| `build-first50-queue` | `## Workflow 1` | No |
| `prepare-source-packet` | `## Workflow 2` | No |
| `batch-plan-card-targets` | `## Workflow 3` | No |
| `run-one-artifact-pass` | `## Workflow 4` | Maybe — only through the invoked workflow |
| `receipt-reconcile` | `## Workflow 5` | Maybe — only operator-approved receipt/status fixes |
| `weekly-operator-review-board` | `## Workflow 6` | No |

## Shared contract

Every workflow inherits these rules. If a workflow would violate one, stop and surface the blocker.

- **Orchestration is not judgment.** This skill may rank work, prepare packets, run checks, and propose the next action. It may not mark artifacts reviewed, resolve tensions, promote canon, or bless eval results without explicit operator approval and the matching specialized workflow.
- **One public artifact pass at a time.** Batch planning is allowed. Batch approval is forbidden. When the next step writes a map, source card, claim/tension card, or eval output, invoke exactly one artifact workflow for exactly one artifact/pass.
- **Respect the artifact ladder.** Metadata/registry decisions precede maps; reviewed maps may guide source-card selection; source cards require local-source grounding; claim/tension cards cite reviewed source cards only; evals operationalize reviewed tensions; canon remains out of scope.
- **Book maps are discovery aids only.** This skill may use reviewed maps to propose targets, but a source-card packet must still require local-source verification before public drafting.
- **Raw source material stays local-only.** Public outputs never include raw source prose, private paths, raw filenames, extracted-source paths, or raw-source format details. Local-only packets may record what needs to be checked, but not publish source prose.
- **Model outputs are receipts only.** Eval outputs are test artifacts. They never become source evidence or canon.
- **No graph edges or canon candidates.** This skill may suggest future relation checks, but it does not create graph edges, canon candidates, or canonical claims.
- **No hidden status lifts.** `operator_review_status`, `tension_status`, `scoring_status`, and Result changes are handled only by the specialized workflow that owns that status and only when the operator has approved the lift or the policy clearly determines it.
- **No `git add` or `git commit` unless the operator explicitly requested it.** Run the closing-gate suite and report results after public edits.

## Packet shape

Use this shape for local-only planning packets. Keep it concise.

```yaml
packet_id: BK-XXXX-purpose-short-name
artifact_type: metadata | book_map | source_card | claim_tension_card | eval_case | eval_run | receipt_repair
source_ids: [BK-XXXX]
stage: target_selected | packet_ready | blocked | ready_for_operator_review
allowed_inputs:
  - public manifests and registries
  - reviewed maps as discovery aids
  - reviewed source cards as evidence for synthesis
  - local source only for grounding checks
forbidden_inputs:
  - book-map prose as source-card evidence
  - unreviewed source cards as synthesis evidence
  - raw source prose in public output
  - model outputs as world evidence
operator_decisions_needed:
  - locator approval
  - source-card approval
  - tension-card approval
  - eval-result status promotion
blockers: []
next_recommended_workflow: skill/workflow name
```

Packet files live under `local-only/phase-2-verification/` or another local-only planning folder. Public files remain the source of truth for reviewed artifacts.

## Workflow 1 — build-first50-queue

**When to use it.** Producing a ranked queue for the first 50 books or a smaller operator-selected slice.

**Inputs.**
- `make artifact-status`
- `corpus/manifests/books-200.yaml`
- `corpus/manifests/acquisition-registry.yaml`
- `corpus/manifests/source-id-registry.yaml`
- `docs/wip-limits.md`
- Existing public artifacts under `corpus/`, `evals/`, and `runs/`

**Outputs (local-only or report-only).**
- A queue summary listing source ID, current level, blockers, next artifact type, and recommended priority.

**Steps.**

1. Run `make artifact-status` and treat its drift summary as the first control-plane input.
2. Bucket each wave-1 source at its highest reached level:
   - L0 registered
   - L1 sourced and locatable
   - L2 reviewed book map
   - L3 at least one reviewed source card
   - L4 participates in a reviewed claim/tension card or eval case
3. Mark blockers separately from backlog:
   - rights/access unresolved
   - edition or locator unverified
   - map missing or unreviewed
   - source-card target missing
   - review WIP cap reached
   - receipt/status drift
4. Rank next work by value and readiness:
   - first: drift and receipt repairs that preserve trust
   - second: map-ready sources that unlock multiple cards
   - third: source-card targets needed by a planned tension/eval
   - fourth: breadth targets for first-50 coverage
5. Output a compact queue. Do not draft artifacts in this workflow.

## Workflow 2 — prepare-source-packet

**When to use it.** Preparing one local-only packet for a source before drafting a map, source card, or higher artifact.

**Inputs.**
- The source's rows in `books-200.yaml`, `acquisition-registry.yaml`, and `source-id-registry.yaml`
- Existing reviewed book map, if any
- Existing source cards and claim/tension references
- Local-only extraction or review notes when needed

**Outputs (local-only).**
- One packet under `local-only/phase-2-verification/<source_id>/artifact-packets/`.

**Steps.**

1. Snapshot the source's public state: metadata verification, locator scheme, processing status, map status, source-card counts, and eval/tension references.
2. Identify the next rung:
   - no verified metadata or locator: route to `anti-slop-book-map` Workflow 1 or 2
   - verified and unmapped: route to `anti-slop-book-map` Workflow 3
   - reviewed map and no target: prepare source-card target candidates
   - reviewed source cards: prepare possible synthesis or eval targets
3. List allowed and forbidden inputs for the next rung.
4. Record operator decisions needed. Be explicit when the operator must approve rights/access, locator granularity, source-card status, tension status, eval Result status, or canon relevance.
5. Name exactly one recommended next workflow. If multiple are possible, rank them but mark only one as recommended.
6. Do not edit public files.

## Workflow 3 — batch-plan-card-targets

**When to use it.** Planning 5-10 candidate source-card targets across reviewed maps without drafting cards.

**Inputs.**
- Reviewed book maps
- Existing source-card inventory
- The first-50 queue from Workflow 1
- WIP limits

**Outputs (local-only or report-only).**
- A target table with source ID, locator, candidate claim, claim type guess, reason, risk, and required local-source check.

**Hard limits.**
- Plan only. Do not create source cards.
- Do not use a book map as evidence.
- Do not put more than 10 targets into one planning batch.
- Do not put more targets into the review queue than the operator can realistically review.

**Steps.**

1. Filter to sources with reviewed book maps and no blocking drift.
2. Prefer targets that unlock a planned claim/tension card, eval case, or first-50 coverage gap.
3. For each candidate, record:
   - source ID and title
   - reviewed map section that suggested the target
   - locator to verify locally
   - single claim boundary
   - likely `claim_type`
   - why this target matters
   - misuse/quote/locator risk
4. Pick a recommended next card target and route it to `anti-slop-source-card` Workflow 5.
5. Stop before drafting.

## Workflow 4 — run-one-artifact-pass

**When to use it.** Running exactly one existing specialized workflow from an approved packet.

**Allowed invocations.**
- `anti-slop-book-map` — one metadata packet, one map draft, one map review, or one operator-approved map status lift.
- `anti-slop-source-card` — one target selection, one approval-ready draft, one review, or one operator-approved status lift.
- `docs/claim-tension-card-workflow.md` — one claim/tension draft, review, repair, or operator-approved status lift.
- `anti-slop-eval-run` — one eval condition, one score, one receipt repair, one summary, or one approval-ready eval pass.

**Steps.**

1. Read the packet and confirm the recommended workflow is still valid against current repo state.
2. Check WIP limits and drift status before starting.
3. Invoke exactly one specialized workflow and follow its rules, including its stronger constraints.
4. If the invoked workflow writes public files, run that workflow's closing-gate suite.
5. Report whether the artifact is:
   - `READY FOR OPERATOR APPROVAL`
   - `SEND BACK`
   - `BLOCKED`
   - `DONE` for non-review actions such as receipt reconciliation
6. Do not chain into the next rung unless the operator explicitly asks.

## Workflow 5 — receipt-reconcile

**When to use it.** Public files disagree about artifact state, registry flags, queue status, score sheets, model-output files, or log receipts.

**Inputs.**
- `make artifact-status`
- Relevant public artifacts and manifests
- `kb/log.md`
- Eval `case.md`, `score-sheet.md`, and `model-outputs/` when reconciling evals

**Modes.**
- `report-only` — default. Identify drift and propose exact fixes.
- `apply-approved-fix` — only when the operator explicitly approves the fix scope.

**Steps.**

1. Run the scanner or manually compare the relevant files.
2. Classify each issue:
   - registry/artifact status drift
   - stale receipt text
   - missing or extra output file listing
   - score-sheet / case Result mismatch
   - queue status mismatch
   - log chronology mismatch
3. In report-only mode, stop with a proposed patch plan. Do not edit.
4. In apply-approved-fix mode, edit only receipt/status descriptions. Do not alter claims, source grounding, scores, model outputs, scenarios, prompts, tension substance, or canon implications.
5. Append one public-safe log bullet if public files changed.
6. Run `make artifact-status` and the closing-gate suite.

## Workflow 6 — weekly-operator-review-board

**When to use it.** Producing a compact review board for a human operator or trusted reviewer.

**Inputs.**
- `make artifact-status`
- Current packets
- Unreviewed artifact inventory
- WIP limits
- Open Linear issues, if the operator asks for project tracking

**Outputs (local-only or report-only).**
- A board grouped by decision type: approve, send back, defer, unblock, and next draft.

**Steps.**

1. List every item awaiting human decision:
   - map approvals
   - source-card approvals
   - claim/tension approvals
   - eval Result/status decisions
   - metadata/locator rights decisions
2. For each item, give the operator only the review-critical facts:
   - artifact path
   - authority level
   - claim or tension boundary
   - locator / lineage
   - gates already run
   - known blocker or risk
   - recommended decision
3. Keep approvals separate. The board may recommend multiple approvals, but this skill does not batch-approve them.
4. End with a ranked next-work list and the likely bottleneck.
5. Do not edit public files.

## Closing-gate suite

After any workflow that writes public files, run:

```sh
make validate
make check-raw
make kb-lint
make report
make phase2-queue
python3 -m py_compile scripts/*.py
git diff --check
make artifact-status
```

Then run the public-artifact private-path/archive-name sweep over `corpus/`, `kb/`, `docs/`, `evals/`, and `runs/`; expect zero matches. Do not include skill or script directories in that sweep unless the task explicitly asks, because validator scripts may contain the forbidden strings as test patterns.

Remove `scripts/__pycache__/` after `py_compile`.

## Final report format

Report:

- Workflow run.
- Packet or artifact path.
- What changed, if anything.
- Gate results.
- Remaining human-gated decisions.
- Explicit no-higher-artifact statement when relevant: no canon candidate, graph edge, unapproved status lift, or batch approval was created.

