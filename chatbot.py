print("Bot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if "hello" in user:
        print("Bot: Hii!")

    elif "how are you" in user:
        print("Bot: I'm fine, thanks for asking!")

    elif "thank you" in user:
        print("Bot: You're welcome!")

    elif "bye" in user:
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: I didn't understand.")