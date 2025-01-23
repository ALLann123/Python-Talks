#!/usr/bin/python3
import webbrowser
import speech_recognition as sr

print("[+]Shadow welcomes You!!")
print("*************************************")
#function to convert text to speech
speech=sr.Recognizer()

def voice_to_text():
	voice_input=""
	with sr.Microphone() as source:
		speech.adjust_for_ambient_noise(source)
		try:
			audio=speech.listen(source)
			voice_input=speech.recognize_google(audio)
		except sr.UnknownValueError:
			pass
		except sr.RequestError:
			pass
		except sr.WaitTimeoutError:
			pass
	return voice_input

while True:
	print("[+]Shadow is listening")
	inp = voice_to_text()    #call the function
	print("===============================")
	print(f'[+]You just said {inp}')
	#the magic word to stop the script
	if inp == "stop listening":
		print("[-]Goodbye Sir!")
		break
	elif "browser" in inp:       #get browser url and open the browser
		inp=inp.replace('browser ', '')
		webbrowser.open("http://"+inp)
		continue


