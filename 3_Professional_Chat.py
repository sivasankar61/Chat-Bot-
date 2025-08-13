import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

qa_dict = {
    "what can you do": "I can help with work-related questions and ideas.",
    "can you help me with work": "Yes, tell me about your project and I'll assist.",
    "how can i improve my skills": "Practice daily, learn from resources, and take small projects.",
    "what are trending technologies": "AI, Blockchain, Cloud Computing, and IoT are trending.",
    "how can i prepare for an interview": "Research the company, practice common questions, and be confident.",
    "what are soft skills": "Soft skills include communication, teamwork, and adaptability.",
    "what is teamwork": "Teamwork is working together to achieve a common goal."
}

def get_response(user_input):
    return qa_dict.get(user_input, "Sorry, I don't understand that yet.")

def main():
    print("Professional Chatbot: Type 'bye' to exit.")
    speak("Hello! I am your professional chatbot. Type bye to exit.")
    while True:
        user_input = input("You: ").strip().lower()
        response = get_response(user_input)
        print(f"Chatbot: {response}")
        speak(response)
        if user_input == "bye":
            break

if __name__ == "__main__":
    main()
