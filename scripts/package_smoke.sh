#!/usr/bin/env bash
# Package smoke for the deterministic Anti-Slop CLIs.
#
# Installs the anti-slop-lineage package into a throwaway isolated venv, then
# proves the INSTALLED console commands behave exactly like the in-tree gates:
#   1. anti-slop-lineage --self-test                       -> exit 0
#   2. CLI audit of the holdout brief-assisted note         -> exit 0 (PASS)
#      (--root <packet> --require-reviewed)
#   3. CLI audit of the holdout source-free note            -> exit 1 (FAIL)
#      (--root <packet> --require-reviewed)
#   4. anti-slop-pr --self-test                             -> exit 0
#   5. anti-slop-pr-event --self-test                       -> exit 0
#   6. anti-slop-claims --self-test                         -> exit 0
#   7. generic AGENT_FINAL_REPORT valid fixture             -> exit 0 (PASS)
#   8. generic AGENT_FINAL_REPORT fabricated fixture        -> exit 1 (FAIL)
#
# Deterministic in behaviour (the asserted CLI outcomes are fixed); no model, no
# API, no credentials. Install prefers a normal isolated `pip install` (which may
# fetch the build backend from the package index over the network); it falls back
# to --no-build-isolation against the system setuptools for offline/local runs.
# The venv is created with --system-site-packages so that offline fallback can
# see the system setuptools. The venv is removed on exit. Rerun:
# `make package-smoke` or `bash scripts/package_smoke.sh`.

set -u

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PACKET="$REPO/runs/holdout-transfer-smoke/v1-citation-lineage-naturalist-holdout-2026-05-29"
GOOD="$PACKET/outputs/brief-assisted-note.md"
SLOP="$PACKET/outputs/source-free-note.md"
CLAIMS_ROOT="$REPO/proof/claims-demo/fixture-root"
CLAIMS_GOOD="$REPO/proof/claims-demo/valid/AGENT_FINAL_REPORT.md"
CLAIMS_BAD="$REPO/proof/claims-demo/fabricated/AGENT_FINAL_REPORT.md"

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

echo "== Anti-Slop package smoke =="
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
PRCLI="$BIN/anti-slop-pr"
[ -x "$PRCLI" ] || { echo "FAIL: console script not installed at $PRCLI"; exit 1; }
EVCLI="$BIN/anti-slop-pr-event"
[ -x "$EVCLI" ] || { echo "FAIL: console script not installed at $EVCLI"; exit 1; }
CLAIMSCLI="$BIN/anti-slop-claims"
[ -x "$CLAIMSCLI" ] || { echo "FAIL: console script not installed at $CLAIMSCLI"; exit 1; }

# 1. installed anti-slop-lineage self-test
"$CLI" --self-test >/dev/null 2>&1; st=$?
# 2. brief-assisted note -> PASS (exit 0)
"$CLI" --root "$PACKET" --require-reviewed "$GOOD" >/dev/null 2>&1; good=$?
# 3. source-free note -> FAIL (exit 1)
"$CLI" --root "$PACKET" --require-reviewed "$SLOP" >/dev/null 2>&1; slop=$?
# 4. installed anti-slop-pr self-test
"$PRCLI" --self-test >/dev/null 2>&1; prst=$?
# 5. installed anti-slop-pr-event (GitHub Actions wrapper) self-test
"$EVCLI" --self-test >/dev/null 2>&1; evst=$?
# 6. installed anti-slop-claims generic-artifact self-test
"$CLAIMSCLI" --self-test >/dev/null 2>&1; claimst=$?
# 7. generic final-report fixture: valid file ref -> PASS
"$CLAIMSCLI" --root "$CLAIMS_ROOT" "$CLAIMS_GOOD" >/dev/null 2>&1; claimsgood=$?
# 8. generic final-report fixture: fabricated file ref -> FAIL
"$CLAIMSCLI" --root "$CLAIMS_ROOT" "$CLAIMS_BAD" >/dev/null 2>&1; claimsbad=$?

echo "[1/8] installed anti-slop-lineage --self-test  -> exit $st   (expect 0)"
echo "[2/8] CLI audit brief-assisted (--root)        -> exit $good (expect 0 / PASS)"
echo "[3/8] CLI audit source-free   (--root)         -> exit $slop (expect 1 / FAIL)"
echo "[4/8] installed anti-slop-pr --self-test        -> exit $prst (expect 0)"
echo "[5/8] installed anti-slop-pr-event --self-test  -> exit $evst (expect 0)"
echo "[6/8] installed anti-slop-claims --self-test    -> exit $claimst (expect 0)"
echo "[7/8] claims valid AGENT_FINAL_REPORT          -> exit $claimsgood (expect 0 / PASS)"
echo "[8/8] claims fabricated AGENT_FINAL_REPORT     -> exit $claimsbad (expect 1 / FAIL)"

if [ "$st" -eq 0 ] && [ "$good" -eq 0 ] && [ "$slop" -eq 1 ] \
   && [ "$prst" -eq 0 ] && [ "$evst" -eq 0 ] && [ "$claimst" -eq 0 ] \
   && [ "$claimsgood" -eq 0 ] && [ "$claimsbad" -eq 1 ]; then
  echo "PACKAGE SMOKE PASSED: installed anti-slop-lineage + anti-slop-pr + anti-slop-pr-event + anti-slop-claims self-test and audit the fixtures identically to the in-tree gates."
  exit 0
fi
echo "PACKAGE SMOKE FAILED (lineage=$st good=$good slop=$slop pr=$prst event=$evst claims=$claimst claims_good=$claimsgood claims_bad=$claimsbad)."
exit 1
