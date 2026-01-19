import sys
from pathlib import Path

# Fix imports
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from app.chatbot import generate_response
from app.llm_client import LLMClient

def run():
    llm_client = LLMClient()
    print("Customer Support Bot (type 'exit' to quit)")

    while True:
        user_input = input("User: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        response = generate_response(user_input, llm_client)
        print("Bot:", response)

if __name__ == "__main__":
    run()


