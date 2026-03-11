from __future__ import annotations


class SchemaVersion:
    V1 = "v1"

    SUPPORTED = {V1}
    DEPRECATED: set[str] = set()

    @classmethod
    def validate(cls, version: str) -> None:
        if version not in cls.SUPPORTED:
            raise ValueError(f"unsupported schema version: {version}")

    @classmethod
    def is_deprecated(cls, version: str) -> bool:
        cls.validate(version)
        return version in cls.DEPRECATED

    @classmethod
    def negotiate(cls, requested_version: str | None) -> str:
        if requested_version is None:
            return cls.V1
        cls.validate(requested_version)
        return requested_version
