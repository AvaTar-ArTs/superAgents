# SuperSkills Integration Plan

## Goal

Make SuperSkills the curated, contract-first skill catalog consumed by SuperAgents while preserving agent-skills as the broader upstream ecosystem.

## Scope

- Publish the initial SuperSkills catalog and schema.
- Record both SuperSkills and agent-skills as explicit catalog sources.
- Keep synchronization offline and provenance-preserving.
- Verify that agents only reference skills present in the selected manifest.
- Record the integration in both repositories' changelogs.

## Follow-up

- Pin source commits instead of tracking only main.
- Add JSON Schema validation for imported SuperSkills entries.
- Add a catalog lockfile with source commit, export hash, and generated timestamp.
- Add a CI job that detects stale generated manifests without network execution.
