#!/usr/bin/env bash
set -euo pipefail
python -m src.specification_grammar.render
python scripts/export.py
