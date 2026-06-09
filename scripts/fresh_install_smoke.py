#!/usr/bin/env python3
"""Fresh-checkout install smoke for the Anti-Slop Receipts tag candidate.

This script installs from the documented public git/SHA spec in temporary
storage. It commits only a compact public-safe summary; raw venv logs, local
paths, stdout/stderr dumps, and temp checkouts are not persisted.
"""

from __future__ import annotations

from pathlib import Path
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "proof" / "fresh-install-smoke"
SUMMARY_JSON = OUT_DIR / "summary.json"
SUMMARY_MD = OUT_DIR / "summary.md"
PACKET = ROOT / "docs" / "tag-approval-packet.md"
REPO_URL = "https://github.com/nferna26/anti-slop.git"
PACKAGE_SPEC_BASE = "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop"
SCHEMA = "anti-slop-fresh-install-smoke.v1"
DEFAULT_CANDIDATE_COMMIT = "75ac7fbe80f62d50409ebc8fe1f736e9bc2fa649"
COMMANDS = [
    "anti-slop-lineage",
    "anti-slop-pr",
    "anti-slop-pr-event",
    "anti-slop-claims",
    "anti-slop-run",
]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run(cmd: list[str], cwd: Path | None = None, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    merged_env = os.environ.copy()
    merged_env.update(env or {})
    merged_env.setdefault("PIP_DISABLE_PIP_VERSION_CHECK", "1")
    return subprocess.run(cmd, cwd=str(cwd or ROOT), capture_output=True, text=True, env=merged_env)


def packet_candidate() -> str:
    if PACKET.is_file():
        match = re.search(
            r"Candidate commit:\s*`([0-9a-f]{40})`",
            PACKET.read_text(encoding="utf-8"),
        )
        if match:
            return match.group(1)
    env_candidate = os.environ.get("ANTI_SLOP_TAG_CANDIDATE_SHA")
    if env_candidate:
        return env_candidate
    return DEFAULT_CANDIDATE_COMMIT


def command_status(name: str, exit_code: int, expected: int = 0) -> dict[str, Any]:
    return {
        "command": name,
        "exit_code": exit_code,
        "expected_exit_code": expected,
        "status": "pass" if exit_code == expected else "fail",
    }


def blocked_summary(candidate: str, stage: str, reason: str) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA,
        "status": "blocked_fresh_install",
        "candidate_commit": candidate,
        "repository": "nferna26/anti-slop",
        "install_spec": f"{PACKAGE_SPEC_BASE}@{candidate}",
        "blocked_stage": stage,
        "blocked_reason": reason[:240],
        "source_clone": {"status": "blocked" if stage == "source_clone" else "not_run"},
        "install": {"status": "blocked" if stage == "install" else "not_run"},
        "commands": [],
        "report_mode_demo": {"status": "not_run"},
        "notes": [
            "Fresh install could not complete due to checkout/install infrastructure.",
            "No raw venv logs, local paths, or temp checkout contents are committed.",
            "Blocked install evidence is not an external adopter success claim.",
        ],
    }


def run_smoke() -> dict[str, Any]:
    candidate = packet_candidate()
    with tempfile.TemporaryDirectory(prefix="anti-slop-fresh-install-") as tmp:
        tmp_path = Path(tmp)
        clone_dir = tmp_path / "candidate"
        clone = run(["git", "clone", "--quiet", REPO_URL, str(clone_dir)])
        if clone.returncode != 0:
            return blocked_summary(candidate, "source_clone", clone.stderr or clone.stdout)
        checkout = run(["git", "-C", str(clone_dir), "checkout", "--quiet", candidate])
        if checkout.returncode != 0:
            return blocked_summary(candidate, "source_clone", checkout.stderr or checkout.stdout)
        rev = run(["git", "-C", str(clone_dir), "rev-parse", "HEAD"])
        if rev.returncode != 0:
            return blocked_summary(candidate, "source_clone", rev.stderr or rev.stdout)
        checked_out = rev.stdout.strip()

        venv_dir = tmp_path / "venv"
        venv = run([sys.executable, "-m", "venv", str(venv_dir)])
        if venv.returncode != 0:
            return blocked_summary(candidate, "install", venv.stderr or venv.stdout)
        python = venv_dir / "bin" / "python"
        install_spec = f"{PACKAGE_SPEC_BASE}@{candidate}"
        install = run([
            str(python),
            "-m",
            "pip",
            "install",
            "--no-cache-dir",
            install_spec,
        ])
        if install.returncode != 0:
            return blocked_summary(candidate, "install", install.stderr or install.stdout)

        bin_dir = venv_dir / "bin"
        command_results: list[dict[str, Any]] = []
        for name in COMMANDS:
            proc = run([str(bin_dir / name), "--self-test"])
            command_results.append(command_status(f"{name} --self-test", proc.returncode))

        demo_root = tmp_path / "demo-root"
        demo_root.mkdir()
        (demo_root / "README.md").write_text("# Demo\n", encoding="utf-8")
        report = tmp_path / "AGENT_FINAL_REPORT.md"
        claims_json = tmp_path / "claims.json"
        report.write_text(
            "# Agent Final Report\n\n"
            "Checked `README.md` and docs/missing.md in report mode.\n",
            encoding="utf-8",
        )
        demo = run([
            str(bin_dir / "anti-slop-claims"),
            "--root", str(demo_root),
            "--report",
            "--json", str(claims_json),
            str(report),
        ])
        findings_exposed = False
        if claims_json.is_file():
            claims = json.loads(claims_json.read_text(encoding="utf-8"))
            findings_exposed = any(
                claim.get("status") == "fail" and claim.get("type") == "file"
                for claim in claims.get("claims", [])
            )
        report_mode_demo = {
            "command": "anti-slop-claims --report --json AGENT_FINAL_REPORT.md",
            "exit_code": demo.returncode,
            "status": "pass" if demo.returncode == 0 and findings_exposed else "fail",
            "fabricated_ref_exposed": findings_exposed,
        }
        smoke_passed = (
            checked_out == candidate
            and all(item["status"] == "pass" for item in command_results)
            and report_mode_demo["status"] == "pass"
        )
        return {
            "schema_version": SCHEMA,
            "status": "pass" if smoke_passed else "fail",
            "candidate_commit": candidate,
            "repository": "nferna26/anti-slop",
            "install_spec": install_spec,
            "source_clone": {
                "status": "pass" if checked_out == candidate else "fail",
                "checked_out_commit": checked_out,
                "storage": "temporary local-only checkout; not committed",
            },
            "install": {
                "status": "pass",
                "method": "documented public git/SHA pip install",
                "package": "anti-slop-lineage",
            },
            "commands": command_results,
            "report_mode_demo": report_mode_demo,
            "notes": [
                "Fresh install checks only that the documented git/SHA install path and installed CLIs smoke on this machine.",
                "It is not external adopter install success, correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon evidence.",
                "No raw venv logs, local paths, raw API JSON, external repo contents, secrets, or stdout/stderr dumps are committed.",
            ],
        }


def write_markdown(summary: dict[str, Any]) -> None:
    lines = [
        "# Fresh Install Smoke",
        "",
        f"- Schema: `{summary['schema_version']}`",
        f"- Status: `{summary['status']}`",
        f"- Candidate commit: `{summary['candidate_commit']}`",
        f"- Install spec: `{summary['install_spec']}`",
        "",
        "This smoke uses temporary storage and installs from the public git/SHA spec, not a local editable checkout. Raw venv logs and temp paths are not committed.",
        "",
        "Boundary: this checks only install/CLI smoke facts for the candidate commit. It is not external adopter install success and does not prove correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.",
    ]
    if summary["status"] == "pass":
        lines.extend(["", "## Commands", ""])
        for item in summary["commands"]:
            lines.append(f"- `{item['command']}`: {item['status']} (exit {item['exit_code']})")
        demo = summary["report_mode_demo"]
        lines.extend([
            "",
            "## Report-Mode Demo",
            "",
            f"- `{demo['command']}`: {demo['status']} (exit {demo['exit_code']})",
            f"- Fabricated ref exposed: {demo['fabricated_ref_exposed']}",
        ])
    else:
        lines.extend([
            "",
            f"Blocked stage: `{summary.get('blocked_stage', 'n/a')}`",
            f"Blocked reason: {summary.get('blocked_reason', 'n/a')}",
        ])
    SUMMARY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def validate_summary(errors: list[str]) -> dict[str, Any] | None:
    if not SUMMARY_JSON.is_file():
        errors.append(f"missing fresh install summary: {rel(SUMMARY_JSON)}")
        return None
    data = json.loads(SUMMARY_JSON.read_text(encoding="utf-8"))
    if data.get("schema_version") != SCHEMA:
        errors.append(f"fresh install schema mismatch: {data.get('schema_version')}")
    if data.get("status") not in {"pass", "fail", "blocked_fresh_install"}:
        errors.append(f"invalid fresh install status: {data.get('status')}")
    candidate = data.get("candidate_commit", "")
    if not re.fullmatch(r"[0-9a-f]{40}", str(candidate)):
        errors.append(f"fresh install candidate_commit must be full SHA: {candidate}")
    if data.get("status") == "pass":
        if not data.get("install_spec", "").endswith(f"@{candidate}"):
            errors.append("fresh install spec must end with the candidate full SHA")
        command_names = {str(item.get("command", "")).split()[0] for item in data.get("commands", [])}
        missing = sorted(set(COMMANDS) - command_names)
        if missing:
            errors.append(f"fresh install command self-tests missing: {missing}")
        for item in data.get("commands", []):
            if item.get("status") != "pass":
                errors.append(f"fresh install command failed: {item}")
        demo = data.get("report_mode_demo", {})
        if demo.get("status") != "pass" or demo.get("fabricated_ref_exposed") is not True:
            errors.append("fresh install report-mode demo must exit 0 and expose fabricated ref")
    text = json.dumps(data, sort_keys=True)
    for forbidden in (str(ROOT), "/Users/", "/private/var/", "GITHUB_TOKEN", "OPENAI_API_KEY", "ANTHROPIC_API_KEY"):
        if forbidden in text:
            errors.append(f"{rel(SUMMARY_JSON)} contains forbidden private/token-like snippet: {forbidden}")
    if not SUMMARY_MD.is_file():
        errors.append(f"missing fresh install Markdown summary: {rel(SUMMARY_MD)}")
    elif "/Users/" in SUMMARY_MD.read_text(encoding="utf-8"):
        errors.append(f"{rel(SUMMARY_MD)} contains private local path")
    return data


def self_test() -> int:
    summary = run_smoke()
    write_json(SUMMARY_JSON, summary)
    write_markdown(summary)
    errors: list[str] = []
    validate_summary(errors)
    if errors:
        print("FRESH INSTALL SMOKE FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    if summary["status"] == "blocked_fresh_install":
        print(
            "FRESH INSTALL SMOKE RECORDED BLOCKED: "
            f"{summary.get('blocked_stage')} ({summary.get('blocked_reason')})"
        )
        return 0
    if summary["status"] != "pass":
        print("FRESH INSTALL SMOKE FAILED: installed candidate did not pass smoke.")
        return 1
    print(
        "FRESH INSTALL SMOKE PASSED: "
        f"{len(summary['commands'])} installed command self-tests and report-mode demo passed."
    )
    return 0


def check_only() -> int:
    errors: list[str] = []
    validate_summary(errors)
    if errors:
        print("FRESH INSTALL SMOKE CHECK FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"FRESH INSTALL SMOKE CHECK PASSED: {SCHEMA} summary is valid.")
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
