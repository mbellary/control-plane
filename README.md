# Control Plane

Deterministic AI Governance Control Plane runtime orchestration layer.

## Responsibilities
- Intent lifecycle management
- Plan reconciliation
- Execution orchestration
- Artifact lineage registration
- Drift monitoring

## Layout
This repository uses a `src/` package layout. Application code lives in `src/control_plane` and tests live in `tests/`.

## Run
```bash
uv run python -m control_plane.cmd.control_plane_server
```

## Development
```bash
uv sync --group dev
uv run ruff check .
uv run pytest
```
