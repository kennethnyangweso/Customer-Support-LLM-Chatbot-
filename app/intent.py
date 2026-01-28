# app/intent.py

def detect_intent(user_message):
    """
    Simple keyword-based intent detection.
    Returns: 'billing', 'technical', 'escalation', or 'fallback'
    """
    text = user_message.lower()

    # Billing-related keywords
    if any(word in text for word in ["charge", "billing", "invoice", "payment", "bill"]):
        return "billing"

    # Technical-related keywords
    elif any(word in text for word in ["error", "issue", "technical", "bug", "modem", "connection"]):
        return "technical"

    # Escalation keywords (user asking for human or frustrated)
    elif any(word in text for word in ["human", "agent", "supervisor", "complaint", "frustrated", "refund"]):
        return "escalation"

    # Default fallback
    else:
        return "fallback"
