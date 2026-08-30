# SG_0001 — Specification Roles

Derived from `mathematical-basis/analysis/INVARIANT_EXTRACTION_MB_0001_0002_0003.md`, which compared three completed mathematical-basis specimens (MB_0001, number theory/counting; MB_0002, finite group theory; MB_0003, nonassociative algebra) built under three different verification regimes. This document proposes general roles from that evidence; it does not introduce a new YAML schema, and every proposed rule below cites the specimen(s) it's drawn from.

Provenance runs one direction: MB_0001/2/3 → observed invariants (in mathematical-basis) → proposed roles (here). This document does not bind back onto the specimens or require they change.

## 1. Observed invariants (summary; full evidence in the source analysis)

- A fixed seven-role envelope recurred exactly across all three: identity, state, provenance, specification, verification, result, and a closing principle/policy note.
- Within the specification role, a stable core recurred: the admissible domain, the leading claim itself, a list of positive constraints, and a list of excluded generalizations — plus exactly one domain-specific extension per specimen.
- A four-way independently-gradable state recurred (mathematical/computational/provenance/publication in MB's binding).
- Numerical or specific readings were always presented as consequences of a stated general specification, never as free-standing facts explained afterward — while the source analysis is explicit that this is a presentation-order fact, not a discovery-order one.
- Results were always captured (actual output, executable hash, run timestamp) rather than asserted, with unavailable provenance (commit hash) left null rather than fabricated.
- The role separation between justification (proof) and checking (verification) was not self-enforcing: MB_0001 and MB_0002 kept it clean from their first drafts; MB_0003's first draft violated it (its proof cited its own verification's output to close a step), and it took two rounds of review, not the directory layout alone, to fix.

## 2. Proposed SG roles

**SG-1. A specification names six distinct roles: Identity, State, Provenance, Specification, Verification, Result.** Evidence: the seven-key envelope, identical across MB_0001/2/3 (§1). Kept abstract deliberately — this document does not mandate that every SG-governed repository use these as literal YAML keys, or use YAML at all. Mathematical-basis is one binding of these roles onto its own key names; other repositories may bind them differently.

**SG-2. Independent aspects of a specification's state remain independently gradable.** Evidence: MB's four-axis status (§1), and specifically MB_0003, where treating "proved" and "verified" as one collapsed axis would have hidden the exact defect the review caught. Not proposed as universal that every domain needs *these four* axes — an engineering repository's independently-gradable axes might be specification/implementation/measurement/publication, or something else again. What's proposed as invariant is only that State is a set of independently-gradable dimensions, not a single up/down flag.

**SG-3. A specification states both what constrains the admissible object and which extensions remain outside the claim.** Evidence: `leading_constraints` and `excluded_generalizations`, present with different content but the same structural role in all three specimens (§1). This is the single most directly transferable rule — the three specimens used it for three unrelated mathematical boundaries (squarefree-modulus scope, single-group scope, single-labeling scope), with the role itself unchanged.

**SG-4. Discovery order and specification order are not the same thing, and a specification records the latter.** Evidence: MB_0001's actual history went numeral-first (24/25, corrected to 3) before the general C(m)=m/φ(m) form existed; MB_0003's 16 was found by enumeration before the rank-4 structural reason was found. In both cases the *finished* specification states the general form first and the number as its reading. This rule does not claim mathematics is discovered top-down — it claims a finished specification should make clear which statement is leading and which reading follows from it, regardless of which came first in the work that produced it.

**SG-5. Recorded results preserve the provenance actually available at the time of recording; unavailable provenance is left explicitly unspecified, not fabricated.** Evidence: all three `results/*.yaml` carry `commit_hash: null` with a comment explaining why, rather than a placeholder value someone could later mistake for real (§1). SHA-256 hashes, timestamps, and environment versions are implementation bindings of this rule, not the rule itself.

**SG-6. A specification's justification (proof) and its checking (verification) are distinct roles, and neither may silently stand in for the other.** Evidence: this is the rule MB_0003's first draft actually violated — its proof cited its own exhaustive verification's output as a necessary step in closing an unproven claim. The fix was not adding a `proofs/` directory (MB_0003 already had one); the fix was rewriting the proof's logical content so it no longer depended on the verification's result. **This is proposed as a checklist question, not a structural guarantee**: *does this specification's justification cite its own verification's output as evidence for a step the justification has not independently established?* A directory split cannot answer this question by itself; someone has to ask it.

**SG-7. Domain-specific content is an explicit extension point, not a gap to be standardized away.** Evidence: verification method (numerical sweep / exact enumeration / analytic derivation), justification weight (full paper / short proof file), and the relationship between a specification and its source (correction / independent re-derivation / extension past the source's own claim) all varied legitimately across the three specimens, and the source analysis found no common structure among them worth extracting (§1, "Explicitly NOT invariant"). SG should name this as a role that is *supposed* to keep varying, not treat the current lack of a common pattern as an artifact of having only three specimens so far.

## 3. Explicitly left domain-specific (not proposed for SG)

- The literal YAML key names mathematical-basis uses (`statement`, `status`, `source_provenance`, `specification`, `verification`, `result`, `footer`) — these are one binding of SG-1's roles, not the roles themselves.
- The specific four status axes MB uses (`mathematical`/`computational`/`provenance`/`publication`) — one binding of SG-2.
- Verification method, justification weight, and source-relationship type (SG-7).
- The specific closing sentence "Admissible generalizations trail leading specifications" — this recurred because all three specimens were written under one standing instruction in one project, not because three independent domains converged on the same sentence. Whether this belongs in SG as a named principle, or stays a mathematical-basis-specific convention, is unresolved and should not be assumed either way without evidence from a repository outside mathematical-basis.

## 4. Next pressure test (not performed here)

These seven roles should be checked against a repository that was never built with mathematical-basis's vocabulary in mind — residue-manifold-learning or sensors-becker are the two available candidates. If SG-1 through SG-7 describe what's actually in those repositories without forcing mathematical-basis-shaped language onto them, that's evidence for a genuinely cross-repository grammar. If they don't fit without distortion, the abstraction should be revised, not the repositories.
