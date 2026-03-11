from control_plane.api.contracts import ApiEnvelope
from control_plane.domain.versioning import SchemaVersion


def list_plans(request_id: str = "req-plan-list") -> dict:
    return ApiEnvelope(
        version=SchemaVersion.V1,
        request_id=request_id,
        data={"plans": []},
    ).to_dict()


def get_plan(plan_id: str, request_id: str = "req-plan-get") -> dict:
    return ApiEnvelope(
        version=SchemaVersion.V1,
        request_id=request_id,
        data={"plan_id": plan_id, "status": "registered"},
    ).to_dict()
