import pyttsx3
import os
while True:
    engine=pyttsx3.init()

    i=input("Enter The Text You Want To Speak:")
    engine.say(i)
    engine.runAndWait()
    

    engine.stop()
    os.system("cls")
    # engine.disconnect()

