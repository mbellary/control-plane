from control_plane.api.contracts import ApiEnvelope
from control_plane.domain.versioning import SchemaVersion


def create_execution(service_plan_id: str, request_id: str = "req-exec-create") -> dict:
    return ApiEnvelope(
        version=SchemaVersion.V1,
        request_id=request_id,
        data={"execution_id": f"run-{service_plan_id}", "status": "started"},
    ).to_dict()


def list_runs(request_id: str = "req-exec-list") -> dict:
    return ApiEnvelope(
        version=SchemaVersion.V1,
        request_id=request_id,
        data={"runs": []},
    ).to_dict()
