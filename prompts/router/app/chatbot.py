# src/chatbot.py

from router import route_prompt
from pathlib import Path

# -------------------------
# Utility: Load Prompt Text
# -------------------------
def load_prompt(prompt_name: str) -> str:
    prompt_path = Path("prompts") / f"{prompt_name}_prompt.txt"
    return prompt_path.read_text(encoding="utf-8")

# -------------------------
# Core Chatbot Logic
# -------------------------
def generate_response(user_message: str, llm_client) -> str:
    """
    Orchestrates routing and response generation.
    """

    # Step 1: Determine route
    route = route_prompt(user_message, llm_client)

    # Step 2: Load prompts
    system_prompt = load_prompt("system")
    task_prompt = load_prompt(route)

    # Step 3: Construct messages
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "system", "content": task_prompt},
        {"role": "user", "content": user_message},
    ]

    # Step 4: Call LLM
    response = llm_client.chat_completion(messages)

    return response
