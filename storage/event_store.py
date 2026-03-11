class EventStore:
    def __init__(self) -> None:
        self._events: list[dict] = []

    def append(self, event: dict) -> None:
        self._events.append(event)

    def all(self) -> list[dict]:
        return list(self._events)
