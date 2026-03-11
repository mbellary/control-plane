from collections import defaultdict
from collections.abc import Callable

from control_plane.events.contracts import validate_event


class EventBus:
    def __init__(self) -> None:
        self._subscribers: dict[str, list[Callable[[dict], None]]] = defaultdict(list)

    def subscribe(self, event_type: str, handler: Callable[[dict], None]) -> None:
        self._subscribers[event_type].append(handler)

    def publish(self, event_type: str, payload: dict) -> None:
        validate_event(event_type, payload)
        for handler in self._subscribers[event_type]:
            handler(payload)
