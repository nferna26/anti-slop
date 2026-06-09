# Anti-Slop Receipts v0.1.1 — deterministic receipt checks for AI coding-agent reports

GitHub Release title:
`Anti-Slop Receipts v0.1.1 — deterministic receipt checks for AI coding-agent reports`

This is a narrow public preview release for Anti-Slop Receipts.

Anti-Slop Receipts checks whether AI coding-agent reports cite references and
receipts that resolve: files, tests, commits, changed-file claims, command
receipts, and simple metric receipts. It is report mode by default.

Install from the pinned tag:

```sh
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@anti-slop-receipts-v0.1.1"
anti-slop-claims --self-test
anti-slop-run --self-test
anti-slop-pr-event --self-test
```

Run a command and write a local receipt:

```sh
anti-slop-run -- make validate
```

Check an agent final report in report mode:

```sh
anti-slop-claims \
  --receipts .anti-slop/receipts \
  --json .anti-slop/claims.json \
  --report \
  AGENT_FINAL_REPORT.md
```

Use the report-mode GitHub Actions template:

```sh
cp templates/anti-slop-report.yml .github/workflows/anti-slop-report.yml
```

Boundary:

- A PASS means referenced files/receipts resolved under the configured local
  checks.
- This does not prove correctness, relevance, source truth, support, safety,
  advice quality, reasoning, benchmark validity, statistical meaning, or canon.
- This is not a code review, security review, test-quality review, semantic diff
  review, or advice-quality review.
- Report mode remains default; enforcement is explicit opt-in.
- No outreach, external PR/comment/issue, maintainer contact, HN/X launch blast,
  enforcement workflow, telemetry, model/API runtime, GitHub API, or token is
  included in this release.

This release does not prove correctness, relevance, source truth, support,
safety, advice quality, reasoning, benchmark validity, statistical meaning, or
canon. It is not a code review, security review, test-quality review, semantic
diff review, or advice-quality review.

Boundary summary: does not prove correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon; not a code review, security review, test-quality review, semantic diff review, or advice-quality review.

Source/tag note:

- The install source is the existing annotated tag
  `anti-slop-receipts-v0.1.1`, which peels to
  `4bb51ced8035d0984515002197306dfc737e1f09`.
- The GitHub Release record is the publication receipt for this preview. The tag
  source docs were authored before a GitHub Release record could exist, so
  release-created status lives in the GitHub Release record and current default
  branch docs, not inside the tag commit.
The tag source docs were authored before a GitHub Release record could exist.
- Do not force-move `anti-slop-receipts-v0.1.0` or
  `anti-slop-receipts-v0.1.1`.
- The historical `anti-slop-receipts-v0.1.0` tag installs, but its embedded docs
  predate PR #46 finalization; a release from v0.1.0 would require explicit
  disclosure.

Suggested repository metadata:

- Description: `Deterministic receipt checks for AI coding-agent reports. Report mode by default; no model/API/token.`
- Topics: `ai-agents`, `developer-tools`, `github-actions`, `ci`,
  `receipts`, `provenance`, `python`, `anti-slop`.

Next step after this release: run 2-3 friendly external installs in report mode.
Do not do broad outreach yet.
