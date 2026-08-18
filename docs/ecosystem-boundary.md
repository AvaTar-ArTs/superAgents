# Ecosystem Boundary

| Repository | Owns | Does not own |
| --- | --- | --- |
| [superSkills](https://github.com/AvaTar-ArTs/superSkills) | Curated reusable skill contracts and provenance | Runtime execution and agent routing |
| [superAgents](https://github.com/AvaTar-ArTs/superAgents) | Agents, routing, policy, envelopes, audit, verification | The complete skill library |
| [agent-skills](https://github.com/AvaTar-ArTs/agent-skills) | Broad upstream skill ecosystem and long-form implementations | The SuperAgents runtime contract |

## Current integration

SuperAgents records SuperSkills as the preferred curated catalog and agent-skills as the broader upstream source in [manifests/sources.json](../manifests/sources.json). Synchronization accepts exported JSON and does not fetch or execute remote content.

## Data flow

1. Skills originate in agent-skills or are authored in SuperSkills.
2. SuperSkills curates and normalizes reusable metadata.
3. SuperAgents consumes a pinned or exported catalog.
4. SuperAgents selects skills, applies policy, emits an execution envelope, and records evidence.
