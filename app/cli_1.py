# app/cli_1.py
from app.chatbot import generate_response
from app.llm_client_1 import LLMClient1


def run():
    print("Customer Support Bot (type 'exit' to quit)")
    llm_client = LLMClient1()

    while True:
        try:
            user_input = input("User: ").strip()
            if user_input.lower() in ("exit", "quit"):
                print("Exiting chatbot. Goodbye!")
                break

            response = generate_response(user_input, llm_client)
            print("Bot:", response)
            print()

        except KeyboardInterrupt:
            print("\nExiting chatbot. Goodbye!")
            break
        except Exception as e:
            print(f"[ERROR] {e}")


if __name__ == "__main__":
    run()

