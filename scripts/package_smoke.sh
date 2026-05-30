#!/usr/bin/env bash
# Package smoke for the deterministic citation-lineage CLI.
#
# Installs the anti-slop-lineage package into a throwaway isolated venv, then
# proves the INSTALLED console command behaves exactly like the in-tree gate:
#   1. anti-slop-lineage --self-test                       -> exit 0
#   2. CLI audit of the holdout brief-assisted note         -> exit 0 (PASS)
#      (--root <packet> --require-reviewed)
#   3. CLI audit of the holdout source-free note            -> exit 1 (FAIL)
#      (--root <packet> --require-reviewed)
#
# Deterministic, offline: no network, no model, no API. The venv is created with
# --system-site-packages so the build backend (setuptools) is found locally, and
# pip runs with --no-build-isolation so nothing is fetched. The venv is removed
# on exit. Rerun: `make package-smoke` or `bash scripts/package_smoke.sh`.

set -u

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PACKET="$REPO/runs/holdout-transfer-smoke/v1-citation-lineage-naturalist-holdout-2026-05-29"
GOOD="$PACKET/outputs/brief-assisted-note.md"
SLOP="$PACKET/outputs/source-free-note.md"

VENV="$(mktemp -d -t anti-slop-lineage-smoke-XXXXXX)/venv"
LOG="$(dirname "$VENV")/install.log"
# Clean up the transient venv AND the in-tree build artifacts `pip install .`
# leaves behind (build/, *.egg-info/), so reruns leave the checkout pristine.
# These are also gitignored.
cleanup() {
  rm -rf "$(dirname "$VENV")"
  rm -rf "$REPO/build" "$REPO/scripts/anti_slop_lineage.egg-info"
}
trap cleanup EXIT

echo "== anti-slop-lineage package smoke =="
echo "Repo:   $REPO"
echo "Venv:   $VENV (transient)"

# --system-site-packages so the offline fallback can see system setuptools.
python3 -m venv --system-site-packages "$VENV" || { echo "FAIL: venv creation"; exit 1; }
BIN="$VENV/bin"
# Prefer a normal isolated install (works online / in CI, where pip fetches the
# build backend); fall back to --no-build-isolation for offline/local runs that
# reuse the system setuptools. Either way the asserted CLI behaviour is the same.
echo "[install] pip install (isolated; falls back to --no-build-isolation offline) ..."
if ! "$BIN/python" -m pip install --quiet "$REPO" >"$LOG" 2>&1; then
  if ! "$BIN/python" -m pip install --no-build-isolation --quiet "$REPO" >>"$LOG" 2>&1; then
    echo "FAIL: package install (isolated and offline fallback both failed). Last lines:"
    tail -20 "$LOG"
    exit 1
  fi
fi

CLI="$BIN/anti-slop-lineage"
[ -x "$CLI" ] || { echo "FAIL: console script not installed at $CLI"; exit 1; }

# 1. installed self-test
"$CLI" --self-test >/dev/null 2>&1; st=$?
# 2. brief-assisted note -> PASS (exit 0)
"$CLI" --root "$PACKET" --require-reviewed "$GOOD" >/dev/null 2>&1; good=$?
# 3. source-free note -> FAIL (exit 1)
"$CLI" --root "$PACKET" --require-reviewed "$SLOP" >/dev/null 2>&1; slop=$?

echo "[1/3] installed --self-test                 -> exit $st   (expect 0)"
echo "[2/3] CLI audit brief-assisted (--root)      -> exit $good (expect 0 / PASS)"
echo "[3/3] CLI audit source-free   (--root)       -> exit $slop (expect 1 / FAIL)"

if [ "$st" -eq 0 ] && [ "$good" -eq 0 ] && [ "$slop" -eq 1 ]; then
  echo "PACKAGE SMOKE PASSED: installed CLI self-tests and audits the holdout fixture identically to the in-tree gate."
  exit 0
fi
echo "PACKAGE SMOKE FAILED (self-test=$st good=$good slop=$slop)."
exit 1
