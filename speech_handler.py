import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_command(timeout=5, phrase_time_limit=5):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your command...")
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            if(len(command) >= 5):
                command = command.replace("play", "")
            return command.lower()
        except sr.WaitTimeoutError:
            print("Listening timed out. No speech detected.")
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError:
            print("Speech Recognition service unavailable.")
    return None

# refence followed for the code:
# https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst