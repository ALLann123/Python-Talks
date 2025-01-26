#!/usr/bin/python3
import platform
from mysr import voice_to_text

# Initialize the speech engine for Windows
if platform.system().lower() == "windows":
    import pyttsx3
    engine = pyttsx3.init()
    engine.say("Welcome. I am Shadow, how can I help you?")
    engine.runAndWait()
else:
    import os
    os.system('gtts-cli --nocheck "Welcome. I am Shadow, how can I help you?" | mpg123 -q -')

while True:
    print("Shadow is listening")
    inp = voice_to_text()

    if inp == "stop listening":
        print("Goodbye Sir, powering off")
        if platform.system().lower() == "windows":
            engine.say("Shutting down, sir. Goodbye.")
            engine.runAndWait()
        else:
            os.system('gtts-cli --nocheck "Shutting down, sir. Goodbye." | mpg123 -q -')
        break
    else:
        print(f"You just said: {inp}")
        if platform.system().lower() == "windows":
            engine.say(f"You just said: {inp}")
            engine.runAndWait()
        else:
            os.system(f'gtts-cli --nocheck "You just said: {inp}" | mpg123 -q -')
