#!/bin/sh
set -eu

BASE_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
WORK_DIR="$BASE_DIR/build/work"
OUT_DIR="$BASE_DIR/build/output"
UPSTREAM_URL="https://github.com/PasarGuard/subscription-template/releases/download/v2.2.0/en.html"
SRC_HTML="$WORK_DIR/en.html"
OUT_HTML="$OUT_DIR/index.html"

rm -rf "$WORK_DIR" "$OUT_DIR"
mkdir -p "$WORK_DIR" "$OUT_DIR"

curl -L --retry 3 --retry-delay 2 "$UPSTREAM_URL" -o "$SRC_HTML"
python3 "$BASE_DIR/scripts/patch-release-asset.py" "$SRC_HTML" "$OUT_HTML"

printf 'Built English artifact: %s\n' "$OUT_HTML"
printf 'Upstream asset: %s\n' "$UPSTREAM_URL"
