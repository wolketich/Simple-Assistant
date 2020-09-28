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
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=2,phrase_time_limit=5)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
    except Exception:
        speak("Can you please say that again ... ")
        return 'none'
    return query

# To wish
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<=12:
        speak("Good morning Sir")
    elif hour>12 and hour<16:
        speak("Good afternoon Sir")
    elif hour>16 and hour<22: