"""Deterministic capability router for the SuperAgents foundation."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

_TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9-]*")


def _tokens(value: str) -> set[str]:
    return set(_TOKEN_RE.findall(value.lower().replace("_", "-")))


def load_catalog(root: Path | None = None) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    base = root or Path(__file__).resolve().parents[1]
    agents = json.loads((base / "manifests" / "agents.json").read_text())
    skills = json.loads((base / "manifests" / "skills.json").read_text())
    return agents["agents"], skills["skills"]


def route(intent: str, required_capabilities: list[str] | None = None, root: Path | None = None) -> list[dict[str, Any]]:
    """Return deterministic ranked agent candidates without executing anything."""
    intent_tokens = _tokens(intent)
    required = set(required_capabilities or [])
    if not intent_tokens and not required:
        return []

    agents, _ = load_catalog(root)
    ranked: list[dict[str, Any]] = []
    for agent in agents:
        capability_hits = required.intersection(agent["capabilities"])
        tag_hits = intent_tokens.intersection(_tokens(" ".join(agent["tags"])))
        name_hits = intent_tokens.intersection(_tokens(agent["name"]))
        if required and capability_hits != required:
            continue
        score = len(capability_hits) * 10 + len(tag_hits) * 2 + len(name_hits)
        if score:
            ranked.append({
                "agent_id": agent["id"],
                "score": score,
                "matched_capabilities": sorted(capability_hits),
                "matched_tags": sorted(tag_hits),
                "approval": agent["approval"]
            })
    return sorted(ranked, key=lambda item: (-item["score"], item["agent_id"]))
