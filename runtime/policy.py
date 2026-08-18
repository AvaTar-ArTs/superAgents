"""Approval-policy evaluation for SuperAgents."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_policies(root: Path | None = None) -> list[dict[str, Any]]:
    base = root or Path(__file__).resolve().parents[1]
    return json.loads((base / "manifests" / "policies.json").read_text())["policies"]


def evaluate(action: str, risk: str = "low", confirmed: bool = False, root: Path | None = None) -> dict[str, Any]:
    """Return a decision without performing the requested action."""
    policies = {policy["risk"]: policy for policy in load_policies(root)}
    if risk not in policies:
        return {"decision": "deny", "reason": f"unknown risk: {risk}", "action": action, "risk": risk}
    policy = policies[risk]
    if action in policy["denied_actions"]:
        return {"decision": "deny", "reason": "action is explicitly denied", "action": action, "risk": risk}
    if action not in policy["allowed_actions"]:
        return {"decision": "deny", "reason": "action is not allowlisted", "action": action, "risk": risk}
    if policy["requires_confirmation"] and not confirmed:
        return {"decision": "confirm", "reason": "explicit confirmation required", "action": action, "risk": risk}
    return {"decision": "allow", "reason": "policy allows action", "action": action, "risk": risk}
