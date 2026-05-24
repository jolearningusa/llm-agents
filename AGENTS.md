# AGENTS.md — llm-agents

Instructions for AI coding agents working in this repository.

## Purpose

**llm-agents** stores agentics configuration for jolearningusa: prompts, skills, rules, and platform-specific overlays for **OpenClaw**, **Hermes**, and other agent OS / VM hosts. It does not contain product app code or infrastructure.

Submodule path: `llm-agents/` in [mothership](https://github.com/jolearningusa/mothership).

## Boundaries

- **In scope:** Agent behavior, skills, hooks, MCP notes, OpenClaw/Hermes config trees under this repo.
- **Out of scope:** `web`, `api`, `tianshu` application code; GCP/nginx/deploy in `infra`.
- **Commits:** Push changes here first; then bump the mothership submodule pointer.
- **Secrets:** Never commit keys, tokens, or `.env` files.

## Layout (target)

```text
llm-agents/
├── AGENTS.md          # this file
├── shared/            # cross-platform skills & prompts
├── openclaw/          # OpenClaw-specific
├── hermes/            # Hermes-specific
└── docs/ARCHITECTURE.md
```

## Commands

```bash
# From mothership
git submodule update --init llm-agents
cd llm-agents
```

## Conventions

- Prefer `shared/` for reusable content; use `openclaw/` or `hermes/` only for deltas.
- Update `docs/ARCHITECTURE.md` when adding a new platform or changing agent boundaries.
- Match naming and tone of existing jolearningusa repos (see mothership `templates/submodule/`).

## Related repos

| Repo | Role |
|------|------|
| [mothership](https://github.com/jolearningusa/mothership) | Parent meta-repo |
| [infra](https://github.com/jolearningusa/infra) | GCP / nginx edge |
| [tianshu](https://github.com/jolearningusa/tianshu) | Tianshu apps |
