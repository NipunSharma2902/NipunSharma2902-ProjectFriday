#This is to see if git pull is working or not

from datetime import datetime
import pyttsx3 
import speech_recognition as sr  
import subprocess
import webbrowser
import random

speak=pyttsx3.init('sapi5')
voice_id=speak.getProperty('voices')
speak.setProperty('voice', voice_id[1].id)
speak.say("Hello user!")
speak.setProperty('rate', 150)
speak.runAndWait()

greet=["What's up Boss","Yes Boss","Good to see you too sir"]
fakeBye=["But....","Whyyyyyy","Nope","But I don't want to"]
stop=["Bye Sir","Okay Sir","Aye aye Captain!!","Have a nice day!"]

i=0
while (i==0):
    ch=str(input("What's your command: "))
    ch=ch.lower()
    if "hey" in ch:
        x=random.choice(greet)
        print(x)
        mytext=x
    elif ch=="time":
        time = str(datetime.now().time().hour)+":"+str(datetime.now().time().minute)
        print("Current time is:",time)
        mytext="Current time is:"+str(time)
    elif ch=="day" or ch=="date":
        today=datetime.now().date()
        print("Today's date is: ",today)
        mytext="Today's date is: "+str(today)
    elif "bye" in ch:
        x=random.choice(fakeBye)
        print(x)
        mytext=x
    elif "stop" in ch:
        i=1
        x=random.choice(stop)
        print(x)
        mytext=x
    elif ch=="glad to have you back buddy":
        print("That's my Pleasure Boss")
        mytext="That's my Pleasure Boss"
    elif ch=="search":
        query="https://www.google.com/search?client=firefox-b-d&q="+str(input("What do you want to search: "))
        webbrowser.open(query)
    elif ch=="open":
        print("Apps that I can open are:")
        mytext="Apps that I can open are"
        print("Notepad")
        print("Calculator")
        print("Paint")

        ex=str(input("Enter program name: "))
        ex=ex.lower()
        if ex=="notepad":
            program="notepad.exe"
        elif ex=="calculator":
            program="C:\WINDOWS\system32\calc.exe"
        elif ex=="paint":
            program="C:\WINDOWS\system32\mspaint.exe"
        subprocess.call(program)

    else:
        print("I don't recognise that command")
        mytext="I don't recognise that command"

    speak.say(mytext)
    speak.runAndWait()
    