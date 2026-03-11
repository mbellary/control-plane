class GovernanceViolationError(Exception):
    pass


class PolicyEngine:
    def __init__(self) -> None:
        self.approved_datasets: set[str] = set()

    def evaluate(self, intent: dict) -> bool:
        dataset = intent.get("dataset")
        if dataset and dataset not in self.approved_datasets:
            raise GovernanceViolationError(f"Dataset {dataset} is not approved")
        return True
