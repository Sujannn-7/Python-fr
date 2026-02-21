import pyttsx3
engine = pyttsx3.init()
text = input("Enter something as input: ")
engine.say(text)
engine.runAndWait()