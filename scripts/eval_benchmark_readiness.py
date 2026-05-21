#!/usr/bin/env python3
"""Benchmark-readiness dashboard for the books-kb eval proof surface.

Read-only. For every eval case under evals/ it reports how far the case is from
a `benchmark_supported` Result — the only Result status eligible to back a canon
candidate (see docs/eval-result-status-policy.md). It complements
`make eval-lab-status`: that dashboard reports per-case readiness in general;
this one focuses on the specific gap list between the case's current evidence
and benchmark evidence.

It runs nothing, scores nothing, promotes nothing, and edits nothing. It does
not change a case's status, a score sheet, a model output, or any Result value.

- Standard library only. No model/API calls, no embeddings, no graph DB.
- Reads eval case / score-sheet / run-packet / model-output files and the
  referenced source-card frontmatter only; reads no raw source files.
- Public-safe output: prints case ids, conditions, counts, and gap text.
- Always exits 0. This is a dashboard, not a gate.

See docs/eval-benchmark-upgrade.md for what a benchmark pass requires.
"""

from __future__ import annotations

from pathlib import Path
import sys

from artifact_status import read_frontmatter
from eval_lab_status import (
    CARD_ID_RE,
    LONG_PROMPT_MARKERS,
    MIN_BENCHMARK_RUNS,
    case_model_conditions,
    classify_output,
    condition_of,
    result_status,
)

ROOT = Path(__file__).resolve().parents[1]
EVALS_DIR = ROOT / "evals"
SOURCE_CARDS_DIR = ROOT / "corpus" / "source-cards"

# Phrases that indicate the judge limitation has been recorded honestly. An
# independent judge is NOT affirmatively detected from free text — substring
# matching cannot reliably tell "an independent judge was used" from "not an
# independent judge" — so this dashboard reports independence conservatively:
# a benchmark pass needs an independent judge, and that step is treated as
# outstanding unless a case carries explicit, structured evidence otherwise.
JUDGE_LIMITATION_MARKERS = (
    "not an independent",
    "not a fully independent",
    "same agent",
    "model-family separation",
    "model-family-separated",
)


def is_long_prompt(name: str) -> bool:
    return any(m in name for m in LONG_PROMPT_MARKERS)


class CaseReadiness:
    def __init__(self, case_path: Path) -> None:
        self.case_path = case_path
        self.case_id = ""
        self.eval_type = ""
        self.scoring_status = ""
        self.result: str | None = None
        self.declared: list[str] = []
        self.runs_by_condition: dict[str, int] = {}
        self.real = 0
        self.simulated = 0
        self.unknown = 0
        self.long_prompt_declared = False
        self.long_prompt_has_output = False
        self.cards_all_reviewed = True
        self.unreviewed_cards: list[str] = []
        self.missing_cards: list[str] = []
        self.judge_recorded = False
        self.judge_limitation_noted = False
        self.classification = "not_started"
        self.gaps: list[str] = []

    @property
    def output_total(self) -> int:
        return sum(self.runs_by_condition.values())

    @property
    def rel(self) -> str:
        return str(self.case_path.relative_to(ROOT))

    @property
    def conditions_with_output(self) -> list[str]:
        return [c for c, n in self.runs_by_condition.items() if n > 0]

    @property
    def declared_missing_output(self) -> list[str]:
        return [c for c in self.declared if self.runs_by_condition.get(c, 0) == 0]

    @property
    def min_runs(self) -> int:
        """Minimum run count across declared conditions that have any output."""
        counts = [self.runs_by_condition.get(c, 0)
                  for c in self.declared
                  if self.runs_by_condition.get(c, 0) > 0]
        return min(counts) if counts else 0

    @property
    def thin_conditions(self) -> list[str]:
        """Declared conditions with output but fewer than MIN_BENCHMARK_RUNS runs."""
        return sorted(
            c for c in self.declared
            if 0 < self.runs_by_condition.get(c, 0) < MIN_BENCHMARK_RUNS
        )


def scan_case(case_path: Path) -> CaseReadiness:
    rep = CaseReadiness(case_path)
    case_dir = case_path.parent
    case_text = case_path.read_text(encoding="utf-8")
    fm = read_frontmatter(case_path)
    rep.case_id = fm.get("case_id") or case_dir.name
    rep.eval_type = fm.get("eval_type") or ""
    rep.scoring_status = fm.get("scoring_status") or "(missing)"

    score_sheet = case_dir / "score-sheet.md"
    run_packet = case_dir / "run-packet.md"
    rep.result = result_status(score_sheet)

    rep.declared = case_model_conditions(case_text)
    rep.long_prompt_declared = any(is_long_prompt(c) for c in rep.declared)

    # model outputs
    outputs_dir = case_dir / "model-outputs"
    output_files = sorted(p for p in outputs_dir.glob("*.md")) if outputs_dir.is_dir() else []
    for path in output_files:
        ofm = read_frontmatter(path)
        cond = condition_of(path, ofm)
        rep.runs_by_condition[cond] = rep.runs_by_condition.get(cond, 0) + 1
        kind = classify_output(ofm)
        setattr(rep, kind, getattr(rep, kind) + 1)
        if (ofm.get("judge_model_id") or "").strip():
            rep.judge_recorded = True
    rep.long_prompt_has_output = any(
        is_long_prompt(c) for c in rep.conditions_with_output
    )

    # judge signals from score sheet and run packet
    judge_text = ""
    for doc in (score_sheet, run_packet):
        if doc.is_file():
            judge_text += "\n" + doc.read_text(encoding="utf-8").lower()
    if "judge_model_id" in judge_text or "judge notes" in judge_text:
        rep.judge_recorded = True
    rep.judge_limitation_noted = any(m in judge_text for m in JUDGE_LIMITATION_MARKERS)

    # referenced source cards
    for card_id in sorted(set(CARD_ID_RE.findall(case_text))):
        card_path = SOURCE_CARDS_DIR / f"{card_id}.md"
        if not card_path.is_file():
            rep.missing_cards.append(card_id)
        elif read_frontmatter(card_path).get("operator_review_status") != "reviewed":
            rep.unreviewed_cards.append(card_id)
    rep.cards_all_reviewed = not (rep.missing_cards or rep.unreviewed_cards)

    classify(rep)
    return rep


def classify(rep: CaseReadiness) -> None:
    """Set rep.classification and rep.gaps (what is still missing for benchmark)."""
    gaps: list[str] = []

    # gap: conditions declared but with no output
    if rep.declared_missing_output:
        gaps.append(
            "no output for declared condition(s): "
            + ", ".join(rep.declared_missing_output)
        )
    # gap: equal-length control
    if not rep.long_prompt_declared:
        gaps.append("no vanilla_long_prompt / equal-length control condition declared")
    elif not rep.long_prompt_has_output:
        gaps.append("vanilla_long_prompt / equal-length control declared but not run")
    # gap: simulated or unclassified outputs
    if rep.simulated > 0:
        gaps.append(
            f"{rep.simulated} simulated output(s) — benchmark requires all-real runs"
        )
    if rep.unknown > 0:
        gaps.append(
            f"{rep.unknown} output(s) not classifiable real vs simulated from receipts"
        )
    # gap: repeat runs
    if rep.output_total > 0 and rep.thin_conditions:
        gaps.append(
            f"fewer than {MIN_BENCHMARK_RUNS} runs for: "
            + ", ".join(rep.thin_conditions)
        )
    # gap: independent judge — always outstanding until a benchmark pass adds one
    if rep.output_total > 0:
        if rep.judge_limitation_noted:
            gaps.append(
                "no independent judge — judging is model-family-separated only "
                "(limitation recorded)"
            )
        elif rep.judge_recorded:
            gaps.append(
                "independent judge not confirmed — a benchmark pass needs one"
            )
        else:
            gaps.append("no judge recorded — a benchmark pass needs an independent judge")
    # gap: source-card lineage
    if rep.unreviewed_cards:
        gaps.append("referenced source card(s) not reviewed: "
                    + ", ".join(rep.unreviewed_cards))
    if rep.missing_cards:
        gaps.append("referenced source card(s) missing: "
                    + ", ".join(rep.missing_cards))

    # Result / status consistency
    if rep.output_total > 0 and rep.scoring_status != "scored":
        gaps.append(
            f"model outputs present but scoring_status is '{rep.scoring_status}'"
        )
    if rep.result == "benchmark_supported":
        if rep.simulated > 0 or rep.unknown > 0:
            gaps.append(
                "Result claims benchmark_supported but non-real outputs are present"
            )
        if rep.thin_conditions or not rep.long_prompt_has_output:
            gaps.append(
                "Result claims benchmark_supported but repeat-run / control "
                "requirements are not met"
            )

    rep.gaps = gaps

    # classification
    if rep.output_total == 0:
        rep.classification = "not_started"
    elif rep.result == "benchmark_supported":
        rep.classification = "benchmark_supported_claimed"
    elif rep.simulated > 0 or rep.unknown > 0 or rep.result == "dry_run_supported":
        rep.classification = "dry_run_only"
    elif (rep.long_prompt_has_output
          and not rep.thin_conditions
          and not rep.declared_missing_output
          and rep.min_runs >= MIN_BENCHMARK_RUNS):
        rep.classification = "benchmark_candidate"
    else:
        rep.classification = "real_single_run"


CLASSIFICATION_NOTE = {
    "not_started": "no model outputs yet",
    "dry_run_only": "evidence includes simulated outputs — design evidence only, "
                    "not canon-eligible",
    "real_single_run": "all outputs real, but single-run and/or missing the "
                       "equal-length control — stronger than dry-run, short of benchmark",
    "benchmark_candidate": "all-real with repeat runs and the control — ready for "
                           "an independent-judge benchmark pass",
    "benchmark_supported_claimed": "Result claims benchmark_supported — verify the "
                                   "gap list is empty",
}


def main() -> int:
    case_paths = sorted(EVALS_DIR.rglob("case.md")) if EVALS_DIR.is_dir() else []
    reports = [scan_case(p) for p in case_paths]

    out: list[str] = []
    out.append("== Anti-Slop eval benchmark-readiness ==")
    out.append("Read-only dashboard (scripts/eval_benchmark_readiness.py). Runs nothing,")
    out.append("scores nothing, promotes nothing. Reports the gap between each case's")
    out.append("current evidence and a benchmark_supported Result.")
    out.append("See docs/eval-benchmark-upgrade.md and docs/eval-result-status-policy.md.")
    out.append(f"Scanned: {len(reports)} eval case(s) under evals/.")
    out.append("")

    out.append("-- Per-case benchmark readiness --")
    if not reports:
        out.append("(no eval cases found)")
    for rep in reports:
        out.append(f"{rep.case_id}  [{rep.eval_type or 'eval'}]")
        out.append(f"  case:            {rep.rel}")
        out.append(f"  scoring_status:  {rep.scoring_status}    Result: "
                   f"{rep.result or '(none)'}")
        out.append(f"  classification:  {rep.classification} "
                   f"— {CLASSIFICATION_NOTE[rep.classification]}")
        out.append(f"  conditions:      {', '.join(rep.declared) or '(none declared)'}")
        if rep.runs_by_condition:
            per = ", ".join(f"{c}×{n}" for c, n in sorted(rep.runs_by_condition.items()))
        else:
            per = "none"
        out.append(f"  outputs/cond:    {per}")
        out.append(f"  outputs:         {rep.output_total} total — "
                   f"{rep.real} real, {rep.simulated} simulated, "
                   f"{rep.unknown} unclassified")
        out.append(f"  equal-length control: "
                   + ("present, run" if rep.long_prompt_has_output
                      else "declared, not run" if rep.long_prompt_declared
                      else "not declared"))
        out.append(f"  min runs/condition:   {rep.min_runs} "
                   f"(benchmark needs {MIN_BENCHMARK_RUNS})")
        out.append(f"  source cards:    "
                   + ("all reviewed" if rep.cards_all_reviewed else "ISSUES"))
        judge = ("model-family-separated, limitation recorded"
                 if rep.judge_limitation_noted
                 else "recorded, independence not confirmed" if rep.judge_recorded
                 else "not recorded")
        out.append(f"  judge:           {judge}")
        if rep.gaps:
            out.append(f"  gaps to benchmark_supported ({len(rep.gaps)}):")
            for g in rep.gaps:
                out.append(f"    - {g}")
        else:
            out.append("  gaps to benchmark_supported: none detected")
        out.append("")

    # aggregate
    out.append("-- Aggregate --")
    by_class: dict[str, int] = {}
    for rep in reports:
        by_class[rep.classification] = by_class.get(rep.classification, 0) + 1
    for key in ("not_started", "dry_run_only", "real_single_run",
                "benchmark_candidate", "benchmark_supported_claimed"):
        if by_class.get(key):
            out.append(f"  {key}: {by_class[key]}")
    candidates = [r.case_id for r in reports
                  if r.classification == "benchmark_candidate"]
    out.append("Cases ready for an independent-judge benchmark pass: "
               + (", ".join(candidates) or "none"))
    closest = [r.case_id for r in reports if r.classification == "real_single_run"]
    out.append("Cases all-real but short of benchmark (need repeats + independent judge): "
               + (", ".join(closest) or "none"))
    out.append("")
    out.append("Reminder: only a benchmark_supported Result may back a canon candidate.")
    out.append("This dashboard changes nothing.")
    out.append("")
    out.append("Exit status: 0 (read-only dashboard)")

    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
