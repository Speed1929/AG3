import speech_recognition as sr
import time
import wikipedia
import webbrowser
import os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from ag3ui import Ui_MainWindow
import sys
import random
from requests import get
import subprocess

def speak(audio):
    try:
        print(f"Speaking: {audio}")
        # Use PowerShell to access Windows Speech API
        # Escape single quotes in the text
        text = audio.replace("'", "''")
        # Create PowerShell command to speak text
        command = f'powershell -command "Add-Type -AssemblyName System.Speech; $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; $speak.Speak(\'{text}\')"'
        # Execute the command
        subprocess.call(command, shell=True)
    except Exception as e:
        print(f"Speech error: {e}")
        # Print the speech as fallback
        print(f"SPEECH: {audio}")

def intro(thread_instance):
    hour = int(time.strftime('%H'))
    if 0 <= hour < 12:
        thread_instance.speak_signal.emit("good morning master!,I am AG3! How can I help you?")
    elif 12 <= hour < 18:
        thread_instance.speak_signal.emit("good afternoon master!,I am AG3! How can I help you?")
    else:
        thread_instance.speak_signal.emit("good evening master!,I am AG3! How can I help you?")

class mainthread(QThread):
    speak_signal = pyqtSignal(str)  # Signal for thread-safe speech

    def __init__(self):
        super(mainthread, self).__init__()
        self.speak_signal.connect(speak)  # Connect signal to speak function

    def listen(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening..")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                print("Recognizing..")
                self.query = recognizer.recognize_google(audio)
                print(f"User: {self.query}")
                if self.query:
                    return self.query.lower()
                else:
                    return ""
            except sr.UnknownValueError:
                self.speak_signal.emit("Sorry, I couldn't understand the audio.")
                return ""
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                return ""

    def run(self):
        intro(self)
        while True:
            self.query = self.listen()
            if "wikipedia" in self.query:
                print("About to emit: searching wikipedia")
                self.speak_signal.emit("searching wikipedia")
                query = self.query.replace("wikipedia", "").strip()
                try:
                    result = wikipedia.summary(query, sentences=3)
                    print(f"Wikipedia result: {result}")
                    self.speak_signal.emit(f"according to wikipedia{result}")
                    import re
                    result = re.sub(r'[^\x00-\x7F]+', ' ', result)
                    sentences = result.split('. ')
                    for sentence in sentences:
                        if sentence.strip():
                            self.speak_signal.emit(sentence.strip())
                    print(result)
                except wikipedia.exceptions.DisambiguationError as e:
                    self.speak_signal.emit("Multiple results found. Please be more specific.")
                    print(f"Disambiguation error: {e}")
                except wikipedia.exceptions.PageError:
                    self.speak_signal.emit("Sorry, no Wikipedia page found for that query.")
                    print(f"Page error: No page found for {query}")
                except Exception as e:
                    self.speak_signal.emit("Sorry, I couldn't retrieve or speak the Wikipedia information.")
                    print(f"Wikipedia error: {e}")
            elif "open youtube" in self.query:
                print("About to emit: opening youtube")
                self.speak_signal.emit("opening youtube")
                webbrowser.open('https://www.youtube.com')
            elif "open google" in self.query:
                print("About to emit: opening google")
                self.speak_signal.emit("opening google")
                webbrowser.open('https://www.google.com')
            elif "open quora" in self.query:
                print("About to emit: opening quora")
                self.speak_signal.emit("opening quora")
                webbrowser.open('https://www.quora.com')
            elif "open facebook" in self.query:
                print("About to emit: opening facebook")
                self.speak_signal.emit("opening facebook")
                webbrowser.open('https://www.facebook.com')
            elif "open code with harry website" in self.query:
                print("About to emit: opening code with harry website")
                self.speak_signal.emit("opening code with harry website")
                webbrowser.open('https://www.CodeWithHarry.com')
            elif "open stack overflow" in self.query:
                print("About to emit: opening stackoverflow")
                self.speak_signal.emit("opening stackoverflow")
                webbrowser.open('https://www.stackoverflow.com')
            elif "open instagram" in self.query:
                print("About to emit: opening instagram")
                self.speak_signal.emit("opening instagram")
                webbrowser.open('https://www.instagram.com/direct/inbox/?utm_source=web_push_encrypted&ndid=61aec4471e1faHc3f3d63bfH0H380')
            elif "play music" in self.query:
                print("About to emit: playing music")
                self.speak_signal.emit("playing music")
                music_dir = 'C:\\Users\\HP\\Music\\music'
                print(os.path.exists(music_dir))
                print(os.listdir(music_dir))
                songs = os.listdir(music_dir)
                if songs:
                    rd = random.choice(songs)
                    os.startfile(os.path.join(music_dir, rd))
                else:
                    self.speak_signal.emit("No music found in the directory")
            elif "open vs code" in self.query:
                print("About to emit: opening vs code")
                self.speak_signal.emit("opening vs code")
                vs_code = 'C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                os.startfile(vs_code)
            elif "open command prompt" in self.query:
                print("About to emit: opening command prompt")
                self.speak_signal.emit("opening command prompt")
                os.system('start cmd')
            elif "what's the time now" in self.query:
                timestamp = time.strftime('%H:%M')
                print(f"About to emit: master, the time is {timestamp}")
                self.speak_signal.emit(f"master, the time is {timestamp}")
            elif "how are you" in self.query:
                print("About to emit: I am just a computer program, but I am feeling byte-sized awesome!")
                self.speak_signal.emit("I am just a computer program, but I am feeling byte-sized awesome!")
            elif "search" in self.query:
                query = self.query.replace("search", "").strip()
                print(f"About to search: {query}")
                webbrowser.open('https://www.google.com/search?q=' + query)
            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                print(f"About to emit: your ip address is {ip}")
                self.speak_signal.emit(f"your ip address is {ip}")
            elif "very good" in self.query:
                print("About to emit: Thank you! I'm glad I could help")
                self.speak_signal.emit("Thank you! I'm glad I could help")
            elif "just shut up" in self.query:
                print("About to emit: Ok")
                self.speak_signal.emit("Ok")
                break
            elif "bye" in self.query:
                print("About to emit: Goodbye! If you need assistance in the future, feel free to reach out. Have a great day")
                self.speak_signal.emit("Goodbye! If you need assistance in the future, feel free to reach out. Have a great day")
                sys.exit()

class main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.thread = mainthread()
        self.ui.pushButton.clicked.connect(self.start_task)
        self.ui.pushButton_2.clicked.connect(self.close)

    def start_task(self):
        self.ui.movie = QtGui.QMovie("ag3.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.thread.start()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec_())