import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold = 300
r.pause_threshold = 0.8

with sr.Microphone() as source:
    print("Mic detected")
    print("Speak now...")
    audio = r.listen(source, phrase_time_limit=5)

print("Audio captured")

try:
    text = r.recognize_google(audio)
    print("You said:", text)
except Exception as e:
    print("Recognition error:", e)