#ALL KINK COMMANDS

import subprocess
import wolframalpha
import pyttsx3
import multiprocessing
from multiprocessing import Process
import tkinter
import json
import random
import operator
import cv2
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import urllib
import time
import turtle
import random
import os
import playsound
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import selenium
from selenium import webdriver
import urllib.request






#-----------------------------------
mic = sr.Microphone(device_index=1)

global data


def msg(Msg,Amt,TimeP):
    for Printr in range(1,Amt+1):
        print(Msg, end='')
        time.sleep(TimeP)
	

		
def clr(Deg):
    print("\n"*Deg)



def speak(text):
    tts = gTTS(text=text, lang='en')
    filename="inputvoice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

       



def recordAudio():
    data = ""

    r = sr.Recognizer()
    with sr.Microphone() as source:       
        r.adjust_for_ambient_noise(source,duration=1)
        print("I'",end='')
        time.sleep(0.0075)
        print("m l",end='')
        time.sleep(0.0075)
        print("is",end='')
        time.sleep(0.0075)
        print("te",end='')
        time.sleep(0.0075)
        print("n",end='')
        time.sleep(0.0075)
        print("in",end='')
        time.sleep(0.0075)
        print("g",end='')
        time.sleep(0.0125)
        print(".",end='')
        time.sleep(0.0125)
        print(".",end='')
        time.sleep(0.0125)
        print(".",end='')
        audio = r.listen(source)
        
  
        
    try:
   
        data = r.recognize_google(audio)
        print(data)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Could not understand the audio.")

    except sr.RequestError as e:
        print("Could not load results; {0}", format(e))

    else :
        print("Other error.")




def search(data):
    driver = webdriver.Chrome('/Users/aksharadinkar/Downloads/chromedriver')
    r = sr.Recognizer()
    noofwords=1
    for i in range(0,len(data)):
        if  data[i]==' ':
             noofwords+=1      

 
    if "search" in data and "youtube" not in data and noofwords>=2:
        split_list=data.split()
        split_list.remove("search")
        data=' '.join(split_list)

        driver.get('http://www.google.com');
        time.sleep(2)
        search_box = driver.find_element_by_name('q')
        search_box.send_keys(data)
        search_box.submit()

        
    if "stop" or "quit" or "close" in data and 'search' or 'youtube' or 'wikipedia' not in data and noofwords==1:
        print("CLOSED.")



    if "youtube" in data and "search" not in data:
        noofwords=1
        for i in range(0,len(data)):
            if  data[i]==' ':
                 noofwords+=1      
        split_list=data.split()
        split_list.remove("youtube")
        data=' '.join(split_list)        
        data=data.split(" ")
        driver.get('http://www.youtube.com');
        time.sleep(6)
        search_box = driver.find_element_by_name('search_query')
        search_box.send_keys(data)
        search_box.submit()
    

        
    if "youtube search" in data:
        noofwords=1
        for i in range(0,len(data)):
            if  data[i]==' ':
                 noofwords+=1      
        split_list=data.split()
        split_list.remove("youtube")
        split_list.remove("search")
        data=' '.join(split_list)        

        driver.get('http://www.youtube.com');
        time.sleep(6)
        search_box = driver.find_element_by_name('search_query')
        search_box.send_keys(data)
        search_box.submit()
    


    if "search on youtube" in data:
        noofwords=1
        for i in range(0,len(data)):
            if  data[i]==' ':
                 noofwords+=1      
        split_list=data.split()
        split_list.remove("youtube")
        split_list.remove("search")
        split_list.remove("on")
        data=' '.join(split_list)        
   
        driver.get('http://www.youtube.com');
        time.sleep(6)
        search_box = driver.find_element_by_name('search_query')
        search_box.send_keys(data)
        search_box.submit()

    if "how are you" in data and 'search' not in data:
        noofwords=1
        for i in range(0,len(data)):
            if  data[i]==' ':
                 noofwords+=1      
        howami=random.randint(0,3)
        if howami==1:
            speak("I am fine. Thanks!")
        if howami==2:
            speak("I am all good!")    
        if howami==3:
            speak("I am fine. How are you?") 
            
            

    if "time" in data:
        noofwords=1
        for i in range(0,len(data)):
            if  data[i]==' ':
                 noofwords+=1      

        speak(ctime())



    if "where is" in data:
        noofwords=1
        for i in range(0,len(data)):
            if  data[i]==' ':
                 noofwords+=1      
        data = data.split(" ")
        location = data[2]
        speak("Hold on sir, I will show you where "+location+" is")
        webbrowser.open("https://www.google.in/maps/place/" + location + "/&amp;")
      

    if "what is" in data:
        noofwords=1
        for i in range(0,len(data)):
            if  data[i]==' ':
                 noofwords+=1      
        data=data.split("")
        for t in range(3, noofwords+1):
            something=data[t]+' '


speak("I'm listening...")

recordAudio()


  
tts.runAndWait()
    
    
