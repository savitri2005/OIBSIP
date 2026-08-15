# 🎙️ Python Voice Assistant

## 📌 Project Overview

The Python Voice Assistant is a beginner-level voice-controlled application developed using Python as part of the Python Programming internship at Oasis Infobyte.

The application captures voice commands through a microphone, converts speech into text, processes the command, and provides responses using text-to-speech.

---

## ✨ Features

- 🎤 Voice input using a microphone
- 👋 Responds to "Hello"
- 🕐 Provides the current time
- 📅 Provides the current date
- 🕐📅 Provides both current time and date
- 🌐 Performs web searches
- 🔊 Provides spoken responses using text-to-speech
- ❌ Handles speech that cannot be understood
- ⚠️ Handles speech recognition errors
- 🚪 Supports an exit command

---

## 🛠️ Technologies Used

- Python 3.11
- SpeechRecognition
- PyAudio
- pyttsx3
- datetime
- webbrowser

---

## ⚙️ How It Works

The Voice Assistant works through the following process:

1. The application starts the voice assistant.
2. The microphone captures the user's voice.
3. SpeechRecognition converts the voice into text.
4. The recognized command is processed.
5. The appropriate action is performed.
6. pyttsx3 converts the response into spoken audio.
7. The assistant continues listening for new commands.
8. The assistant stops when the user says "exit", "quit", or "stop".

---

## 🎯 Supported Commands

### 👋 Greeting

Say:

```text
Hello


### ✅ That's all

You need **only this one `README.md`** for documentation.

Your folder can simply be:

```text
Python-Task1-VoiceAssistant/
│
├── main.py
└── README.md