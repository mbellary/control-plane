import unittest

from controllers.execution_controller import ExecutionController


class IntegrationTests(unittest.TestCase):
    def test_execution_controller_generates_manifest(self) -> None:
        controller = ExecutionController()
        manifest = controller.execute({"id": "svc-plan"})
        self.assertIn("run_manifest", manifest)


if __name__ == "__main__":
    unittest.main()
