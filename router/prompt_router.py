def route_prompt(user_message: str) -> str:
    text = user_message.lower()

    if any(word in text for word in ["bill", "charge", "payment", "refund", "invoice"]):
        return "billing"

    if any(word in text for word in ["error", "issue", "not working", "problem", "crash"]):
        return "technical"

    if any(word in text for word in ["human", "agent", "manager", "complaint"]):
        return "escalation"

    return "fallback"
