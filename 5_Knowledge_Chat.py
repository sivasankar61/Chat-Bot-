import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

qa_dict = {
    "what is cpu": "CPU is the Central Processing Unit — the brain of the computer.",
    "what is ram": "RAM is Random Access Memory — temporary memory for processing data.",
    "what is an operating system": "An OS is software that manages computer hardware and software.",
    "what is a programming language": "A programming language is used to give instructions to a computer.",
    "what is cloud computing": "Cloud computing is storing and accessing data over the internet.",
    "what is cybersecurity": "Cybersecurity protects systems from digital attacks.",
    "what is hacking": "Hacking is unauthorized access to computer systems.",
    "what is a virus": "A computer virus is malicious software that can harm a system.",
    "difference between hardware and software": "Hardware is the physical part of a computer, software is the programs."
}

def get_response(user_input):
    return qa_dict.get(user_input, "Sorry, I don't understand that yet.")

def main():
    print("Computer Knowledge Chatbot: Type 'bye' to exit.")
    speak("Hello! I am your computer knowledge chatbot. Type bye to exit.")
    while True:
        user_input = input("You: ").strip().lower()
        response = get_response(user_input)
        print(f"Chatbot: {response}")
        speak(response)
        if user_input == "bye":
            break

if __name__ == "__main__":
    main()
