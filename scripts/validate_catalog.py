#!/usr/bin/env python3
"""Validate SuperAgents manifests using only the Python standard library."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9._-]+$")


def fail(message: str) -> None:
    raise ValueError(message)


def validate_entry(entry: dict, required: set[str], label: str) -> None:
    missing = required - entry.keys()
    if missing:
        fail(f"{label} missing required fields: {sorted(missing)}")
    if not ID_PATTERN.fullmatch(entry["id"]):
        fail(f"{label} has invalid id: {entry['id']}")
    for field in ("tags", "capabilities"):
        if not isinstance(entry[field], list) or len(entry[field]) != len(set(entry[field])):
            fail(f"{label}.{field} must be a unique list")


def main() -> int:
    agents_doc = json.loads((ROOT / "manifests/agents.json").read_text())
    skills_doc = json.loads((ROOT / "manifests/skills.json").read_text())
    agents = agents_doc["agents"]
    skills = skills_doc["skills"]
    agent_ids = [entry["id"] for entry in agents]
    skill_ids = [entry["id"] for entry in skills]
    if len(agent_ids) != len(set(agent_ids)):
        fail("duplicate agent id")
    if len(skill_ids) != len(set(skill_ids)):
        fail("duplicate skill id")
    for entry in agents:
        validate_entry(entry, {"id", "name", "description", "tags", "capabilities", "skills", "source", "approval"}, f"agent {entry['id']}")
        for skill_id in entry["skills"]:
            if skill_id not in skill_ids:
                fail(f"agent {entry['id']} references unknown skill {skill_id}")
    for entry in skills:
        validate_entry(entry, {"id", "name", "description", "tags", "capabilities", "source", "risk"}, f"skill {entry['id']}")
    print(f"catalog valid: {len(agents)} agents, {len(skills)} skills")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"catalog invalid: {exc}", file=sys.stderr)
        raise SystemExit(1)
