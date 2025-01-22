#!/usr/bin/python3
import speech_recognition as sr 

speech=sr.Recognizer() #function to convert text to speech
while True:
	print("[+]Python is listening")
	inp=""
	with sr.Microphone() as source:  #the source of the audio comes from the text
		speech.adjust_for_ambient_noise(source)  #cleans the noise of the audio
		try:
			audio=speech.listen(source)
			inp=speech.recognize_google(audio) #uses google API to convert the speech to text
		except sr.UnknownValueError:
			pass
		except sr.RequestError:
			pass
		except sr.WaitTimeoutError:
			pass

	print(f'You just said {inp}') #print the output in text
	if inp=="stop listening":
		print('GoodBye!!')
		break
