import pytest

from control_plane.domain.models import (
    DriftModel,
    IntentModel,
    PlanModel,
    SchemaValidationError,
)
from control_plane.domain.versioning import SchemaVersion


def test_intent_model_requires_objective() -> None:
    with pytest.raises(SchemaValidationError):
        IntentModel(id="intent-1", objective="")


def test_plan_model_validates_required_fields() -> None:
    with pytest.raises(SchemaValidationError):
        PlanModel(id="plan-1", intent_id="", steps=("compile",))


def test_drift_model_requires_difference() -> None:
    with pytest.raises(SchemaValidationError):
        DriftModel(id="drift-1", resource_id="svc", desired={"a": 1}, actual={"a": 1})


def test_schema_version_negotiates_default() -> None:
    assert SchemaVersion.negotiate(None) == SchemaVersion.V1
