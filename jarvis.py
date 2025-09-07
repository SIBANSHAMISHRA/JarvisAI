import speech_recognition as sr
import pyttsx3
import os
import datetime

# Initialize speech engine
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
        except:
            talk("Sorry, I didn’t catch that")
            return ""

talk("Hello, I am Jarvis. How can I help you?")

while True:
    command = listen()

    if "open folder" in command:
        talk("Opening your documents folder")
        os.startfile("C:\\Users\\YourName\\Documents")  # change path

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        talk("The time is " + time)

    elif "stop" in command or "exit" in command:
        talk("Goodbye")
        break

    else:
        talk("I am still learning. Please try another command.")
