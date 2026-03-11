class EngineBinding:
    def bind(self, optimized_ir: dict) -> dict:
        return {"service_plan": optimized_ir, "engine": "default"}
