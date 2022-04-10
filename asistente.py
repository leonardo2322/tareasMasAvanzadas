import pyttsx3

engine = pyttsx3.init()

engine.setProperty("voice","spanish")
engine.setProperty("rate",120)

engine.say("hola ethan que quieres")
engine.runAndWait()

