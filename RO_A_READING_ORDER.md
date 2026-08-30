# RO_A — Reading Order

Purpose: understand this repository, in the order a new reader should move through it. This is a human reading sequence, not a dependency or provenance order — SG_0001's own provenance runs backward, from the mathematical-basis specimens to this document, which reads forward.

1. **README.md** — what this repository is and what it's becoming: a proposed grammar for specification roles, evidenced from external specimens, kept separate from the repository's original rendering-pipeline content.
2. **SG_0001_SPECIFICATION_ROLES.md** — the first evidence-derived proposal: seven roles (Identity, State, Provenance, Specification, Verification, Result, plus independently-gradable State and the leading-constraints/excluded-generalizations pairing), each citing which mathematical-basis specimen(s) it was drawn from, and an explicit list of what was found NOT to generalize. Ends with the next pressure test this repository owes itself: checking these roles against a specimen with no mathematical-basis vocabulary in it.
3. **DEV_NOTES.md — the repository’s original internal conventions and rendering-era material. Read this as historical/internal context, not as the external pressure test for SG_0001.
4. **source/, exports/, reference/, scripts/, src/specification_grammar/** — the existing rendering pipeline (the Specification Grammar plate as an SVG/PDF/PNG artifact). Unrelated to SG_0001's current work; read only if working on the rendering pipeline itself.

A reader who only has time for one file should read SG_0001 — it is the only artifact in this repository so far that makes a checkable claim rather than describing a rendering pipeline or a naming convention.

Next validation target: apply SG-1 through SG-7 to an external specimen such as Sensors-Becker; results should be recorded in a new analysis artifact before any schema or code changes.
