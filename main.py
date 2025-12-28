import speech_recognition as sr
import pyttsx3
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            return command.lower()
    except:
        return ""

def run_aura():
    speak("Hello, I am Aura")

    while True:
        command = take_command()

        if "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "your name" in command:
            speak("My name is Aura")

        elif "exit" in command or "stop" in command:
            speak("Goodbye")
            break

        elif command != "":
            speak("Sorry, I did not understand")

run_aura()