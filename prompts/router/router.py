# src/router.py

from pathlib import Path


def load_router_prompt() -> str:
    """
    Loads the prompt router instructions from file.
    """
    router_path = Path("prompts") / "prompt_router.txt"
    return router_path.read_text(encoding="utf-8")


def route_prompt(user_message: str, llm_client) -> str:
    """
    Uses the LLM to classify the user's message
    into a routing category.
    """

    router_prompt = load_router_prompt()

    messages = [
        {"role": "system", "content": router_prompt},
        {"role": "user", "content": user_message},
    ]

    route = llm_client.chat_completion(messages).strip().lower()

    # Safety guard: fallback if unexpected output
    allowed_routes = {"billing", "technical", "escalation", "fallback"}
    if route not in allowed_routes:
        return "fallback"

    return route
