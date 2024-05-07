import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import webbrowser
import smtplib
import sys
import winsound
import requests



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#TEXT T0 SPEECH
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
 
    #TO CONVERT VOICE INTO TEXT   
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)


    try:
        print("Recognition...")
        query = r.recognize_google(audio, language="en-IN")
        print(f"User said: {query}")
        return query
    
    except Exception as e:
        speak("Say that again please...")
        return "none"
#to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<=12:
        speak('good morning')
    elif hour>12 and hour<18:
        speak('good afternoon')
    else:
        speak('good evening')
    speak("I am your voice assitant. please tell me how can i help you sir")
    
#to send mail


    
if __name__ == "__main__":
   wish()
   while True:
#if 1:
       
       query = takecommand().lower()
       
       #logic building for tasks
       
       if "open notepad" in query:
           npath= "C:\\Windows\\notepad.exe"
           os.startfile(npath)
           
       elif "open command prompt" in query:
          os.system("start cmd")
          
       elif "open camera" in query:
            cap = cv2.VideoCapture(0) 
            while True:
                 ret, img = cap.read()
                 cv2.imshow("webcam", img)
                 k = cv2.waitKey(50)
                 if k==27:
                     break;
            cap.release()
            cv2.destroyAllWindows()            
                
       elif "ip address" in query:
           ip = get("https://api.ipify.org").text
           speak(f"your ip address is {ip}")
            
           
       elif "open youtube" in query:
           webbrowser.open("www.youtube.com")
       
       elif "open facebook" in query:
           webbrowser.open('www.facebook.com')
           
           
       elif "open google" in query:
           speak("sir, what should i search on google")
           cm = takecommand().lower()
           webbrowser.open(f"{cm}")
       
         
       elif"open playstore" in query:
           webbrowser.open("https://play.google.com/")
           
       elif "open udemy" in query:
          webbrowser.open("www.udemy.com ")
          
       elif "open geeks" in query:
           webbrowser.open("www.geeksforgeeks.org ")
          
       elif "open bit" in query:
           webbrowser.open("www.bitsathy.ac.in ")
           
       elif "open moodle" in query:
               webbrowser.open("https://moodle.bitsathy.ac.in/ ")        
                         
       
       elif "where i am" in query or "where we are " in query:
           speak("wait sir, let me check")
           try:
               ipAdd = requests.get("https://api.ipify.org").text
               print(ipAdd)
               url = f"https://get.geojs.io/v1/ip/geo/{ipAdd}.json"
               geo_requests = requests.get(url)
               geo_data = geo_requests.json()
               city = geo_data["city"]
               country = geo_data["country"]
               speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
           except Exception as e:
               speak("sorry sir, DUE to internet i am not able to find where we are.")
               pass
           
     
       elif "thank you" in query:
           speak("thanks for using me sir, have a good day.")
           sys.exit()
           speak("sir, do you have any other work")
       
       
      

      

       