#!/usr/bin/env python3
"""anti-slop-run: run a local command and write a deterministic receipt.

The receipt is a local fact record for agent claim verification. It records the
command, cwd, exit code, duration, git head, timestamp, stdout/stderr hashes,
tool version, and optional bounded excerpts/metrics. It does not judge whether
the command proves correctness, relevance, support, safety, or advice quality.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import shlex
import subprocess
import sys
import tempfile
import time

TOOL_VERSION = "0.1.0"
SCHEMA_VERSION = "anti-slop-command-receipt.v1"
METRIC_RE = re.compile(r"^[A-Za-z_][\w.-]*=.+$")


def _git_head(cwd: Path) -> str | None:
    try:
        proc = subprocess.run(
            ["git", "-C", str(cwd), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
        )
    except OSError:
        return None
    if proc.returncode != 0:
        return None
    return proc.stdout.strip() or None


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _json_value(raw: str) -> object:
    if re.fullmatch(r"-?\d+", raw):
        return int(raw)
    if re.fullmatch(r"-?\d+\.\d+", raw):
        return float(raw)
    return raw


def _parse_metrics(items: list[str] | None) -> dict:
    metrics: dict[str, object] = {}
    for item in items or []:
        if not METRIC_RE.match(item):
            raise ValueError(f"invalid --metric {item!r}; expected name=value")
        name, value = item.split("=", 1)
        metrics[name] = _json_value(value)
    return metrics


def _infer_tags(command: list[str]) -> list[str]:
    tags: set[str] = set()
    if not command:
        return []
    cmd_string = shlex.join(command)
    lower_tokens = [Path(t).name.lower() for t in command]
    lower_string = cmd_string.lower()
    if command[0] == "make" and len(command) > 1:
        tags.add(f"make:{command[1]}")
    if "pytest" in lower_tokens or "pytest" in lower_string:
        tags.update({"pytest", "tests"})
    if re.search(r"\btest(s|ing)?\b", lower_string):
        tags.add("tests")
    return sorted(tags)


def _excerpt(data: bytes, limit: int) -> tuple[str | None, bool]:
    if limit <= 0:
        return None, False
    clipped = data[:limit]
    return clipped.decode("utf-8", errors="replace"), len(data) > limit


def _receipt_path(receipts_dir: Path, started: datetime, command: list[str]) -> Path:
    stem = started.strftime("%Y%m%dT%H%M%SZ")
    digest = hashlib.sha256(shlex.join(command).encode("utf-8")).hexdigest()[:10]
    return receipts_dir / f"command-{stem}-{os.getpid()}-{digest}.json"


def run_and_write(command: list[str], cwd: Path, receipts_dir: Path,
                  metrics: dict, excerpt_bytes: int) -> tuple[int, Path]:
    started = datetime.now(timezone.utc)
    start = time.perf_counter()
    stdout = b""
    stderr = b""
    try:
        proc = subprocess.run(command, cwd=str(cwd), capture_output=True)
        exit_code = proc.returncode
        stdout = proc.stdout
        stderr = proc.stderr
    except OSError as exc:
        exit_code = 127
        stderr = f"{exc}\n".encode("utf-8", errors="replace")
    duration_ms = int(round((time.perf_counter() - start) * 1000))

    if stdout:
        sys.stdout.buffer.write(stdout)
        sys.stdout.buffer.flush()
    if stderr:
        sys.stderr.buffer.write(stderr)
        sys.stderr.buffer.flush()

    out_excerpt, out_truncated = _excerpt(stdout, excerpt_bytes)
    err_excerpt, err_truncated = _excerpt(stderr, excerpt_bytes)
    receipt = {
        "schema_version": SCHEMA_VERSION,
        "receipt_type": "command",
        "command": command,
        "command_string": shlex.join(command),
        "command_tags": _infer_tags(command),
        "cwd": str(cwd.resolve()),
        "exit_code": exit_code,
        "duration_ms": duration_ms,
        "git_head": _git_head(cwd),
        "started_at": started.replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "stdout_sha256": _sha256(stdout),
        "stderr_sha256": _sha256(stderr),
        "stdout_bytes": len(stdout),
        "stderr_bytes": len(stderr),
        "tool_version": TOOL_VERSION,
        "metrics": metrics,
    }
    if out_excerpt is not None:
        receipt["stdout_excerpt"] = out_excerpt
        receipt["stdout_excerpt_bytes"] = min(len(stdout), excerpt_bytes)
        receipt["stdout_excerpt_truncated"] = out_truncated
    if err_excerpt is not None:
        receipt["stderr_excerpt"] = err_excerpt
        receipt["stderr_excerpt_bytes"] = min(len(stderr), excerpt_bytes)
        receipt["stderr_excerpt_truncated"] = err_truncated

    receipts_dir.mkdir(parents=True, exist_ok=True)
    path = _receipt_path(receipts_dir, started, command)
    path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"anti-slop-run receipt: {path}")
    return exit_code, path


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cwd", type=Path,
                        help="working directory for the command (default: current directory)")
    parser.add_argument("--receipts-dir", type=Path, default=Path(".anti-slop/receipts"),
                        help="directory for JSON receipts (default: .anti-slop/receipts under cwd)")
    parser.add_argument("--metric", action="append",
                        help="record a numeric/string metric as name=value; repeatable")
    parser.add_argument("--excerpt-bytes", type=int, default=0,
                        help="store bounded stdout/stderr excerpts; default 0 stores hashes only")
    parser.add_argument("--self-test", action="store_true",
                        help="run the deterministic anti-slop-run self-test")
    parser.add_argument("command", nargs=argparse.REMAINDER,
                        help="command to run after --")
    return parser.parse_args(argv)


def self_test() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        subprocess.run(["git", "-C", str(root), "init"], capture_output=True, check=True)
        subprocess.run(["git", "-C", str(root), "config", "user.email", "test@example.invalid"],
                       capture_output=True, check=True)
        subprocess.run(["git", "-C", str(root), "config", "user.name", "Anti Slop Test"],
                       capture_output=True, check=True)
        (root / "README.md").write_text("# Fixture\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(root), "add", "."], capture_output=True, check=True)
        subprocess.run(["git", "-C", str(root), "commit", "-m", "base"],
                       capture_output=True, check=True)

        ok_dir = root / "ok-receipts"
        bad_dir = root / "bad-receipts"
        metric_dir = root / "metric-receipts"
        ok = main(["--cwd", str(root), "--receipts-dir", str(ok_dir), "--",
                   sys.executable, "-c", "print('ok')"])
        bad = main(["--cwd", str(root), "--receipts-dir", str(bad_dir), "--",
                    sys.executable, "-c", "import sys; print('bad'); sys.exit(7)"])
        metric = main(["--cwd", str(root), "--receipts-dir", str(metric_dir),
                       "--metric", "score=0.82", "--",
                       sys.executable, "-c", "print('metric')"])

        ok_receipts = list(ok_dir.glob("*.json"))
        bad_receipts = list(bad_dir.glob("*.json"))
        metric_receipts = list(metric_dir.glob("*.json"))
        ok_data = json.loads(ok_receipts[0].read_text(encoding="utf-8")) if ok_receipts else {}
        bad_data = json.loads(bad_receipts[0].read_text(encoding="utf-8")) if bad_receipts else {}
        metric_data = json.loads(metric_receipts[0].read_text(encoding="utf-8")) if metric_receipts else {}
        checks = [
            ("exit 0 command returns 0", ok == 0),
            ("exit 0 receipt written", ok_data.get("exit_code") == 0),
            ("stdout hash recorded by default", bool(ok_data.get("stdout_sha256"))),
            ("stdout excerpt omitted by default", "stdout_excerpt" not in ok_data),
            ("nonzero command returns command code", bad == 7),
            ("nonzero receipt still written", bad_data.get("exit_code") == 7),
            ("metric recorded on command receipt", metric == 0 and metric_data.get("metrics", {}).get("score") == 0.82),
        ]
        failed = [name for name, passed in checks if not passed]
        if failed:
            print("anti-slop-run self-test FAILED:")
            for name in failed:
                print(f"  - {name}")
            return 1
    print("anti-slop-run self-test passed (exit 0 and nonzero commands write hashed receipts; metrics supported).")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.self_test:
        return self_test()
    command = list(args.command)
    if command and command[0] == "--":
        command = command[1:]
    if not command:
        print("Usage: anti-slop-run [--cwd DIR] [--receipts-dir DIR] [--metric name=value] -- <command>")
        return 2
    if args.excerpt_bytes < 0:
        print("--excerpt-bytes must be >= 0")
        return 2
    cwd = (args.cwd or Path.cwd()).resolve()
    if not cwd.is_dir():
        print(f"Missing cwd: {cwd}")
        return 2
    receipts_dir = args.receipts_dir
    if not receipts_dir.is_absolute():
        receipts_dir = cwd / receipts_dir
    try:
        metrics = _parse_metrics(args.metric)
    except ValueError as exc:
        print(str(exc))
        return 2
    exit_code, _ = run_and_write(command, cwd, receipts_dir, metrics, args.excerpt_bytes)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
