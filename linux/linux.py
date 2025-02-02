#!/usr/bin/python3
import os
import time
import pyaudio
import speech_recognition as sr
import playsound
from gtts import gTTS

language = 'en'

os.system(f'gtts-cli --nocheck "Hello Sir" | mpg123 -q -')

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        audio = r.listen(source)
        said = ''
        try:
            said = r.recognize_google(audio)
            print(said)
            global guy
            guy = said

            if 'attack' in said:
                said2 = said.split(" ")[1]
                print("Starting Vulnerability scan")
                os.system(f"nmap -sS {said2}.com")

            elif "Shadow" in said:
                speech = gTTS(text=said, lang=language, slow=False, tld="com.au")
                speech.save("welcome1.mp3")
                playsound.playsound("welcome1.mp3")

        except Exception as e:
            print(f"Exception: {e}")
    return said

while True:
    get_audio()
    if "stop" in guy:
        break