#!/usr/bin/env python3
"""60-second launch demo for agent claim verification.

The demo is offline and deterministic. It builds a temporary git fixture, checks
a fake report that must fail, then checks a receipt-backed report that must pass.
"""

from __future__ import annotations

from pathlib import Path
import json
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "proof" / "agent-claim-demo"
FAKE_REPORT = PROOF / "fake-agent-report.md"
BACKED_REPORT = PROOF / "receipt-backed-report.md"
SAMPLE_OUTPUT = PROOF / "sample-output.md"

sys.path.insert(0, str(ROOT / "scripts"))
import gate_claims  # noqa: E402


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def git(root: Path, *args: str) -> str:
    proc = subprocess.run(
        ["git", "-C", str(root), *args],
        capture_output=True,
        text=True,
        check=True,
    )
    return proc.stdout.strip()


def command_receipt(path: Path, fixture_root: Path, head: str) -> None:
    write(path, json.dumps({
        "schema_version": "anti-slop-command-receipt.v1",
        "receipt_type": "command",
        "command": ["make", "validate"],
        "command_string": "make validate",
        "command_tags": ["make:validate"],
        "cwd": str(fixture_root),
        "exit_code": 0,
        "duration_ms": 1,
        "git_head": head,
        "started_at": "2026-06-08T00:00:00Z",
        "stdout_sha256": "0" * 64,
        "stderr_sha256": "0" * 64,
        "stdout_bytes": 0,
        "stderr_bytes": 0,
        "tool_version": "demo-fixture",
        "metrics": {"score": 0.82},
    }, indent=2, sort_keys=True) + "\n")


def setup_fixture(tmp: Path) -> tuple[Path, Path]:
    fixture_root = tmp / "repo"
    fixture_root.mkdir()
    git(fixture_root, "init")
    git(fixture_root, "config", "user.email", "test@example.invalid")
    git(fixture_root, "config", "user.name", "Anti Slop Demo")
    write(fixture_root / "docs" / "changed.md", "# Changed\n\nbefore\n")
    write(
        fixture_root / "tests" / "test_demo.py",
        "def test_demo():\n"
        "    assert True\n",
    )
    git(fixture_root, "add", ".")
    git(fixture_root, "commit", "-m", "base fixture")
    head = git(fixture_root, "rev-parse", "HEAD")
    write(fixture_root / "docs" / "changed.md", "# Changed\n\nafter\n")
    receipts_dir = tmp / "receipts"
    command_receipt(receipts_dir / "make-validate.json", fixture_root, head)
    return fixture_root, receipts_dir


def check(report: Path, fixture_root: Path, receipts_dir: Path) -> dict:
    return gate_claims.structured_receipt(
        artifact_path=report,
        root=fixture_root,
        registry=None,
        require_reviewed_cards=False,
        diff_range="HEAD",
        receipts_dir=receipts_dir,
    )


def status(receipt: dict) -> str:
    return "PASS" if receipt.get("passed") else "FAIL"


def hard_fail_lines(receipt: dict) -> list[str]:
    lines = []
    for claim in receipt.get("claims", []):
        if claim.get("tier") == "hard" and claim.get("status") == "fail":
            lines.append(
                f"line {claim['line']}: {claim['type']} {claim['ref']} -> {claim['reason']}"
            )
    return lines


def hard_pass_count(receipt: dict) -> int:
    return sum(
        1 for claim in receipt.get("claims", [])
        if claim.get("tier") == "hard" and claim.get("status") == "pass"
    )


def render(fake: dict, backed: dict) -> str:
    lines = [
        "# Agent Claim Verification Demo Output",
        "",
        "Command:",
        "",
        "```sh",
        "make agent-claim-demo",
        "```",
        "",
        "## Fake Report",
        "",
        f"`proof/agent-claim-demo/fake-agent-report.md`: {status(fake)}",
        "",
    ]
    for line in hard_fail_lines(fake):
        lines.append(f"- {line}")
    lines.extend([
        "",
        "## Receipt-Backed Report",
        "",
        f"`proof/agent-claim-demo/receipt-backed-report.md`: {status(backed)}",
        f"- hard claims passed: {hard_pass_count(backed)}",
        "- hard claims failed: 0",
        "",
        "Boundary: this demo proves deterministic reference/receipt resolution only.",
    ])
    return "\n".join(lines) + "\n"


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        fixture_root, receipts_dir = setup_fixture(Path(tmp))
        fake = check(FAKE_REPORT, fixture_root, receipts_dir)
        backed = check(BACKED_REPORT, fixture_root, receipts_dir)

    output = render(fake, backed)
    SAMPLE_OUTPUT.write_text(output, encoding="utf-8")
    print(output, end="")
    if fake.get("passed"):
        print("demo failure: fake report unexpectedly passed", file=sys.stderr)
        return 1
    if not backed.get("passed"):
        print("demo failure: receipt-backed report unexpectedly failed", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
