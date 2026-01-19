# app/cli_1.py
import sys
from app.chatbot import generate_response
from app.llm_client_1 import LLMClient1

def run():
    print("Customer Support Bot (type 'exit' to quit)")
    # Instantiate realistic local LLM
    llm_client = LLMClient1()

    while True:
        try:
            user_input = input("User: ").strip()
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting chatbot. Goodbye!")
                break

            # Generate response using your routing + LLM
            response = generate_response(user_input, llm_client)
            print("Bot:", response)
            print("\n")  # blank line for readability

        except KeyboardInterrupt:
            print("\nExiting chatbot. Goodbye!")
            break
        except Exception as e:
            print(f"[ERROR] {e}")

if __name__ == "__main__":
    run()
