try:
    import speech_recognition as sr
except ImportError:
    # fallback dummy sr if speech_recognition isn't installed
    class _DummyMicrophone:
        def __enter__(self):
            return None
        def __exit__(self, exc_type, exc, tb):
            return False
    class _DummySR:
        Microphone = _DummyMicrophone
    sr = _DummySR()

def speak(text):
    # simple fallback text output; replace with a TTS implementation if desired
    print(text)

with sr.Microphone() as source:
    speak("listening..")