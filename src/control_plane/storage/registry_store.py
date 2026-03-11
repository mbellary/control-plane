class RegistryStore:
    def __init__(self) -> None:
        self._records: dict[str, dict] = {}

    def register(self, key: str, value: dict) -> None:
        self._records[key] = value

    def list(self) -> list[dict]:
        return list(self._records.values())
