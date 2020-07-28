import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
from selenium import  webdriver
import requests
import json
import pyowm

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voice)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sajib!")

    elif hour>=12 and hour<18:
        speak("Good afternoon sajib!")
    else:
        speak("Good Evenning Sajib!")
    
    speak("i am jarvis. How can i help you sir")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold=1
        audio=r.listen(source)      
    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print(e)
        print("say that again please..")
        return "None"
    return query

if __name__ == "__main__":
   wishMe()
   while True:
       query=takeCommand().lower()
       
       if 'wikipedia' in query:
           speak('Searching wikipedia..')
           query=query.replace("wikipedia","")
           result=wikipedia.summary(query,sentences=2)
          # if result==True:
           speak("According to wikipedia")
           print(result)
           speak(result)
           #else:
               #speak('sorry sir. Not found')

       elif 'open youtube' in query:
            webbrowser.open("youtube.com")

       elif 'open google' in query:
           webbrowser.open("google.com")

       elif 'music' in query:
           music_dir='C:\\Users\\Sajib roy\\Desktop\\music'
           songs=os.listdir(music_dir)
           print(songs)
           speak("Playing music. Enjoy the song")
           os.startfile(os.path.join(music_dir,songs[random.randrange(3)]))

       elif 'time' in query:
           strTime=datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"sir, the time is {strTime}")

       elif 'video' in query:
           music_dir='G:\\favourite'
           songs=os.listdir(music_dir)
           print(songs)
           speak("Playing video. Enjoy the video")
           os.startfile(os.path.join(music_dir,songs[random.randrange(10)]))

       elif 'exit' in query:
           speak('goodbye. have a nice day sir')
           exit()

       elif 'how are you' in query:
           speak("I am good. What about you..")

       elif "whatsapp" in query:
           path="C:\\Users\\Sajib roy\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
           os.startfile(path)
       elif "my location" in query:
           res=requests.get('https://ipinfo.io/')
           data=res.json()
           print(data)
           speak(data) 

       elif "colse whatsapp" in query:
           os.system('TASKKILL /F /IM WhatsApp')
       
       elif "weather" in query:
           api_address='https://api.openweathermap.org/data/2.5/weather?appid=06accab0b4510deaa01dfbba1b0c2308&q='
           speak("Please enter the city name:")
           city =takeCommand().lower()
           speak("searching...")
           url = api_address + city
           json_data = requests.get(url).json()
           
           print(json_data)
           speak(json_data)
       elif 'who are you' in query:
           speak('I am jarvis.')
