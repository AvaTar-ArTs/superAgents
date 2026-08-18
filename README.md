# SuperAgents

> A focused orchestration and agent-runtime layer for the AvaTar-ArTs ecosystem.

SuperAgents is the control plane for selecting, composing, validating, and executing specialized agents. It complements [SuperSkills](https://github.com/AvaTar-ArTs/superSkills), the curated reusable-skill catalog, and the broader [agent-skills](https://github.com/AvaTar-ArTs/agent-skills) ecosystem.

## What belongs here

- deterministic agent and skill contracts
- routing and capability selection
- execution envelopes and audit events
- validation, verification, and release gates
- adapters for SuperSkills and agent-skills catalogs
- compact core process workflows derived from Superpowers

## What belongs in SuperSkills

- curated reusable skill definitions
- skill metadata, provenance, tags, capabilities, and risk
- composition and lifecycle status

## What belongs in agent-skills

- the large reusable skill library
- creative, research, MCP, memory, and domain-specific skills
- specialist agent definitions
- long-form references, examples, fixtures, and experiments

## Current status

This repository contains the initial foundation plus execution policy primitives, an offline catalog synchronizer, and an explicit SuperSkills integration boundary.

## Quick start

```bash
python scripts/validate_catalog.py
python -m unittest discover -s tests -v
```

To import an exported SuperSkills catalog:

```bash
python scripts/sync_agent_skills_catalog.py \
  exported/superskills.json manifests/skills.json \
  --source-label AvaTar-ArTs/superSkills
```

## Design principles

1. Contracts before behavior.
2. Explicit routing before execution.
3. Verification before completion claims.
4. Human approval for consequential writes.
5. SuperSkills is the preferred curated catalog; agent-skills remains the broad upstream source.
6. Every execution should be inspectable after the fact.

See [ARCHITECTURE.md](ARCHITECTURE.md), [ecosystem-boundary.md](docs/ecosystem-boundary.md), and the [design specification](docs/superpowers/specs/2026-08-18-superagents-foundation-design.md).
