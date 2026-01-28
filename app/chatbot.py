from pathlib import Path
import random

PROMPT_DIR = Path(__file__).parent / "prompts"

# -------------------------------
# Load prompt files
# -------------------------------
def load_prompt(prompt_name):
    """Load a text prompt file."""
    path = PROMPT_DIR / f"{prompt_name}.txt"
    return path.read_text(encoding="utf-8")

def get_prompt_by_intent(intent):
    """Return intent-specific prompt text."""
    if intent == "billing":
        return load_prompt("billing")
    elif intent == "technical":
        return load_prompt("technical")
    elif intent == "escalation":
        return load_prompt("escalation")
    else:
        return load_prompt("fallback")

def build_prompt(user_message, intent):
    """Combine system + intent prompt + user message for LLM."""
    system_prompt = load_prompt("system")
    intent_prompt = get_prompt_by_intent(intent)

    final_prompt = f"""
{system_prompt}

{intent_prompt}

User message:
"{user_message}"

Respond naturally and professionally.
"""
    return final_prompt.strip()

# -------------------------------
# Pre-written human-like responses
# -------------------------------
BILLING_RESPONSES = [
    "I’m sorry for the inconvenience this may have caused. Duplicate charges can sometimes occur due to pending transactions or billing overlaps. I recommend reviewing your latest invoice to confirm whether one charge is temporary. If you’d like, I can guide you on how to check this.",
    "Thank you for reaching out. Duplicate charges can occasionally happen due to pending authorizations. Please check your latest billing statement, and I can assist further if both charges appear.",
    "I understand this is frustrating. Sometimes charges appear twice due to system delays. Have you had a chance to review your recent invoice?"
]

TECHNICAL_RESPONSES = [
    "I’m sorry you’re experiencing technical difficulties. Have you tried restarting your device or checking your network connection?",
    "Let’s troubleshoot this together. Can you provide more details about the issue or any error messages you see?",
    "Thank you for reporting this. A quick first step is to restart the device and see if the problem persists."
]

ESCALATION_RESPONSES = [
    "I understand your frustration and I can escalate this to a human agent who can assist further.",
    "Thank you for your patience. I’m escalating this issue to a supervisor who will be in touch shortly.",
]

FALLBACK_RESPONSES = [
    "I’m here to help. Could you provide more details about the issue?",
    "I’m not sure I fully understand. Can you clarify your request so I can assist you better?",
]

# -------------------------------
# Main response function
# -------------------------------
def generate_response(user_message, intent, llm=None):
    """
    Generate a response for the user.
    
    Parameters:
    - user_message: str
    - intent: str
    - llm: optional, any LLM object with an 'invoke(prompt)' method
    
    Returns:
    - response: str
    """

    # Build the prompt (for LLM use)
    prompt = build_prompt(user_message, intent)

    if llm:
        # Example for Hugging Face / OpenAI LLMs
        response = llm.invoke(prompt)  # Replace with your model's API call
        return response.strip()

    # Fallback to pre-written human-like responses
    if intent == "billing":
        return random.choice(BILLING_RESPONSES)
    elif intent == "technical":
        return random.choice(TECHNICAL_RESPONSES)
    elif intent == "escalation":
        return random.choice(ESCALATION_RESPONSES)
    else:
        return random.choice(FALLBACK_RESPONSES)

