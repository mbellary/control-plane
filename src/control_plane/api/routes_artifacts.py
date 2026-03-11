from control_plane.api.contracts import ApiEnvelope
from control_plane.domain.versioning import SchemaVersion


def list_artifacts(request_id: str = "req-artifact-list") -> dict:
    return ApiEnvelope(
        version=SchemaVersion.V1,
        request_id=request_id,
        data={"artifacts": []},
    ).to_dict()
