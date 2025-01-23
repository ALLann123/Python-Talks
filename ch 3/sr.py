import speech_recognition as sr 

speech=sr.Recognizer()     #call function use to convert voice to text

print("Shadow Is listening")

#we tell the script that the source of the audio comes from microphone
with sr.Microphone() as source:
	speech.adjust_for_ambient_noise(source)    #we reduce the noise on our voice
	audio=speech.listen(source)
	inp=speech.recognize_google(audio)   #uses google API to recognize speech from audio source

print(f"You just said {inp}")

