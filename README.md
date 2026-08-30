# Specification Grammar

Vector implementation of the canonical Specification Grammar plate.

## Scope

This repository is developing into a grammar for distinguishing specification roles and their dependencies — currently one proposed set of roles (identity, state, provenance, specification, verification, result), evidenced by comparison across independently-built specimens rather than declared in advance. See `SG_0001_SPECIFICATION_ROLES.md` for the first such proposal and its evidence.

This is separate from, and does not yet constrain, the existing rendering pipeline below (the "Engineering SVG" plate and its five-line reference chain in `DEV_NOTES.md`), which remains the repository's original content.

## Build

```
python -m src.specification_grammar.render
python scripts/export.py
```

Generated assets:

- `source/specification-grammar.svg`
- `exports/specification-grammar.pdf`
- `exports/specification-grammar-1600.png`
- `exports/specification-grammar-2400.png`
- `exports/specification-grammar-3200.png`

The reference PNG is retained in `reference/` for visual comparison.

## About

Admissible generalizations trail leading specifications.
