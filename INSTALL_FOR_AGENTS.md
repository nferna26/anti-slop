# Install Anti-Slop Receipts

Make AI coding agents cite receipts, not vibes.

This is a protocol a coding agent or person can follow to add deterministic
reference/receipt resolution to a repository, wire a report-mode GitHub PR
check, run a smoke, and open a PR.

**Canonical checker:** `anti-slop-claims` checks Markdown/text artifacts such as
`AGENT_FINAL_REPORT.md`.

**Receipt producer:** `anti-slop-run` writes local command/metric receipts under
`.anti-slop/receipts/`.

**GitHub preset:** `anti-slop-pr-event` checks PR bodies from the Actions event
payload. `anti-slop-pr` remains the PR-body compatibility wrapper.

**Naming posture:** Anti-Slop Receipts is the product name. The current Python
distribution remains `anti-slop-lineage`; do not rename adopter workflows into a
broad slop detector. See
[`docs/package-install-naming.md`](docs/package-install-naming.md).

Anti-Slop checks whether cited **file, test, source-card, issue, commit,
command, and metric** references resolve against repo state and local receipts.
It does **not** prove the change is correct, relevant, supported, safe, or true,
and says nothing about source truth, advice quality, reasoning, benchmark
validity, statistical meaning, or canon. It is a checker, not a judge. No model,
no network runtime, no GitHub API, no token.

> **Copy/paste user prompt:** "Install report-mode Anti-Slop in this repo, copy
> the turnkey workflow, run the smoke, and open a PR."

## Prerequisites

- Python **3.9+** (`python3 --version`).
- `git` (optional — only used to resolve commit-SHA refs locally; absent → commit
  refs degrade to advisory).
- That's all. The checker has **no runtime dependencies** (stdlib only).

## 1. Install

Pick one. Both give you `anti-slop-claims`, `anti-slop-run`, `anti-slop-pr`,
and `anti-slop-pr-event`.

```sh
# Option A — pinned install from the v0.1.0 tag:
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@anti-slop-receipts-v0.1.0"

# Option A1 — preview install from repo head:
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop"

# Option A2 — reproducible install pinned to a release tag or full commit SHA:
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@<tag-or-full-sha>"

# Option B — vendor the five stdlib files (no install), then run with python3:
#   scripts/gate_citation_lineage.py   (the resolver, reused unchanged)
#   scripts/gate_pr_provenance.py      (anti-slop-pr)
#   scripts/gate_claims.py             (anti-slop-claims)
#   scripts/anti_slop_run.py           (anti-slop-run)
#   scripts/pr_provenance_from_github_event.py  (anti-slop-pr-event)
# Run as: python3 path/to/gate_pr_provenance.py --root . <pr-body.md>
# Or:     python3 path/to/gate_claims.py --root . <artifact.md>
```

The unpinned preview install is useful for first trials but tracks repo head.
Pinned tags/SHAs are the safer supply-chain posture for repeatable CI. The
`anti-slop-receipts-v0.1.0` tag exists for reproducible installs; no GitHub
release, outreach, external PR/comment, maintainer contact, enforcement
workflow, or default enforcement change is approved by that tag.
There is no outreach approval in this install path.
See [`docs/release-install-plan.md`](docs/release-install-plan.md) for the
release readiness checklist, exact tag/SHA pin flow, and adopter update path.
For the current operator tag gate, see
[`docs/tag-approval-packet.md`](docs/tag-approval-packet.md),
[`docs/operator-tag-decision.md`](docs/operator-tag-decision.md), and
[`proof/fresh-install-smoke/summary.md`](proof/fresh-install-smoke/summary.md),
plus the pushed-tag smoke at
[`proof/tag-install-smoke/summary.md`](proof/tag-install-smoke/summary.md).
That gate is deterministic reference/receipt resolution only; future release,
outreach, or enforcement action still requires operator approval.

## 2. Self-test (checks the install, offline)

```sh
anti-slop-pr --self-test          # 22 checks
anti-slop-pr-event --self-test    # 9 checks incl. GitHub Step Summary
anti-slop-claims --self-test      # JSON + diff-aware generic artifact fixtures
anti-slop-run --self-test         # command receipts, nonzero receipts, metrics
```

From a checkout of this repo, the full end-to-end smoke (throwaway venv + temp
adopter repo; install → self-tests → clean PASS / fabricated FAIL; offline, no
GitHub API) is: `make agent-install-smoke`.

From a checkout of this repo, the Week 4 proof/demo commands are also offline:

```sh
make agent-claim-demo       # fake report FAILS; receipt-backed report PASSES
make agent-claim-benchmark  # 50 synthetic checker cases
make agent-claim-audit      # report-mode audit over committed real PR bodies
make adoption-smoke         # workflow-template + artifact-retention smoke
make launch-check           # launch-facing docs/proof/naming/privacy check
make launch-decision-check  # release plan, demo assets, outreach packet, decision memo
```

## 3. Check a PR body locally

```sh
# Write the PR description to a file, then resolve its cited claims against the repo:
anti-slop-pr --root . my-pr-body.md
#   exit 0 = every hard reference resolves (PASS)
#   exit 1 = a cited file / test / source-card (or registry issue) does not resolve
#   add --report to print findings but always exit 0 (advisory)
```

A minimal example body to adapt: `templates/example-pr-body.md`.

## 3b. Check a generic artifact locally

```sh
# Resolve references cited by a non-PR Markdown/text artifact:
anti-slop-claims --root . AGENT_FINAL_REPORT.md
#   add --report for advisory adoption, same as anti-slop-pr

# Write a machine-readable receipt:
anti-slop-claims --root . --json claims.json AGENT_FINAL_REPORT.md

# Hard-check changed-file wording against a local git diff/range:
anti-slop-claims --root . --diff HEAD~1..HEAD AGENT_FINAL_REPORT.md

# Write local command receipts before claiming commands passed:
anti-slop-run -- make validate
anti-slop-claims --root . --receipts .anti-slop/receipts AGENT_FINAL_REPORT.md

# Record simple metric values on command receipts:
anti-slop-run --metric score=0.82 -- python3 scripts/report_score.py
anti-slop-run --metric score.before=0.70 --metric score.after=0.82 -- python3 scripts/report_score.py
```

This is the same resolver engine used by `anti-slop-pr`. JSON receipts and
diff-aware changed-file checks do not prove semantic correctness, relevance, or
support. Command and metric receipts record only local command/metric facts, not
semantic correctness, benchmark validity, or support.

## 4. Add the GitHub PR check (report mode by default)

Copy `templates/anti-slop-report.yml` to
`.github/workflows/anti-slop-report.yml`. It runs on `pull_request`, reads the
PR body from the event payload, and runs the agent claim verification surface in
**report mode** (advisory — never fails the check):

```yaml
permissions: { contents: read }     # no write/token scope
# ...
- run: anti-slop-pr-event --root . --report
```

`anti-slop-pr-event` SKIPs non-PR events (exit 0), so the step is harmless on
push / schedule / comment triggers.

The template also includes opt-in receipt steps:

```yaml
env:
  ANTI_SLOP_RUN_VALIDATE: "true"
  ANTI_SLOP_CHECK_AGENT_REPORT: "true"
```

When enabled, the workflow runs `anti-slop-run -- make validate`, then checks
`AGENT_FINAL_REPORT.md` with `anti-slop-claims --receipts .anti-slop/receipts
--json .anti-slop/claims.json --report`. `anti-slop-pr-event` and
`anti-slop-claims` append compact Markdown tables to `$GITHUB_STEP_SUMMARY` when
GitHub provides it. The final upload step retains `.anti-slop/receipts/*.json`
and `.anti-slop/claims.json` as CI artifacts. Those JSON files are local
command/reference receipts only; they do not prove correctness, relevance,
support, benchmark validity, safety, source truth, advice quality, reasoning, or
canon.

For generic final reports, use the copyable contract in
[`docs/agent-report-contract.md`](docs/agent-report-contract.md).
For data handling, artifact upload risk, and forbidden report/receipt content,
see [`docs/privacy-security.md`](docs/privacy-security.md). For the machine and
manual launch gate, see [`docs/launch-checklist.md`](docs/launch-checklist.md).
For demo assets, see [`docs/demo-repo.md`](docs/demo-repo.md). For future
opt-in outreach copy, see
[`docs/maintainer-outreach-packet.md`](docs/maintainer-outreach-packet.md). For
the current go/no-go status, see [`docs/launch-decision.md`](docs/launch-decision.md).
For the tag approval packet and install proof, see
[`docs/tag-approval-packet.md`](docs/tag-approval-packet.md),
[`docs/operator-tag-decision.md`](docs/operator-tag-decision.md), and
[`proof/fresh-install-smoke/summary.md`](proof/fresh-install-smoke/summary.md),
[`proof/tag-install-smoke/summary.md`](proof/tag-install-smoke/summary.md).

For a minimal PR-body-only workflow without artifact upload, the older
`templates/anti-slop-pr.yml` remains available.

## 5. Optional: resolve issue refs (`#123`)

Offline there is no way to know an issue's state without a credential, and this
tool adds none — so `#123` refs are **advisory** unless you supply a registry of
valid issue numbers. Generate one however you like (it is just numbers), e.g.
`gh issue list --state all --limit 1000 --json number -q '.[].number' > .known-issues.txt`,
then pass `--issue-registry .known-issues.txt`. Example: `templates/known-issues.example.txt`.

## 6. Enforcement (opt-in, only when ready)

Once a repo is comfortable, **drop `--report`** to make the check fail on an
unresolved reference:

```yaml
- run: anti-slop-pr-event --root . --issue-registry .known-issues.txt
```

For PRs that cite fabricated example references on purpose (e.g. a PR that
documents this tool), wrap those lines with explicit, auditable ignore
directives instead of weakening the check:

```md
<!-- anti-slop-pr: ignore-next-line -->
This line's example refs are not checked.

<!-- anti-slop-pr: ignore-start -->
A block of example references.
<!-- anti-slop-pr: ignore-end -->
```

## Troubleshooting

- **Everything flags in a docs PR** → it cites example refs; wrap them in ignore
  directives (step 6) or run `--report`.
- **`#123` always advisory** → supply `--issue-registry` (step 5).
- **A commit SHA shows advisory** → commit refs are advisory by design (a hex
  token is ambiguous); ensure you run inside a git checkout if you want them
  resolved.
- **Bare filenames not flagged** → file refs must be path-like (contain `/`); a
  bare basename is treated as a name, not a path.

## Stop conditions (done / when to stop)

- **Done** when: the self-tests pass, a local `anti-slop-pr --root . <body>`
  resolves a real PR body,
  `.github/workflows/anti-slop-report.yml` exists in report mode, receipt upload
  behavior is understood, and a PR is opened with that change.
- **Stop and report** if: Python < 3.9, the install cannot run offline and no
  network is available, or the repo forbids adding workflows — record the blocker
  rather than weakening the checker or adding a token/API.

## What this is not

It resolves references and receipts; it does not verify correctness, relevance,
support, safety, source truth, advice quality, reasoning, or canon. See
[`docs/agent-claim-verification.md`](docs/agent-claim-verification.md) and
[`docs/pr-provenance.md`](docs/pr-provenance.md). Privacy/security rules are in
[`docs/privacy-security.md`](docs/privacy-security.md); naming/install posture
is in [`docs/package-install-naming.md`](docs/package-install-naming.md).
