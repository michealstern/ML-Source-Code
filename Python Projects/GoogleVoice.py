import pyttsx3

engine = pyttsx3.init()

text = "Micheal Stern is Funtastic guy."

engine.say(text)

engine.runAndWait()