from control_plane.execution.adapter_resolver import Adapter


class ExecutionManager:
    def run(self, service_plan: dict) -> dict:
        runtime = self.resolve_runtime(service_plan)
        return runtime.execute(service_plan)

    def resolve_runtime(self, service_plan: dict) -> Adapter:
        _ = service_plan
        return Adapter()
