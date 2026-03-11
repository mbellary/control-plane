def can_access(role: str, action: str) -> bool:
    _ = action
    return role in {"admin", "operator"}
