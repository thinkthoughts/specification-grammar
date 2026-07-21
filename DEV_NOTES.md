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
