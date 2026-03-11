class Adapter:
    def run(self, service_plan: dict) -> dict:
        return {"status": "completed", "service_plan": service_plan}

    def execute(self, service_plan: dict) -> dict:
        return self.run(service_plan)


class AdapterResolver:
    def resolve(self, service_plan: dict) -> Adapter:
        _ = service_plan
        return Adapter()
