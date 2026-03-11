class ArtifactRegistryClient:
    def register_artifact(self, artifact: dict) -> str:
        return artifact.get("hash", "artifact-hash")
