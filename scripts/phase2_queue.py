#!/usr/bin/env python3
"""Print the Phase 2 verification queue in a non-engineer-readable format."""

from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "corpus" / "manifests" / "phase-2-verification-queue.yaml"


def strip_quotes(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    return value


def read_queue(path: Path) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    batch: list[dict[str, str]] = []
    watchlist: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    section: str | None = None

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        content = line.strip()
        indent = len(line) - len(line.lstrip(" "))
        if not content or content.startswith("#"):
            continue
        if content == "verification_batch:":
            section = "batch"
            current = None
            continue
        if content == "rights_watchlist:":
            if current and section == "batch":
                batch.append(current)
            section = "watchlist"
            current = None
            continue
        if indent == 0 and re.match(r"^[a-z_]+:", content) and not content.startswith("- "):
            if current and section == "batch":
                batch.append(current)
            elif current and section == "watchlist":
                watchlist.append(current)
            current = None
            section = None
            continue
        if section not in {"batch", "watchlist"}:
            continue
        if content.startswith("- "):
            if current and section == "batch":
                batch.append(current)
            elif current and section == "watchlist":
                watchlist.append(current)
            current = {}
            rest = content[2:].strip()
            if ":" in rest:
                key, value = rest.split(":", 1)
                current[key.strip()] = strip_quotes(value)
            continue
        if current is not None and ":" in content:
            key, value = content.split(":", 1)
            current[key.strip()] = strip_quotes(value)

    if current and section == "batch":
        batch.append(current)
    elif current and section == "watchlist":
        watchlist.append(current)

    return batch, watchlist


def main() -> int:
    if not QUEUE.exists():
        print(f"Missing queue: {QUEUE.relative_to(ROOT)}")
        return 1

    batch, watchlist = read_queue(QUEUE)

    print("== Phase 2 verification queue ==")
    for item in batch:
        print(
            f"{item.get('queue_rank', '?')}. {item.get('source_id', '')} — "
            f"{item.get('title', '')} ({item.get('author', '')})"
        )
        print(f"   Why: {item.get('reason', '')}")
        print(f"   Next: {item.get('next_operator_action', '')}")
    print()

    print("== Rights/access watchlist ==")
    for item in watchlist:
        print(f"- {item.get('source_id', '')} — {item.get('title', '')}: {item.get('reason', '')}")

    print()
    print("Rule: no raw book text, raw paths, or raw filenames in the public repo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
