def create_execution(service_plan_id: str) -> dict:
    return {"execution_id": f"run-{service_plan_id}", "status": "started"}


def list_runs() -> dict:
    return {"runs": []}
