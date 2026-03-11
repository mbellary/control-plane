from governance.constraint_evaluator import ConstraintEvaluator
from governance.policy_engine import PolicyEngine


class GovernanceValidator:
    def __init__(self) -> None:
        self.policy_engine = PolicyEngine()
        self.constraint_evaluator = ConstraintEvaluator()

    def validate(self, intent: dict, constraints: list[dict] | None = None) -> bool:
        self.policy_engine.evaluate(intent)
        return self.constraint_evaluator.evaluate(constraints or [], intent)
