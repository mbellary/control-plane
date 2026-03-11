import unittest

from control_plane.controllers.intent_controller import IntentController
from control_plane.controllers.plan_controller import PlanController


class ControllerTests(unittest.TestCase):
    def test_intent_controller_processes_intent(self) -> None:
        controller = IntentController()
        intent_hash = controller.process_intent({"b": 2, "a": 1})
        self.assertEqual(len(intent_hash), 64)

    def test_plan_controller_creates_service_plan(self) -> None:
        controller = PlanController()
        plan = controller.on_intent_created("intent-hash")
        self.assertIn("service_plan", plan)


if __name__ == "__main__":
    unittest.main()
