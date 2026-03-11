class StateStore:
    def __init__(self) -> None:
        self._state: dict[str, dict] = {}

    def put(self, key: str, value: dict) -> None:
        self._state[key] = value

    def get(self, key: str) -> dict | None:
        return self._state.get(key)
