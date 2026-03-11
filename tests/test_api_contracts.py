import pytest

from control_plane.api.contracts import ApiEnvelope, ApiError
from control_plane.api.routes_intents import create_intent
from control_plane.domain.versioning import SchemaVersion


def test_api_envelope_requires_data_or_error() -> None:
    with pytest.raises(ValueError):
        ApiEnvelope(version=SchemaVersion.V1, request_id="req-1")


def test_api_envelope_supports_error_shape() -> None:
    envelope = ApiEnvelope(
        version=SchemaVersion.V1,
        request_id="req-1",
        error=ApiError(code="BAD_REQUEST", message="invalid payload"),
    )
    assert envelope.to_dict()["error"]["code"] == "BAD_REQUEST"


def test_routes_emit_versioned_envelope() -> None:
    response = create_intent({"id": "intent-1", "objective": "deploy"}, request_id="req-123")
    assert response["version"] == SchemaVersion.V1
    assert response["request_id"] == "req-123"
    assert response["data"]["status"] == "accepted"
