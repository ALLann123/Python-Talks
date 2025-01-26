#!/usr/bin/python3
import pyttsx3

engine = pyttsx3.init()  # Create an object from the class

# Get the available voices
voices = engine.getProperty('voices')
print("Available voices:")
for voice in voices:
    print(f"Voice ID: {voice.id}, Name: {voice.name}, Language: {voice.languages}")

# Get and display the current speech rate
rate = engine.getProperty("rate")
print("The default speed of the speech is:", rate)

# Get and display the current volume
volume = engine.getProperty("volume")
print("The default volume is:", volume)

# Speak out the settings
engine.say("Hello Sir, Here are my settings.")
engine.say(f"My default speed is {rate}, and my volume is {volume}.")
engine.runAndWait()
