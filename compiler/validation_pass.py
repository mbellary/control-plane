class ValidationPass:
    def validate(self, ir: dict) -> None:
        if not ir:
            raise ValueError("IR cannot be empty")
