# SG Cycle 1 — Evidence Record

Records the first complete specification-grammar analysis cycle. Kept as evidence, not as a claim about what SG_0001 should become next — that decision follows from this, and belongs in a separate revision.

## The cycle, with artifacts

```
MB_0001 / MB_0002 / MB_0003
        ↓
mathematical-basis/analysis/INVARIANT_EXTRACTION_MB_0001_0002_0003.md
        ↓
SG_0001_SPECIFICATION_ROLES.md  (initial draft, seven proposed roles)
        ↓
sensors-becker pressure test
   · GitHub blob fetches (v1–v3, partial, working from one secondhand file description)
   · Full ZIP inspection (v4, complete RP_37 thread from source PDF to session report)
        ↓
specification-grammar/analysis/SENSORS_BECKER_SG_AUDIT.md  (v4, real content)
        ↓
SG_0001_SPECIFICATION_ROLES.md  (revised: SG-1, SG-2, SG-6 updated; SG-3 left open)
        ↓
sensors-becker engineering improvements (direct consequence of applying SG-6's distinction):
   · Repair 1: DEV_NOTES.md superseded note
   · Repair 2: RP_37_ENGINEERING_SESSION_REPORT.md organization error (INL → University of Colorado)
   · Repair 3: NB_00_SOURCE_EXTRACTION.ipynb renamed → NB_00_RP_37_SOURCE_EXTRACTION.ipynb
   · V1/V2/V3 verification added to the renamed notebook
   · Author error found and fixed by V3 on first live run (Daniel Becker → Dan Becker)
   · Repository-wide filename mismatch traced to template root cause, documented, held for separate repair
        ↓
sensors-becker/analysis/RP_37_VERIFICATION_DEPTHS.md  (evidence note, not SG revision)
```

## What happened that was genuinely novel, not just pattern-matching

**1. v1–v3 got the headline wrong; v4 reversed it.** The first three audit passes, working from one secondhand description and GitHub blob fetches of ES files, concluded "sensors-becker specifies a process, not a verified claim." Reading the complete RP_37 thread from source PDF to session report showed this was wrong: the repository carries checkable claims with page-cited provenance, and checking them found real errors. The reversal came from actually reading the evidence, not from adjusting priors.

**2. The inspection found errors the repository itself had not found.** Two citation errors in `RP_37_ENGINEERING_SESSION_REPORT.md` (organization, author) survived V1's structural check, were not flagged anywhere in the repository's existing process, and were caught only by checking the report's content against the canonical `SOURCE` dict — i.e., by applying the same auditing discipline that `mathematical-basis` applies to its own sources. Those errors are now fixed and the check that caught them is a regression test that runs on every notebook execution.

**3. SG functioned as an analysis tool, not just a description.** The three-depth distinction (V1: artifact integrity / V2: source-content presence / V3: cross-artifact consistency) wasn't in SG_0001 before the pressure test — it emerged from applying SG-6's structural/content distinction to a real case and finding that "content" split into two different things that catch different failure modes. That's a new distinction that came out of doing the work, not something that was noticed from the outside and recorded.

**4. The filename mismatch audit changed the repair unit.** What looked like 17 independent field errors turned out to be one template defect propagated. The audit document records this specifically so the eventual repair begins at `RP_TEMPLATE.yaml` rather than 17 individual corrections — a consequential difference that only becomes visible once the full scope is traced.

## What was explicitly held

- **SG-6 was not revised** to say "verification has exactly three levels." RP_37 produced evidence of three useful depths; one implementation is not a fixed count. `RP_37_VERIFICATION_DEPTHS.md` holds the evidence without prematurely resolving what SG-6 should say next.
- **SG-3's open question was not resolved.** The distinction "domain constraint ≠ claim boundary" was surfaced but not answered by sensors-becker — its `engineering_constraints` fields record facts about the domain (e.g., "decay time limits count rate"), not epistemic boundaries on a claim. Whether that's a fundamental difference between engineering and mathematical specifications, or a gap sensors-becker should fill, is left open for the next specimen.
- **The filename mismatch was not fixed** in the RP specifications or other extraction notebooks. Documented in `analysis/SOURCE_FILENAME_MISMATCH_AUDIT.md`, held for a template-first repair.

## What the next pressure test is actually for

SG-3 is the precise unresolved question:

> Does the distinction between *domain constraints* (facts about what the object does, derived from the source) and *claim boundaries* (facts about what a specification does or doesn't assert) actually matter across domains, and is it an invariant worth naming, or is it an artifact of mathematics having a different relationship to its claims than engineering does?

The fourth MB specimen should be chosen specifically to apply pressure to this question rather than simply to "fit SG." A domain where the claim-boundary role is clearly present and clearly different from domain constraints would either confirm SG-3 applies across both mathematics and engineering, or reveal that claim boundaries are mathematics-specific and SG-3 should be split or scoped. Either outcome is more useful than a fourth specimen that happens to pass all seven rules without strain.
