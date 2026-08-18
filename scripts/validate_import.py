#!/usr/bin/env python3
"""Validate imported skill entries against a JSON Schema subset used by SuperSkills."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


def validate(value: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    errors: list[str] = []
    expected = schema.get("type")
    if expected == "object":
        if not isinstance(value, dict):
            return [f"{path}: expected object"]
        for name in schema.get("required", []):
            if name not in value:
                errors.append(f"{path}: missing required property {name}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            errors.extend(f"{path}: unexpected property {name}" for name in value if name not in properties)
        for name, child_schema in properties.items():
            if name in value:
                errors.extend(validate(value[name], child_schema, f"{path}.{name}"))
    elif expected == "array":
        if not isinstance(value, list):
            return [f"{path}: expected array"]
        if schema.get("uniqueItems") and len({json.dumps(item, sort_keys=True) for item in value}) != len(value):
            errors.append(f"{path}: items must be unique")
        for index, item in enumerate(value):
            errors.extend(validate(item, schema.get("items", {}), f"{path}[{index}]"))
    elif expected == "string":
        if not isinstance(value, str):
            return [f"{path}: expected string"]
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{path}: string is too short")
        pattern = schema.get("pattern")
        if pattern and not re.match(pattern, value):
            errors.append(f"{path}: does not match {pattern}")
    elif expected == "integer":
        if not isinstance(value, int) or isinstance(value, bool):
            errors.append(f"{path}: expected integer")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: expected one of {schema['enum']}")
    return errors


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: validate_import.py CATALOG.json SCHEMA.json")
    catalog_path, schema_path = map(Path, sys.argv[1:])
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    errors = []
    for index, skill in enumerate(catalog.get("skills", [])):
        errors.extend(validate(skill, schema, f"$.skills[{index}]"))
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"import valid: {len(catalog.get('skills', []))} skills against {schema_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
