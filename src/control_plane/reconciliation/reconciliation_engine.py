from control_plane.reconciliation.drift_detector import DriftDetector
from control_plane.reconciliation.state_reconciler import StateReconciler


class ReconciliationEngine:
    def __init__(self) -> None:
        self.drift_detector = DriftDetector()
        self.state_reconciler = StateReconciler()

    def reconcile(self, desired_state: dict, actual_state: dict) -> dict:
        drift = self.detect_drift(desired_state, actual_state)
        if drift:
            return self.correct_state(drift)
        return {"status": "in_sync"}

    def detect_drift(self, desired_state: dict, actual_state: dict) -> dict:
        return self.drift_detector.detect(desired_state, actual_state)

    def correct_state(self, drift: dict) -> dict:
        return self.state_reconciler.correct(drift)
