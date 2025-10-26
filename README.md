🧠 AG3 — AI-Powered Desktop Voice Assistant

AG3 is a smart desktop voice assistant built in Python with a sleek PyQt5 GUI.
It listens, understands, and responds to your commands — from web searches to Wikipedia queries, music playback, and even system operations — all hands-free.

AG3 combines Speech Recognition, System Speech API, and AI enhancements to make your everyday computer interactions faster and more natural.

✨ What’s New

This is an improved version of my earlier project — now upgraded with:

Smarter, more stable speech engine

Dual speech synthesis support (System.Speech + pyttsx3)

AI-based voice handling with fallbacks for different environments

Cleaner and safer threading with PyQt5 signals

Improved user feedback and error handling

Even though the core logic remains the same, these small yet thoughtful AI-driven updates made AG3 smoother, faster, and more intuitive 🌟

🎯 Key Features

✅ Voice recognition via speech_recognition
✅ Text-to-speech using:

System.Speech.Synthesis (Windows native)

pyttsx3 (cross-platform fallback)

PowerShell (backup voice output)
✅ Wikipedia search and summarized results
✅ Quick access to popular websites:

YouTube, Google, Stack Overflow, Quora, Instagram, Facebook, and more
✅ System controls:

Open VS Code, Command Prompt, check IP address, play music, tell time
✅ Polished PyQt5 GUI with live status display and animations (ag3.gif)
✅ Multi-threaded event handling — no freezing during recognition or playback

🧩 Tech Stack
Component	Purpose
Python 3.x	Core language
PyQt5	GUI and threading
speech_recognition	Microphone voice input
System.Speech / pyttsx3	Text-to-speech synthesis
wikipedia	Fetch summarized info
requests	IP lookup
subprocess, os, webbrowser	System and web integrations
⚙️ Setup Instructions

Clone the repository:

git clone https://github.com/<yourusername>/AG3-Voice-Assistant.git
cd AG3-Voice-Assistant


Create a virtual environment:

python -m venv .venv
.venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Run the assistant:

python AG3.py

🗣️ Voice System Setup

AG3 automatically detects available speech engines:

System.Speech (default on Windows)

pyttsx3 (auto fallback if System.Speech unavailable)

PowerShell speech (final fallback)

If you face this error:

Could not load file or assembly 'System.Speech'


➡️ Install .NET Framework 4.8:
🔗 https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48

🎨 User Interface Preview
Idle	Listening	Speaking

	
	

(Replace with your actual screenshots or AG3.gif preview)

💬 Example Commands
Command	Action
“Open YouTube”	Launches YouTube in your browser
“Search Wikipedia for Python”	Speaks and shows Wikipedia summary
“Play music”	Plays a random song from your music folder
“What’s the time now?”	Tells current time
“Open VS Code”	Opens Visual Studio Code
“IP address?”	Reads out your public IP
"shut up" it will stop loop
"search" with using search video you can search anything on google with this
“Bye” or “Just shut up”	Stops the assistant
💻 Project Structure
AG3/
│
├── ag3ui.py            # PyQt5 UI file
├── AG3.py              # Main application logic
├── ag3.gif             # Animation for GUI
├── requirements.txt    # Dependencies
└── assets/             # Optional screenshots

💡 Future Enhancements

Add NLP-powered conversational mode

Integrate OpenAI or LLM-based dialogue for contextual replies

Add weather and calendar integrations

UI voice settings for tone, pitch, and gender

🧑‍💻 Author

Vaishnavi Sutar
Developer of AG3 Assistant
📍 Maharashtra, India

“Even small improvements can make your code more alive — AI just makes it smarter.” 💬
