
import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr  #pip install speechRecognition

import numpy as np
import wikipedia #pip install wikipedia
import webbrowser
import os
import requests
import time
from plyer import notification
import random
from word2number import w2n
import PyPDF2
from tkinter.filedialog import askopenfilename
import spacy
nlp = spacy.load('en_core_web_sm')


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("A very Good Morning !")

    elif hour >=12 and hour<18:
        speak("Good Afternoon Sir! ")

    else:
        speak("Good Evening sir!")
        
        
def timeStamped(fname, fmt='%Y-%m-%d_{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

 
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"Boss said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query




if __name__=="__main__":
    wishMe()
    while True:
    # if 1:
        query=takeCommand().lower()

   
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        # for weather forecast
       
        elif ('weather report') in query:
            speak("Which city's weather report you want to know")
            city =query=takeCommand().lower()

            print("Displaying weather details of :" , city)

            url=(f'https://wttr.in/{city}')
            res=requests.get(url)
            print(res.text)
            

        elif 'open youtube' in query:
             webbrowser.open('www.youtube.com')

        elif 'open google' in query:
             webbrowser.open('www.google.com')
        
        elif 'open photos' in query:
            webbrowser.open('https://photos.google.com/?tab=rq&pageId=none&pli=1')

        elif 'the time ' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")
            
            
        

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
        
            a = takeCommand()  
            print(a)
            time.sleep(w2n.word_to_num(a))
            print(f"halting for {w2n.word_to_num(a)} seconds ")
               
               
        elif 'how are you' in query:
             speak("I m absolutely fine and living my life to the fullest,   There's no remorse ,    there's no obsession ,  there's no compunction,   there's no regret  just breath in   and    breath out   and     move on")
        
        elif 'describe yourself' in query:
             speak("I m alluring,appealing,begulling,pulchritude,charming ,winsome AI created by my Boss")
            #  speak("I m best friend of Jarvis , A smart Assistant who is just a rather very intelligent system")
        
        elif 'capricious' in query:
             speak("rapidly changing aka whimsical")

        elif 'read a book' in query:
            speak("Which book shall I open for you")
            book= askopenfilename()
            pdfreader= PyPDF2.PdfFileReader(book)
            try:
                speak("Let me know the start page number ")
                a = takeCommand()
                start_page = w2n.word_to_num(a)
            except :
                speak("Please repeat")
            
            try:   
                speak("Let me know the end page number ")
                a = takeCommand()
                end_page = w2n.word_to_num(a)
            except :
                speak("Please repeat")
            print(f"Reading the book from page number {start_page} to {end_page } ")
            pages=pdfreader.numPages
            for num in range(int(start_page),int(end_page)):
                page=pdfreader.getPage(num)
                text=page.extractText()
                player=pyttsx3.init()
                player.say(text)
                print(text)
                player.runAndWait()


        elif 'see you' in query:
            speak("Have a great day sir ..!! i m signing off")
            exit()
