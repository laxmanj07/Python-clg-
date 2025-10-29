# Creating a bot that responds to user inputs and stops when the user types "stop"

import random

print("Hello! I am your friendly chatbot. Type 'stop' anytime to end the chat.")

# Hard-coded responses
responses = [
    "I see what you mean.",
    "That's interesting!",
    "Hmm, tell me more.",
    "Oh really?",
    "I understand.",
    "Got it!",
    "Okay!"
]

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() == "stop":
        print("Bot: bye 👋")
        break
    else:
        print("Bot:", random.choice(responses))
