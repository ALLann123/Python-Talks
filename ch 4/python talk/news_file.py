#!/usr/bin/python3
from mysr import voice_to_text
from mysay import print_say
import pathlib

print_say("Hello Sir, welcome")
print_say("Do you want to here the article?")
respond=voice_to_text()

print_say(f'you said {respond}')
if respond.lower() == "start":
	print_say("Lets start")
	myfile=pathlib.Path.cwd() / 'files' / 'bane.txt'
	with open(myfile, 'r')as f:
		content=f.read()		
	#let python speak the text
	print_say(content)
	print_say("Finished, Powering down")
elif respond.lower()=="stop":
	print_say("Powering down Sir")