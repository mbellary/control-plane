import unittest

from control_plane.reconciliation.reconciliation_engine import ReconciliationEngine


class ReconciliationTests(unittest.TestCase):
    def test_reconcile_detects_drift(self) -> None:
        engine = ReconciliationEngine()
        result = engine.reconcile({"desired": 1}, {"desired": 2})
        self.assertEqual(result["status"], "reconciled")


if __name__ == "__main__":
    unittest.main()
