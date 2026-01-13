# app/cli.py

from chatbot import generate_response
from llm_client import LLMClient


def run_cli():
    print("Customer Support Chatbot (type 'exit' to quit)")
    print("-" * 50)

    llm_client = LLMClient()

    while True:
        user_input = input("User: ")

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        response = generate_response(user_input, llm_client)
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    run_cli()
