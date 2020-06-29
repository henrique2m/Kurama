import speech_recognition as sr
import pyttsx3
import Browser
import Workspace

from random import choice

listErrors = [
    "Não entendi nada.",
    "Desculpe, não entendi.",
    "Repita novamente, por favor.",
]

reproduction = pyttsx3.init('sapi5')

def out_sound(res):
    reproduction.say(res)
    reproduction.runAndWait()

def toRecognize(res_error_random):
    rec = sr.Recognizer()

    with sr.Microphone() as s:
        rec.adjust_for_ambient_noise(s)

        while True:
            try:
                audio = rec.listen(s)
                entry = rec.recognize_google(audio, language="pt")
                return entry
            except sr.UnknownValueError:
                return res_error_random

question = 'O que vamos fazer hoje?'
print(question)
out_sound(question)

while True:
    res_error_random = choice(listErrors)
    speak = toRecognize(res_error_random)

    speakUpper = speak.upper()

    if 'WORKSPACE' in speakUpper:
        workspace = Workspace.Workspace()
        workspace.openProgram('VSCODE')

    elif 'NAVEGAR' in speakUpper: 
        browser = Browser.Browser()
        if not browser.controllers(speak) : break
   

    print(speak)
    out_sound(speak)