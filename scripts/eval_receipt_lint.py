#!/usr/bin/env python3
"""Receipt lint for the books-kb eval proof surface.

Read-only. Scans every eval model-output receipt under evals/ and reports
missing or empty provenance fields. A receipt with thin provenance is not
benchmark evidence — this lint surfaces the gaps before a status lift.

- Standard library only. No model/API calls, no embeddings, no network.
- Reads model-output frontmatter and the per-case benchmark-readiness
  classification only; reads no raw source files.
- Public-safe output: prints file paths, field names, and counts.
- Default: report-only, always exits 0. With `--strict`: exits nonzero when
  any base provenance field is missing (the benchmark-candidate extra-field
  checks are forward-looking warnings and never fail, even under --strict).

See docs/eval-benchmark-upgrade.md for the receipt fields a benchmark pass needs.
"""

from __future__ import annotations

from pathlib import Path
import sys

from artifact_status import read_frontmatter
from eval_benchmark_readiness import scan_case

ROOT = Path(__file__).resolve().parents[1]
EVALS_DIR = ROOT / "evals"

# Provenance every model-output receipt should carry.
BASE_FIELDS = [
    "run_id", "case_id", "model_condition", "model_id", "temperature", "top_p",
    "seed", "prompt_sha256", "source_packet_sha256", "output_file",
    "judge_model_id", "raw_model_output_public_safe",
]
# Extra provenance a benchmark pass needs (benchmark-candidate cases).
BENCHMARK_FIELDS = [
    "condition_packet_sha256", "judge_prompt_sha256", "model_snapshot",
    "benchmark_version", "run_number", "judge_independence",
]
BENCHMARK_CLASSES = {"benchmark_candidate", "benchmark_supported_claimed"}


def field_missing(fm: dict[str, str], key: str) -> bool:
    """True if the frontmatter key is absent or its value is empty."""
    return key not in fm or not str(fm.get(key) or "").strip()


def lint_receipt(path: Path, benchmark_case: bool) -> tuple[list[str], list[str]]:
    """Return (missing base fields, missing benchmark fields) for one receipt."""
    fm = read_frontmatter(path)
    base: list[str] = []
    for key in BASE_FIELDS:
        if field_missing(fm, key):
            base.append(key)
    # provider/runtime — at least one must be present
    if field_missing(fm, "provider") and field_missing(fm, "runtime"):
        base.append("provider/runtime")
    bench: list[str] = []
    if benchmark_case:
        for key in BENCHMARK_FIELDS:
            if field_missing(fm, key):
                bench.append(key)
    return base, bench


def main() -> int:
    strict = "--strict" in sys.argv[1:]
    case_paths = sorted(EVALS_DIR.rglob("case.md")) if EVALS_DIR.is_dir() else []

    out: list[str] = []
    out.append("== Anti-Slop eval receipt lint ==")
    if strict:
        out.append("Read-only lint (--strict). Exits nonzero if any base provenance")
        out.append("field is missing; benchmark-candidate extra fields only warn.")
    else:
        out.append("Read-only lint (scripts/eval_receipt_lint.py). Reports missing")
        out.append("provenance fields in eval model-output receipts. Always exits 0.")
    out.append("")

    total_receipts = 0
    total_base_findings = 0
    total_bench_findings = 0

    for case_path in case_paths:
        case_dir = case_path.parent
        rep = scan_case(case_path)
        benchmark_case = rep.classification in BENCHMARK_CLASSES
        outputs_dir = case_dir / "model-outputs"
        receipts = sorted(outputs_dir.glob("*.md")) if outputs_dir.is_dir() else []

        out.append(f"{rep.case_id}  [{rep.eval_type or 'eval'}]  "
                   f"classification={rep.classification}")
        if not receipts:
            out.append("  (no model-output receipts)")
            out.append("")
            continue
        for receipt in receipts:
            total_receipts += 1
            base, bench = lint_receipt(receipt, benchmark_case)
            total_base_findings += len(base)
            total_bench_findings += len(bench)
            rel = receipt.relative_to(ROOT)
            if not base and not bench:
                out.append(f"  OK   {rel}")
                continue
            out.append(f"  LINT {rel}")
            if base:
                out.append(f"    missing base provenance: {', '.join(base)}")
            if bench:
                out.append(f"    missing benchmark provenance (warn): {', '.join(bench)}")
        out.append("")

    out.append("-- Summary --")
    out.append(f"Receipts scanned: {total_receipts}")
    out.append(f"Missing base-provenance fields: {total_base_findings}")
    out.append(f"Missing benchmark-provenance fields (warn): {total_bench_findings}")
    if strict:
        exit_code = 1 if total_base_findings else 0
        out.append("Mode: --strict (missing base provenance fails; benchmark-field "
                   "warnings do not)")
        out.append(f"Exit status: {exit_code}")
    else:
        exit_code = 0
        out.append("Exit status: 0 (report-only)")
    out.append("")
    out.append("A model output is a test artifact, never an authority. Thin provenance")
    out.append("is not benchmark evidence; see docs/eval-benchmark-upgrade.md.")

    print("\n".join(out))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
