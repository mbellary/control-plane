import pytest

from control_plane.events.contracts import EventContractError
from control_plane.events.event_bus import EventBus
from control_plane.events.event_types import INTENT_CREATED


def test_event_bus_rejects_invalid_payload() -> None:
    bus = EventBus()
    with pytest.raises(EventContractError):
        bus.publish(INTENT_CREATED, {"intent_id": "intent-1"})


def test_event_bus_publishes_valid_payload() -> None:
    bus = EventBus()
    received: list[dict] = []
    bus.subscribe(INTENT_CREATED, received.append)

    payload = {"intent_id": "intent-1", "actor": "system"}
    bus.publish(INTENT_CREATED, payload)

    assert received == [payload]
