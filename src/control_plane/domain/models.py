from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from control_plane.domain.versioning import SchemaVersion


class SchemaValidationError(ValueError):
    """Raised when a domain schema fails validation."""


@dataclass(slots=True, frozen=True)
class BaseModel:
    id: str
    version: str = SchemaVersion.V1
    created_at: datetime = field(
        default_factory=lambda: datetime.now(tz=timezone.utc),  # noqa: UP017
    )
    metadata: dict[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.id:
            raise SchemaValidationError("id cannot be empty")
        SchemaVersion.validate(self.version)


@dataclass(slots=True, frozen=True)
class IntentModel(BaseModel):
    actor: str = "system"
    objective: str = ""
    constraints: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        BaseModel.__post_init__(self)
        if not self.objective:
            raise SchemaValidationError("objective cannot be empty")


@dataclass(slots=True, frozen=True)
class PlanModel(BaseModel):
    intent_id: str = ""
    steps: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        BaseModel.__post_init__(self)
        if not self.intent_id:
            raise SchemaValidationError("intent_id cannot be empty")
        if not self.steps:
            raise SchemaValidationError("steps cannot be empty")


@dataclass(slots=True, frozen=True)
class ExecutionModel(BaseModel):
    plan_id: str = ""
    status: str = "pending"

    def __post_init__(self) -> None:
        BaseModel.__post_init__(self)
        if not self.plan_id:
            raise SchemaValidationError("plan_id cannot be empty")
        if self.status not in {"pending", "running", "completed", "failed"}:
            raise SchemaValidationError(f"unsupported execution status: {self.status}")


@dataclass(slots=True, frozen=True)
class ArtifactModel(BaseModel):
    execution_id: str = ""
    uri: str = ""
    digest: str = ""

    def __post_init__(self) -> None:
        BaseModel.__post_init__(self)
        if not self.execution_id:
            raise SchemaValidationError("execution_id cannot be empty")
        if not self.uri:
            raise SchemaValidationError("uri cannot be empty")
        if not self.digest:
            raise SchemaValidationError("digest cannot be empty")


@dataclass(slots=True, frozen=True)
class DriftModel(BaseModel):
    resource_id: str = ""
    desired: dict[str, Any] = field(default_factory=dict)
    actual: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        BaseModel.__post_init__(self)
        if not self.resource_id:
            raise SchemaValidationError("resource_id cannot be empty")
        if self.desired == self.actual:
            raise SchemaValidationError(
                "drift model requires a difference between desired and actual"
            )


@dataclass(slots=True, frozen=True)
class PolicyModel(BaseModel):
    name: str = ""
    rules: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        BaseModel.__post_init__(self)
        if not self.name:
            raise SchemaValidationError("name cannot be empty")
        if not self.rules:
            raise SchemaValidationError("rules cannot be empty")
