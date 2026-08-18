"""Execution-envelope and audit-event constructors."""
from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def build_execution(intent: str, agent_id: str, skills: list[str], required_capabilities: list[str] | None = None) -> dict:
    if not intent.strip():
        raise ValueError("intent must not be empty")
    return {
        "execution_id": f"exec_{uuid4().hex}",
        "request": {"intent": intent, "required_capabilities": required_capabilities or []},
        "status": "planned",
        "selected_agent": agent_id,
        "selected_skills": sorted(set(skills)),
        "approval": "pending",
        "verification": "not_started",
        "outputs": [],
        "events": [],
        "metadata": {"created_at": now()}
    }


def build_event(execution_id: str, event_type: str, actor: str, payload: dict | None = None) -> dict:
    if not execution_id or not actor:
        raise ValueError("execution_id and actor are required")
    return {
        "event_id": f"evt_{uuid4().hex}",
        "execution_id": execution_id,
        "event_type": event_type,
        "timestamp": now(),
        "actor": actor,
        "payload": payload or {}
    }
