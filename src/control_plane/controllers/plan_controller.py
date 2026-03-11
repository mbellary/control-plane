from control_plane.compiler.service_plan_compiler import ServicePlanCompiler
from control_plane.planner_client.planner_client import PlannerClient


class PlanController:
    def __init__(self) -> None:
        self.planner_client = PlannerClient()
        self.compiler = ServicePlanCompiler()

    def start(self) -> None:
        return

    def on_intent_created(self, intent_hash: str) -> dict:
        intent = self.load_intent(intent_hash)
        resolved_plan = self.call_planner(intent)
        service_plan = self.compile_service_plan(resolved_plan)
        self.register_plan(service_plan)
        return service_plan

    def load_intent(self, intent_hash: str) -> dict:
        return {"intent_hash": intent_hash}

    def call_planner(self, intent: dict) -> dict:
        return self.planner_client.generate_plan(intent)

    def compile_service_plan(self, resolved_plan: dict) -> dict:
        return self.compiler.compile(resolved_plan)

    def register_plan(self, service_plan: dict) -> None:
        _ = service_plan
