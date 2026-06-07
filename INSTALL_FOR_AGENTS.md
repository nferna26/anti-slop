# Install Anti-Slop agent claim verification (`anti-slop-pr` surface)

Make AI coding agents cite receipts, not vibes.

A protocol a coding agent (or a person) can follow to add Anti-Slop's first
agent-claim-verification surface, **`anti-slop-pr`**, to any repository: install
it, wire a report-mode GitHub PR check, run a smoke, and open a PR.

**What `anti-slop-pr` does (narrow):** it is a deterministic **reference
and receipt resolver** for claims in AI-written PR descriptions. PR bodies are
surface #1, not the category. It checks whether the **file, test, source-card,
issue, and commit** references a PR body cites actually **resolve** against the
repo. It does **not** prove the change is correct, relevant, supported, safe, or
true, and says nothing about source truth, advice quality, reasoning, or canon.
It is a checker, not a judge. No model, no network, no GitHub API, no token.

The package also exposes **`anti-slop-claims`**, the generic Markdown/text
artifact entrypoint. `anti-slop-pr` remains the PR-body surface and compatibility
wrapper; `anti-slop-claims` is for non-PR artifacts such as
`AGENT_FINAL_REPORT.md`.

> **Copy/paste user prompt:** "Install anti-slop-pr in this repo, run the smoke,
> add report-mode CI, and open a PR."

## Prerequisites

- Python **3.9+** (`python3 --version`).
- `git` (optional — only used to resolve commit-SHA refs locally; absent → commit
  refs degrade to advisory).
- That's all. The checker has **no runtime dependencies** (stdlib only).

## 1. Install

Pick one. Both give you the `anti-slop-pr` and `anti-slop-pr-event` commands.
They also install `anti-slop-claims`.

```sh
# Option A — pip install from the repo (preview; pin to a tag/commit for repro):
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop"

# Option B — vendor the four stdlib files (no install), then run with python3:
#   scripts/gate_citation_lineage.py   (the resolver, reused unchanged)
#   scripts/gate_pr_provenance.py      (anti-slop-pr)
#   scripts/gate_claims.py             (anti-slop-claims)
#   scripts/pr_provenance_from_github_event.py  (anti-slop-pr-event)
# Run as: python3 path/to/gate_pr_provenance.py --root . <pr-body.md>
# Or:     python3 path/to/gate_claims.py --root . <artifact.md>
```

## 2. Self-test (proves the install, offline)

```sh
anti-slop-pr --self-test          # 22 checks
anti-slop-pr-event --self-test    # 8 checks
anti-slop-claims --self-test      # JSON + diff-aware generic artifact fixtures
```

From a checkout of this repo, the full end-to-end smoke (throwaway venv + temp
adopter repo; install → self-tests → clean PASS / fabricated FAIL; offline, no
GitHub API) is: `make agent-install-smoke`.

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
```

This is the same resolver engine used by `anti-slop-pr`. JSON receipts and
diff-aware changed-file checks do not prove semantic correctness, relevance, or
support. Command-receipt and benchmark-receipt validation are not implemented.

## 4. Add the GitHub PR check (report mode by default)

Copy `templates/anti-slop-pr.yml` to `.github/workflows/anti-slop-pr.yml`. It
runs on `pull_request`, reads the PR body from the event payload (no token), and
runs the agent claim verification surface in **report mode** (advisory — never
fails the check):

```yaml
permissions: { contents: read }     # no write/token scope
# ...
- run: anti-slop-pr-event --root . --report
```

`anti-slop-pr-event` SKIPs non-PR events (exit 0), so the step is harmless on
push / schedule / comment triggers.

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
  resolves a real PR body, `.github/workflows/anti-slop-pr.yml` exists in report
  mode, and a PR is opened with that change.
- **Stop and report** if: Python < 3.9, the install cannot run offline and no
  network is available, or the repo forbids adding workflows — record the blocker
  rather than weakening the checker or adding a token/API.

## What this is not

It resolves references and receipts; it does not verify correctness, relevance,
support, safety, source truth, advice quality, reasoning, or canon. See
[`docs/agent-claim-verification.md`](docs/agent-claim-verification.md) and
[`docs/pr-provenance.md`](docs/pr-provenance.md).
