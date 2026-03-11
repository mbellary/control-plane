def create_intent(intent: dict) -> dict:
    return {"status": "accepted", "intent": intent}


def get_intent(intent_id: str) -> dict:
    return {"intent_id": intent_id, "status": "stored"}
