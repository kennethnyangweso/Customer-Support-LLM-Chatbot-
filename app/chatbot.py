from router.prompt_router import route_prompt
from pathlib import Path

def load_prompt(file_name: str) -> str:
    return (Path("prompts") / file_name).read_text(encoding="utf-8")

SYSTEM_PROMPT = load_prompt("system_prompt.txt")
BILLING_PROMPT = load_prompt("billing_prompt.txt")
TECHNICAL_PROMPT = load_prompt("technical_prompt.txt")
ESCALATION_PROMPT = load_prompt("escalation_prompt.txt")
FALLBACK_PROMPT = load_prompt("fallback_prompt.txt")


def generate_response(user_message: str, llm_client) -> str:
    route = route_prompt(user_message)

    print("[DEBUG] Raw user_message:", user_message)
    print("[DEBUG] Normalized text:", user_message.lower())
    print(f"[DEBUG] → {route} matched")

    if route == "billing":
        domain_prompt = BILLING_PROMPT
    elif route == "technical":
        domain_prompt = TECHNICAL_PROMPT
    elif route == "escalation":
        domain_prompt = ESCALATION_PROMPT
    else:
        domain_prompt = FALLBACK_PROMPT

    messages = [
        {
            "role": "system",
            "content": f"{SYSTEM_PROMPT}\n\n{domain_prompt}"
        },
        {
            "role": "user",
            "content": user_message
        }
    ]

    return llm_client.generate(messages)


