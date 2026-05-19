#!/usr/bin/env python3
"""Validate the public 200-book manifest with standard-library Python only."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "corpus" / "manifests" / "books-200.yaml"
ACQUISITION_STATUSES = ROOT / "corpus" / "manifests" / "acquisition-statuses.yaml"
PUBLICATION_STATUSES = ROOT / "corpus" / "manifests" / "publication-statuses.yaml"

REQUIRED_FIELDS = [
    "source_id",
    "category",
    "author",
    "title",
    "status_tag",
    "availability_tier",
    "acquisition_status",
    "publication_status",
    "raw_source_status",
    "eval_relevance",
    "rationale",
]

EVAL_KEYS = [
    "bibliographic_adversary",
    "contradiction_preservation",
    "canon_promotion_tournament",
    "long_tail_transfer",
    "source_lineage_hostile",
]

CATEGORIES = {
    "cognition",
    "decision_quality",
    "epistemology",
    "evidence",
    "rhetoric",
    "media",
    "systems",
    "institutions",
    "governance",
    "strategy",
    "operations",
    "management",
    "product",
    "design",
    "technology",
    "economics",
    "psychology",
    "sociology",
    "anthropology",
    "philosophy",
    "history",
    "science",
    "writing",
    "education",
    "risk",
    "safety",
    "ethics",
    "law_policy",
    "biography",
    "other",
}

STATUS_TAGS = {"COMMITTED", "NEW", "RESTORED"}
AVAILABILITY_TIERS = {"MM", "AP", "UB", "PD"}
RAW_SOURCE_STATUSES = {
    "not_acquired",
    "local_only",
    "unavailable",
    "public_domain",
    "metadata_only",
}


class ManifestError(Exception):
    """Raised when the manifest cannot be parsed by the local lightweight parser."""


def strip_comment(line: str) -> str:
    in_single = False
    in_double = False
    escaped = False
    for index, char in enumerate(line):
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == "'" and not in_double:
            in_single = not in_single
        elif char == '"' and not in_single:
            in_double = not in_double
        elif char == "#" and not in_single and not in_double:
            return line[:index]
    return line


def parse_scalar(value: str):
    value = value.strip()
    if value == "[]":
        return []
    if value in {"", "null", "Null", "NULL", "~"}:
        return ""
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def set_key(target: dict, content: str) -> tuple[str | None, int | None]:
    if ":" not in content:
        raise ManifestError(f"Expected key/value pair, got: {content}")
    key, value = content.split(":", 1)
    key = key.strip()
    value = value.strip()
    if not key:
        raise ManifestError(f"Empty key in line: {content}")
    if value == "":
        target[key] = {}
        return key, None
    target[key] = parse_scalar(value)
    return None, None


def parse_books_manifest(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    books: list[dict] = []
    in_books = False
    current: dict | None = None
    nested_key: str | None = None
    nested_indent: int | None = None

    for raw_line in text.splitlines():
        line = strip_comment(raw_line).rstrip()
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        content = line.strip()

        if not in_books:
            if content.startswith("books:"):
                in_books = True
                value = content[len("books:") :].strip()
                if value == "[]":
                    return []
                if value:
                    raise ManifestError("Use block-list form for non-empty books.")
            continue

        if indent == 0 and not content.startswith("- "):
            break

        if content.startswith("- "):
            if current is not None:
                books.append(current)
            current = {}
            nested_key = None
            nested_indent = None
            rest = content[2:].strip()
            if rest:
                nested_key, _ = set_key(current, rest)
                nested_indent = indent if nested_key else None
            continue

        if current is None:
            raise ManifestError("Found book field before first list item.")

        if ":" not in content:
            raise ManifestError(f"Expected key/value pair, got: {content}")

        key, value = content.split(":", 1)
        key = key.strip()
        value = value.strip()

        if nested_key and nested_indent is not None and indent > nested_indent:
            nested = current.setdefault(nested_key, {})
            if not isinstance(nested, dict):
                raise ManifestError(f"Nested field collision at {nested_key}")
            nested[key] = parse_scalar(value)
            continue

        if value == "":
            current[key] = {}
            nested_key = key
            nested_indent = indent
        else:
            current[key] = parse_scalar(value)
            nested_key = None
            nested_indent = None

    if current is not None:
        books.append(current)

    return books


def load_status_values(path: Path) -> set[str]:
    values: set[str] = set()
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = strip_comment(raw_line).strip()
        if line.startswith("- "):
            values.add(str(parse_scalar(line[2:].strip())))
    return values


def is_missing(value) -> bool:
    return value is None or value == "" or value == {}


def main() -> int:
    if not MANIFEST.exists():
        print(f"Missing manifest: {MANIFEST}")
        return 1

    try:
        books = parse_books_manifest(MANIFEST)
    except ManifestError as exc:
        print(f"Manifest parse error: {exc}")
        return 1

    acquisition_statuses = load_status_values(ACQUISITION_STATUSES)
    publication_statuses = load_status_values(PUBLICATION_STATUSES)

    errors: list[str] = []
    source_ids: set[str] = set()
    category_counts: Counter[str] = Counter()
    tier_counts: Counter[str] = Counter()

    for index, book in enumerate(books, start=1):
        label = book.get("source_id") or f"book #{index}"
        for field in REQUIRED_FIELDS:
            if is_missing(book.get(field)):
                errors.append(f"{label}: missing required field `{field}`")

        source_id = book.get("source_id")
        if source_id:
            if source_id in source_ids:
                errors.append(f"{label}: duplicate source_id `{source_id}`")
            source_ids.add(source_id)

        category = book.get("category")
        if category:
            category_counts[str(category)] += 1
            if category not in CATEGORIES:
                errors.append(f"{label}: invalid category `{category}`")

        tier = book.get("availability_tier")
        if tier:
            tier_counts[str(tier)] += 1
            if tier not in AVAILABILITY_TIERS:
                errors.append(f"{label}: invalid availability_tier `{tier}`")

        status_tag = book.get("status_tag")
        if status_tag and status_tag not in STATUS_TAGS:
            errors.append(f"{label}: invalid status_tag `{status_tag}`")

        acquisition_status = book.get("acquisition_status")
        if acquisition_status and acquisition_status not in acquisition_statuses:
            errors.append(f"{label}: invalid acquisition_status `{acquisition_status}`")

        publication_status = book.get("publication_status")
        if publication_status and publication_status not in publication_statuses:
            errors.append(f"{label}: invalid publication_status `{publication_status}`")

        raw_source_status = book.get("raw_source_status")
        if raw_source_status and raw_source_status not in RAW_SOURCE_STATUSES:
            errors.append(f"{label}: invalid raw_source_status `{raw_source_status}`")

        eval_relevance = book.get("eval_relevance")
        if isinstance(eval_relevance, dict):
            for key in EVAL_KEYS:
                value = eval_relevance.get(key)
                if value is None:
                    errors.append(f"{label}: missing eval_relevance.{key}")
                elif not isinstance(value, bool):
                    errors.append(f"{label}: eval_relevance.{key} must be boolean")
        elif eval_relevance:
            errors.append(f"{label}: eval_relevance must be a mapping")

    print(f"Manifest: {MANIFEST.relative_to(ROOT)}")
    print(f"Books: {len(books)}")

    print("Count by category:")
    if category_counts:
        for category, count in sorted(category_counts.items()):
            print(f"  {category}: {count}")
    else:
        print("  none")

    print("Count by availability tier:")
    if tier_counts:
        for tier, count in sorted(tier_counts.items()):
            print(f"  {tier}: {count}")
    else:
        print("  none")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
