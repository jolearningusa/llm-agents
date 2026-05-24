# llm-agents

Agentics configuration and knowledge for **jolearningusa** — portable across agent runtimes and “agent OS” environments (OpenClaw, Hermes, and similar VMs or local setups).

Part of **[jolearningusa](https://github.com/jolearningusa)** — submodule path `llm-agents/` in [mothership](https://github.com/jolearningusa/mothership).

**Remote:** `git@github.com:jolearningusa/llm-agents.git`

## Purpose

This repo is **not** application code (`web` / `api`) and **not** cloud deploy (`infra`). It holds:

- Agent instructions (`AGENTS.md`, skills, rules)
- Prompts, workflows, and tool/MCP notes
- Per-platform overlays for OpenClaw, Hermes, or other agentic hosts
- Shared conventions so the same behavior works in Cursor, a claw VM, or a headless agent OS

Think of it as the **source of truth for how your agents behave**, checked out beside product repos in mothership.

## Intended layout

Organize by runtime or share common files at the top level:

```text
llm-agents/
├── README.md                 # this file
├── AGENTS.md                 # default agent entry (all platforms)
├── shared/                   # cross-platform: skills, hooks, prompts
│   ├── skills/
│   └── prompts/
├── openclaw/                 # OpenClaw-specific config & docs
│   ├── AGENTS.md             # optional override / extension
│   └── ...
├── hermes/                   # Hermes-specific config & docs
│   └── ...
└── docs/
    └── ARCHITECTURE.md       # how pieces fit together
```

Add folders as you grow; keep **shared** for anything reused across OpenClaw and Hermes.

## Related repos (mothership)

| Submodule | Role |
|-----------|------|
| [mothership](https://github.com/jolearningusa/mothership) | Parent; pins submodule commits |
| [infra](https://github.com/jolearningusa/infra) | GCP edge, nginx, deploy |
| [tianshu](https://github.com/jolearningusa/tianshu) | Tianshu application monorepo |
| `web` / `api` | Product frontend and backend (when added) |

## Quick start

```bash
# From mothership root
git submodule update --init llm-agents
cd llm-agents

# Copy or symlink into your agent host (examples)
# OpenClaw: point workspace or config at this tree
# Hermes:   mount or copy shared/ + hermes/ into the VM
# Cursor:   rules/skills can reference files here or via mothership workspace
```

## Conventions

- **No secrets** in git — API keys, tokens, and `.env` stay local or in Secret Manager.
- **Platform-specific** files live under `openclaw/`, `hermes/`, etc.; don’t fork the same prompt in three places without reason.
- **Commit here first**, then bump the submodule pointer in mothership after `git push` to `jolearningusa/llm-agents`.

## Status

Repository scaffold — add `shared/`, `openclaw/`, and `hermes/` content as you wire each agentic system.
