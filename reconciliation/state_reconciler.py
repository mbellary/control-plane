class StateReconciler:
    def correct(self, drift: dict) -> dict:
        return {"status": "reconciled", "details": drift}
