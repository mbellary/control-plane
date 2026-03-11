import hashlib
import json
from typing import Any


class IntentController:
    def __init__(self) -> None:
        self._intents: dict[str, dict[str, Any]] = {}

    def start(self) -> None:
        return

    def fetch_new_intents(self) -> list[dict[str, Any]]:
        return []

    def process_intent(self, intent: dict[str, Any]) -> str:
        canonical_intent = self.canonicalize(intent)
        intent_hash = self.hash(canonical_intent)
        self.store_intent(intent_hash, canonical_intent)
        self.emit_event("intent.created", intent_hash)
        return intent_hash

    def canonicalize(self, intent: dict[str, Any]) -> dict[str, Any]:
        return dict(sorted(intent.items(), key=lambda item: item[0]))

    def hash(self, canonical_intent: dict[str, Any]) -> str:
        payload = json.dumps(canonical_intent, sort_keys=True).encode("utf-8")
        return hashlib.sha256(payload).hexdigest()

    def store_intent(self, intent_hash: str, canonical_intent: dict[str, Any]) -> None:
        self._intents[intent_hash] = canonical_intent

    def emit_event(self, event_type: str, intent_hash: str) -> None:
        _ = (event_type, intent_hash)
