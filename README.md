# SuperAgents

> A focused orchestration and agent-runtime layer for the AvaTar-ArTs ecosystem.

SuperAgents is the control plane for selecting, composing, validating, and executing specialized agents. It complements the broader [AvaTar-ArTs/agent-skills](https://github.com/AvaTar-ArTs/agent-skills) repository instead of duplicating its entire library.

## What belongs here

- deterministic agent and skill contracts
- routing and capability selection
- execution envelopes and audit events
- validation, verification, and release gates
- adapters for the canonical agent-skills ecosystem
- compact core process workflows derived from Superpowers

## What belongs in agent-skills

- the large reusable skill library
- creative, research, MCP, memory, and domain-specific skills
- specialist agent definitions
- long-form references, examples, fixtures, and experiments

## Current status

This repository contains the initial foundation: schemas, manifests, a deterministic router, catalog validation, architecture documentation, and a verification workflow.

## Quick start

```bash
python scripts/validate_catalog.py
python -m unittest discover -s tests -v
```

## Design principles

1. Contracts before behavior.
2. Explicit routing before execution.
3. Verification before completion claims.
4. Human approval for consequential writes.
5. The canonical `agent-skills` repository remains the source for reusable domain capability.
6. Every execution should be inspectable after the fact.

See [ARCHITECTURE.md](ARCHITECTURE.md) and the [design specification](docs/superpowers/specs/2026-08-18-superagents-foundation-design.md).
