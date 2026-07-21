# Development Notes

## 2026-07-21 — Footer and Reference Standard

### Observation

The Specification Grammar serves two different purposes:

1. defining the engineering language (reference standard)
2. concluding an engineering report (footer)

These purposes should remain separate.

### Decision

Maintain two complementary forms.

#### Reference Standard

The complete Specification Grammar belongs in the repository reference
documentation and Specification Grammar SVG.

```
Leading constraints specify connected lanes.

Connected lanes specify engineering objects.

Engineering objects specify measurable states.

Leading specifications constrain admissible generalizations.

Admissible generalizations trail leading specifications.
```

#### Report Footer

Reports and infographics conclude with a single engineering statement.

Preferred footer:

```
Admissible generalizations trail leading specifications.
```

### Rationale

The complete grammar explains.

The report illustrates.

The footer concludes.

The footer should function as the report's final engineering statement rather
than an abbreviated reference standard.

Future revisions should preserve this separation of roles unless a simpler
Specification Grammar is developed.

### Engineering SVG

An Engineering SVG is not just "an SVG file." It is the graphical reference standard for a concept at a given stage of refinement.

That's analogous to how engineering disciplines use:

a circuit diagram,
a mechanical drawing,
a UML class diagram,
a process flow diagram.

Those aren't illustrations. They're reference artifacts.

I would define it something like this:

Engineering SVG
A versioned graphical reference standard that specifies an engineering concept through the Specification Grammar.

### Engineering SVG

An Engineering SVG is a versioned graphical reference standard.

It defines the current engineering relationship for a concept using
Specification Grammar.

An Engineering SVG is intended to remain stable until a refinement is
adopted into the reference standard.

Engineering SVGs are reference artifacts rather than presentation graphics.

### Generalizations vs Research; Susatinable vs Admissible

## 2026-07-21 — Repository Language

### Observation

Engineering SVG titles identify engineering objects rather than engineering
outputs.

Examples:

- Reaction Selectivity Specifies Battery Lifetime
- Differential Sensitivity Specifies the DFS State
- Research Integrity Specifies Sustainable Research

The accompanying Engineering Statement may introduce Specification Grammar.

Example:

    Leading specifications constrain admissible generalizations.

### Rationale

Repository titles should use the language of the engineering activity or
engineering object ("research", "battery", "state", "representation") rather
than the resulting generalizations.

Specification Grammar remains the reference language used to explain how those
engineering objects develop admissible generalizations.

This distinction helps Engineering SVG titles communicate naturally while
preserving the precision of the reference standard.
