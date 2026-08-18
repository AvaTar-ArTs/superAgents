# SuperAgents Architecture

## Position

SuperAgents is the orchestration layer between a user request and the larger capability ecosystem in AvaTar-ArTs/agent-skills.

It owns routing, contracts, execution metadata, approval boundaries, and verification. It does not copy every domain skill into this repository.

## Layers

1. Contracts — JSON Schemas define agents, skills, requests, and execution results.
2. Catalogs — manifests expose available agents and external skill sources.
3. Router — deterministic tag and capability matching selects candidates.
4. Execution envelope — future runners will record request, selection, approvals, outputs, and verification.
5. Adapters — external repositories and tool providers remain referenced by stable identifiers.
6. Verification — catalog validation and tests prevent malformed or ambiguous runtime state.

## Runtime flow

request -> normalize intent -> match capabilities -> rank agents -> apply approval policy -> execute through an adapter -> verify output -> emit audit event

## Boundaries

- agent-skills is the canonical source for broad reusable skills and specialist content.
- superAgents is the canonical source for orchestration contracts and routing behavior.
- External actions require an explicit policy decision; selection does not imply authorization.
- A route is advisory until an execution adapter and approval policy accept it.

## Initial non-goals

- copying the complete agent-skills tree
- implementing a model provider abstraction
- autonomous external writes
- replacing GitHub, Airtable, Slack, or other connected systems
- claiming distributed execution before a runner exists
