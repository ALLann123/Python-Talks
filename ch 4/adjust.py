#!/usr/bin/python3
import pyttsx3

engine=pyttsx3.init()

voice_id=0

voices=engine.getProperty('voices')
engine.setProperty('voice', voices[voice_id].id)

engine.setProperty('rate', 140)
engine.setProperty('volume', 2)
engine.say("Testing new settings")
engine.runAndWait()

