#!/usr/bin/env bash
set -euo pipefail

SOURCE="source/specification-grammar.svg"
OUT="exports"

if [[ ! -f "$SOURCE" ]]; then
  echo "Missing $SOURCE"
  exit 1
fi

mkdir -p "$OUT"

if command -v inkscape >/dev/null 2>&1; then
  inkscape "$SOURCE" --export-type=png --export-width=3200 --export-filename="$OUT/specification-grammar.png"
  inkscape "$SOURCE" --export-type=pdf --export-filename="$OUT/specification-grammar.pdf"
  cp "$SOURCE" "$OUT/specification-grammar.svg"
  echo "Exported SVG, PDF, and PNG to $OUT/"
else
  echo "Inkscape is required for deterministic exports."
  exit 1
fi
