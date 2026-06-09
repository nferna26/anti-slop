# Citation-Lineage MCP — deferred (and why)

**Status: deferred, documented.** No MCP server is added in this tranche. This
note records the decision and a thin, dependency-free local sketch so it can be
picked up later under the same narrow, deterministic contract.

## Decision

An MCP wrapper around the deterministic citation-lineage gate is **deferred**,
not implemented, for three concrete reasons:

1. **It would add a runtime + a non-stdlib dependency.** A real MCP server needs
   the `mcp` Python SDK and runs a long-lived stdio/socket server process. The
   CLI is stdlib-only with no network/model/API; an MCP server is the first thing
   in this repo that would not be. `AGENTS.md` is explicit: *"Do not introduce
   model or API integrations. This repo is an inspectable substrate, not a
   runtime."* The packaging tranche's constraints likewise forbid hosted
   services / runtime / advisory agents and ask for stdlib-only unless
   unavoidable.
2. **It adds transport, not capability.** The deterministic value — does a cited
   ID resolve to reviewed lineage — is already fully delivered by
   `gate_citation_lineage.py` / the `anti-slop-lineage` CLI and by the importable
   `build_index` + `check_paths` functions. An MCP tool would only re-expose that
   over a wire protocol. There is no model, RAG, vector store, or advisor
   behaviour to add, so the server would be pure plumbing.
3. **No concrete local consumer yet.** Nothing in the repo currently drives the
   gate over MCP. Adding a server before there is a caller is speculative
   runtime work (`CLAUDE.md` §8: minimum artifact).

If a concrete local agent later needs the gate over MCP, the wrapper must stay
**thin, local, and deterministic**: it wraps the existing functions, calls no
model/API/network, ships no corpus (the caller passes `root`), and is labelled
experimental / local-only. It must never become an advisor or promote canon.

## Thin deterministic core (dependency-free, ready today)

The gate already exposes everything a wrapper needs. This helper is pure stdlib
and calls only the existing resolver — no behaviour fork:

```python
# audit_citations: deterministic, no model/network. Wraps the EXISTING gate.
from pathlib import Path
from gate_citation_lineage import build_index, check_paths

def audit_citations(paths, root, require_reviewed=False):
    index = build_index(Path(root))
    findings, ref_count = check_paths(
        [Path(p).resolve() for p in paths], index, require_reviewed=require_reviewed
    )
    return {
        "root": str(index.root),
        "mode": "existence+reviewed" if require_reviewed else "existence",
        "files_checked": len(paths),
        "references_checked": ref_count,
        "passed": not findings,
        "findings": findings,   # list of "path:line: unresolved ... : <ref>"
    }
```

## MCP wrapper sketch (experimental / local-only — NOT added here)

For reference only. Adding this would introduce the `mcp` dependency and a server
runtime, which is why it is deferred:

```python
# DEFERRED — do not commit as a runtime. Requires the `mcp` SDK (non-stdlib).
# from mcp.server.fastmcp import FastMCP
# srv = FastMCP("anti-slop-lineage")            # local stdio server
#
# @srv.tool()
# def audit_citations_tool(paths: list[str], root: str,
#                          require_reviewed: bool = False) -> dict:
#     """Deterministic citation-lineage audit. No model, no network, no corpus
#     shipped — the caller supplies `root`. Returns resolve/findings only."""
#     return audit_citations(paths, root, require_reviewed)
#
# if __name__ == "__main__":
#     srv.run()   # local-only; never a hosted service
```

A future `compile_brief` or `lint_universalization` tool could be added the same
way (each wrapping the existing function), but `lint_universalization` is
**heuristic/advisory**, not benchmark-backed, and must be labelled as such — see
the gate tiers in [citation-lineage-gate.md](citation-lineage-gate.md).
