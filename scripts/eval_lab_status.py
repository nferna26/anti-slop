#!/usr/bin/env python3
"""Eval Lab status dashboard for the books-kb proof surface.

Read-only. Scans every eval case under evals/ and reports its readiness as
proof-surface evidence — conditions run, real vs simulated outputs, result
status, controls present, and the receipt blockers that keep a case from being
mistaken for benchmark (canon-eligible) evidence.

It runs nothing and scores nothing. It does not change a case's status, a score
sheet, a model output, or any Result value.

- Standard library only. No model/API calls, no embeddings, no graph DB.
- Reads eval case / score-sheet / model-output files and referenced source-card
  frontmatter only; reads no raw source files.
- Public-safe output: prints case ids, conditions, statuses, and counts.
- Always exits 0. This is a dashboard, not a gate.

See docs/eval-lab-protocol.md for what the statuses and controls mean.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

from artifact_status import read_frontmatter

ROOT = Path(__file__).resolve().parents[1]
EVALS_DIR = ROOT / "evals"
SOURCE_CARDS_DIR = ROOT / "corpus" / "source-cards"

CARD_ID_RE = re.compile(r"\bBK-\d{4}-card-\d{3}\b")
RESULT_STATUSES = ("partial", "inconclusive", "falsified",
                   "dry_run_supported", "benchmark_supported")
LONG_PROMPT_MARKERS = ("vanilla_long_prompt", "long_prompt", "equal_length", "equal-length")
MIN_BENCHMARK_RUNS = 3  # per docs/eval-benchmark-upgrade.md


def result_status(score_sheet: Path) -> str | None:
    """First status word in a score-sheet.md ## Result section."""
    if not score_sheet.is_file():
        return None
    lines = score_sheet.read_text(encoding="utf-8").splitlines()
    for i, raw in enumerate(lines):
        if raw.strip() == "## Result":
            for follow in lines[i + 1:]:
                if follow.strip():
                    token = follow.strip().split()[0].strip("`*—-:")
                    return token or None
    return None


def classify_output(fm: dict) -> str:
    """Return 'real', 'simulated', or 'unknown' for a model-output receipt."""
    notes = (fm.get("operator_notes") or "").lower()
    if any(p in notes for p in ("real local-model run", "real external model run",
                                "real model run", "genuine local-model output")):
        return "real"
    if (fm.get("runtime") or "").strip():
        return "real"
    if "simulation" in notes or "simulated" in notes:
        return "simulated"
    return "unknown"


def condition_of(path: Path, fm: dict) -> str:
    """Model condition for an output file: frontmatter, else filename stem (less -NN)."""
    cond = (fm.get("model_condition") or "").strip()
    if cond:
        return cond
    return re.sub(r"-\d+$", "", path.stem)


def case_model_conditions(case_text: str) -> list[str]:
    """Parse the model_conditions: list block from case.md frontmatter."""
    conditions: list[str] = []
    in_fm = False
    in_list = False
    for raw in case_text.splitlines():
        if raw.strip() == "---":
            if in_fm:
                break
            in_fm = True
            continue
        if not in_fm:
            continue
        if raw.startswith("model_conditions:"):
            in_list = True
            continue
        if in_list:
            stripped = raw.strip()
            if stripped.startswith("- "):
                conditions.append(stripped[2:].strip())
                continue
            in_list = False
    return conditions


def listed_outputs(case_text: str) -> set[str]:
    """model-outputs/<name>.md filenames mentioned anywhere in case.md."""
    return set(re.findall(r"model-outputs/([A-Za-z0-9_.-]+\.md)", case_text))


def read_eval_decision(case_dir: Path) -> dict | None:
    """Frontmatter of a case's eval-decision.md receipt, if present.

    An eval-decision receipt is a public-safe, operator-facing decision record
    that sits on top of the score-sheet ## Result. It records a decision — for
    example `eval_decision: do_not_promote` — without changing or replacing the
    Result status. See docs/eval-lab-protocol.md. Returns None when no
    eval-decision.md exists for the case.
    """
    path = case_dir / "eval-decision.md"
    if not path.is_file():
        return None
    fm = read_frontmatter(path)
    fm["_path"] = str(path.relative_to(ROOT))
    return fm


# --- per-case scan ---------------------------------------------------------

class CaseReport:
    def __init__(self, case_path: Path) -> None:
        self.case_path = case_path
        self.case_id = ""
        self.eval_type = ""
        self.status = ""
        self.scoring_status = ""
        self.result = None
        self.has_score_sheet = False
        self.conditions: dict[str, int] = {}     # condition -> run count
        self.real = 0
        self.simulated = 0
        self.unknown = 0
        self.has_long_prompt_control = False
        self.unreviewed_cards: list[str] = []
        self.missing_cards: list[str] = []
        self.eval_decision: dict | None = None
        self.blockers: list[str] = []
        self.warnings: list[str] = []

    @property
    def output_total(self) -> int:
        return sum(self.conditions.values())

    @property
    def rel(self) -> str:
        return str(self.case_path.relative_to(ROOT))


def scan_case(case_path: Path) -> CaseReport:
    rep = CaseReport(case_path)
    case_dir = case_path.parent
    case_text = case_path.read_text(encoding="utf-8")
    fm = read_frontmatter(case_path)
    rep.case_id = fm.get("case_id") or case_dir.name
    rep.eval_type = fm.get("eval_type") or ""
    rep.status = fm.get("status") or "(missing)"
    rep.scoring_status = fm.get("scoring_status") or "(missing)"

    score_sheet = case_dir / "score-sheet.md"
    rep.has_score_sheet = score_sheet.is_file()
    rep.result = result_status(score_sheet)
    rep.eval_decision = read_eval_decision(case_dir)

    # model outputs
    outputs_dir = case_dir / "model-outputs"
    output_files = sorted(p for p in outputs_dir.glob("*.md")) if outputs_dir.is_dir() else []
    declared = set(case_model_conditions(case_text))
    for path in output_files:
        ofm = read_frontmatter(path)
        cond = condition_of(path, ofm)
        rep.conditions[cond] = rep.conditions.get(cond, 0) + 1
        kind = classify_output(ofm)
        setattr(rep, kind, getattr(rep, kind) + 1)
    declared_long = any(any(m in c for m in LONG_PROMPT_MARKERS) for c in declared)
    run_long = any(any(m in c for m in LONG_PROMPT_MARKERS) for c in rep.conditions)
    rep.has_long_prompt_control = declared_long or run_long

    # referenced source cards
    for card_id in sorted(set(CARD_ID_RE.findall(case_text))):
        card_path = SOURCE_CARDS_DIR / f"{card_id}.md"
        if not card_path.is_file():
            rep.missing_cards.append(card_id)
            continue
        if read_frontmatter(card_path).get("operator_review_status") != "reviewed":
            rep.unreviewed_cards.append(card_id)

    # blockers
    if not rep.has_score_sheet:
        rep.blockers.append("score-sheet.md is missing")
    for cid in rep.missing_cards:
        rep.blockers.append(f"referenced source card {cid} does not exist")
    for cid in rep.unreviewed_cards:
        rep.blockers.append(f"referenced source card {cid} is not operator-reviewed")
    if rep.result == "benchmark_supported":
        if rep.simulated > 0:
            rep.blockers.append(
                f"Result is benchmark_supported but {rep.simulated} model output(s) "
                "are in-session simulations — benchmark evidence must be real runs"
            )
        thin = sorted(c for c, n in rep.conditions.items() if n < MIN_BENCHMARK_RUNS)
        if thin:
            rep.blockers.append(
                f"Result is benchmark_supported but conditions with fewer than "
                f"{MIN_BENCHMARK_RUNS} runs: {', '.join(thin)}"
            )
    if rep.result and rep.result not in RESULT_STATUSES:
        rep.blockers.append(f"Result status '{rep.result}' is not in the controlled vocabulary")

    # warnings
    listed = listed_outputs(case_text)
    on_disk = {p.name for p in output_files}
    missing_on_disk = sorted(listed - on_disk)
    unlisted = sorted(on_disk - listed)
    if missing_on_disk:
        rep.warnings.append(
            f"case.md lists model outputs not on disk: {', '.join(missing_on_disk)}"
        )
    if unlisted:
        rep.warnings.append(
            f"model-outputs files not listed in case.md: {', '.join(unlisted)}"
        )
    if rep.output_total == 0:
        rep.warnings.append("no model outputs present")
    if rep.scoring_status == "unscored":
        rep.warnings.append("scoring_status is unscored — no run has been judged")
    if rep.result == "dry_run_supported":
        rep.warnings.append(
            "Result is dry_run_supported — informs methodology, NOT canon-eligible; "
            "needs a benchmark upgrade (see docs/eval-benchmark-upgrade.md)"
        )
    if not rep.has_long_prompt_control and rep.output_total > 0:
        rep.warnings.append(
            "no vanilla_long_prompt / equal-length control — substrate advantage is "
            "not yet separated from prompt length"
        )
    if rep.unknown > 0:
        rep.warnings.append(
            f"{rep.unknown} model output(s) could not be classified real vs simulated "
            "from their receipts"
        )
    return rep


# --- report ----------------------------------------------------------------

def main() -> int:
    case_paths = sorted(EVALS_DIR.rglob("case.md")) if EVALS_DIR.is_dir() else []
    reports = [scan_case(p) for p in case_paths]

    out: list[str] = []
    out.append("== Anti-Slop Eval Lab status ==")
    out.append("Read-only dashboard (scripts/eval_lab_status.py). Runs nothing, scores")
    out.append("nothing, promotes nothing. See docs/eval-lab-protocol.md.")
    out.append(f"Scanned: {len(reports)} eval case(s) under evals/.")
    out.append("")

    out.append("-- Per-case readiness --")
    if not reports:
        out.append("(no eval cases found)")
    for rep in reports:
        out.append(f"{rep.case_id}  [{rep.eval_type or 'eval'}]")
        out.append(f"  case:           {rep.rel}")
        out.append(f"  status:         {rep.status}    scoring_status: {rep.scoring_status}")
        out.append(f"  Result:         {rep.result or '(none — no score sheet / unset)'}")
        if rep.conditions:
            conds = ", ".join(
                f"{c}×{n}" if n > 1 else c
                for c, n in sorted(rep.conditions.items())
            )
        else:
            conds = "none"
        out.append(f"  conditions run: {conds}")
        out.append(
            f"  outputs:        {rep.output_total} total — "
            f"{rep.real} real, {rep.simulated} simulated, {rep.unknown} unclassified"
        )
        out.append(
            f"  long-prompt control: {'present' if rep.has_long_prompt_control else 'MISSING'}"
        )
        cards_line = "all referenced source cards reviewed"
        if rep.missing_cards or rep.unreviewed_cards:
            parts = []
            if rep.unreviewed_cards:
                parts.append(f"unreviewed: {', '.join(rep.unreviewed_cards)}")
            if rep.missing_cards:
                parts.append(f"missing: {', '.join(rep.missing_cards)}")
            cards_line = "; ".join(parts)
        out.append(f"  source cards:   {cards_line}")
        if rep.eval_decision:
            dec = rep.eval_decision.get("eval_decision", "(unspecified)")
            dclass = rep.eval_decision.get("decision_class", "")
            label = dec + (f" [{dclass}]" if dclass else "")
            out.append(f"  eval decision:  {label}  (see {rep.eval_decision['_path']})")
            summary = rep.eval_decision.get("decision_summary", "")
            if summary:
                out.append(f"                  {summary}")
        for b in rep.blockers:
            out.append(f"  BLOCKER: {b}")
        for w in rep.warnings:
            out.append(f"  warning: {w}")
        out.append("")

    # aggregate
    out.append("-- Aggregate --")
    by_result: dict[str, int] = {}
    by_scoring: dict[str, int] = {}
    for rep in reports:
        key = rep.result or "(unset)"
        by_result[key] = by_result.get(key, 0) + 1
        by_scoring[rep.scoring_status] = by_scoring.get(rep.scoring_status, 0) + 1
    out.append("By Result status:   " + (
        "  ".join(f"{k}={v}" for k, v in sorted(by_result.items())) or "(none)"))
    out.append("By scoring_status:  " + (
        "  ".join(f"{k}={v}" for k, v in sorted(by_scoring.items())) or "(none)"))

    needs_upgrade = [r.case_id for r in reports
                     if r.result in ("partial", "inconclusive", "dry_run_supported")
                     or (r.result is None and r.output_total > 0)]
    out.append(
        f"Cases needing benchmark upgrade ({len(needs_upgrade)}): "
        + (", ".join(needs_upgrade) or "none")
    )
    missing_long = [r.case_id for r in reports
                    if not r.has_long_prompt_control and r.output_total > 0]
    out.append(
        f"Cases missing a long-prompt / equal-length control ({len(missing_long)}): "
        + (", ".join(missing_long) or "none")
    )
    benchmark_ready = [r.case_id for r in reports if r.result == "benchmark_supported"
                       and not r.blockers]
    out.append(
        f"Cases at benchmark_supported with clean receipts ({len(benchmark_ready)}): "
        + (", ".join(benchmark_ready) or "none")
    )
    non_promoted = [r.case_id for r in reports
                    if r.eval_decision
                    and r.eval_decision.get("eval_decision") == "do_not_promote"]
    out.append(
        f"Cases with a recorded non-promotion decision ({len(non_promoted)}): "
        + (", ".join(non_promoted) or "none")
    )
    total_blockers = sum(len(r.blockers) for r in reports)
    total_warnings = sum(len(r.warnings) for r in reports)
    out.append(f"Total blockers: {total_blockers}    Total warnings: {total_warnings}")
    out.append("")
    out.append("Reminder: dry_run_supported informs methodology only. Canon promotion is")
    out.append("operator-gated and requires benchmark_supported evidence. This dashboard")
    out.append("changes nothing.")
    out.append("")
    out.append("Exit status: 0 (read-only dashboard)")

    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
