#!/usr/bin/env python3
"""Validate corpus/manifests/acquisition-registry.yaml against books-200.yaml.

Enforces:
- 1:1 correspondence between manifest source_ids and acquisition registry source_ids.
  No missing IDs, no extras.
- rights.raw_text_public_allowed is false for every current entry. Hard rule: any future
  public-domain exception requires an explicit schema/validator change first.
- rights.raw_text_public_allowed is boolean.
- edition_verified is boolean.
- local_source_status.raw_file_path_public is null/blank for every entry.
- processing_status fields are present and boolean (mapped, source_cards_started,
  deep_card_candidate, canon_candidate_exists).
- deep_card_candidate is aligned exactly between source-id-registry.yaml and
  acquisition-registry.yaml. The wave-1 IDs flagged true in the source-id-registry
  must be true in the acquisition registry, AND no acquisition-registry true flags
  appear for IDs not flagged in the source-id-registry.
- Public registry string values do not contain raw/private path or source-file markers
  (/Users/, Desktop, Archive.zip, or blocked file extensions like .epub, .pdf, .mobi,
  .azw, .azw3, .djvu, .cbz, .cbr).

Standard library only. Exits nonzero on failure.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "corpus" / "manifests" / "books-200.yaml"
ACQ_REGISTRY = ROOT / "corpus" / "manifests" / "acquisition-registry.yaml"
ID_REGISTRY = ROOT / "corpus" / "manifests" / "source-id-registry.yaml"

# Markers that must never appear inside acquisition registry string values.
# Catches accidental paste of raw paths or raw filenames.
PRIVATE_PATH_MARKERS = (
    "/Users/",
    "Desktop",
    "Archive.zip",
)
BLOCKED_EXTENSION_RE = re.compile(
    r"\.(epub|pdf|mobi|azw|azw3|djvu|cbz|cbr)\b",
    re.IGNORECASE,
)


def strip_comment(line: str) -> str:
    in_s = in_d = esc = False
    for i, c in enumerate(line):
        if esc:
            esc = False
            continue
        if c == "\\":
            esc = True
            continue
        if c == "'" and not in_d:
            in_s = not in_s
        elif c == '"' and not in_s:
            in_d = not in_d
        elif c == "#" and not in_s and not in_d:
            return line[:i]
    return line


def parse_scalar(v: str):
    v = v.strip()
    if v == "[]":
        return []
    if v in {"", "null", "Null", "NULL", "~"}:
        return None
    if v.lower() == "true":
        return True
    if v.lower() == "false":
        return False
    if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
        return v[1:-1]
    return v


def parse_blocklist(text: str, list_key: str) -> list[dict]:
    """Parse a top-level list-of-dicts whose key is `list_key`, with up to two levels of nesting."""
    items: list[dict] = []
    in_list = False
    cur: dict | None = None
    nested_key: str | None = None
    nested_indent: int | None = None

    for raw in text.splitlines():
        line = strip_comment(raw).rstrip()
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        content = line.strip()

        if not in_list:
            if content.startswith(f"{list_key}:"):
                in_list = True
            continue

        if indent == 0 and not content.startswith("- "):
            break

        if content.startswith("- "):
            if cur is not None:
                items.append(cur)
            cur = {}
            nested_key = None
            nested_indent = None
            rest = content[2:].strip()
            if rest and ":" in rest:
                k, v = rest.split(":", 1)
                k = k.strip()
                v = v.strip()
                if v == "":
                    cur[k] = {}
                    nested_key = k
                    nested_indent = indent
                else:
                    cur[k] = parse_scalar(v)
            continue

        if cur is None:
            continue
        if ":" not in content:
            continue
        k, v = content.split(":", 1)
        k = k.strip()
        v = v.strip()

        if nested_key and nested_indent is not None and indent > nested_indent:
            inner = cur.setdefault(nested_key, {})
            if isinstance(inner, dict):
                inner[k] = parse_scalar(v)
            continue

        if v == "":
            cur[k] = {}
            nested_key = k
            nested_indent = indent
        else:
            cur[k] = parse_scalar(v)
            nested_key = None
            nested_indent = None

    if cur is not None:
        items.append(cur)
    return items


def parse_manifest_ids(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    ids = []
    for raw in text.splitlines():
        line = strip_comment(raw)
        m = re.match(r"\s*-\s*source_id:\s*(\S+)", line)
        if m:
            ids.append(m.group(1))
    return ids


def _walk_strings(value, prefix: str = ""):
    """Yield (field_path, string_value) pairs for every string leaf in a parsed entry."""
    if isinstance(value, dict):
        for k, v in value.items():
            child = f"{prefix}.{k}" if prefix else k
            yield from _walk_strings(v, child)
    elif isinstance(value, list):
        for i, v in enumerate(value):
            child = f"{prefix}[{i}]"
            yield from _walk_strings(v, child)
    elif isinstance(value, str):
        yield (prefix, value)


def parse_id_registry_deep_card_ids(path: Path) -> set[str]:
    """Return the set of source_ids with deep_card_candidate=true in the wave-1 registry."""
    text = path.read_text(encoding="utf-8")
    result: set[str] = set()
    current: str | None = None
    for raw in text.splitlines():
        line = strip_comment(raw)
        m = re.match(r"\s*-\s*source_id:\s*(\S+)", line)
        if m:
            current = m.group(1)
            continue
        m = re.match(r"\s*deep_card_candidate:\s*(\S+)", line)
        if m and current is not None:
            if parse_scalar(m.group(1)) is True:
                result.add(current)
            current = None
    return result


def main() -> int:
    errors: list[str] = []

    if not MANIFEST.exists():
        print(f"Missing manifest: {MANIFEST}")
        return 1
    if not ACQ_REGISTRY.exists():
        print(f"Missing acquisition registry: {ACQ_REGISTRY}")
        return 1

    manifest_ids = parse_manifest_ids(MANIFEST)
    manifest_set = set(manifest_ids)
    if len(manifest_set) != len(manifest_ids):
        errors.append("manifest contains duplicate source_ids")

    acq_text = ACQ_REGISTRY.read_text(encoding="utf-8")
    entries = parse_blocklist(acq_text, "entries")
    acq_ids = [e.get("source_id") for e in entries if e.get("source_id")]
    acq_set = set(acq_ids)

    if len(acq_set) != len(acq_ids):
        errors.append("acquisition registry contains duplicate source_ids")

    missing = manifest_set - acq_set
    extra = acq_set - manifest_set
    if missing:
        errors.append(f"manifest source_ids missing from acquisition registry: {sorted(missing)}")
    if extra:
        errors.append(f"acquisition registry source_ids not in manifest: {sorted(extra)}")

    for entry in entries:
        sid = entry.get("source_id", "(unknown)")
        local = entry.get("local_source_status")
        if isinstance(local, dict):
            rfpp = local.get("raw_file_path_public")
            if rfpp not in (None, ""):
                errors.append(f"{sid}: raw_file_path_public must be null/blank (got {rfpp!r})")
        else:
            errors.append(f"{sid}: local_source_status missing or malformed")

        rights = entry.get("rights")
        if not isinstance(rights, dict):
            errors.append(f"{sid}: rights block missing or malformed")
        else:
            allowed = rights.get("raw_text_public_allowed")
            if not isinstance(allowed, bool):
                errors.append(f"{sid}: rights.raw_text_public_allowed must be boolean (got {allowed!r})")
            elif allowed is True:
                errors.append(
                    f"{sid}: rights.raw_text_public_allowed must be false for every current entry. "
                    f"A public-domain exception requires an explicit schema/validator change first."
                )

        ev = entry.get("edition_verified")
        if not isinstance(ev, bool):
            errors.append(f"{sid}: edition_verified must be boolean (got {ev!r})")

        proc = entry.get("processing_status")
        if not isinstance(proc, dict):
            errors.append(f"{sid}: processing_status block missing")
        else:
            for key in ("mapped", "source_cards_started", "deep_card_candidate", "canon_candidate_exists"):
                if key not in proc:
                    errors.append(f"{sid}: processing_status.{key} missing")
                elif not isinstance(proc[key], bool):
                    errors.append(f"{sid}: processing_status.{key} must be boolean (got {proc[key]!r})")

    # Deep-card alignment: exact match between source-id-registry and acquisition registry.
    # No missing true flags and no extra true flags.
    if ID_REGISTRY.exists():
        wave1_dc = parse_id_registry_deep_card_ids(ID_REGISTRY)
        acq_dc = {e["source_id"] for e in entries
                  if isinstance(e.get("processing_status"), dict)
                  and e["processing_status"].get("deep_card_candidate") is True}
        missing = wave1_dc - acq_dc
        extra = acq_dc - wave1_dc
        if missing:
            errors.append(
                f"deep-card-candidate misalignment: source-id-registry has true for {sorted(missing)} "
                f"but acquisition registry does not"
            )
        if extra:
            errors.append(
                f"deep-card-candidate misalignment: acquisition registry has true for {sorted(extra)} "
                f"but source-id-registry does not"
            )

    # Private-path / raw-extension scan over all string values in every entry.
    for entry in entries:
        sid = entry.get("source_id", "(unknown)")
        for field_path, value in _walk_strings(entry):
            for marker in PRIVATE_PATH_MARKERS:
                if marker in value:
                    errors.append(
                        f"{sid}: {field_path} contains private-path marker '{marker}': {value!r}"
                    )
            m = BLOCKED_EXTENSION_RE.search(value)
            if m:
                errors.append(
                    f"{sid}: {field_path} contains raw-source extension '{m.group(0)}': {value!r}"
                )

    print(f"Manifest: {MANIFEST.relative_to(ROOT)}")
    print(f"Acquisition registry: {ACQ_REGISTRY.relative_to(ROOT)}")
    print(f"Manifest source_ids: {len(manifest_ids)}")
    print(f"Acquisition registry entries: {len(acq_ids)}")

    if errors:
        print("Acquisition registry validation FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("Acquisition registry validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
