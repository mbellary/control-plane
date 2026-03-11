from execution.adapter_resolver import AdapterResolver
from execution.execution_manager import ExecutionManager
from execution.run_manifest_generator import RunManifestGenerator


class ExecutionController:
    def __init__(self) -> None:
        self.adapter_resolver = AdapterResolver()
        self.execution_manager = ExecutionManager()
        self.manifest_generator = RunManifestGenerator()

    def start(self) -> None:
        return

    def execute(self, service_plan: dict) -> dict:
        adapter = self.resolve_adapter(service_plan)
        result = adapter.run(service_plan)
        run_manifest = self.generate_run_manifest(result)
        self.register_manifest(run_manifest)
        return run_manifest

    def resolve_adapter(self, service_plan: dict):
        return self.adapter_resolver.resolve(service_plan)

    def generate_run_manifest(self, result: dict) -> dict:
        return self.manifest_generator.generate(result)

    def register_manifest(self, run_manifest: dict) -> None:
        _ = run_manifest
