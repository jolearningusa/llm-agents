# scripts

Custom utilities used with agentic workflows (OpenClaw, Hermes, local `~/bin`, etc.).

## Adding a script

1. Copy or write the script here (e.g. from your OpenClaw VM `~/bin/`).
2. Make it executable: `chmod +x scripts/<name>`
3. Commit in **llm-agents**, push, then bump the submodule in mothership.

## Planned / local copies

| Script | Source | Notes |
|--------|--------|--------|
| `pdf-replace` | OpenClaw VM `~/bin/pdf-replace` | Copy when ready |

## Usage

Run from repo root or add to `PATH`:

```bash
./scripts/pdf-replace --help   # after you copy the file
```

Or symlink into `~/bin`:

```bash
ln -sf "$(pwd)/scripts/pdf-replace" ~/bin/pdf-replace
```

## Conventions

- Prefer POSIX shell or Python with a short header comment describing inputs/outputs.
- No secrets in scripts; use env vars or local config outside git.
