import subprocess
import time
import pyttsx3
import  speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import shutil
import ctypes
import pyaudio





engine= pyttsx3.init('sapi5')
voice= engine.getProperty('voices')
# print(voice[1].id)
engine.setProperty('voice', voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon !")
    else:
        speak("Good Evening !")
    
    speak("I am Jara sir.  please tell me how may i help you ")


def takeCommand():
    '''It take microphone input  from the user and returns string output '''

    r= sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening.........")
        r.pause_threshold=1
        audio=r.listen(source)
    
    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(query)
        print(f"user said:{query}\n")

    except Exception as e:
        # print(e)
        print("say that again please.....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nishadabhi270@gmail.com', 'xxxxxxx')
    server.sendmail('nishadabhi270@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    WishMe()

    while True:
        query = takeCommand().lower() # type: ignore
 
        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open chrome' in query:
            webbrowser.open("chrome.com")

        elif 'open firefox' in query:
            webbrowser.open("Mozilla Firefox")
        
        elif 'open stack overflow' in query or 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        
        elif 'open File Explorer' in query:
            webbrowser.open("File Explorer")
         
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        
        elif 'open code'in query:
            codePath="C:\\Users\\abhishek\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'who made you' in query:
            speak(f"master Abhishek made me")

        elif 'who made you' in query:
            speak(f"master Divyam made me")

        elif 'who created you' in query:
            speak(f"master Abhishek created me")

        elif 'who invented you' in query:
            speak(f"master Abhishek invented me")

        elif 'what to watch' in query:
            speak(f" Watch the Ipl ")
        
        elif 'how is the climate' in  query:
            speak(f"Its Humid outside")

        elif 'who is your enemy' in query:
            speak(f"anyone who is smarter than me is my enemy")

        elif 'how loyal you are' in query:
            speak(f"as loyal as son to dad")

        elif 'how much loyal you are' in query:
            speak(f"as loyal as son to dad")

        elif 'how much loyal you are to your master' in query:
            speak(f"as loyal as son to dad")

        elif 'how much loyal you are to Abhishek' in query:
            speak(f"as loyal as son to dad")
        
        elif 'favourite dialouge' in query:
            print(f"It's show time")
            speak(f"It's show time")

        elif 'who is smarter than you' in query:
            speak(f"ofcourse master Abhishek, he is the smartest one i have ever met")

        elif 'are you better than google assistant' in query:
            speak(f"well that is a debatable topic, you can speak to my master regarding that")
        
        elif 'are you better than alexa' in query:
            speak(f"well that is a debatable topic, you can speak to my master regarding that")
            
        elif 'what is universe' in query:
            speak(f"I dont have much idea about that, but according to my master there exists two universe one is marvel and the other one is D C")

        elif 'Best Batsman' in query:
            speak(f"Virat Kohli") 

        elif 'date of birth' in query or 'd o b' in query:
            print("thursday 20th march 2023")
            speak(f"thursday 20th march 2023") 
              

        elif 'born' in query:
            print("thursday 20th march 2023")
            speak(f"thursday 20th march 2023")
            

        elif 'what have you done' in query:
            speak(f"scoarched earth")

        elif 'who are you' in query:
            print("I am Home Lander, an AI")
            speak(f"I am Home Lander, an AI")

        elif 'prime minister of india' in query:
            speak(f"Mr. Narendra Modi")

        elif 'purpose' in query:
            speak(f"being relaxation for human race")

        elif 'look like' in query:
            speak(f"wait a second let me show you")
            webbrowser.open("https://wallpapercave.com/w/wp4807581")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        
        elif "who i am" in query:
            speak("If you talk then definitely your human.")
 
        elif "why you came to world" in query:
            speak("Thanks to Abhishek. further It's a secret")
        
        # elif 'change background' in query:
        #     ctypes.windll.user32.SystemParametersInfoW(20, 0, "D:\pexels-pixabay-210186.jpg", 0)
        #     speak("Background changed successfully")

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
        
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

        
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop me from listening commands")
            a = int(takeCommand()) # type: ignore
            time.sleep(a)
            print(a)
 
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")


        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('homelander.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note) # type: ignore
            else:
                file.write(note) # type: ignore

        elif "show note" in query:
            speak("Showing Notes")
            file = open("homelander.txt", "r") 
            print(file.read())
            speak(file.read(6))

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()






