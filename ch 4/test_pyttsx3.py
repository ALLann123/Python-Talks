#!/usr/bin/python3
import pyttsx3

engine=pyttsx3.init() #create a pyttsx3 object
engine.say("Hello Sir, I am shadow")   #the say() function converts the test to speech siganal and prepares it to send to the speaker
engine.say("You are Allan and I am your personal Assistant")
engine.say("Good Bye for now")
engine.runAndWait()  #sends the speech to the speaker
