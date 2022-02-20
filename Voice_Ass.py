from multiprocessing.sharedctypes import Value
from matplotlib.pyplot import text
import speech_recognition as sr
import pyttsx3  
import pywhatkit 
import datetime
import wikipedia
import pyjokes  

Listener = sr.Recognizer()
engine = pyttsx3.init()
# for changing the voice
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def talk(text): 
    engine.say(text)
    engine.runAndWait() 

def chintu_command():  
    try: 
        with sr.Microphone() as source:
         print("Listening .......")
         voice = Listener.listen(source)
         command = Listener.recognize_google(voice)
         command = command.lower()
         if "chintu" in command: 
             command = command.replace("chintu","")
             print(command)
    except:
       pass 
    return command

def run_chintu():
    command = chintu_command()
    print(command)
    if "play" in command:
        song = command.replace("play","")
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk("Current time is" + time)
    elif "Superstar" in command:
        person = command.replace("Superstar","")
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif "joke" in command:
        talk(pyjokes.get_joke())
        
run_chintu()
