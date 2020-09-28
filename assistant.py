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
        speak("Good evening Sir")
    speak("I am jarvis, Please tell me how can i help you !")


if __name__ == "__main__":
    wish()
    if 1:
        query = takecommand().lower()

        if 'open notepad' in query:
            npath = 'C:\\Windows\\System32\\notepad.exe'
            os.startfile(npath)
            speak("Please wait ! While I am opening notepad for you!")

        elif "open cmd" in query: