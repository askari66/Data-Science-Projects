import pyttsx3  #pip install pyttsx
import webbrowser #pip install Webbrowser
import smtplib 
import random
import speech_recognition as sr  #pip install speech recognition
import datetime  #pip install datetime
import wolframalpha # pip install wolframalpha
import os           #by default Library
import sys
from pygame import mixer  #pip install pygame
import re
from gtts import gTTS   #pip install gTTs
import requests 
import urllib.request  #pip install urllib
import urllib.parse
import bs4            #pip install beautifulspace4
from selenium import webdriver #pip install selenium 
from selenium.webdriver.common.keys import Keys

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('E2AE9E-XET5926KHU')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print('Jarvis: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('You will never have this day again so make it count! ... Good Morning Sayed!')

    if currentH >= 12 and currentH < 18:
        speak('Be bright like the afternoon sun and let everyone who sees you feel inspired by all the great things you do. ..Good Afternoon Sayed!')

    if currentH >= 18 and currentH !=0:
        speak('This evening is as brief as the twinkling of an eye yet such twinklings is what eternity is made of. ..Good Evening !')

greetMe()

speak('Hello Sayed, I am Jarvis your virtual assistant')
speak('How may I help you?')


def myCommand():
    "listens for commands"
    #Initialize the recognizer
    #The primary purpose of a Recognizer instance is, of course, to recognize speech. 
    r = sr.Recognizer()

    with sr.Microphone(device_index=0,	chunk_size=2048,sample_rate=48000) as source:
        print('Jarvis ...')
        r.pause_threshold = 1
        #wait for a second to let the recognizer adjust the  
        #energy threshold based on the surrounding noise level 
        r.adjust_for_ambient_noise(source, duration=1)
        #listens for the user's input
        audio = r.listen(source)
        print('i am on it sir...')

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
        

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        speak('Sorry sir! your last command could not be heard please repeat it sir')
        command=myCommand();

    return command

        

if __name__ == '__main__':

    while True:
    
        query = myCommand()
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')
        elif 'carter road on map' in query:
            webbrowser.open('https://www.google.com/maps/place/Sangeet+Samrat+Naushad+Ali+Marg,+Mumbai,+Maharashtra/@19.0682119,72.8204795,17z/data=!3m1!4b1!4m5!3m4!1s0x3be7c96dd29a01ab:0x95783fd3b11a9e80!8m2!3d19.0682119!4d72.8226682')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif "self" in query:
            speak('okay')
            speak('i was made by a Askari Sayed. i am glad that i could help everyone whenever they need me!')

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("askarizaidi3@gmail.com", '9619280802')
                    server.sendmail('askarizaidi3@gmail.com', "askarisayed16@yahoo.com", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")


        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()


        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('According to WOLFRAM-ALPHA- ')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')
