from collections import defaultdict
from collections.abc import Callable


class EventBus:
    def __init__(self) -> None:
        self._subscribers: dict[str, list[Callable[[dict], None]]] = defaultdict(list)

    def subscribe(self, event_type: str, handler: Callable[[dict], None]) -> None:
        self._subscribers[event_type].append(handler)

    def publish(self, event_type: str, payload: dict) -> None:
        for handler in self._subscribers[event_type]:
            handler(payload)
