def route_prompt(user_message: str) -> str:
    print("[DEBUG] Raw user_message:", user_message)

    text = user_message.lower()
    print("[DEBUG] Normalized text:", text)

    if any(word in text for word in ["bill", "charge", "charged", "payment", "refund", "invoice"]):
        print("[DEBUG] → billing matched")
        return "billing"

    if any(word in text for word in ["error", "issue", "problem", "not working", "crash", "internet"]):
        print("[DEBUG] → technical matched")
        return "technical"

    if any(word in text for word in ["human", "agent", "manager", "complaint", "escalate"]):
        print("[DEBUG] → escalation matched")
        return "escalation"

    print("[DEBUG] → fallback matched")
    return "fallback"
