from __future__ import annotations

from dataclasses import dataclass


class GovernanceViolationError(Exception):
    pass


@dataclass(slots=True, frozen=True)
class PolicyDecision:
    allowed: bool
    reason: str


class PolicyEngine:
    def __init__(self) -> None:
        self.approved_datasets: set[str] = set()
        self.required_intent_fields: set[str] = {"id", "objective", "actor"}

    def evaluate(self, intent: dict) -> bool:
        decision = self.evaluate_with_reason(intent)
        if not decision.allowed:
            raise GovernanceViolationError(decision.reason)
        return True

    def evaluate_with_reason(self, intent: dict) -> PolicyDecision:
        missing_fields = sorted(
            field for field in self.required_intent_fields if field not in intent
        )
        if missing_fields:
            missing = ", ".join(missing_fields)
            return PolicyDecision(False, f"Intent missing required fields: {missing}")

        dataset = intent.get("dataset")
        if dataset and dataset not in self.approved_datasets:
            return PolicyDecision(False, f"Dataset {dataset} is not approved")

        return PolicyDecision(True, "intent approved")
