import speech_recognition as sr
import webbrowser
import pyttsx3


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    print(c)

if __name__ == "__main__":
    speak("Initialising Jarvis...")
    
    while True:     
        r = sr.Recognizer()
        print("recognizing")
        try: 
            with sr.Microphone() as source:
                print("Listening")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source)
            command = r.recognize_google(audio)
            if (command.lower() == "jarvis"):
                speak("Yeah")

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)

                    processCommand(command)

        except Exception as e: 
            print("Error; {0}".format(e))
            
