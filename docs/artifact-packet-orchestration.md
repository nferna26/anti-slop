# Artifact-Packet Orchestration

The books-kb control plane has two read-only views of first-50 verification work:

- `make first50-queue` — ranks the first-50 source queue from **public** manifests and **public** artifacts only.
- `make packet-status` — a dashboard over the **local-only operator-approval packets** prepared for metadata/locator verification.

This note explains how the two relate and why the boundary between them is deliberate.

## Local-only packets are preparation, not approval

For each sourced first-50 book that still needs bibliographic metadata and a locator scheme, an operator-approval packet is prepared under `local-only/phase-2-verification/<source_id>/operator-approval/`:

- `approval-summary.md`
- `proposed-public-update.yaml`
- `operator-checklist.md`
- `quality-audit.md`

A packet is a **proposal**. It records candidate values for the operator to confirm against the actual local file. Preparing a packet changes nothing public and approves nothing. The `proposed-public-update.yaml` carries the guard `edition_verified: false` with a `set true only after operator approval` comment precisely so a packet can never be mistaken for an applied change.

These packet files are git-ignored. They are never committed.

## `first50-queue` intentionally does not read local-only packets

`first50_queue.py` reads only public manifests and public artifacts. It does **not** read the local-only packets. This is deliberate: the public queue must reflect what is actually true in the committed repo, not what a local-only proposal hopes will become true. A book whose packet is fully prepared but not yet operator-approved is still, in the public view, an unverified book — and the queue says so.

If `first50-queue` read the packets, a prepared-but-unapproved proposal would silently advance a book's apparent level. The packet boundary keeps the public queue honest.

## `packet-status` is the bridge for operator review

`make packet-status` (`scripts/artifact_packet_status.py`) is the read-only bridge. It reads the public manifests **and** the local-only packets, and reports:

- packet inventory — count, four-file shape validity, YAML parse validity, guarded-proposal convention;
- first-50 and first-30 packet coverage;
- packet application state against the public manifests:
  - **PENDING** — public manifest fields still blank; the packet is a live proposal awaiting review;
  - **APPLIED** — the public manifest already carries the packet's values;
  - **STALE** — the public manifest was verified to *different* values; the packet is superseded and must not be applied;
- the operator review queue. Its awaiting-approval lanes (map candidates, first-30 candidates, remaining sourced first-50) carry **only PENDING packets** — APPLIED packets are done and STALE packets are superseded, so neither appears as awaiting approval; both are listed separately, along with the artifact-bearing anchors and the rights/access blockers.

It is a dashboard, not a gate. It always exits 0, reads no raw source files, and is not part of the closing-gate suite.

## Applying a packet is a separate operator-approved action

`packet-status` reports; it does not apply. Moving a packet's proposed values into `corpus/manifests/books-200.yaml` and `corpus/manifests/acquisition-registry.yaml` is the `anti-slop-book-map` **Workflow 2 — apply-verified-metadata** action, and it runs only on explicit operator approval recorded against that source's `operator-checklist.md`.

No artifact authority changes — no metadata applied, no `operator_review_status` lifted, no `edition_verified` flipped — ever happen from `packet-status` or `first50-queue`. Those scripts are inert with respect to public state by design.

## A note on a future orchestration skill

A coordinating skill (`anti-slop-artifact-packet`) that sequences the existing per-artifact skills — `anti-slop-book-map`, `anti-slop-source-card`, `anti-slop-eval-run` — into a single first-50 control-plane loop has been sketched but is deliberately deferred. The dashboards (`artifact-status`, `artifact-preflight`, `first50-queue`, `packet-status`) and the existing per-artifact skills already cover the work; a coordinating skill should be designed once a few more verification batches show which hand-offs are actually friction. Until then, the operator drives the sequence by hand, one operator-approved Workflow 2 application at a time.
