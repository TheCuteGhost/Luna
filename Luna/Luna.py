import speech_recognition as sr
import pyttsx3, pywhatkit

name = "Luna"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def talk():
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Luna esta escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc)
            rec = rec.lower()

            if name in rec:
                rec = rec.remplace(name, '')
    except:
        pass
    return rec

