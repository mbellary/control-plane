from dataclasses import dataclass


@dataclass
class ArtifactRecord:
    hash: str
    kind: str


@dataclass
class CapabilityRecord:
    name: str
    version: str
