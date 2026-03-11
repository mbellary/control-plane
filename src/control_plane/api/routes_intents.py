from control_plane.api.contracts import ApiEnvelope
from control_plane.domain.versioning import SchemaVersion


def create_intent(intent: dict, request_id: str = "req-intent-create") -> dict:
    return ApiEnvelope(
        version=SchemaVersion.V1,
        request_id=request_id,
        data={"status": "accepted", "intent": intent},
    ).to_dict()


def get_intent(intent_id: str, request_id: str = "req-intent-get") -> dict:
    return ApiEnvelope(
        version=SchemaVersion.V1,
        request_id=request_id,
        data={"intent_id": intent_id, "status": "stored"},
    ).to_dict()
