import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import psutil # type: ignore
import pyautogui
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import requests
from bs4 import BeautifulSoup
import time
import pyjokes
import urllib.parse
import random
import subprocess
import json
from urllib.request import urlopen




engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices', voices[1].id)


#for text to speach
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#voice to text  
def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("sir ,say that again please....")
        return "none"
    return query


def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<12:

        speak(f"Good Morning Sir ,its {tt}")

    elif hour>=12 and hour<18:

        speak(f"Good Afternoon sir ,its {tt}")

    else:

        speak(f"Good Evening sir ,its {tt}")    

    speak('I am Jarvis sir , please tell me how can i help you sir')  

#to send email
def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('your email id','your password')
    server.sendmail('your email id',to,content)
    server.close()

def news():
    main_url="https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=1640847a57d1416c8c05174e4a7c2d33"

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day=["first","second","third ","fourth","fifth","sixth","seventh","eigth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f" sir , today's {day[i]} news is: {head[i]}")



if __name__ == "__main__":
    #speak("hello sir")
    wish()
    while True:
        #if 1:

        query = takecommand().lower()

         
             #logic blocks

        if "open notepad" in query:
             npath ="c:\\Windows\\system32\\notepad.exe"
             os.startfile(npath)
        
        elif "open command prompt" in query:
              os.system("start cmd")

        elif "open camera" in query:
             cap = cv2.VideoCapture(0)
             while True:
                 
                    ret,img = cap.read()
                    cv2.imshow('webcam',img)
                    k = cv2.waitKey(50)
                    if k==27:
                       break 
             
             cap.release()
             cv2.destroyAllWindows()

      
        elif 'play music' in query or 'play some songs' in query or 'musics'in query:
            music_dir = 'c:\\Users\\NITHIN\\Music'
            songs = os.listdir(music_dir)
            random_song = os.path.join(music_dir, random.choice(songs))
            os.startfile(random_song)     

        elif "what is my ip address" in query or "what is my IP address"  in query:
            ip = get('https://api64.ipify.org?format=json').text
            speak(f"sir your ip address is {ip}")   

  
        elif "wikipedia" in query:
            speak("searching wikipedia.....")  
            query=query.replace("wikipedia","")   
            results = wikipedia.summary(query,sentences=5)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "tell me a joke" in query:
            joke = pyjokes.get_jokes()
            speak(joke)    

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open amazon" in query:
            webbrowser.open("www.amazon.in")

        elif "open flipkart" in query:
            webbrowser.open("www.flipkart.in") 

        elif "shut down my system" in query:
            os.system("shutdown /s /t 5") 

        elif "restart my system" in query:
            os.system("shutdown / /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSusupendstate 0,1,0")  

        elif "news" in query:
            speak("please wait sir, fetching the latest news")
            news()

        
        elif "open google" in query:
            speak("Sir, what should I search in Google?")
            cm = takecommand().lower()
            query_encoded = urllib.parse.quote_plus(cm)
            webbrowser.open(f"https://www.google.com/search?q={query_encoded}")   
        
        elif "open calculator" in query:
             speak("opening calculator")
             subprocess.Popen('calc.exe')
         
        elif 'how are you' in query or 'how r you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        
        elif " send whatsapp message" in query:
            kit.sendwhatmsg("","hello",2,25)

        elif "play songs on youtube" in query:
            kit.playonyt("let me down slowly") 

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by  , Nithin.")  

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Nithin")
        
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")
        

        elif "are you intelligent" in query:
            speak(" Well, when I was at school, I had to cheat on my metaphysics exam by looking into the soul of the boy next to me.")

        elif "how old are you" in query:
           speak("sir  , say that age is nothing but a number. But technically, its also a word.")  


        elif "write a note" in query:
           speak("What should I write, sir?")
           note = takecommand()
    
           with open('jarvis.txt', 'w') as file:
            file.write(note)
    
            speak("Note written successfully, sir.")

                
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")                      

        elif "how much power left " in query or "how much power we have " in query:
            battery=psutil.sensors_battery()
            percentage =battery.percent
            speak(f"sir our system have {percentage} percentage of battery")

        elif "you can sleep " in query or "sleep now" in query:
            speak("okay sir, i am going to sleep you can call me anytime sir , i will be there")    
            break
        
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl // maps // place//" + location + "")                  

        elif "volume up" in query or "increase volume" in query:
            pyautogui.press("volumeup")

        elif "volume down " in query or "decrease volume " in query:
            pyautogui.press("volume down")

        elif "mute" in query:
            pyautogui.press("volumemute") 
          

            
        elif "temperature" in query:
           speak("Tell me the city name")
           time.sleep(1)
       
           city = takecommand()
       
           if city == "none":
               speak("I did not hear the city name")
           else:
               city = city.replace(" ", "")
               print("City heard:", city)
       
               try:
                   url = f"https://wttr.in/{city}?format=%t"
                   response = requests.get(url)
                   temperature = response.text
       
                   speak(f"The temperature in {city} is {temperature}")
       
               except Exception as e:
                   print(e)
                   speak("Unable to fetch temperature")


      


        elif "send email to my friend" in query:
            try:
                speak("what should i say")
                content=takecommand().lower()
                to = "rangalanithin1844@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to nithin")
               

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to send this email to nithin,something went wrong")

         

            speak("sir ,how can i help you ? please tell me ")
            
        elif "no need thank you" in query:
            speak("your welcome sir, thanks for using me ,have a wonderful day sir ")    
            sys.exit()

            
        
 #if __name__ == "__main__":
  #    while True:
   #       permission=takecommand()
    #      if "wake up" in permission:
     #         TaskExecution()
#
 #         elif "goodbye" in permission:
  #            speak("thanks for using me sir,have a good day")
   #           sys.exit()