# Eval Result Status Policy

Every eval case carries a result status in its `score-sheet.md` → `## Result`. This policy defines the controlled vocabulary for that status, the difference between dry-run and benchmark evidence, and the bar an eval result must clear before it may support a canon candidate.

It is a v1 policy: lightweight and judgment-based, with no automation. The status is set by hand by whoever scores the case, against the definitions below.

For the practical operating checklist that turns a `dry_run_supported` case into a benchmark candidate, see `docs/eval-benchmark-upgrade.md`.

## Why this exists

`docs/public-writing-rules.md` (Claim boundary) forbids "Anti-Slop produces better advice" claims without an eval result that says so. This policy defines what "an eval result that says so" means — so a score sheet cannot drift into implying more than its evidence supports, and so canon promotion has a stated evidentiary bar.

## Status vocabulary

A score sheet's `## Result` is exactly one of these five values, plus a one-line justification.

| Status | Meaning |
|---|---|
| `partial` | Scoring is incomplete — not all required conditions or runs are in yet. The case is mid-evaluation. |
| `inconclusive` | All required conditions are run, but the signal neither clearly supports the substrate nor meets the case's falsifier. The comparison is ambiguous. |
| `falsified` | The case's `## Falsifier` condition is met. The eval's hypothesis is refuted for this case. A `falsified` result is itself a recorded finding. |
| `dry_run_supported` | The substrate beat the baselines by the case's `## Positive result` criterion and the v1 support requirements below are met, but the evidence rests wholly or partly on in-session simulated outputs. Informs methodology; not strong enough for canon promotion. |
| `benchmark_supported` | As `dry_run_supported`, but every output the substrate-vs-baseline comparison rests on is a real external model run — no in-session simulations. This is the strong status. |

A status is never implied by a blank or by silence — `## Result` always carries one of these five words and a justification.

## Dry-run vs real-run evidence

Model outputs come in two kinds, and the score sheet must say which each is — in the model-output frontmatter and in Judge Notes:

- **In-session simulation** — an output written in-session as a good-faith simulation of how a model would answer under a condition. Useful for building and exercising the eval harness and for methodology iteration. It is not independent evidence about model behaviour.
- **Real external model run** — an output produced by actually running a model (local or hosted) on the case prompt, recorded verbatim with its exact model ID and runtime.

An eval result that rests on in-session simulations can reach at most `dry_run_supported`. `benchmark_supported` requires real external model runs for every condition the substrate-vs-baseline comparison depends on.

## v1 requirements for a "supported" status

Before a result may be `dry_run_supported` or `benchmark_supported`, all of the following must hold and be visible in the score sheet:

1. **Conditions run.** Every condition the case requires has been run, or is explicitly waived in the score sheet with a stated reason.
2. **A baseline exists.** At least one non-substrate baseline condition was run (for example, `vanilla`).
3. **The substrate wins by the case's criterion.** `substrate_workflow` beats the baselines by the standard set in the case's `## Positive result`, and the case's `## Falsifier` is not met.
4. **Receipts exist.** A model-output receipt file exists under `model-outputs/` for every scored run.
5. **Limitations recorded.** The score sheet states the result's limitations — sample size, the dry-run vs real-run mix, and anything else that bounds the claim.

If any requirement fails, the result stays `partial`, `inconclusive`, or `falsified`, as applicable.

## What an eval result may support

- `partial`, `inconclusive`, `falsified` — support no public advice claim. A `falsified` result is a recorded finding, not a failure to hide.
- `dry_run_supported` — may inform methodology and substrate iteration. It may **not** support a canon candidate, and may not back a "the substrate produces better advice" claim.
- `benchmark_supported` — is the eval evidence `docs/public-writing-rules.md` (Claim boundary) requires. A canon candidate that cites an eval result must cite a `benchmark_supported` one.

Dry-run support and benchmark support are not the same strength of evidence. Dry-run support says the harness and the substrate behave as intended under simulation; benchmark support says real models behave that way. Only the second is strong enough for canon promotion.

## Recording the status

In `score-sheet.md` → `## Result`, write the status word followed by a one-line justification that names the deciding facts — which conditions ran, the substrate-vs-baseline scores, and why the status is not higher. Keep `scoring_status` in the score-sheet frontmatter as the separate `unscored` / `scored` flag for whether any run has been judged at all.

Before lifting a result to `benchmark_supported`, verify the case against `docs/eval-benchmark-upgrade.md`: frozen packet, real model outputs for every comparison condition, exact model IDs and runtime metadata, prompt/source-packet hashes, repeat runs, judge separation, and receipt consistency.
