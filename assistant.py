import pyttsx3,datetime,os,random,requests
import wikipedia,webbrowser,sys,pywhatkit
import speech_recognition as sr 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)

