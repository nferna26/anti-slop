# Launch Checklist

This checklist keeps the public Anti-Slop Receipts launch surface honest. It
separates machine checks from manual review so the repo can ship receipt-first
docs without widening the product claim.

## Machine checks

- `make launch-check`: README proof links/metrics, product/package naming,
  `docs/privacy-security.md`, `docs/package-install-naming.md`, workflow report
  mode, Step Summary support, demo output, and history placement.
- `make launch-decision-check`: `docs/release-install-plan.md`,
  `docs/demo-repo.md`, `docs/maintainer-outreach-packet.md`,
  `docs/launch-decision.md`, release pin guidance, outreach evidence links, and
  go/no-go completeness.
- `make adoption-smoke`: vendorable report-mode workflow, artifact retention,
  Step Summary tables, fabricated-ref report mode, command receipts, and claims
  JSON.
- `make external-dry-run-smoke`: report-mode-only dry run over committed
  public-safe saved PR bodies plus `anti-slop-external-dry-run.v1`
  schema/policy compatibility checks.
- `make external-dry-run-compat`: compatibility check for committed external
  dry-run policy, target manifest, and aggregate summaries.
- `make external-dry-run-cluster-smoke`: cluster dry-run findings, publish the
  no-change resolver memo, and regenerate kill-criteria status.
- `make external-dry-run-cluster-compat`: compatibility check for committed
  cluster and kill-criteria artifacts.
- `make external-sample-smoke`: report-mode-only expanded sample over saved
  public PR bodies from external AI/devtool repos.
- `make external-sample-compat`: compatibility check for the expanded external
  sample summary, comparison, target manifest, and actionability labels.
- `make actionability-label-check`: validates aggregate actionability labels
  without raw external line text.
- `make command-receipt-dogfood`: regenerates local anti-slop-run receipts in a
  temporary repo and checks a public-safe `AGENT_FINAL_REPORT.md` fixture with
  `anti-slop-claims --receipts`.
- `make agent-claim-demo`: fake report fails with exact line reasons and
  receipt-backed report passes.
- `make agent-claim-benchmark`: regenerates the synthetic corpus summary at
  `benchmarks/agent-claim-corpus-v0.1/results/summary.json`.
- `make agent-claim-audit`: regenerates the public-safe audit summary at
  `proof/agent-claim-audit/summary.json`.
- `make claims-self-test && make run-self-test`.
- `make agent-install-smoke && make package-smoke`.
- `make tag-approval-check && make fresh-install-smoke && make tag-install-smoke`.
- `make pr-provenance-demo && make pr-provenance-event-demo`.
- `make validate && make check-raw && make kb-lint`.
- `python3 -m py_compile scripts/*.py`.
- `python3 scripts/artifact_preflight.py --strict`.
- `git diff --check`.

## Manual checks

- The claim stays narrow: deterministic reference/receipt resolution only.
- report mode remains default; enforcement is explicit opt-in.
- No correctness, relevance, source truth, support, safety, advice quality,
  reasoning, benchmark validity, statistical meaning, or canon claim appears in
  front-door copy.
- No model/API/RAG/vector-store/runtime dependency, telemetry, or GitHub
  API/token requirement is added; no external outreach is performed.
- `anti-slop-receipts-v0.1.0` exists for pinned installs; do not force-move it.
  No GitHub release, outreach, or enforcement change is approved by that tag.
- v0.1.1 Source-Doc Invariant: `anti-slop-receipts-v0.1.1` is the clean tag
  path after PR #46. The source docs must remain truthful when viewed before tag
  creation, after tag creation, and when viewed from the tag itself. Do not
  force-move any tag. The post-tag install proof may live outside the tag commit
  because it can only be generated after the tag exists.
- Future release/tag readiness must follow
  [`docs/release-install-plan.md`](release-install-plan.md); operator approval
  is required before creating a new tag or GitHub release.
- Narrow public preview release body must match
  [`docs/github-release-v0.1.1.md`](github-release-v0.1.1.md); the GitHub
  Release record is the publication receipt and may live outside the tag commit.
- Demo and launch assets must follow [`docs/demo-repo.md`](demo-repo.md).
- Maintainer outreach must follow
  [`docs/maintainer-outreach-packet.md`](maintainer-outreach-packet.md) and
  remain opt-in only.
- The current go/no-go status is recorded in
  [`docs/launch-decision.md`](launch-decision.md).
- No frozen evals, canon, registry decisions, source-card statuses, raw sources,
  local-only artifacts, credentials, answer keys, private paths, raw API JSON,
  raw transcripts, or raw copyrighted text are touched or committed.
- Product/package naming matches `docs/package-install-naming.md`.
- Privacy/security language matches `docs/privacy-security.md`.
- Books-KB, eval-lab, canon, and benchmark history remains preserved below the
  launch front door, not deleted or promoted as the product category.

## Proof Links

- Benchmark summary:
  [`benchmarks/agent-claim-corpus-v0.1/results/summary.json`](../benchmarks/agent-claim-corpus-v0.1/results/summary.json)
- Audit summary:
  [`proof/agent-claim-audit/summary.json`](../proof/agent-claim-audit/summary.json)
- Demo sample output:
  [`proof/agent-claim-demo/sample-output.md`](../proof/agent-claim-demo/sample-output.md)
- Report-mode workflow:
  [`templates/anti-slop-report.yml`](../templates/anti-slop-report.yml)
- Tag install smoke:
  [`proof/tag-install-smoke/summary.json`](../proof/tag-install-smoke/summary.json)

The proof links measure resolver behavior and launch consistency only. They do
not prove semantic correctness, source truth, benchmark validity, statistical
meaning, support, safety, advice quality, reasoning, or canon.
