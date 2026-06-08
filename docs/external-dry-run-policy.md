# External Dry-Run Policy

Policy version: `external-dry-run-policy.v1`.

This policy defines report-mode-only external dry runs for Anti-Slop Receipts.
The goal is to learn whether saved public agent/PR artifacts contain enough
checkable references to justify later opt-in adoption work. A dry run is not
adoption, outreach, enforcement, or a correctness review.

## Allowed Inputs

Allowed inputs are:

- committed saved public PR-body artifacts;
- committed saved public agent-report artifacts;
- local checkout artifact files supplied by an operator;
- public metadata such as source path, target repo/PR URL, artifact kind, and
  checker command.

For the expanded external sample, target-selection rules are:

- use at least 10 distinct public AI/devtool repositories outside
  `nferna26/anti-slop`;
- use saved public PR bodies or agent reports that were manually reviewed for
  public-safe storage before commit;
- prefer artifacts with checkable file/test/command/issue/change claims over
  empty release notes;
- record public origin URLs and mark each target `reviewed_public_safe`;
- keep the no-contact/no-outreach boundary: saving public artifacts for local
  aggregate analysis does not authorize maintainer contact, comments, PRs, or
  adoption.

The harness must not fetch live PR bodies at runtime. It must not require a
GitHub API token, a hosted model, a network call, a private repo, or a workflow
secret. Public PR-body handling is limited to artifacts already committed under
the repo's public-safe rules.

## Committed Outputs

Committed outputs may include:

- aggregate JSON summaries using `anti-slop-external-dry-run.v1`;
- aggregate Markdown summaries;
- target manifests that identify public artifact files and public origin URLs.

Committed outputs must not include raw API JSON, raw transcripts, command
stdout/stderr dumps, hidden maps, answer keys, secrets, credentials, `.env`
values, private paths, raw copyrighted text, or private repo data.

## Redaction And Aggregation

The dry-run harness records aggregate counts and compact per-artifact metrics:
line counts, claim counts, hard unresolved counts, advisory counts, checker
surface, public source path, and public origin URL. Redaction is mandatory for
anything outside those fields. Do not commit line-level findings or full
resolver receipts from external targets unless a later policy explicitly allows
that public-safe artifact.

Reasons are normalized into clusters such as unresolved file refs or advisory
issue refs. This avoids storing long excerpts while still preserving the
actionable signal for false-positive clustering.

The expanded external sample may use an empty public fixture root when external
checkouts are not committed. In that mode, root-dependent hard failures are
useful for claim-density and cluster-shape learning, but they are not
maintainer-actionable until rechecked against a real local checkout.

## Runtime Constraints

The dry-run harness is report mode only:

- no token;
- no model;
- no GitHub API;
- no network runtime;
- no automated adoption;
- no external PRs, comments, issues, or outreach;
- no enforcement mode.

The harness may run existing local commands such as `anti-slop-pr-event
--report` or `anti-slop-claims --report` against committed local artifacts. It
must not fork resolver logic or claim anything beyond deterministic
reference/receipt resolution.

## Outreach Boundary

Any later outreach must be opt-in outreach: a separate human-approved tranche
with target-specific review, contribution-guideline checks, maintainer-friendly
copy, report mode by default, and a clear removal path. This policy does not
authorize outreach.

## Aggregate Schema

`anti-slop-external-dry-run.v1` required fields:

| Field | Meaning |
| --- | --- |
| `schema_version` | Must be `anti-slop-external-dry-run.v1`. |
| `target` | Human-readable target set summary. |
| `artifact_count` | Number of saved public artifacts checked. |
| `checkable_claims_per_100_lines` | Aggregate detected refs/receipts per 100 artifact lines. |
| `hard_unresolved_rate` | Hard unresolved refs divided by hard refs. |
| `advisory_rate` | Advisory refs divided by total detected refs/receipts. |
| `top_reasons` | Normalized reason clusters and counts. |
| `status` | Must be `dry_run_not_adoption` for this tranche. |
| `policy_version` | Must be `external-dry-run-policy.v1`. |

Optional fields may include `sample_status`, `top_claim_types`,
`kill_criterion`, `usefulness`, `targets`, and compact per-artifact metrics.

## Expanded External Sample Schema

`anti-slop-external-sample-expansion.v1` records the same aggregate fields for
saved public external PR bodies plus `repo_count` and `root_mode`.
`anti-slop-external-sample-comparison.v1` compares the original this-repo sample
against the expanded external sample.

## Actionability Labels

This section defines actionability labels for aggregate clusters.

`anti-slop-actionability-labels.v1` labels aggregate clusters, not raw external
lines. Allowed labels are:

- `actionable`: a maintainer could plausibly act after rechecking in a local
  checkout;
- `non_actionable`: the finding is expected noise or a resolver limitation for
  this sample;
- `unclear`: aggregate evidence is insufficient to classify;
- `excluded`: excluded from usefulness rates, for example root-unavailable
  findings from an empty fixture root.

Actionability labels are triage labels for future learning. They are not
correctness, relevance, source-truth, support, safety, advice-quality,
reasoning, benchmark-validity, statistical-meaning, or canon judgments.

## Interpretation Boundary

Dry-run metrics can say whether saved public artifacts contain resolvable or
unresolved references. They do not prove correctness, relevance, source truth,
support, safety, advice quality, reasoning, benchmark validity, statistical
meaning, or canon.
