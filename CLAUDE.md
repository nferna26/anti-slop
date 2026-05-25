# CLAUDE.md

Behavioral and project-specific instructions for Claude Code working in the Anti-Slop books-kb repo.

These guidelines bias toward caution, narrow diffs, and verifiable evidence. For trivial tasks, use judgment, but never bypass the authority, raw-text, or status gates.

## 1. Think Before Acting

Do not assume the summary is true. Inspect the current worktree.

Before editing:
- State the task in one sentence.
- Identify the artifact layer being touched: manifest, map, source card, claim/tension card, eval, receipt, dashboard, docs, or canon.
- If multiple interpretations exist, name them and choose conservatively.
- If a request would cross an authority gate, stop and ask for explicit operator approval.
- If something is unclear, ask before creating public artifacts.

## 2. Surgical Changes Only

Every changed line should trace to the user's request.

- Touch only the files needed for the goal.
- Do not refactor adjacent docs/scripts unless required.
- Do not "clean up" unrelated wording, formatting, metadata, or old log entries.
- Preserve existing style and artifact shape.
- Remove only mess your own change creates.
- If you notice unrelated drift, report it; do not fix it unless asked.

## 3. Authority Order Is Load-Bearing

Never collapse the ladder.

Authority order:
1. Book maps are discovery aids, not evidence and not canon.
2. Source cards are evidence units, not canon.
3. Claim/tension cards are synthesis units, not canon.
4. Eval outputs are test artifacts, not authorities.
5. Canon candidates are proposals.
6. Canon requires explicit operator approval and registry decision.

Do not:
- Treat a book map as source evidence.
- Let a tension card become advice or hidden canon.
- Promote any `Result` without the required gate and operator approval.
- Cite model outputs as evidence about the world.
- Create canon, graph edges, registry decisions, or public claims unless explicitly asked.

## 4. No Raw Source Leakage

Public artifacts are receipts, not source copies.

Never commit:
- PDFs, EPUBs, OCR dumps, extracted book text, raw filenames, private paths, long excerpts, model reasoning blocks, or local runtime logs.
- Raw source prompts or public embeddings of copyrighted text.
- Anything from `local-only/`.

Prefer:
- Locator + independent paraphrase.
- `Short excerpt: None.` unless a workflow explicitly requires a short compliant excerpt.
- Public-safe IDs and artifact paths only.

Always run or confirm:
- `make check-raw`
- private path sweep when touching public artifacts:
  `rg "(/Users/|Desktop|Archive[.]zip)" corpus/ kb/ docs/ evals/ runs/ registry/ proof/ gates/`

## 5. Status Discipline

Status changes are authority changes. Treat them as gates.

Never mark an artifact reviewed unless the user explicitly provides operator approval.

For status-only approvals:
- Confirm the prior status before editing.
- Re-run the relevant checklist.
- Change only status fields and approval notes.
- Preserve claim/body/rubric/output content.
- Log the approval concisely.

For evals:
- `partial` means not enough evidence.
- `dry_run_supported` is methodology evidence only, not canon-eligible.
- `benchmark_supported` requires benchmark gates and explicit operator approval.
- Decision labels such as `do_not_promote` or `weakened_by_blind_judge` are not `Result` statuses.

## 6. Eval Lab Rules

Evals test model behavior, not truth.

Before drafting an eval:
- Use reviewed source cards and reviewed claim/tension cards only.
- Do not cite book maps as evidence.
- Pre-register scenario, conditions, rubric, positive result, falsifier, judge protocol, and anti-overfitting safeguards.

Before running:
- Freeze packet recipes and hashes before generating outputs.
- Include an equal-length control for contradiction-preservation benchmark claims.
- Keep answer keys local-only.
- Anonymize outputs before judging.
- Never inspect condition-labelled outputs during blind judging.

When running:
- Real outputs only unless the task explicitly says dry run/simulation.
- Record timeouts and retries honestly.
- Do not fabricate missing outputs.
- Keep model reasoning/thinking blocks local-only.
- Commit public-safe final-output receipts with full provenance.

When judging:
- Judges see only condition-blind packet files.
- Do not read `model-outputs/` or answer keys while judging.
- Score criterion-level, not vibes.
- Do not reconcile conditions in the same step unless explicitly requested.
- Keep `scoring_status` and `Result` unchanged unless the goal explicitly includes the status lift.

## 7. Receipt Discipline

Receipts are evidence trails. Keep them auditable and compact.

For model-output receipts include:
- benchmark version
- condition
- run number
- seed
- model ID and snapshot or unavailable reason
- decoding params
- condition packet hash
- prompt/advisor hash
- real/simulated classification
- verbatim final answer only
- public-safe flag
- judge fields as pending/unavailable if not judged

For indexes:
- Generate or validate `receipt-index.yaml` when outputs change.
- Do not summarize away backing receipts.
- Keep answer keys local-only.

## 8. Simplicity First

Minimum artifact that satisfies the workflow.

- No speculative dashboards.
- No new scripts if an existing helper can do it.
- No broad architecture work during artifact goals.
- No API/model integrations in the public repo.
- Runtime harnesses, raw prompts, raw outputs, thinking blocks, and keys stay local-only.

If a task starts growing, pause and ask: "Is this still the requested artifact layer?"

## 9. Goal-Driven Execution

For multi-step work, define success criteria and verify them.

Use a short plan:
1. Inspect current state.
2. Make scoped edits.
3. Run gates.
4. Review diff.
5. Commit only if clean.

Do not stop at drafting if the user asked you to implement. Do not claim success until the current worktree proves it.

## 10. Required Gates Before Commit

At minimum, run:

```sh
make validate
make check-raw
make kb-lint
python3 -m py_compile scripts/*.py
git diff --check
```

When relevant, also run:

```sh
make eval-lab-status
make eval-benchmark-readiness
python3 scripts/artifact_preflight.py --strict
python3 scripts/receipt_index.py <case-dir> --check
python3 scripts/eval_receipt_lint.py --case <case-id> --strict-benchmark
```

For judge packets:
- Scan judge-facing files for condition names, model_condition, seeds, run numbers, and answer-key leaks.
- Confirm Surface 2 calibration references are not copied into judge-facing files.

## 11. Commit Reports

Final reports must be concrete and audit-friendly.

Include:
- Verdict: MOVE FORWARD or READY FOR OPERATOR APPROVAL or SEND BACK.
- Commit hash.
- Files changed.
- Exact status fields changed, if any.
- Gate results.
- Explicit confirmation of what did not happen: no raw text, no hidden canon, no Result lift, no judging/scoring/reconciliation unless requested.

If blocked:
- State the blocker plainly.
- Leave the working tree safe.
- Say exactly what should happen next.

## 12. Review Mode

When asked to review:
- Inspect the actual diff and surrounding files.
- Do not trust implementation summaries.
- Findings first, ordered by severity.
- Use file/line references.
- Separate blockers from non-blocking improvements.
- If SEND BACK, provide a scoped, copy-paste prompt.

## 13. The North Star

Anti-Slop is a maintained KB plus receipt trail. It is not a raw archive, not query-time RAG, not a prompt pack, and not an advisory system yet.

The work is good when:
- artifacts stay public-safe;
- authority boundaries stay explicit;
- contradictions are preserved;
- failed or weakened evals are recorded honestly;
- gates catch drift before claims grow;
- no result is stronger than the evidence.
