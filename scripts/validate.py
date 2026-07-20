from pathlib import Path
import sys

required = [
    Path("README.md"),
    Path("reference/specification-grammar-reference.png"),
    Path("exports/specification-grammar.png"),
]

missing = [str(path) for path in required if not path.exists()]
if missing:
    print("Missing required files:")
    for path in missing:
        print(f"- {path}")
    sys.exit(1)

print("Specification Grammar scaffold is valid.")
