#!/usr/bin/env python3
"""Fresh install smoke for the pushed Anti-Slop Receipts tag.

This installs from the public tag, verifies the remote tag target, and commits
only a compact public-safe summary. Raw venv logs, local paths, stdout/stderr
dumps, and temp checkout contents are not persisted.
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
OUT_DIR = ROOT / "proof" / "tag-install-smoke"
SUMMARY_JSON = OUT_DIR / "summary.json"
SUMMARY_MD = OUT_DIR / "summary.md"
REPO_URL = "https://github.com/nferna26/anti-slop.git"
PACKAGE_SPEC_BASE = "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop"
SCHEMA = "anti-slop-tag-install-smoke.v1"
TAG_NAME = "anti-slop-receipts-v0.1.0"
TARGET_COMMIT = "75ac7fbe80f62d50409ebc8fe1f736e9bc2fa649"
STALE_TAG_DOC_CANDIDATE = "4bda4fd727018a2a027ba8c660c48c30b8aa2144"
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


def command_status(name: str, exit_code: int, expected: int = 0) -> dict[str, Any]:
    return {
        "command": name,
        "exit_code": exit_code,
        "expected_exit_code": expected,
        "status": "pass" if exit_code == expected else "fail",
    }


def unavailable_summary(stage: str, status: str = "fail") -> dict[str, Any]:
    return {
        "schema_version": SCHEMA,
        "status": status,
        "tag_name": TAG_NAME,
        "target_commit": TARGET_COMMIT,
        "repository": "nferna26/anti-slop",
        "install_spec": f"{PACKAGE_SPEC_BASE}@{TAG_NAME}",
        "failed_stage": stage,
        "remote_tag": {"status": "not_available" if stage == "remote_tag" else "not_run"},
        "install": {"status": "not_run"},
        "commands": [],
        "report_mode_demo": {"status": "not_run"},
        "notes": [
            "Tag install smoke did not complete.",
            "Raw venv logs, local paths, temp paths, and stdout/stderr dumps are not committed.",
            "This is deterministic install/CLI smoke evidence only, not correctness or source-truth evidence.",
        ],
    }


def remote_tag_target() -> dict[str, str]:
    proc = run(["git", "ls-remote", "--tags", REPO_URL, f"refs/tags/{TAG_NAME}*"])
    if proc.returncode != 0:
        return {"status": "unavailable"}
    direct = ""
    peeled = ""
    for line in proc.stdout.splitlines():
        parts = line.split()
        if len(parts) != 2:
            continue
        sha, ref = parts
        if ref == f"refs/tags/{TAG_NAME}":
            direct = sha
        elif ref == f"refs/tags/{TAG_NAME}^{{}}":
            peeled = sha
    if not direct and not peeled:
        return {"status": "missing"}
    return {
        "status": "pass" if (peeled or direct) == TARGET_COMMIT else "fail",
        "tag_object": direct,
        "peeled_commit": peeled or direct,
    }


def tag_source_docs() -> dict[str, Any]:
    packet = run(["git", "show", f"{TAG_NAME}:docs/tag-approval-packet.md"])
    text = packet.stdout if packet.returncode == 0 else ""
    stale = (
        "Decision: ready_to_request_operator_tag" in text
        and STALE_TAG_DOC_CANDIDATE in text
        and "No tag has been created" in text
    )
    return {
        "status": "stale_pre_finalization_docs" if stale else "unexpected",
        "path": "docs/tag-approval-packet.md",
        "decision": "ready_to_request_operator_tag" if "Decision: ready_to_request_operator_tag" in text else "unknown",
        "candidate_commit": STALE_TAG_DOC_CANDIDATE if STALE_TAG_DOC_CANDIDATE in text else "unknown",
        "contains_no_tag_created": "No tag has been created" in text,
        "disclosure": (
            "tag's embedded docs predate PR #46 finalization; installable package "
            "smoke passes, but any GitHub release from v0.1.0 requires explicit "
            "disclosure, or the safer path is creating anti-slop-receipts-v0.1.1 "
            "after PR #46 merges and fresh tag-install proof passes"
        ),
    }


def run_smoke() -> dict[str, Any]:
    tag = remote_tag_target()
    source_docs = tag_source_docs()
    if tag.get("status") != "pass":
        summary = unavailable_summary("remote_tag")
        summary["remote_tag"] = tag
        summary["tag_source_docs"] = source_docs
        return summary

    with tempfile.TemporaryDirectory(prefix="anti-slop-tag-install-") as tmp:
        tmp_path = Path(tmp)
        venv_dir = tmp_path / "venv"
        venv = run([sys.executable, "-m", "venv", str(venv_dir)])
        if venv.returncode != 0:
            return unavailable_summary("install")
        python = venv_dir / "bin" / "python"
        install_spec = f"{PACKAGE_SPEC_BASE}@{TAG_NAME}"
        install = run([
            str(python),
            "-m",
            "pip",
            "install",
            "--no-cache-dir",
            install_spec,
        ])
        if install.returncode != 0:
            return unavailable_summary("install")

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
            tag.get("peeled_commit") == TARGET_COMMIT
            and all(item["status"] == "pass" for item in command_results)
            and report_mode_demo["status"] == "pass"
        )
        return {
            "schema_version": SCHEMA,
            "status": "pass" if smoke_passed else "fail",
            "tag_name": TAG_NAME,
            "target_commit": TARGET_COMMIT,
            "repository": "nferna26/anti-slop",
            "install_spec": install_spec,
            "remote_tag": tag,
            "tag_source_docs": source_docs,
            "install": {
                "status": "pass",
                "method": "documented public tag pip install",
                "package": "anti-slop-lineage",
            },
            "commands": command_results,
            "report_mode_demo": report_mode_demo,
            "notes": [
                "Tag install checks only that the pushed tag resolves to the target commit and installed CLIs smoke on this machine.",
                "Do not force-move anti-slop-receipts-v0.1.0; the tag's embedded docs predate PR #46 finalization.",
                "Installable package smoke passes, but a GitHub release from v0.1.0 requires explicit disclosure, or the safer path is creating anti-slop-receipts-v0.1.1 after PR #46 merges and fresh tag-install proof passes.",
                "It is not external adopter install success, correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon evidence.",
                "No raw venv logs, local paths, raw API JSON, external repo contents, secrets, or stdout/stderr dumps are committed.",
            ],
        }


def write_markdown(summary: dict[str, Any]) -> None:
    lines = [
        "# Tag Install Smoke",
        "",
        f"- Schema: `{summary['schema_version']}`",
        f"- Status: `{summary['status']}`",
        f"- Tag: `{summary['tag_name']}`",
        f"- Target commit: `{summary['target_commit']}`",
        f"- Install spec: `{summary['install_spec']}`",
        "",
        "This smoke installs from the public tag in temporary storage, not a local editable checkout. Raw venv logs and temp paths are not committed.",
        "",
        "Boundary: this checks only tag resolution and install/CLI smoke facts. It is not external adopter install success and does not prove correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.",
    ]
    if summary["status"] == "pass":
        remote = summary["remote_tag"]
        lines.extend([
            "",
            "## Remote Tag",
            "",
            f"- Peeled commit: `{remote.get('peeled_commit')}`",
            "",
            "## Tag Source Disclosure",
            "",
            "- Do not force-move `anti-slop-receipts-v0.1.0`.",
            "- The tag's embedded docs predate PR #46 finalization: `docs/tag-approval-packet.md` inside the tag says Decision: `ready_to_request_operator_tag`, candidate `4bda4fd727018a2a027ba8c660c48c30b8aa2144`, and `No tag has been created`.",
            "- The installable package smoke passes, but the tag's embedded docs predate PR #46 finalization.",
            "- Any GitHub release from v0.1.0 requires explicit disclosure, or the safer path is creating `anti-slop-receipts-v0.1.1` after PR #46 merges and fresh tag-install proof passes.",
            "",
            "## Commands",
            "",
        ])
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
            f"Failed stage: `{summary.get('failed_stage', 'n/a')}`",
            f"Remote tag status: `{summary.get('remote_tag', {}).get('status', 'n/a')}`",
        ])
    SUMMARY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def validate_summary(errors: list[str]) -> dict[str, Any] | None:
    if not SUMMARY_JSON.is_file():
        errors.append(f"missing tag install summary: {rel(SUMMARY_JSON)}")
        return None
    data = json.loads(SUMMARY_JSON.read_text(encoding="utf-8"))
    if data.get("schema_version") != SCHEMA:
        errors.append(f"tag install schema mismatch: {data.get('schema_version')}")
    if data.get("tag_name") != TAG_NAME:
        errors.append(f"tag install tag_name must be {TAG_NAME}: {data.get('tag_name')}")
    if data.get("target_commit") != TARGET_COMMIT:
        errors.append(f"tag install target_commit must be {TARGET_COMMIT}: {data.get('target_commit')}")
    if data.get("status") != "pass":
        errors.append(f"tag install status must be pass: {data.get('status')}")
    if data.get("status") == "pass":
        if data.get("install_spec") != f"{PACKAGE_SPEC_BASE}@{TAG_NAME}":
            errors.append("tag install spec must use the public tag")
        if data.get("remote_tag", {}).get("peeled_commit") != TARGET_COMMIT:
            errors.append("tag install remote tag must peel to the target commit")
        command_names = {str(item.get("command", "")).split()[0] for item in data.get("commands", [])}
        missing = sorted(set(COMMANDS) - command_names)
        if missing:
            errors.append(f"tag install command self-tests missing: {missing}")
        for item in data.get("commands", []):
            if item.get("status") != "pass":
                errors.append(f"tag install command failed: {item}")
        demo = data.get("report_mode_demo", {})
        if demo.get("status") != "pass" or demo.get("fabricated_ref_exposed") is not True:
            errors.append("tag install report-mode demo must exit 0 and expose fabricated ref")
        source_docs = data.get("tag_source_docs", {})
        if source_docs.get("status") != "stale_pre_finalization_docs":
            errors.append("tag install summary must disclose stale pre-finalization tag-source docs")
        if source_docs.get("candidate_commit") != STALE_TAG_DOC_CANDIDATE:
            errors.append("tag install source-doc candidate must record the stale PR #44 SHA")
    text = json.dumps(data, sort_keys=True)
    for forbidden in (str(ROOT), "/Users/", "/private/var/", "GITHUB_TOKEN", "OPENAI_API_KEY", "ANTHROPIC_API_KEY"):
        if forbidden in text:
            errors.append(f"{rel(SUMMARY_JSON)} contains forbidden private/token-like snippet: {forbidden}")
    if not SUMMARY_MD.is_file():
        errors.append(f"missing tag install Markdown summary: {rel(SUMMARY_MD)}")
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
        print("TAG INSTALL SMOKE FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(
        "TAG INSTALL SMOKE PASSED: "
        f"{TAG_NAME} resolves to {TARGET_COMMIT}; "
        f"{len(summary['commands'])} installed command self-tests and report-mode demo passed."
    )
    return 0


def check_only() -> int:
    errors: list[str] = []
    validate_summary(errors)
    if errors:
        print("TAG INSTALL SMOKE CHECK FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"TAG INSTALL SMOKE CHECK PASSED: {SCHEMA} summary is valid.")
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
