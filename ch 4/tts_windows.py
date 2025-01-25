#!/usr/bin/python3
import pyttsx3

engine=pyttsx3.init()
while True:
	inp=input("What do you want to convert to speech?\n")
	if inp=="done":
		print(f"You just typed {inp}, goodbye!!")
		engine.say(f"You just typed {inp}, goodbye")
		engine.runAndWait()
		break
	else:
		print(f"You just typed {inp}")
		engine.say(f"You just typed {inp}")
		engine.runAndWait()
		continue