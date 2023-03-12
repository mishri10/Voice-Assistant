import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

import smtplib
from ecapture import ecapture as ec



listener = sr.Recognizer()
va=pyttsx3.init()
def say(text):
    va.say(text)
    va.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        say("Good Morning!")

    elif hour>=12 and hour<17:
        say("Good Afternoon!")   

    else:
        say("Good Evening!")  

    say("how can I help you")       

def take_cmd(): 
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.pause_threshold = 1
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
    except:
        
        print("I didn't recognize what you said please repeat")
      
    return command
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email_id@gmail.com', 'email password')# since google has restriced the access of smtp so in place of email password put app password (can be created when you complete 2 step verification of your google account )
    server.sendmail('your_email_id@gmail.com', to, content)
    server.close()
def run():
    
    command=take_cmd()
    if 'play' in command:
        song=command.replace('play','')
        say('playing'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M')
        print(time)
        say('The current time is'+ time)
    elif 'search' in command or 'who' in command or 'what' in command:
        info=wikipedia.summary(command,2)
        say(info)
    elif 'joke' in command:
        say(pyjokes.get_joke())
    
    elif "camera" in command or "take a photo" in command:
        ec.capture(0, "Camera ", "sample_image.jpg")
        say('done')
    elif 'email' in command:
            try:
                say("sending email")
                content = command.replace('send an email saying','')
                to = "reciver_emai_id@gmail.com"    
                sendEmail(to, content)
                say("Email has been sent!")
            except Exception as e:
                print(e)
                say("not able to send this email")    

    else:
        say('please repeat your command')
wishMe()
while True:
    run()         