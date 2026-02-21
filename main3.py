import speech_recognition as sr
import webbrowser
import pyttsx3


recognizer = sr.Recognizer()
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
for voice in voices:
    if "male" in voice.name.lower() or "david" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()
    if "open google" in c:
        speak("Opening Google now")
        webbrowser.open("https://google.com")
    elif "open insta" in c:
        speak("Opening Instagram now")
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c:
        speak("Opening YouTube now")
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        speak("Opening LinkedIn now")
        webbrowser.open("https://linkedin.com")
    elif "open chatgpt" in c:
        speak("Opening ChatGPT now")
        webbrowser.open("https://chatgpt.com")
    else:
        speak("Sorry, I didn't understand that command.")

    

if __name__ == "__main__":
    speak("Initialising Jarvis...")
    speak("Hello")
    
    while True:     
        print("recognizing")
        try: 
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            if "jarvis" in command.lower():
                speak("Yeah")

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)

                processCommand(command)

        except Exception as e: 
            print("Error; {0}".format(e))
            
