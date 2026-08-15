import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
from urllib.parse import quote


# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set speech properties
engine.setProperty("rate", 160)
engine.setProperty("volume", 1.0)


def speak(message):
    """Speak the given message using text-to-speech."""
    print("Assistant:", message)
    engine.say(message)
    engine.runAndWait()


def listen():
    """Capture voice input from the microphone."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        except sr.WaitTimeoutError:
            speak("I did not hear anything. Please try again.")
            return ""

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I could not understand what you said. Please repeat.")
        return ""

    except sr.RequestError:
        speak("Sorry, the speech recognition service is unavailable.")
        return ""


def tell_time():
    """Tell the current time."""
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}.")


def tell_date():
    """Tell the current date."""
    current_date = datetime.datetime.now().strftime("%A, %d %B %Y")
    speak(f"Today is {current_date}.")


def tell_time_and_date():
    """Tell both the current time and date."""
    now = datetime.datetime.now()

    current_time = now.strftime("%I:%M %p")
    current_date = now.strftime("%A, %d %B %Y")

    speak(f"The current time is {current_time}.")
    speak(f"Today is {current_date}.")


def web_search(topic):
    """Open a web search for the specified topic."""
    if not topic:
        speak("Please tell me what you want me to search for.")
        return

    speak(f"Searching the web for {topic}.")

    search_url = "https://www.google.com/search?q=" + quote(topic)
    webbrowser.open(search_url)


def process_command(command):
    """Process the recognized voice command."""

    if not command:
        return True

    # Greeting
    if "hello" in command or "hi" in command:
        speak("Hello Savitri! How can I help you?")

    # Time and date together
    elif ("time" in command and "date" in command) or "time and date" in command:
        tell_time_and_date()

    # Date only
    elif "date" in command:
        tell_date()

    # Time only
    elif "time" in command:
        tell_time()

    # Web search
    elif command.startswith("search for"):
        topic = command.replace("search for", "", 1).strip()
        web_search(topic)

    elif command.startswith("search"):
        topic = command.replace("search", "", 1).strip()
        web_search(topic)

    # Exit
    elif "exit" in command or "quit" in command or "stop" in command:
        speak("Goodbye! Have a nice day.")
        return False

    # Unknown command
    else:
        speak(
            "Sorry, I do not understand that command. "
            "Please say hello, ask for the time or date, "
            "or say search for followed by a topic."
        )

    return True


def main():
    """Main function of the voice assistant."""

    print("=" * 55)
    print("              PYTHON VOICE ASSISTANT")
    print("=" * 55)

    speak(
        "Hello Savitri. I am your voice assistant. "
        "You can say hello, ask for the time or date, "
        "or ask me to search for something."
    )

    running = True

    while running:
        command = listen()
        running = process_command(command)


if __name__ == "__main__":
    main()