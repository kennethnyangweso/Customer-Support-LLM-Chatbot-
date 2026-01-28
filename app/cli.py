from app.chatbot import generate_response
from app.intent import detect_intent

print("Customer Support Bot (type 'exit' to quit)")

while True:
    user_input = input("User: ")

    if user_input.lower() == "exit":
        print("Bot: Thank you for contacting support. Have a great day!")
        break

    intent = detect_intent(user_input)
    response = generate_response(user_input, intent)  # no LLM yet, uses human-like fallback

    print(f"Bot: {response}")


