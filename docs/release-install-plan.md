# Release And Install Plan

Anti-Slop Receipts is the product. anti-slop-lineage remains the Python distribution.
The public command hierarchy stays:

- `anti-slop-claims`: canonical Markdown/text artifact checker.
- `anti-slop-run`: local command and metric receipt producer.
- `anti-slop-pr-event`: GitHub PR-body report-mode preset.
- `anti-slop-pr`: PR-body compatibility wrapper.
- `anti-slop-lineage`: source/card lineage compatibility command.

The historical `anti-slop-receipts-v0.1.0` tag was created with operator
approval and must not be force-moved. The clean public tag path after PR #46 is
`anti-slop-receipts-v0.1.1`. GitHub releases, outreach, or enforcement default
changes require separate operator approval. This plan is deterministic
reference/receipt resolution only. There is no outreach approval in this
release/install plan.
The release posture remains deterministic reference/receipt resolution only.

## v0.1.0 Tag Source Disclosure

Do not force-move `anti-slop-receipts-v0.1.0`. The tag's embedded docs predate
PR #46 finalization: `docs/tag-approval-packet.md` inside the tag says
Decision: `ready_to_request_operator_tag`, candidate
`4bda4fd727018a2a027ba8c660c48c30b8aa2144`, and `No tag has been created`.
The installable package smoke passes, but the tag's embedded docs predate PR
#46 finalization. GitHub release from v0.1.0 requires explicit disclosure.

## v0.1.1 Source-Doc Invariant

`anti-slop-receipts-v0.1.1` is the clean tag path after PR #46. This source
tree is written to remain truthful when viewed before tag creation, after tag
creation, and when viewed from the tag itself. Do not force-move any tag.
The post-tag install proof may live outside the tag commit because it can only be
generated after the tag exists. Absence of post-tag proof inside the tagged
source tree is expected, not stale-doc evidence.

## Pinning Flow

Preview install from repo head:

```sh
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop"
```

Reproducible CI install pinned to a tag or full commit SHA:

```sh
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@anti-slop-receipts-v0.1.0"
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@anti-slop-receipts-v0.1.1"
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@<tag-or-full-sha>"
```

The preview install is acceptable for first report-mode trials. A tag or full
commit SHA is the repeatable supply-chain posture for CI. A short SHA is easier
to read but less reproducible than a full commit SHA; prefer the full SHA in
workflow templates once the adopter chooses a revision.

## release readiness checklist

Before a future tag or GitHub release, the operator should verify:

- PR CI is green on the release candidate commit.
- `make launch-decision-check`, `make launch-check`, `make adoption-smoke`,
  `make agent-claim-demo`, `make agent-claim-benchmark`, `make package-smoke`,
  `make validate`, `make check-raw`, and `make kb-lint` pass.
- `python3 -m py_compile scripts/*.py`, `python3 scripts/artifact_preflight.py
  --strict`, and `git diff --check` pass.
- `docs/privacy-security.md` still says local execution, no telemetry, no
  GitHub API token, no model, stdout/stderr hashes by default, and forbidden
  report/receipt content.
- `templates/anti-slop-report.yml` remains report mode by default, uses
  `permissions: contents: read`, and includes the pinned install placeholder.
- README proof metrics still come from committed JSON/Markdown summaries.
- The launch decision in `docs/launch-decision.md` is reviewed and still
  matches the evidence.
- The tag name, release notes, and install examples have operator approval.
- Existing tag proof remains public-safe:
  `proof/tag-install-smoke/summary.json`.
- v0.1.1 post-tag install proof may live outside the tag commit and should be
  checked from the branch/PR that records proof after tag creation.

## adopter update path

1. Start with report mode and the preview install for a short trial.
2. Pin the install spec to a reviewed tag or full commit SHA once the workflow is
   useful enough to keep.
3. When updating, change only the tag/SHA in `ANTI_SLOP_INSTALL_SPEC`, rerun
   self-tests, and compare report-mode findings before and after.
4. Keep enforcement opt-in. Remove `--report` only after the adopter has boring
   evidence that unresolved references are actionable in that repo.

No correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon claim
is made by a release, tag, install pin, command receipt, metric receipt, or PASS
result.
