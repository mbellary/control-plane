class DriftController:
    def start(self) -> None:
        return

    def monitor(self) -> None:
        while False:
            drift_events = self.detect_drift()
            for event in drift_events:
                self.trigger_reconciliation(event)

    def detect_drift(self) -> list[dict]:
        return []

    def trigger_reconciliation(self, event: dict) -> None:
        _ = event
