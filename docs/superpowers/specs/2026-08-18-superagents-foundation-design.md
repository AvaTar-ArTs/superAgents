# SuperAgents Foundation Design

## Goal

Create a compact, inspectable control plane that routes user intent to the right agent and skill without duplicating the broader AvaTar-ArTs capability library.

## Context

The agent-skills repository contains a large, personalized collection of agents, creative workflows, research systems, MCP integrations, memory tools, and engineering process skills. A separate Superpowers-style process library provides useful planning, TDD, debugging, review, and verification patterns. SuperAgents should compose these capabilities instead of competing with them.

## Requirements

- represent agents and skills with machine-readable contracts
- keep source ownership explicit
- support deterministic capability matching
- distinguish selection from authorization
- make verification a first-class result
- provide a minimal Python implementation with no third-party dependency
- validate catalogs in CI
- preserve future compatibility with richer runners and adapters

## Architecture

The first implementation contains:

- schemas/agent.schema.json
- schemas/skill.schema.json
- manifests/agents.json
- manifests/skills.json
- runtime/router.py
- scripts/validate_catalog.py
- tests/test_catalog.py

The router uses normalized text tags and capability identifiers. It returns ranked candidates and never executes an external action.

## Data flow

A request supplies a textual intent and optional required capabilities. The router tokenizes the intent, compares it with agent tags and declared capabilities, and returns a ranked list. The caller decides whether to ask for approval and which adapter should execute the chosen route.

## Error handling

- malformed JSON manifests fail validation
- duplicate identifiers fail validation
- unknown skill references fail validation
- empty intents return no route rather than an arbitrary default
- external writes remain outside the router

## Testing

The foundation is verified with standard-library unit tests covering catalog shape and uniqueness, capability matching, deterministic ordering, empty and unknown requests, schema presence, and repository references.

## Future extension points

- execution event schema
- approval policy schema
- adapter registry
- provenance and artifact receipts
- model/provider selection
- cross-repository catalog synchronization
