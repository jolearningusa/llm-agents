# Architecture — llm-agents

## Summary

Central store for **agentics** assets used across OpenClaw, Hermes, Cursor, and similar environments. Product and infra repos stay separate; this repo answers “how should agents behave and what context do they load?”

## Context

```text
[mothership]
    ├── llm-agents/     ← agent config (this repo)
    ├── infra/          ← deploy / edge
    ├── tianshu/        ← applications
    └── web, api, …
```

## Responsibilities

- Shared skills, prompts, and rules (`shared/`)
- Platform-specific trees (`openclaw/`, `hermes/`, …)
- Documentation for wiring each agentic OS/VM to this repo

## Non-goals

- Running agents as a service (that lives on the host VM / OpenClaw / Hermes)
- Storing application source or Terraform

## Key decisions

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-05 | Dedicated repo under mothership | Version agent config independently from apps and infra |

## Operations

- Sync: submodule clone or bind-mount into agent host workspace
- No deploy pipeline in this repo unless you add one later for packaging configs
