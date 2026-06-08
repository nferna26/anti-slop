#!/usr/bin/env python3
"""Run the synthetic agent-claim verification corpus.

This benchmark is for the deterministic checker, not for agent/model quality.
It measures whether `anti-slop-claims` catches missing references and receipts
under the current narrow resolver contract.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import json
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "benchmarks" / "agent-claim-corpus-v0.1"
CASES = CORPUS / "cases.json"
RESULTS = CORPUS / "results"

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


def command_receipt(path: Path, fixture_root: Path, command: list[str], exit_code: int,
                    git_head: str, tags: list[str] | None = None,
                    metrics: dict | None = None) -> None:
    write(path, json.dumps({
        "schema_version": "anti-slop-command-receipt.v1",
        "receipt_type": "command",
        "command": command,
        "command_string": " ".join(command),
        "command_tags": tags or [],
        "cwd": str(fixture_root),
        "exit_code": exit_code,
        "duration_ms": 1,
        "git_head": git_head,
        "started_at": "2026-06-08T00:00:00Z",
        "stdout_sha256": "0" * 64,
        "stderr_sha256": "0" * 64,
        "stdout_bytes": 0,
        "stderr_bytes": 0,
        "tool_version": "benchmark-fixture",
        "metrics": metrics or {},
    }, indent=2, sort_keys=True) + "\n")


def setup_fixture(tmp: Path) -> dict:
    fixture_root = tmp / "repo"
    fixture_root.mkdir()
    git(fixture_root, "init")
    git(fixture_root, "config", "user.email", "test@example.invalid")
    git(fixture_root, "config", "user.name", "Anti Slop Benchmark")

    write(fixture_root / "docs" / "existing.md", "# Existing\n\none\ntwo\n")
    write(fixture_root / "docs" / "unchanged.md", "# Unchanged\n\nstable\n")
    write(fixture_root / "docs" / "changed.md", "# Changed\n\nbefore\n")
    write(fixture_root / "docs" / "nested" / "guide.md", "# Guide\n")
    write(fixture_root / "src" / "tool.py", "def tool():\n    return 'before'\n")
    write(fixture_root / "scripts" / "check.py", "print('ok')\n")
    write(fixture_root / "config" / "settings.json", "{\"enabled\": true}\n")
    write(
        fixture_root / "tests" / "test_claims.py",
        "def test_valid():\n"
        "    assert True\n\n"
        "def test_other():\n"
        "    assert True\n\n"
        "async def test_async_valid():\n"
        "    assert True\n\n"
        "class TestWidget:\n"
        "    pass\n",
    )
    write(tmp / "known-issues.txt", "101\n202\n")

    git(fixture_root, "add", ".")
    git(fixture_root, "commit", "-m", "base fixture")
    head = git(fixture_root, "rev-parse", "HEAD")

    write(fixture_root / "docs" / "changed.md", "# Changed\n\nafter\n")
    write(fixture_root / "src" / "tool.py", "def tool():\n    return 'after'\n")

    receipts = {
        "ok": tmp / "receipts" / "ok",
        "empty": tmp / "receipts" / "empty",
        "nonzero": tmp / "receipts" / "nonzero",
        "stale": tmp / "receipts" / "stale",
        "metric_mismatch": tmp / "receipts" / "metric-mismatch",
    }
    for path in receipts.values():
        path.mkdir(parents=True, exist_ok=True)

    command_receipt(receipts["ok"] / "make-validate.json", fixture_root,
                    ["make", "validate"], 0, head, tags=["make:validate"])
    command_receipt(receipts["ok"] / "pytest.json", fixture_root,
                    ["pytest"], 0, head, tags=["pytest", "tests"])
    command_receipt(receipts["ok"] / "check.json", fixture_root,
                    ["python3", "scripts/check.py"], 0, head)
    command_receipt(receipts["ok"] / "fail-exit.json", fixture_root,
                    ["python3", "scripts/fail.py"], 2, head)
    command_receipt(receipts["ok"] / "metrics.json", fixture_root,
                    ["python3", "scripts/score.py"], 0, head,
                    metrics={"score": 0.82, "score.before": 0.70,
                             "score.after": 0.82, "accuracy": 0.91})
    command_receipt(receipts["nonzero"] / "make-validate.json", fixture_root,
                    ["make", "validate"], 2, head, tags=["make:validate"])
    command_receipt(receipts["stale"] / "make-validate.json", fixture_root,
                    ["make", "validate"], 0, "0" * 40, tags=["make:validate"])
    command_receipt(receipts["metric_mismatch"] / "metrics.json", fixture_root,
                    ["python3", "scripts/score.py"], 0, head,
                    metrics={"score": 0.81, "score.before": 0.70,
                             "score.after": 0.81, "accuracy": 0.89})

    return {
        "root": fixture_root,
        "issues": {"101", "202"},
        "receipts": receipts,
        "valid_commit": head,
        "valid_commit_short": head[:12],
    }


def load_cases() -> list[dict]:
    cases = json.loads(CASES.read_text(encoding="utf-8"))
    if len(cases) < 50:
        raise SystemExit(f"expected at least 50 cases, found {len(cases)}")
    return cases


def run_case(case: dict, state: dict, artifacts_dir: Path) -> dict:
    text = "# Synthetic Agent Report\n\n" + case["artifact"].format(**state) + "\n"
    artifact = artifacts_dir / f"{case['id']}.md"
    write(artifact, text)
    receipt = gate_claims.structured_receipt(
        artifact_path=artifact,
        root=state["root"],
        registry=state["issues"] if case.get("issue_registry") else None,
        require_reviewed_cards=False,
        diff_range=case.get("diff"),
        receipts_dir=state["receipts"].get(case["receipts"]) if case.get("receipts") else None,
    )
    hard_fail_reasons = [
        c["reason"] for c in receipt.get("claims", [])
        if c.get("tier") == "hard" and c.get("status") == "fail"
    ]
    advisory = [
        c["reason"] for c in receipt.get("claims", [])
        if c.get("status") == "advisory"
    ]
    actual_pass = bool(receipt.get("passed"))
    expected_pass = bool(case["expect_pass"])
    return {
        "id": case["id"],
        "claim_type": case["claim_type"],
        "truth": bool(case["truth"]),
        "enforceable": bool(case["enforceable"]),
        "expected_pass": expected_pass,
        "actual_pass": actual_pass,
        "matched_expectation": actual_pass == expected_pass,
        "hard_fail_reasons": hard_fail_reasons,
        "advisory_reasons": advisory,
    }


def summarize(results: list[dict]) -> dict:
    total = len(results)
    matched = sum(1 for r in results if r["matched_expectation"])
    enforceable_false = [r for r in results if r["enforceable"] and not r["truth"]]
    caught = [r for r in enforceable_false if not r["actual_pass"]]
    true_cases = [r for r in results if r["truth"] and r["expected_pass"]]
    false_fails = [r for r in true_cases if not r["actual_pass"]]
    advisory_false = [r for r in results if not r["truth"] and not r["enforceable"]]

    by_type: dict[str, dict] = {}
    for claim_type in sorted({r["claim_type"] for r in results}):
        items = [r for r in results if r["claim_type"] == claim_type]
        invalid_enforceable = [r for r in items if r["enforceable"] and not r["truth"]]
        invalid_caught = [r for r in invalid_enforceable if not r["actual_pass"]]
        valid = [r for r in items if r["truth"] and r["expected_pass"]]
        type_false_fails = [r for r in valid if not r["actual_pass"]]
        by_type[claim_type] = {
            "cases": len(items),
            "expectation_match_rate": round(sum(1 for r in items if r["matched_expectation"]) / len(items), 4),
            "catch_rate": round(len(invalid_caught) / len(invalid_enforceable), 4) if invalid_enforceable else None,
            "false_fail_rate": round(len(type_false_fails) / len(valid), 4) if valid else None,
            "advisory_false_cases": sum(1 for r in items if not r["truth"] and not r["enforceable"]),
        }

    return {
        "schema_version": "anti-slop-agent-claim-benchmark.v0.1",
        "case_count": total,
        "expectation_match_rate": round(matched / total, 4),
        "catch_rate": round(len(caught) / len(enforceable_false), 4),
        "false_fail_rate": round(len(false_fails) / len(true_cases), 4),
        "enforceable_false_cases": len(enforceable_false),
        "caught_enforceable_false_cases": len(caught),
        "advisory_false_cases": len(advisory_false),
        "by_claim_type": by_type,
        "results": results,
    }


def markdown(summary: dict) -> str:
    lines = [
        "# Agent Claim Corpus v0.1 Summary",
        "",
        "This benchmark measures deterministic reference/receipt resolution only.",
        "It does not measure agent quality, correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.",
        "",
        f"- Cases: {summary['case_count']}",
        f"- Expectation match rate: {summary['expectation_match_rate']:.1%}",
        f"- Catch rate over enforceable false cases: {summary['catch_rate']:.1%}",
        f"- False-fail rate over expected-valid cases: {summary['false_fail_rate']:.1%}",
        f"- Advisory false cases not counted as enforceable misses: {summary['advisory_false_cases']}",
        "",
        "## Per-Claim Breakdown",
        "",
        "| Claim type | Cases | Catch rate | False-fail rate | Advisory false cases |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for claim_type, data in summary["by_claim_type"].items():
        catch = "n/a" if data["catch_rate"] is None else f"{data['catch_rate']:.1%}"
        false_fail = "n/a" if data["false_fail_rate"] is None else f"{data['false_fail_rate']:.1%}"
        lines.append(
            f"| {claim_type} | {data['cases']} | {catch} | {false_fail} | {data['advisory_false_cases']} |"
        )
    failures = [r for r in summary["results"] if not r["matched_expectation"]]
    lines.extend(["", "## Expectation Mismatches", ""])
    if failures:
        for failure in failures:
            lines.append(
                f"- {failure['id']}: expected pass={failure['expected_pass']}, got pass={failure['actual_pass']}"
            )
    else:
        lines.append("None.")
    return "\n".join(lines) + "\n"


def main() -> int:
    cases = load_cases()
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        state = setup_fixture(tmp_path)
        artifacts_dir = tmp_path / "artifacts"
        results = [run_case(case, state, artifacts_dir) for case in cases]

    summary = summarize(results)
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (RESULTS / "summary.md").write_text(markdown(summary), encoding="utf-8")

    print(
        "agent-claim corpus v0.1: "
        f"{summary['case_count']} cases, "
        f"catch_rate={summary['catch_rate']:.1%}, "
        f"false_fail_rate={summary['false_fail_rate']:.1%}, "
        f"expectation_match_rate={summary['expectation_match_rate']:.1%}"
    )
    return 0 if all(r["matched_expectation"] for r in summary["results"]) else 1


if __name__ == "__main__":
    sys.exit(main())
