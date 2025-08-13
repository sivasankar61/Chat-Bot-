import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

qa_dict = {
    "what is python": "Python is a popular programming language used for many purposes.",
    "what is ai": "AI means Artificial Intelligence — machines simulating human intelligence.",
    "what is machine learning": "Machine learning is teaching computers to learn patterns from data.",
    "what is the internet": "The internet is a global network connecting millions of computers.",
    "what is a chatbot": "A chatbot is a program that talks to people using text or voice.",
    "what is programming": "Programming is giving instructions to a computer to perform tasks.",
    "difference between ai and ml": "AI is the concept of smart machines, ML is how they learn.",
    "who invented the computer": "Charles Babbage is considered the father of the computer."
}

def get_response(user_input):
    return qa_dict.get(user_input, "Sorry, I don't understand that yet.")

def main():
    print("Technical Chatbot: Type 'bye' to exit.")
    speak("Hello! I am your technical chatbot. Type bye to exit.")
    while True:
        user_input = input("You: ").strip().lower()
        response = get_response(user_input)
        print(f"Chatbot: {response}")
        speak(response)
        if user_input == "bye":
            break

if __name__ == "__main__":
    main()
