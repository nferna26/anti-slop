# Anti-Slop Receipts

**Make AI coding agents cite receipts, not vibes.**

Anti-Slop Receipts is deterministic **reference and receipt resolution** for AI
agent reports. It checks whether cited files, tests, issues, commits, command
receipts, and simple metric receipts resolve against the local repo state.

It is intentionally narrow. A PASS means the cited references/receipts resolved.
It does **not** prove correctness, relevance, source truth, support, safety,
advice quality, reasoning, benchmark validity, statistical meaning, or canon.

## Problem

AI coding agents often write confident reports that cite files, tests, commands,
metrics, issues, or commits that do not exist. Reviewers then have to separate
"the agent said it" from "the repo has a receipt for it."

Anti-Slop makes those claims inspectable before merge:

- `anti-slop-run` writes local command/metric receipts.
- `anti-slop-claims` is the canonical checker for `AGENT_FINAL_REPORT.md` and
  other Markdown/text artifacts.
- `anti-slop-pr-event` is the GitHub Actions PR-body preset for report-mode
  adoption.

Everything is stdlib-only at runtime: no model, hosted API, RAG layer, vector
store, telemetry, GitHub API, or token requirement.

## Install

Preview install from the public repo:

```sh
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop"
anti-slop-claims --self-test
anti-slop-run --self-test
anti-slop-pr-event --self-test
```

For reproducible CI, pin the git dependency to a release tag or full commit SHA:

```sh
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@<tag-or-full-sha>"
```

The unpinned preview install is easier for first adoption but tracks repo head.
Pinning is the safer supply-chain posture once a repo depends on the check.

Product/package naming is intentionally conservative: Anti-Slop Receipts is the
product, the current Python distribution remains `anti-slop-lineage`, and the
primary commands remain `anti-slop-claims`, `anti-slop-run`,
`anti-slop-pr-event`, and `anti-slop-pr`. See
[`docs/package-install-naming.md`](docs/package-install-naming.md).

## 60-Second Demo

```sh
make agent-claim-demo
```

The demo checks two committed sample reports against a temporary local fixture:
a fake report FAILS with exact line reasons, and a receipt-backed report PASSES.
Sample output is committed at
[`proof/agent-claim-demo/sample-output.md`](proof/agent-claim-demo/sample-output.md).

## GitHub Action

Copy the vendorable report-mode workflow:

```sh
cp templates/anti-slop-report.yml .github/workflows/anti-slop-report.yml
```

By default it runs:

```sh
anti-slop-pr-event --root . --report
```

Report mode prints findings and exits 0. Enforcement is explicit opt-in by
removing `--report` after a repo has enough boring report-mode data.

The workflow can also retain useful CI artifacts:

```yaml
ANTI_SLOP_RUN_VALIDATE: "true"
ANTI_SLOP_CHECK_AGENT_REPORT: "true"
```

Those options run `anti-slop-run -- make validate`, check
`AGENT_FINAL_REPORT.md` with `anti-slop-claims --receipts .anti-slop/receipts
--json .anti-slop/claims.json --report`, append compact Markdown tables to
`$GITHUB_STEP_SUMMARY`, and upload `.anti-slop/receipts/*.json` plus
`.anti-slop/claims.json`. These artifacts are local command/reference facts, not
proof of correctness.

## Supported Claim Types

- File refs: path-like refs such as `docs/foo.md` or `scripts/tool.py:L42`.
- Changed-file claims: "updated `docs/foo.md`" checked against `--diff` when
  supplied; advisory/skipped without a diff.
- Test refs: `tests/test_api.py::test_limits`.
- Issue refs: advisory by default; hard only with a supplied numbers registry.
- Commit refs: advisory local-git resolution.
- Command claims: "`make validate` passed", "pytest passed", "tests pass", or
  ``command `make validate` exited 0``, backed by fresh `anti-slop-run` receipts.
- Metric claims: "score is 0.82" or "score improved from 0.70 to 0.82", backed
  by fresh receipt metrics.

See [`docs/agent-claim-verification.md`](docs/agent-claim-verification.md) for
the full matrix.

## Non-Goals

Anti-Slop Receipts is not:

- a model, hosted service, agent runtime, telemetry layer, RAG layer, or vector
  store;
- a correctness checker;
- a relevance, support, safety, advice-quality, reasoning, benchmark-validity,
  statistical-meaning, source-truth, or canon judge;
- a public archive of copyrighted source text.

## Privacy And Security

Receipts are local JSON artifacts. By default, `anti-slop-run` stores hashes and
byte counts for stdout/stderr, not raw output. Bounded excerpts are explicit
opt-in; do not enable excerpts for commands that may print secrets,
credentials, `.env` values, private paths, raw API JSON, answer keys, raw
transcripts, or raw copyrighted text.

The GitHub workflow uses `permissions: contents: read`. Anti-Slop commands read
event JSON and local checkout files; they do not require a GitHub API token.
See [`docs/privacy-security.md`](docs/privacy-security.md) for the full
privacy/security launch boundary and forbidden report/receipt content.

## Agent Report Contract

Use [`docs/agent-report-contract.md`](docs/agent-report-contract.md) for a
copyable `AGENT_FINAL_REPORT.md` structure and receipt examples for `pytest`,
`npm`, `pnpm`, `cargo`, `go`, and `make`.

Minimal local flow:

```sh
anti-slop-run -- make validate
anti-slop-claims --root . --receipts .anti-slop/receipts --json .anti-slop/claims.json --report AGENT_FINAL_REPORT.md
```

## Proof Metrics

README proof numbers are smoke-checked against committed summaries:

- [`benchmarks/agent-claim-corpus-v0.1/results/summary.json`](benchmarks/agent-claim-corpus-v0.1/results/summary.json):
  55-case synthetic checker corpus including 5 cluster-derived regression cases;
  100.0% catch rate over enforceable false cases; 0.0% false-fail rate over
  expected-valid cases.
- [`proof/agent-claim-audit/summary.json`](proof/agent-claim-audit/summary.json):
  25 real PR bodies; 25.55 checkable claims per 100 lines; 9.5% hard unresolved rate;
  30-day falsifier trend: PASS.

These numbers measure resolver behavior and report-mode calibration only. They
do not prove semantic correctness, source truth, benchmark validity,
statistical meaning, support, safety, advice quality, reasoning, or canon.

## Docs

- [`INSTALL_FOR_AGENTS.md`](INSTALL_FOR_AGENTS.md): copy-paste install protocol.
- [`llms.txt`](llms.txt): compact agent entrypoint.
- [`templates/anti-slop-report.yml`](templates/anti-slop-report.yml): report-mode
  GitHub Actions workflow with optional receipt artifacts.
- [`docs/package-install-naming.md`](docs/package-install-naming.md):
  product/package naming posture and pinned install guidance.
- [`docs/privacy-security.md`](docs/privacy-security.md): local execution,
  receipt contents, artifact upload risk, and forbidden content.
- [`docs/launch-checklist.md`](docs/launch-checklist.md): machine and manual
  launch checks.
- [`docs/command-receipts.md`](docs/command-receipts.md): command/metric receipt
  schema.
- [`docs/pr-provenance.md`](docs/pr-provenance.md): PR-body preset details.
- [`docs/adoption-loop.md`](docs/adoption-loop.md): external adoption playbook.
- [`docs/external-dry-run-policy.md`](docs/external-dry-run-policy.md):
  report-mode-only external dry-run policy and aggregate schema.
- [`proof/external-dry-run/summary.md`](proof/external-dry-run/summary.md):
  first saved-public-PR-body dry-run aggregate (`dry_run_not_adoption`).
- [`proof/external-dry-run/clusters.md`](proof/external-dry-run/clusters.md):
  public-safe cluster memo and no-change resolver decision.
- [`docs/kill-criteria.md`](docs/kill-criteria.md): kill-criteria dashboard
  for usefulness signals and unknowns.
- [`docs/history/books-kb-eval-lab.md`](docs/history/books-kb-eval-lab.md):
  preserved books-KB, eval-lab, canon, and historical evidence context.

## Repo Map

- `scripts/`: local CLIs and validation helpers.
- `templates/`: vendorable workflow and PR-body examples.
- `proof/`: demo and audit summaries.
- `benchmarks/`: synthetic checker corpus.
- `docs/`: user docs, contract docs, and preserved history.
- `kb/`, `corpus/`, `canon/`, `evals/`, `registry/`, `runs/`: historical
  books-KB/eval-lab artifacts retained as public evidence, not the product
  front door.
