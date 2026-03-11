from control_plane.compiler.engine_binding import EngineBinding
from control_plane.compiler.ir_builder import IRBuilder
from control_plane.compiler.optimizer_pass import OptimizerPass
from control_plane.compiler.validation_pass import ValidationPass


class ServicePlanCompiler:
    def __init__(self) -> None:
        self.ir_builder = IRBuilder()
        self.validation = ValidationPass()
        self.optimizer = OptimizerPass()
        self.engine_binding = EngineBinding()

    def compile(self, resolved_plan: dict) -> dict:
        ir = self.build_ir(resolved_plan)
        self.validate(ir)
        optimized_ir = self.optimize(ir)
        physical_plan = self.bind_engine(optimized_ir)
        return physical_plan

    def build_ir(self, resolved_plan: dict) -> dict:
        return self.ir_builder.build(resolved_plan)

    def validate(self, ir: dict) -> None:
        self.validation.validate(ir)

    def optimize(self, ir: dict) -> dict:
        return self.optimizer.optimize(ir)

    def bind_engine(self, optimized_ir: dict) -> dict:
        return self.engine_binding.bind(optimized_ir)
