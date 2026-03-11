from control_plane.api.http_server import start_http_server
from control_plane.controllers.drift_controller import DriftController
from control_plane.controllers.execution_controller import ExecutionController
from control_plane.controllers.intent_controller import IntentController
from control_plane.controllers.plan_controller import PlanController


def main() -> None:
    intent_controller = IntentController()
    plan_controller = PlanController()
    execution_controller = ExecutionController()
    drift_controller = DriftController()

    intent_controller.start()
    plan_controller.start()
    execution_controller.start()
    drift_controller.start()

    start_http_server()


if __name__ == "__main__":
    main()
