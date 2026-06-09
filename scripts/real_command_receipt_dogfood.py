#!/usr/bin/env python3
"""Dogfood command receipts against current-work public-safe final reports."""

from __future__ import annotations

from pathlib import Path
import argparse
import json
import subprocess
import sys
import tempfile
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "proof" / "real-command-receipt-dogfood"
REPORTS_DIR = OUT_DIR / "reports"
SUMMARY_JSON = OUT_DIR / "summary.json"
SUMMARY_MD = OUT_DIR / "summary.md"
SCHEMA = "anti-slop-real-command-receipt-dogfood.v1"

REPORTS = [
    {
        "id": "real-checkout-final-report",
        "path": REPORTS_DIR / "real-checkout-final-report.md",
        "command": ["python3", "scripts/real_checkout_learning.py", "--check"],
        "display_command": "python3 scripts/real_checkout_learning.py --check",
    },
    {
        "id": "real-checkout-actionability-final-report",
        "path": REPORTS_DIR / "real-checkout-actionability-final-report.md",
        "command": ["python3", "scripts/real_checkout_learning.py", "--check-actionability"],
        "display_command": "python3 scripts/real_checkout_learning.py --check-actionability",
    },
]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run(cmd: list[str], **kwargs: Any) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True, **kwargs)


def validate_reports(errors: list[str]) -> None:
    for report in REPORTS:
        path = report["path"]
        if not path.is_file():
            errors.append(f"missing real dogfood report: {rel(path)}")
            continue
        text = path.read_text(encoding="utf-8")
        for snippet in (
            f"command `{report['display_command']}` exited 0",
            "reference/receipt resolution only",
        ):
            if snippet not in text:
                errors.append(f"{rel(path)} missing snippet: {snippet}")


def run_dogfood() -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="anti-slop-real-command-dogfood-") as tmp:
        tmp_path = Path(tmp)
        receipts_dir = tmp_path / "receipts"
        claim_json_dir = tmp_path / "claims"
        claim_json_dir.mkdir()
        command_results: list[dict[str, Any]] = []
        for report in REPORTS:
            command = list(report["command"])
            run_proc = run([
                sys.executable,
                str(ROOT / "scripts" / "anti_slop_run.py"),
                "--cwd", str(ROOT),
                "--receipts-dir", str(receipts_dir),
                "--",
                *command,
            ])
            command_results.append({
                "id": report["id"],
                "command": report["display_command"],
                "anti_slop_run_exit": run_proc.returncode,
            })
        report_results: list[dict[str, Any]] = []
        total_claims = 0
        passed_claims = 0
        for report in REPORTS:
            claims_json = claim_json_dir / f"{report['id']}.json"
            claims_proc = run([
                sys.executable,
                str(ROOT / "scripts" / "gate_claims.py"),
                "--root", str(ROOT),
                "--receipts", str(receipts_dir),
                "--json", str(claims_json),
                str(report["path"]),
            ])
            claims = json.loads(claims_json.read_text(encoding="utf-8")) if claims_json.is_file() else {}
            command_claims = [
                claim for claim in claims.get("claims", [])
                if claim.get("type") == "command_receipt"
            ]
            total_claims += len(command_claims)
            passed = sum(1 for claim in command_claims if claim.get("status") == "pass")
            passed_claims += passed
            report_results.append({
                "id": report["id"],
                "report": rel(report["path"]),
                "claim_check_exit": claims_proc.returncode,
                "command_receipt_claims": len(command_claims),
                "command_receipt_passed": passed,
            })
        status = "pass" if total_claims >= len(REPORTS) and total_claims == passed_claims else "fail"
        return {
            "schema_version": SCHEMA,
            "status": status,
            "report_count": len(REPORTS),
            "receipt_source": "generated at smoke time with anti-slop-run; raw receipts are not committed",
            "claim_check": "anti-slop-claims --receipts",
            "command_receipt_claims": total_claims,
            "command_receipt_passed": passed_claims,
            "dogfood_rate": round(passed_claims / total_claims, 4) if total_claims else 0.0,
            "commands": command_results,
            "reports": report_results,
            "notes": [
                "Public-safe summary only; raw receipts contain local cwd and are intentionally not committed.",
                "This proves local command receipt matching only, not correctness, relevance, support, safety, source truth, advice quality, reasoning, benchmark validity, statistical meaning, or canon.",
            ],
        }


def write_markdown(summary: dict[str, Any]) -> None:
    lines = [
        "# Real Command Receipt Dogfood",
        "",
        f"- Schema: `{summary['schema_version']}`",
        f"- Status: `{summary['status']}`",
        f"- Reports: {summary['report_count']}",
        f"- Command receipt claims: {summary['command_receipt_claims']}",
        f"- Command receipt dogfood rate: {summary['dogfood_rate']:.0%}",
        f"- Receipt source: {summary['receipt_source']}",
        "",
        "Raw anti-slop-run receipts are regenerated in temporary storage and are not committed because command receipts record local cwd.",
        "",
        "Boundary: command receipts prove local command facts only, not correctness, relevance, support, safety, source truth, advice quality, reasoning, benchmark validity, statistical meaning, or canon.",
        "",
        "## Reports",
        "",
    ]
    for report in summary["reports"]:
        lines.append(
            f"- `{report['report']}`: {report['command_receipt_passed']}/"
            f"{report['command_receipt_claims']} command receipt claims passed"
        )
    SUMMARY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def validate_outputs(errors: list[str]) -> None:
    validate_reports(errors)
    if not SUMMARY_JSON.is_file():
        errors.append(f"missing real command dogfood summary: {rel(SUMMARY_JSON)}")
        return
    summary = json.loads(SUMMARY_JSON.read_text(encoding="utf-8"))
    if summary.get("schema_version") != SCHEMA:
        errors.append(f"real command dogfood schema mismatch: {summary.get('schema_version')}")
    if summary.get("status") != "pass":
        errors.append(f"real command dogfood status must pass: {summary.get('status')}")
    if int(summary.get("report_count", 0)) < 2:
        errors.append("real command dogfood must cover at least 2 public-safe reports")
    if int(summary.get("command_receipt_claims", 0)) < 2:
        errors.append("real command dogfood must detect at least 2 command_receipt claims")
    if float(summary.get("dogfood_rate", 0.0)) < 1.0:
        errors.append("real command dogfood rate must be 1.0")
    text = json.dumps(summary, sort_keys=True)
    for forbidden in (str(ROOT), "/Users/", "/private/var/", "GITHUB_TOKEN", "OPENAI_API_KEY", "ANTHROPIC_API_KEY"):
        if forbidden in text:
            errors.append(f"{rel(SUMMARY_JSON)} contains forbidden private/token-like snippet: {forbidden}")
    if not SUMMARY_MD.is_file():
        errors.append(f"missing real command dogfood Markdown: {rel(SUMMARY_MD)}")
    elif "/Users/" in SUMMARY_MD.read_text(encoding="utf-8"):
        errors.append(f"{rel(SUMMARY_MD)} contains private local path")


def self_test() -> int:
    report_errors: list[str] = []
    validate_reports(report_errors)
    if report_errors:
        print("REAL COMMAND RECEIPT DOGFOOD FAILED:")
        for error in report_errors:
            print(f"  - {error}")
        return 1
    summary = run_dogfood()
    write_json(SUMMARY_JSON, summary)
    write_markdown(summary)
    errors: list[str] = []
    validate_outputs(errors)
    if errors:
        print("REAL COMMAND RECEIPT DOGFOOD FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(
        "REAL COMMAND RECEIPT DOGFOOD PASSED: "
        f"{summary['report_count']} reports, "
        f"{summary['command_receipt_claims']} command receipt claims, "
        f"dogfood_rate={summary['dogfood_rate']:.0%}."
    )
    return 0


def check_only() -> int:
    errors: list[str] = []
    validate_outputs(errors)
    if errors:
        print("REAL COMMAND RECEIPT DOGFOOD CHECK FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"REAL COMMAND RECEIPT DOGFOOD CHECK PASSED: {SCHEMA} summary is valid.")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--check", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.check:
        return check_only()
    return self_test()


if __name__ == "__main__":
    sys.exit(main())
