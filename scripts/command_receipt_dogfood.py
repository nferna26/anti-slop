#!/usr/bin/env python3
"""Dogfood command receipts against a public-safe AGENT_FINAL_REPORT fixture."""

from __future__ import annotations

from pathlib import Path
import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DOG_DIR = ROOT / "proof" / "command-receipt-dogfood"
REPORT = DOG_DIR / "AGENT_FINAL_REPORT.md"
SUMMARY_JSON = DOG_DIR / "summary.json"
SUMMARY_MD = DOG_DIR / "summary.md"
SCHEMA = "anti-slop-command-receipt-dogfood.v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def validate_fixture(errors: list[str]) -> None:
    if not REPORT.is_file():
        errors.append(f"missing command dogfood report fixture: {rel(REPORT)}")
        return
    text = REPORT.read_text(encoding="utf-8")
    for snippet in ("`make validate` passed", "docs/command-receipts.md", "reference/receipt resolution only"):
        if snippet not in text:
            errors.append(f"{rel(REPORT)} missing snippet: {snippet}")


def run_dogfood() -> dict[str, Any]:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "repo"
        root.mkdir()
        shutil.copy(REPORT, root / "AGENT_FINAL_REPORT.md")
        (root / "docs").mkdir()
        (root / "docs" / "command-receipts.md").write_text("# Command Receipts\n", encoding="utf-8")
        (root / "Makefile").write_text("validate:\n\t@true\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(root), "init"], capture_output=True, check=True)
        subprocess.run(["git", "-C", str(root), "config", "user.email", "test@example.invalid"],
                       capture_output=True, check=True)
        subprocess.run(["git", "-C", str(root), "config", "user.name", "Anti Slop Dogfood"],
                       capture_output=True, check=True)
        subprocess.run(["git", "-C", str(root), "add", "."], capture_output=True, check=True)
        subprocess.run(["git", "-C", str(root), "commit", "-m", "fixture"],
                       capture_output=True, check=True)
        receipts = root / ".anti-slop" / "receipts"
        run_proc = subprocess.run([
            sys.executable,
            str(ROOT / "scripts" / "anti_slop_run.py"),
            "--cwd", str(root),
            "--receipts-dir", str(receipts),
            "--",
            "make", "validate",
        ], cwd=str(ROOT), capture_output=True, text=True)
        claims_json = root / ".anti-slop" / "claims.json"
        claims_proc = subprocess.run([
            sys.executable,
            str(ROOT / "scripts" / "gate_claims.py"),
            "--root", str(root),
            "--receipts", str(receipts),
            "--json", str(claims_json),
            str(root / "AGENT_FINAL_REPORT.md"),
        ], cwd=str(ROOT), capture_output=True, text=True)
        claims = json.loads(claims_json.read_text(encoding="utf-8")) if claims_json.is_file() else {}
        command_claims = [
            c for c in claims.get("claims", [])
            if c.get("type") == "command_receipt"
        ]
        passed = run_proc.returncode == 0 and claims_proc.returncode == 0
        return {
            "schema_version": SCHEMA,
            "status": "pass" if passed else "fail",
            "report": rel(REPORT),
            "receipt_source": "generated at smoke time with anti-slop-run; raw receipts are not committed",
            "claim_check": "anti-slop-claims --receipts",
            "command_receipt_claims": len(command_claims),
            "command_receipt_passed": sum(1 for c in command_claims if c.get("status") == "pass"),
            "dogfood_rate": 1.0 if command_claims and all(c.get("status") == "pass" for c in command_claims) else 0.0,
            "notes": [
                "Public-safe summary only; raw receipt contains local cwd and is intentionally not committed.",
                "This proves local command receipt matching only, not correctness, support, safety, or benchmark validity.",
            ],
        }


def write_markdown(summary: dict[str, Any]) -> None:
    lines = [
        "# Command Receipt Dogfood",
        "",
        f"- Schema: `{summary['schema_version']}`",
        f"- Status: `{summary['status']}`",
        f"- Report fixture: `{summary['report']}`",
        f"- Receipt source: {summary['receipt_source']}",
        f"- Claim check: `{summary['claim_check']}`",
        f"- Command receipt claims: {summary['command_receipt_claims']}",
        f"- Command receipt dogfood rate: {summary['dogfood_rate']:.0%}",
        "",
        "Raw anti-slop-run receipts are not committed because the schema records local cwd. The smoke regenerates them in a temporary repo.",
        "",
        "Boundary: command receipts prove local command facts only, not correctness, relevance, support, safety, benchmark validity, source truth, advice quality, reasoning, statistical meaning, or canon.",
    ]
    SUMMARY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def validate_outputs(errors: list[str]) -> None:
    validate_fixture(errors)
    if not SUMMARY_JSON.is_file():
        errors.append(f"missing command dogfood summary: {rel(SUMMARY_JSON)}")
        return
    summary = json.loads(SUMMARY_JSON.read_text(encoding="utf-8"))
    if summary.get("schema_version") != SCHEMA:
        errors.append(f"command dogfood schema mismatch: {summary.get('schema_version')}")
    if summary.get("status") != "pass":
        errors.append(f"command dogfood status must pass: {summary.get('status')}")
    if summary.get("command_receipt_claims", 0) < 1:
        errors.append("command dogfood found no command_receipt claims")
    if summary.get("dogfood_rate", 0.0) < 1.0:
        errors.append("command dogfood rate must be 1.0 for the fixture")
    text = json.dumps(summary, sort_keys=True)
    for forbidden in (str(ROOT), "/Users/", "GITHUB_TOKEN", "OPENAI_API_KEY", "ANTHROPIC_API_KEY"):
        if forbidden in text:
            errors.append(f"{rel(SUMMARY_JSON)} contains forbidden private/token-like snippet: {forbidden}")
    if not SUMMARY_MD.is_file():
        errors.append(f"missing command dogfood Markdown: {rel(SUMMARY_MD)}")


def self_test() -> int:
    fixture_errors: list[str] = []
    validate_fixture(fixture_errors)
    if fixture_errors:
        print("COMMAND RECEIPT DOGFOOD FAILED:")
        for error in fixture_errors:
            print(f"  - {error}")
        return 1
    summary = run_dogfood()
    write_json(SUMMARY_JSON, summary)
    write_markdown(summary)
    errors: list[str] = []
    validate_outputs(errors)
    if errors:
        print("COMMAND RECEIPT DOGFOOD FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(
        "COMMAND RECEIPT DOGFOOD PASSED: "
        f"{summary['command_receipt_claims']} command receipt claim(s), "
        f"dogfood_rate={summary['dogfood_rate']:.0%}."
    )
    return 0


def check_only() -> int:
    errors: list[str] = []
    validate_outputs(errors)
    if errors:
        print("COMMAND RECEIPT DOGFOOD CHECK FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"COMMAND RECEIPT DOGFOOD CHECK PASSED: {SCHEMA} summary is valid.")
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
