def chatbot():
    print("Hello! Type 'bye' to exit")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("chatbot:'Bye!")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("chatbot: Hi there! How can I help you?")

        elif "about you" in user_input:
            print("chatbot: I am a simple rule-based chatbot")

        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M")
            print(f"Time:{now}")

        elif "weather" in user_input:
            print("Live Weather is currently unavailable")

        else:
            print("Sorry, I don't understand that")


chatbot()