#!/usr/bin/env python3
"""Smoke-test the report-mode adoption workflow template.

This is a local simulation of the commands the vendorable GitHub Actions
template runs. It does not call GitHub APIs, models, or network services.
"""

from __future__ import annotations

from pathlib import Path
import json
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "anti-slop-report.yml"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=str(cwd) if cwd else None, capture_output=True, text=True)


def git(root: Path, *args: str) -> None:
    proc = run(["git", "-C", str(root), *args])
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr or proc.stdout)


def check_template() -> list[str]:
    errors: list[str] = []
    if not TEMPLATE.is_file():
        return [f"missing workflow template: {TEMPLATE.relative_to(ROOT)}"]
    text = TEMPLATE.read_text(encoding="utf-8")
    required = [
        "anti-slop-pr-event --root . --report",
        "anti-slop-run -- make validate",
        "anti-slop-claims --root . --receipts .anti-slop/receipts --json .anti-slop/claims.json --report AGENT_FINAL_REPORT.md",
        "actions/upload-artifact",
        ".anti-slop/receipts/*.json",
        ".anti-slop/claims.json",
        "if-no-files-found: ignore",
        "Report mode",
    ]
    for snippet in required:
        if snippet not in text:
            errors.append(f"workflow template missing snippet: {snippet}")
    return errors


def pr_event_report_mode_smoke(tmp: Path) -> list[str]:
    errors: list[str] = []
    repo = tmp / "pr-repo"
    write(repo / "docs" / "exists.md", "# Exists\n")
    event = tmp / "pull_request.json"
    receipt = tmp / "pr-event-receipt.json"
    event.write_text(json.dumps({
        "pull_request": {
            "number": 99,
            "body": "Updates `docs/missing.md` and references `docs/exists.md`.",
        },
    }), encoding="utf-8")
    proc = run([
        sys.executable,
        str(ROOT / "scripts" / "pr_provenance_from_github_event.py"),
        "--event", str(event),
        "--event-name", "pull_request",
        "--root", str(repo),
        "--json", str(receipt),
        "--report",
    ])
    if proc.returncode != 0:
        errors.append(f"anti-slop-pr-event --report exited {proc.returncode}")
    if "UNRESOLVED line 1: file does not resolve: docs/missing.md" not in proc.stdout:
        errors.append("report-mode PR check did not expose fabricated file finding")
    if not receipt.is_file():
        errors.append("report-mode PR check did not write JSON receipt")
    else:
        data = json.loads(receipt.read_text(encoding="utf-8"))
        if data.get("passed") is not False:
            errors.append("report-mode PR receipt should record passed=false for fabricated refs")
    return errors


def generic_artifact_receipt_smoke(tmp: Path) -> list[str]:
    errors: list[str] = []
    repo = tmp / "artifact-repo"
    repo.mkdir()
    git(repo, "init")
    git(repo, "config", "user.email", "test@example.invalid")
    git(repo, "config", "user.name", "Anti Slop Adoption Smoke")
    write(repo / "Makefile", "validate:\n\t@echo validate-ok\n")
    write(repo / "docs" / "exists.md", "# Exists\n")
    write(repo / "AGENT_FINAL_REPORT.md",
          "# Agent Final Report\n\n"
          "Updated `docs/missing.md`.\n"
          "`make validate` passed.\n")
    git(repo, "add", ".")
    git(repo, "commit", "-m", "base")

    receipt_dir = repo / ".anti-slop" / "receipts"
    run_receipt = run([
        sys.executable,
        str(ROOT / "scripts" / "anti_slop_run.py"),
        "--cwd", str(repo),
        "--receipts-dir", ".anti-slop/receipts",
        "--", "make", "validate",
    ])
    if run_receipt.returncode != 0:
        errors.append(f"anti-slop-run exited {run_receipt.returncode}")
    if not list(receipt_dir.glob("*.json")):
        errors.append("anti-slop-run did not write .anti-slop/receipts/*.json")

    claims_json = repo / ".anti-slop" / "claims.json"
    claims = run([
        sys.executable,
        str(ROOT / "scripts" / "gate_claims.py"),
        "--root", str(repo),
        "--receipts", str(receipt_dir),
        "--json", str(claims_json),
        "--report",
        str(repo / "AGENT_FINAL_REPORT.md"),
    ])
    if claims.returncode != 0:
        errors.append(f"anti-slop-claims --report exited {claims.returncode}")
    if "UNRESOLVED line 3: file does not resolve: docs/missing.md" not in claims.stdout:
        errors.append("claims report did not expose fabricated file finding")
    if "fresh command receipt matches expected exit_code 0" not in claims.stdout:
        errors.append("claims report did not match the make validate command receipt")
    if not claims_json.is_file():
        errors.append("anti-slop-claims did not write .anti-slop/claims.json")
    else:
        data = json.loads(claims_json.read_text(encoding="utf-8"))
        if data.get("passed") is not False:
            errors.append("claims JSON should record passed=false for fabricated refs")
        claim_types = {c.get("type") for c in data.get("claims", [])}
        if "command_receipt" not in claim_types:
            errors.append("claims JSON missing command_receipt entry")
    return errors


def main() -> int:
    errors = check_template()
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        errors.extend(pr_event_report_mode_smoke(tmp_path))
        errors.extend(generic_artifact_receipt_smoke(tmp_path))
    if errors:
        print("ADOPTION SMOKE FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("ADOPTION SMOKE PASSED: report-mode workflow template, PR findings, command receipts, and claims JSON artifacts are covered.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
