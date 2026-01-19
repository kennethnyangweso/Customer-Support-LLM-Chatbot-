from router.prompt_router import route_prompt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PROMPTS_DIR = BASE_DIR / "prompts"


def load_prompt(filename: str) -> str:
    return (PROMPTS_DIR / filename).read_text(encoding="utf-8")


def generate_response(user_message: str, llm_client) -> str:
    route = route_prompt(user_message)

    if route == "billing":
        prompt = load_prompt("billing_prompt.txt")
    elif route == "technical":
        prompt = load_prompt("technical_prompt.txt")
    elif route == "escalation":
        prompt = load_prompt("escalation_prompt.txt")
    else:
        prompt = load_prompt("fallback_prompt.txt")

    final_prompt = f"""
{prompt}

User message:
{user_message}
"""

    return llm_client.generate(final_prompt)

