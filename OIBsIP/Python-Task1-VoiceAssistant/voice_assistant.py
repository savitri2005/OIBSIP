"""
VOICE ASSISTANT - Task 1 (Beginner Tier)
Oasis Infobyte - Python Programming Internship
Author: Your Full Name
"""

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import time
import sys

# ============================================
# INITIALIZE TEXT-TO-SPEECH ENGINE
# ============================================
def initialize_engine():
    """Initialize the text-to-speech engine"""
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)    # Speed of speech
        engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
        return engine
    except Exception as e:
        print(f"Error initializing speech engine: {e}")
        return None

# ============================================
# SPEAK FUNCTION
# ============================================
def speak(engine, text):
    """Convert text to speech and print it"""
    print(f"🤖 Assistant: {text}")
    if engine:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"Speech error: {e}")

# ============================================
# LISTEN FUNCTION (Voice Input)
# ============================================
def listen():
    """Listen to microphone and return recognized text"""
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            print("\n🎤 Listening... (Speak now)")
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            try:
                # Listen with timeout (5 seconds)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                print("🔄 Processing your voice...")
                
                # Use Google Speech Recognition (requires internet)
                text = recognizer.recognize_google(audio)
                print(f"🗣️ You said: {text}")
                return text.lower()
                
            except sr.WaitTimeoutError:
                print("⏰ No speech detected. Please try again.")
                return None
                
            except sr.UnknownValueError:
                print("❌ Sorry, I couldn't understand that.")
                return None
                
            except sr.RequestError:
                print("🌐 Network error! Please check your internet connection.")
                return None
                
            except Exception as e:
                print(f"❌ Error: {e}")
                return None
                
    except OSError:
        print("❌ Microphone not found! Please connect a microphone.")
        return None
    except Exception as e:
        print(f"❌ Microphone error: {e}")
        return None

# ============================================
# GREETING FUNCTION
# ============================================
def wish_user(engine):
    """Greet the user based on current time"""
    try:
        hour = datetime.datetime.now().hour
        
        if 5 <= hour < 12:
            greeting = "Good morning"
        elif 12 <= hour < 17:
            greeting = "Good afternoon"
        elif 17 <= hour < 21:
            greeting = "Good evening"
        else:
            greeting = "Good night"
        
        speak(engine, f"{greeting}, sir! I am your voice assistant.")
        speak(engine, "How can I help you today?")
        speak(engine, "You can say hello, time, date, search, or exit.")
    except Exception as e:
        print(f"Error in greeting: {e}")

# ============================================
# PROCESS COMMANDS
# ============================================
def process_command(engine, command):
    """Process the user's voice command"""
    
    # COMMAND 1: Hello
    if "hello" in command or "hi" in command or "hey" in command:
        speak(engine, "Hello there! How are you doing?")
        return True
    
    # COMMAND 2: Time
    elif "time" in command:
        try:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(engine, f"The current time is {current_time}")
        except Exception as e:
            speak(engine, "Sorry, I couldn't get the time.")
            print(f"Time error: {e}")
        return True
    
    # COMMAND 3: Date
    elif "date" in command or "today" in command:
        try:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(engine, f"Today's date is {current_date}")
        except Exception as e:
            speak(engine, "Sorry, I couldn't get the date.")
            print(f"Date error: {e}")
        return True
    
    # COMMAND 4: Web Search
    elif "search" in command:
        try:
            # Extract search query
            search_query = command.replace("search", "").strip()
            if not search_query or search_query == "":
                speak(engine, "What would you like me to search for?")
                return True
            
            speak(engine, f"Searching for {search_query} on the web.")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            speak(engine, "I have opened the browser with your search results.")
        except Exception as e:
            speak(engine, "Sorry, I couldn't perform the search.")
            print(f"Search error: {e}")
        return True
    
    # COMMAND 5: Exit/Quit
    elif "exit" in command or "quit" in command or "bye" in command or "goodbye" in command:
        speak(engine, "Goodbye! Have a great day!")
        return False
    
    # Unknown Command - Graceful Error Handling
    else:
        speak(engine, "I'm sorry, I didn't understand that command.")
        speak(engine, "Please try saying: hello, time, date, search, or exit.")
        return True

# ============================================
# MAIN FUNCTION
# ============================================
def main():
    """Main program loop"""
    
    print("\n" + "="*60)
    print("     🤖 VOICE ASSISTANT - Python Task 1")
    print("     Oasis Infobyte Internship")
    print("="*60)
    print("\n📝 Commands you can say:")
    print("   • 'Hello' - Get a greeting")
    print("   • 'Time' - Get current time")
    print("   • 'Date' - Get today's date")
    print("   • 'Search [topic]' - Search on Google")
    print("   • 'Exit' - Quit the assistant")
    print("="*60 + "\n")
    
    # Initialize text-to-speech engine
    engine = initialize_engine()
    if not engine:
        print("❌ Failed to initialize speech engine. Exiting...")
        sys.exit(1)
    
    # Greet the user
    wish_user(engine)
    
    # Main loop
    while True:
        try:
            # Listen for voice command
            command = listen()
            
            if command is None:
                speak(engine, "I didn't catch that. Could you please repeat?")
                continue
            
            # Process the command
            keep_running = process_command(engine, command)
            
            if not keep_running:
                break  # Exit the loop if user said "exit"
            
            # Small pause before next listening
            time.sleep(1)
            
        except KeyboardInterrupt:
            print("\n👋 Program interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            speak(engine, "Sorry, something went wrong. Let's continue.")
            time.sleep(2)

# ============================================
# PROGRAM ENTRY POINT
# ============================================
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Program interrupted. Goodbye!")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        print("Please restart the program.")