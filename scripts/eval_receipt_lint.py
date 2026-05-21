#!/usr/bin/env python3
"""Receipt lint for the books-kb eval proof surface.

Read-only. Scans eval model-output receipts and reports missing or empty
provenance fields. A receipt with thin provenance is not benchmark evidence —
this lint surfaces the gaps before a status lift.

- Standard library only. No model/API calls, no embeddings, no network.
- Reads model-output frontmatter and the per-case benchmark-readiness
  classification only; reads no raw source files.
- Public-safe output: prints file paths, field names, and counts.

Options:
- (default)                  report-only; always exits 0.
- --strict                   exit nonzero if any base provenance field is
                             missing, in any scanned case.
- --strict-benchmark         exit nonzero if any benchmark-candidate case has a
                             receipt missing base or benchmark-only provenance.
                             Old dry-run / design cases never affect this mode.
- --benchmark-candidates-only  scan only benchmark-candidate cases.
- --case <case_id>           scan only the named case.

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
    base: list[str] = [k for k in BASE_FIELDS if field_missing(fm, k)]
    if field_missing(fm, "provider") and field_missing(fm, "runtime"):
        base.append("provider/runtime")
    bench: list[str] = []
    if benchmark_case:
        bench = [k for k in BENCHMARK_FIELDS if field_missing(fm, k)]
    return base, bench


def parse_args(argv: list[str]) -> dict:
    opts = {
        "strict": "--strict" in argv,
        "strict_benchmark": "--strict-benchmark" in argv,
        "bc_only": "--benchmark-candidates-only" in argv,
        "case": None,
    }
    for i, arg in enumerate(argv):
        if arg == "--case" and i + 1 < len(argv):
            opts["case"] = argv[i + 1]
        elif arg.startswith("--case="):
            opts["case"] = arg.split("=", 1)[1]
    return opts


def main() -> int:
    opts = parse_args(sys.argv[1:])
    case_paths = sorted(EVALS_DIR.rglob("case.md")) if EVALS_DIR.is_dir() else []

    out: list[str] = []
    out.append("== Anti-Slop eval receipt lint ==")
    mode_bits = []
    if opts["strict"]:
        mode_bits.append("--strict")
    if opts["strict_benchmark"]:
        mode_bits.append("--strict-benchmark")
    if opts["bc_only"]:
        mode_bits.append("--benchmark-candidates-only")
    if opts["case"]:
        mode_bits.append(f"--case {opts['case']}")
    out.append("Read-only lint (scripts/eval_receipt_lint.py). Reports missing "
               "provenance in eval model-output receipts.")
    out.append("Mode: " + (" ".join(mode_bits) if mode_bits else "default (report-only)"))
    out.append("")

    total_receipts = 0
    total_base_findings = 0
    total_bench_findings = 0
    # benchmark-candidate receipts that are not benchmark-complete (base or bench gaps)
    benchmark_candidate_incomplete = 0
    scanned_cases = 0

    for case_path in case_paths:
        case_dir = case_path.parent
        rep = scan_case(case_path)
        benchmark_case = rep.classification in BENCHMARK_CLASSES
        if opts["case"] and rep.case_id != opts["case"]:
            continue
        if opts["bc_only"] and not benchmark_case:
            continue
        scanned_cases += 1
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
            if benchmark_case and (base or bench):
                benchmark_candidate_incomplete += 1
            rel = receipt.relative_to(ROOT)
            if not base and not bench:
                out.append(f"  OK   {rel}")
                continue
            out.append(f"  LINT {rel}")
            if base:
                out.append(f"    missing base provenance: {', '.join(base)}")
            if bench:
                out.append(f"    missing benchmark provenance: {', '.join(bench)}")
        out.append("")

    out.append("-- Summary --")
    out.append(f"Cases scanned: {scanned_cases}    Receipts scanned: {total_receipts}")
    out.append(f"Missing base-provenance fields: {total_base_findings}")
    out.append(f"Missing benchmark-provenance fields: {total_bench_findings}")
    out.append(f"Benchmark-candidate receipts not benchmark-complete: "
               f"{benchmark_candidate_incomplete}")

    exit_code = 0
    reasons: list[str] = []
    if opts["strict"] and total_base_findings:
        exit_code = 1
        reasons.append(f"--strict: {total_base_findings} missing base-provenance field(s)")
    if opts["strict_benchmark"] and benchmark_candidate_incomplete:
        exit_code = 1
        reasons.append(f"--strict-benchmark: {benchmark_candidate_incomplete} "
                       f"benchmark-candidate receipt(s) not benchmark-complete")
    if not (opts["strict"] or opts["strict_benchmark"]):
        out.append("Exit status: 0 (report-only)")
    else:
        if reasons:
            out.append("Fails: " + "; ".join(reasons))
        else:
            out.append("Strict checks passed.")
        out.append(f"Exit status: {exit_code}")
    out.append("")
    out.append("A model output is a test artifact, never an authority. Thin provenance")
    out.append("is not benchmark evidence; see docs/eval-benchmark-upgrade.md.")

    print("\n".join(out))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
