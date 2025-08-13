import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

qa_dict = {
    "tell me a joke": "Why did the computer go to the doctor? Because it caught a virus.",
    "another joke": "Why don’t programmers like nature? Too many bugs.",
    "make me laugh": "Why do Java developers wear glasses? Because they can’t C sharp.",
    "i am bored": "Let's play a game or talk about your favorite movie.",
    "do you like music": "Yes! Music makes everything better.",
    "recommend a song": "Try 'Shape of You' by Ed Sheeran.",
    "recommend a movie": "Watch 'Inception' for a great sci-fi experience."
}

def get_response(user_input):
    return qa_dict.get(user_input, "Sorry, I don't understand that yet.")

def main():
    print("Jokes & Fun Chatbot: Type 'bye' to exit.")
    speak("Hello! I am your fun chatbot. Type bye to exit.")
    while True:
        user_input = input("You: ").strip().lower()
        response = get_response(user_input)
        print(f"Chatbot: {response}")
        speak(response)
        if user_input == "bye":
            break

if __name__ == "__main__":
    main()
