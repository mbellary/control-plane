# Control Plane

Deterministic AI Governance Control Plane runtime orchestration layer.

## Responsibilities
- Intent lifecycle management
- Plan reconciliation
- Execution orchestration
- Artifact lineage registration
- Drift monitoring

## Layout
This repository follows the scaffolding in `control-plane-repository-scaffolding.md` and provides module stubs for runtime controllers, APIs, reconciliation, governance, execution, and storage.

## Run
```bash
python cmd/control_plane_server.py
```
