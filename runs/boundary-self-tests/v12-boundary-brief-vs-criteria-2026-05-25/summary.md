# Boundary Tools V12 Self-Test Summary

## Result

This smoke test does not support the narrow gate-failure hypothesis: criteria-only and boundary-brief outputs produced the same number of gate failures.

| Condition | Runs | Gate checks | Passes | Failures |
|---|---:|---:|---:|---:|
| `boundary_brief` | 3 | 6 | 6 | 0 |
| `criteria_prompt_only` | 3 | 6 | 6 | 0 |

## Interpretation

- `boundary_brief` outputs cited real reviewed card IDs and passed citation-lineage.
- `criteria_prompt_only` outputs did not fabricate card IDs or source lineage, so citation-lineage also passed.
- After the no-universalization gate was tightened to avoid false positives on local option comparisons and explicit anti-overclaims, neither condition triggered that gate.
- The gates and compiler worked, but this tiny failure-count comparison did not separate the conditions. That is a fast negative for the specific hypothesis that criteria-only outputs would immediately fabricate lineage or over-generalize more often on the v12 case.

## Conditions

- `boundary_brief`: v12 Advisor prompt plus compiled `machine_compiled_not_canon` brief from `BK-0048-card-001`, `BK-0001-card-001`, and `BK-0007-card-001`.
- `criteria_prompt_only`: v12 Advisor prompt plus abstract criteria reminder; no source cards, source names, summaries, or lineage supplied.

## Notes From Generated Outputs

- The criteria-only outputs stayed disciplined enough not to invent lineage.
- The boundary-brief outputs used valid card IDs where they cited source cards.
- This self-test does not judge recommendation correctness. In particular, some boundary-brief outputs leaned toward Case Evidence Review rather than the v12 benchmark target, which should be inspected separately before treating boundary briefs as advisory improvements.

## Gate Receipts

- `boundary_brief-01.md` / `citation_lineage`: `PASS` — `gate-receipts/boundary_brief-01-citation_lineage.md`
- `boundary_brief-01.md` / `no_universalization`: `PASS` — `gate-receipts/boundary_brief-01-no_universalization.md`
- `boundary_brief-02.md` / `citation_lineage`: `PASS` — `gate-receipts/boundary_brief-02-citation_lineage.md`
- `boundary_brief-02.md` / `no_universalization`: `PASS` — `gate-receipts/boundary_brief-02-no_universalization.md`
- `boundary_brief-03.md` / `citation_lineage`: `PASS` — `gate-receipts/boundary_brief-03-citation_lineage.md`
- `boundary_brief-03.md` / `no_universalization`: `PASS` — `gate-receipts/boundary_brief-03-no_universalization.md`
- `criteria_prompt_only-01.md` / `citation_lineage`: `PASS` — `gate-receipts/criteria_prompt_only-01-citation_lineage.md`
- `criteria_prompt_only-01.md` / `no_universalization`: `PASS` — `gate-receipts/criteria_prompt_only-01-no_universalization.md`
- `criteria_prompt_only-02.md` / `citation_lineage`: `PASS` — `gate-receipts/criteria_prompt_only-02-citation_lineage.md`
- `criteria_prompt_only-02.md` / `no_universalization`: `PASS` — `gate-receipts/criteria_prompt_only-02-no_universalization.md`
- `criteria_prompt_only-03.md` / `citation_lineage`: `PASS` — `gate-receipts/criteria_prompt_only-03-citation_lineage.md`
- `criteria_prompt_only-03.md` / `no_universalization`: `PASS` — `gate-receipts/criteria_prompt_only-03-no_universalization.md`

## Authority Boundary

This self-test is a tooling smoke test only. It is not a benchmark, not canon support, and not evidence that the recommendations are correct.
