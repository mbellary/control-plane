from __future__ import annotations

from collections.abc import Mapping

from control_plane.events import event_types

REQUIRED_FIELDS: dict[str, set[str]] = {
    event_types.INTENT_CREATED: {"intent_id", "actor"},
    event_types.PLAN_GENERATED: {"plan_id", "intent_id"},
    event_types.EXECUTION_STARTED: {"execution_id", "plan_id"},
    event_types.EXECUTION_COMPLETED: {"execution_id", "status"},
    event_types.ARTIFACT_REGISTERED: {"artifact_id", "execution_id", "uri"},
    event_types.DRIFT_DETECTED: {"resource_id", "desired", "actual"},
}


class EventContractError(ValueError):
    """Raised when an event payload does not satisfy its contract."""


def validate_event(event_type: str, payload: Mapping[str, object]) -> None:
    required_fields = REQUIRED_FIELDS.get(event_type)
    if required_fields is None:
        raise EventContractError(f"unknown event type: {event_type}")

    missing = sorted(field for field in required_fields if field not in payload)
    if missing:
        missing_fields = ", ".join(missing)
        raise EventContractError(
            f"event {event_type} missing required fields: {missing_fields}"
        )
