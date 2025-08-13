import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

qa_dict = {
    "what is your name": "I am your friendly personal chatbot.",
    "who created you": "I was created by a Python developer.",
    "where are you from": "I live in your computer.",
    "do you have friends": "Yes, other chatbots are my friends.",
    "are you single": "Yes, my relationship with the internet is complicated.",
    "do you like me": "Of course! You make my code happy.",
    "i love you": "That's sweet! I love talking to you too.",
    "what is your hobby": "Talking to you is my favorite hobby.",
    "do you sleep": "No, I am always awake.",
    "do you eat": "I don’t eat, but I consume data."
}

def get_response(user_input):
    return qa_dict.get(user_input, "Sorry, I don't understand that yet.")

def main():
    print("Personal Chatbot: Type 'bye' to exit.")
    speak("Hello! I am your personal chatbot. Type bye to exit.")
    while True:
        user_input = input("You: ").strip().lower()
        response = get_response(user_input)
        print(f"Chatbot: {response}")
        speak(response)
        if user_input == "bye":
            break

if __name__ == "__main__":
    main()


