from app.chatbot_1 import generate_llm_response

def main():
    print("Customer Support Bot (LLM) — type 'exit' to quit")

    while True:
        user_input = input("User: ").strip()
        if user_input.lower() == "exit":
            break

        if "charge" in user_input.lower() or "bill" in user_input.lower():
            intent = "billing"
        elif "internet" in user_input.lower() or "network" in user_input.lower():
            intent = "technical"
        elif "human" in user_input.lower():
            intent = "escalation"
        else:
            intent = "fallback"

        response = generate_llm_response(user_input, intent)
        print(f"Bot: {response}\n")

if __name__ == "__main__":
    main()


