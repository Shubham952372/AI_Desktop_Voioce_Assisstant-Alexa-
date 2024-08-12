import pyttsx3  # to convert text to speech
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit as wk
import os
import random
import cv2 # type: ignore
import sys
import time
import pyautogui
import operator
import requests
 # type: ignore
import sounddevice as sd
import numpy as np # type: ignore

engine = pyttsx3.init('sapi5')  # microsoft speech api
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")
    speak("Ready to comply. What can I do for you?")


def takeCommand():
    r = sr.Recognizer()
    # r.energy_threshold = 400
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        # speak("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'alexa' in query:
            print("yes sir")
            speak("yes sir")

        elif "hu r u" in query:
            print('My Name is alexa')
            speak('My Name is alexa')
            print('I can do Everything that my creator programmed me to do')
            speak('I can do Everything that my creator programmed me to do')

        elif "who created you" in query:
            print('I do not know his name, I was created with Python Language, in Visual Studio Code')
            speak('I do not know his name, I was created with Python Language, in Visual Studio Code')

        elif 'what is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'who is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'just open google' in query:
            webbrowser.open('google.com')

        elif 'open google' in query:
            speak("what should I search ?")
            qry = takeCommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={qry}")
            results = wikipedia.summary(qry, sentences=1)
            speak(results)

        elif 'just open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open youtube' in query:
            speak("what would you like to watch ?")
            qrry = takeCommand().lower()
            wk.playonyt(qrry)

        elif 'search on youtube' in query:
            query = query.replace("search on youtube", "")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

        elif 'close browser' in query:
            os.system('taskkill /f /im msedge.exe')

        elif 'close chrome' in query:
            os.system('taskkill /f /im chrome.exe')

        # elif "open msword" in query:
        #     npath = "C:\WINDOWS\system32\\msword.exe"
        #     os.startfile("npath")

        # elif "close msword" in query:
        #     os.system("taskkill /f /im msword.exe")    
    
        # elif "open paint" in query:
        #     npath = "C:\WINDOWS\system32\\notepad.exe"
        #     os.startfile(npath)

        # elif "close notepad" in query:
        #     os.system("taskkill /f /im notepad.exe") 

        # elif "open command prompt" in query:
        #     os.system("start cmd") 

        # elif "close command prompt" in query:
        #     os.system("taskkill /f /im cmd.exe") 
                        
        # elif 'play music' in query:
        #     music_dir = 'E:\Music'           
        #     songs = os.listdir(music_dir)
        #     os.startfile(os.path.join(music_dir, random.choice(songs)))

        # elif 'play robot movie' in query:
        #     npath = "E:\robot.mp4"
        #     os.startfile(npath)

        # elif 'close movie' in query:
        #     os.system("taskkill /f /im vlc.exe")

        # elif 'close music' in query:
        #     os.system("taskkill /f /im vlc.exe")    

        # elif 'what is the time' in query:
        #     strtime = datetime.datetime.now().strftime("%H:%M:%S")
        #     speak(f"Sir, the time is{strtime}")

        # elif "shut dowm the system" in query:
        #     os.system("shutdowm /s /t 5")

        # elif "restart the system" in query:
        #     os.system("shutdowm /r /t 5")

        # elif "lock the system" in query:
        #     os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        # elif "hibernate the system" in query:
        #     os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        # elif "open camera" in query:
        #     cap = cv2.VideoCapture(0)
        #     while True:
        #         ret, img = cap.read()
        #         cv2.imshow('webcam',img)
        #         k = cv2.waitKey(50)
        #         if k==27:
        #             break;
        #     cap.release()
        #     cv2.destroyAllWindows()

        # elif "go to sleep" in query:
        #     speak('alright then, I am switching off')
        #     sys.exit()

        # elif "take screenshot" in query:
        #     speak('tell me a name for the file')
        #     name = takeCommand().lower()
        #     time.sleep(3)
        #     img = pyautogui.screenshot()
        #     img.save("f{name}.png")  
        #     speak("screenshot saved")

        # elif "calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Ready")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)

            def get_operator(op):
                return {
                    '+': operator.add,
                    '-': operator.sub,
                    '*': operator.mul,
                    '/': operator.truediv,
                }[op]

            def eval_binary_expr(op1, oper, op2):
                op1, op2 = int(op1), int(op2)
                return get_operator(oper)(op1, op2)

            speak("Your result is")
            speak(eval_binary_expr(*(my_string.split())))

        elif "what is my ip address" in query:
            speak("Checking")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                speak("Your IP address is")
                speak(ipAdd)
            except Exception as e:
                speak("Network is weak, please try again later")

        elif "volume up" in query:
            for _ in range(15):
                sd._set_output_device(sd.query_devices(kind='output')[0]['name'])
                volume = sd._check_output_settings('volume')
                volume.value += 1
                sd.play(0 * np.ones(100), samplerate=100)
                sd.wait()

        elif "volume down" in query:
            for _ in range(15):
                sd._set_output_device(sd.query_devices(kind='output')[0]['name'])
                volume = sd._check_output_settings('volume')
                volume.value -= 1
                sd.play(0 * np.ones(100), samplerate=100)
                sd.wait()

        elif "mute" in query or "unmute" in query:
            sd._set_output_device(sd.query_devices(kind='output')[0]['name'])
            volume = sd._check_output_settings('volume')
            volume.value = 0 if volume.value != 0 else 50
            sd.play(0 * np.ones(100), samplerate=100)
            sd.wait()
