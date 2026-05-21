# WIP Limits

books-kb caps work-in-progress at each layer of the artifact ladder. Caps exist to keep the substrate finishable: an unbounded queue of draft cards or unreviewed maps is not a maintained KB, it is a backlog.

A cap is a ceiling, not a target. The healthy state is well under the cap.

## The caps

| State | Cap |
|---|---|
| Newly acquired but unregistered in the acquisition registry | **0** |
| Acquired but unmapped (no book map yet) | **20** |
| Machine-generated maps awaiting operator review | **5** |
| Draft source cards awaiting review | **20** |
| Draft claim / tension cards awaiting review | **10** |
| Canon candidates awaiting decision (accept / reject / defer) | **3** |

## What the caps mean

### Newly acquired but unregistered: 0

A source moves from "not_started" to "sourced" or "acquired" only after its acquisition registry entry is updated. The cap is hard: acquiring a source without registering it skips the rights/access discipline the registry is for.

### Acquired but unmapped: 20

Once 20 acquired sources are sitting without a book map, no more sources get pulled off the manifest until the queue drains. Acquiring faster than mapping converts the project into a shelf, not a KB.

### Machine maps awaiting operator review: 5

If five machine-drafted book maps are sitting without operator review, the bottleneck is review, not generation. Stop generating more until five become operator-reviewed (which often means edited or rejected outright).

### Draft source cards awaiting review: 20

Source cards are evidence units. An unreviewed source card is not yet evidence. A backlog of 20 unreviewed cards is a signal to drain before drafting more. The reviewer is usually the source owner; the GM may rotate the review role.

### Draft claim/tension cards awaiting review: 10

Synthesis cards build on multiple source cards. A backlog at the synthesis layer compounds: every unreviewed claim card might depend on (or contradict) other unreviewed claim cards. Cap is lower than for source cards because the dependency graph is denser.

### Canon candidates awaiting decision: 3

Canon promotion is the rarest, slowest move. Three candidates pending is plenty — a fourth candidate sitting in queue is a sign the canon owner should focus on deciding, not on additional drafting.

## What happens when a cap is breached

- **Stop creating new artifacts at that layer.** Do not work around the cap by drafting in another directory.
- **Drain.** Either review and accept, review and reject, or explicitly defer (with rationale in `registry/`).
- **If draining is hard, the cap is doing its job.** It is surfacing a real bottleneck. Investigate the bottleneck instead of raising the cap.

## How caps are tracked

In the early scaffold, caps are tracked by inspection: `ls corpus/source-cards/` shows the draft count; `manifest_report.py` reports relevant counts where computable.

The inventory script now exists: `scripts/artifact_status.py` (run `make artifact-status`) is a read-only scanner that derives current artifact state from files on disk and reports the awaiting-review counts at each layer, per-source artifact state, a first-50 level summary, and drift between on-disk artifacts and the acquisition registry. It is a dashboard, not a gate — it changes nothing and is not part of the closing-gate suite.

The caps are not enforced by automation today. They are operator discipline. Per `AGENTS.md`, gates exist to catch failures the discipline missed; the caps are part of the discipline that does not need a gate to be real.

## Caps interact with operator roles

- The **source owner** is responsible for not breaching the acquired-but-unmapped cap on their sources.
- The **GM** is responsible for the aggregate.
- The **canon owner** is responsible for the canon-candidate cap.
- The **editor** is not capped — copy work runs independent of substrate caps.

## Caps and AI-generated drafts

Machine drafts count toward the same caps. A book map drafted by an LLM and not yet operator-reviewed sits under "machine maps awaiting operator review." A model-generated source-card stub counts as a draft source card.

The point of the caps is that operator review is the limiting resource. Machine generation does not change the bottleneck; it only changes whether the operator's time goes to drafting or to reviewing. The caps respect that the bottleneck is real.
