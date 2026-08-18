#!/usr/bin/env python3
"""Convert an exported agent-skills catalog into a SuperAgents skill manifest.

This tool is intentionally offline. It accepts a JSON export rather than
fetching or executing remote content.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def sync(source_path: Path, output_path: Path, source_label: str) -> int:
    source = json.loads(source_path.read_text())
    if isinstance(source, dict):
        entries = source.get("skills", [])
    elif isinstance(source, list):
        entries = source
    else:
        entries = []
    skills = []
    for entry in entries:
        skill_id = entry.get("id") or entry.get("name", "").lower().replace(" ", "-")
        if not skill_id:
            continue
        skills.append({
            "id": skill_id,
            "name": entry.get("name", skill_id),
            "description": entry.get("description", "Imported agent skill"),
            "tags": sorted(set(entry.get("tags", []))),
            "capabilities": sorted(set(entry.get("capabilities", entry.get("tags", [])))),
            "source": entry.get("source", f"{source_label}:{skill_id}"),
            "risk": entry.get("risk", "low"),
            "status": entry.get("status", "new")
        })
    output_path.write_text(json.dumps({"version": 1, "skills": skills}, indent=2) + "\n")
    print(f"wrote {len(skills)} skills to {output_path}")
    return len(skills)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--source-label", default="AvaTar-ArTs/agent-skills")
    args = parser.parse_args()
    sync(args.source, args.output, args.source_label)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
