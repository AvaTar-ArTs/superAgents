# SuperAgents Foundation Implementation Plan

For agentic workers: use a task-by-task execution workflow with verification after each task.

Goal: Establish a validated orchestration foundation for SuperAgents.

Architecture: Keep routing and contracts in this repository while referencing the larger agent-skills library by stable source identifiers. Use a dependency-free Python router and standard-library tests.

Tech Stack: Python 3.11+, JSON Schema documents, GitHub Actions, unittest.

Spec: docs/superpowers/specs/2026-08-18-superagents-foundation-design.md

## Global Constraints

- No third-party runtime dependencies.
- Routing must be deterministic.
- Catalog validation must fail closed.
- Selection must not authorize external writes.
- Domain skills remain owned by AvaTar-ArTs/agent-skills.

## Tasks

### Task 1: Add machine-readable contracts

Files: schemas/agent.schema.json and schemas/skill.schema.json.

Add required identifiers, descriptions, tags, capabilities, source, approval, and risk fields. Verify both files parse as JSON.

### Task 2: Add initial catalogs

Files: manifests/agents.json and manifests/skills.json.

Register the core orchestrator, verifier, and creative director roles. Register core process skills and the external agent-skills source. Ensure every agent skill reference resolves.

### Task 3: Implement deterministic routing

Files: runtime/__init__.py and runtime/router.py.

Normalize intent tokens, score exact capability matches above tag matches, return stable tie-breaking by identifier, and return no candidates for empty intent.

### Task 4: Add catalog validation

File: scripts/validate_catalog.py.

Validate JSON parsing, unique identifiers, source references, and skill references. Exit nonzero on any violation.

### Task 5: Add tests and CI

Files: tests/test_catalog.py, pyproject.toml, and .github/workflows/validate.yml.

Test catalog validation and deterministic routing. Run both checks in GitHub Actions.
