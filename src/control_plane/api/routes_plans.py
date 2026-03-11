def list_plans() -> dict:
    return {"plans": []}


def get_plan(plan_id: str) -> dict:
    return {"plan_id": plan_id, "status": "registered"}
