class DriftDetector:
    def detect(self, desired_state: dict, actual_state: dict) -> dict:
        if desired_state != actual_state:
            return {"drift": True, "desired": desired_state, "actual": actual_state}
        return {}
