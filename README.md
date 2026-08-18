# SuperAgents

> The agent layer for the AvaTar-ArTs ecosystem.

SuperAgents defines specialized agents and the control plane that selects, composes, validates, and executes them. It consumes skills from [SuperSkills](https://github.com/AvaTar-ArTs/superSkills), while the broader [agent-skills](https://github.com/AvaTar-ArTs/agent-skills) repository remains an upstream ecosystem.

## Relationship

- **SuperAgents = agents**: agent identities, roles, routing, capability selection, execution envelopes, approval policy, audit events, and verification.
- **SuperSkills = skills**: reusable capability definitions, metadata, provenance, tags, capabilities, risk, and lifecycle status.
- **agent-skills = broader source ecosystem**: long-form, experimental, and domain-specific skills that can be curated into SuperSkills.

The manifests/skills.json file here is a generated runtime projection used by agents; it is not the authoritative skill library.

## What belongs here

- deterministic agent contracts
- agent routing and capability selection
- execution envelopes and audit events
- validation, verification, and release gates
- adapters for SuperSkills and agent-skills catalogs
- compact core process workflows derived from Superpowers

## Current status

This repository contains the initial agent foundation plus execution policy primitives, an offline skill-catalog synchronizer, and an explicit SuperSkills integration boundary.

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

1. Agents are explicit before execution.
2. Skills are referenced by stable IDs.
3. Routing precedes execution.
4. Verification precedes completion claims.
5. Human approval protects consequential writes.
6. Every execution should be inspectable after the fact.

See [ARCHITECTURE.md](ARCHITECTURE.md), [ecosystem-boundary.md](docs/ecosystem-boundary.md), and the [design specification](docs/superpowers/specs/2026-08-18-superagents-foundation-design.md).
