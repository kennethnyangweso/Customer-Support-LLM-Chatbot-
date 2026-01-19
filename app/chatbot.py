# app/chatbot.py
from router.prompt_router import route_prompt
from pathlib import Path

# Function to load domain prompts
def load_prompt(file_name: str) -> str:
    path = Path("prompts") / file_name
    return path.read_text(encoding="utf-8")


# Load all prompts once at startup
SYSTEM_PROMPT = load_prompt("system_prompt.txt")
BILLING_PROMPT = load_prompt("billing_prompt.txt")
TECHNICAL_PROMPT = load_prompt("technical_prompt.txt")
ESCALATION_PROMPT = load_prompt("escalation_prompt.txt")
FALLBACK_PROMPT = load_prompt("fallback_prompt.txt")


def generate_response(user_message: str, llm_client) -> str:
    """
    Main function to generate chatbot response.
    user_message: string input from user
    llm_client: either mock LLM or real local LLMClient1
    """

    # Step 1: Determine which prompt to use
    route = route_prompt(user_message)

    # Debug prints
    print("[DEBUG] Raw user_message:", user_message)
    print("[DEBUG] Normalized text:", user_message.lower())
    print(f"[DEBUG] → {route} matched")

    # Step 2: Select prompt based on routing
    if route == "billing":
        domain_prompt = BILLING_PROMPT
    elif route == "technical":
        domain_prompt = TECHNICAL_PROMPT
    elif route == "escalation":
        domain_prompt = ESCALATION_PROMPT
    else:
        domain_prompt = FALLBACK_PROMPT

    # Step 3: Combine with system prompt
    final_prompt = f"{SYSTEM_PROMPT}\n\n{domain_prompt}\n\nUser message:\n{user_message}"

    # Step 4: Generate response using provided LLM client
    try:
        return llm_client.generate(final_prompt)
    except Exception as e:
        # Fallback if LLM client fails
        return f"[ERROR generating response: {e}]"

