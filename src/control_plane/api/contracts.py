from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from control_plane.domain.versioning import SchemaVersion


@dataclass(slots=True, frozen=True)
class ApiError:
    code: str
    message: str


@dataclass(slots=True, frozen=True)
class Pagination:
    limit: int = 100
    cursor: str | None = None

    def __post_init__(self) -> None:
        if self.limit < 1 or self.limit > 1000:
            raise ValueError("limit must be between 1 and 1000")


@dataclass(slots=True, frozen=True)
class ApiEnvelope:
    version: str
    request_id: str
    data: dict[str, Any] | None = None
    error: ApiError | None = None

    def __post_init__(self) -> None:
        SchemaVersion.validate(self.version)
        if not self.request_id:
            raise ValueError("request_id cannot be empty")
        if self.data is None and self.error is None:
            raise ValueError("either data or error must be supplied")

    def to_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {
            "version": self.version,
            "request_id": self.request_id,
        }
        if self.data is not None:
            result["data"] = self.data
        if self.error is not None:
            result["error"] = {"code": self.error.code, "message": self.error.message}
        return result
