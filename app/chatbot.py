from pathlib import Path
from router.prompt_router import route_prompt


def load_prompt(filename):
    path = Path("prompts") / filename
    return path.read_text(encoding="utf-8")


def generate_response(user_message, llm_client):
    route = route_prompt(user_message, llm_client)

    system_prompt = load_prompt("system_prompt.txt")
    task_prompt = load_prompt(f"{route}_prompt.txt")

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "system", "content": task_prompt},
        {"role": "user", "content": user_message},
    ]

    return llm_client.chat_completion(messages)
