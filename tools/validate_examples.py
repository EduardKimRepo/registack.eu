import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS_DIR = ROOT / "schemas"
EXAMPLES_DIR = ROOT / "examples"

PREFIX_TO_SCHEMA = {
    "accf": "accf.v0.1.schema.json",
    "mrp": "mrp.v0.1.schema.json",
    "map": "map.v0.1.schema.json",
    "mip": "mip.v0.1.schema.json",
}

def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def main():
    if not EXAMPLES_DIR.exists():
        print("ℹ️ No examples/ directory found. Skipping example validation.")
        return 0

    validators = {}
    for prefix, schema_file in PREFIX_TO_SCHEMA.items():
        schema_path = SCHEMAS_DIR / schema_file
        if schema_path.exists():
            schema = load_json(schema_path)
            validators[prefix] = Draft202012Validator(schema)

    if not validators:
        print("❌ No schemas found in schemas/.")
        return 1

    example_files = sorted(EXAMPLES_DIR.rglob("*.json"))
    if not example_files:
        print("ℹ️ No example JSON files found in examples/.")
        return 0

    failed = False
    for ex_path in example_files:
        name = ex_path.name.lower()
        prefix = name.split(".", 1)[0]  # mrp.sample.json -> "mrp"
        if prefix not in validators:
            print(f"⚠️ Skipping {ex_path} (no schema mapping for prefix '{prefix}')")
            continue

        instance = load_json(ex_path)
        errors = sorted(validators[prefix].iter_errors(instance), key=lambda e: e.path)
        if errors:
            failed = True
            print(f"\n❌ Example does not validate: {ex_path}")
            for e in errors[:25]:
                path = "$" + "".join([f".{p}" for p in e.path])
                print(f"   - {path}: {e.message}")
            if len(errors) > 25:
                print(f"   … and {len(errors)-25} more")
        else:
            print(f"✅ Valid: {ex_path}")

    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
