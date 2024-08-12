import pyttsx3 # to convert text to speech
import wikipedia
import webbrowser
import time
import pyaudio
import os
import pyautogui
import speech_recognition as sr
import sounddevice as sd

# from alexa import takeCommand

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()


# if __name__ == "__main__":
#     while True:
#         query = takeCommand().lower()