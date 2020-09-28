import pyttsx3,datetime,os,random,requests
import wikipedia,webbrowser,sys,pywhatkit
import speech_recognition as sr 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)


# To convdert text into voice
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source: