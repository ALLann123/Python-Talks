#!/usr/bin/python3
import pathlib
import platform
import os
import speech_recognition as sr
from time import sleep

speech = sr.Recognizer()
directory = pathlib.Path.cwd()


def voice_to_text():
    voice_input = ""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source, timeout=5, phrase_time_limit=10)
            voice_input = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    return voice_input

def open_file(filename):
    file_path = directory / filename
    if platform.system() == "Windows":
        os.system(f"explorer {file_path}")
    elif platform.system() == "Darwin":  # macOS
        os.system(f"open {file_path}")
    else:  # Linux/Unix
        os.system(f"xdg-open {file_path}")


while True:
    print("[+] Shadow is listening")
    inp = voice_to_text().lower()
    print(f"You just said {inp}")
    if inp == "stop listening":
        print("Good Bye!!")
        break
    elif "open pdf" in inp:
        inp = inp.replace('open pdf ', '')
        myfile = f'{inp}.pdf'
        open_file(myfile)
        print("===========================")
        continue
    elif "open word" in inp:
        inp = inp.replace('open word ', '')
        myfile = f'{inp}.docx'
        open_file(myfile)
        print("===========================")
        continue
    elif "open excel" in inp:
        inp = inp.replace('open excel ', '')
        myfile = f'{inp}.xlsx'
        open_file(myfile)
        print("===========================")
        continue
    elif "open powerpoint" in inp:
        inp = inp.replace('open powerpoint ', '')
        myfile = f'{inp}.pptx'
        open_file(myfile)
        print("===========================")
        continue
    elif "open audio" in inp:
        inp = inp.replace('open audio ', '')
        myfile = f'{inp}.mp3'
        open_file(myfile)
        print("===========================")
        continue
    elif 'start attack' in inp:
        print("[+] Started Enumeration")
        sleep(2)
        print("[+] Target is vulnerable")
        sleep(2)
        print("shell>>")
        print("Backgrounded the shell")
        print("===========================")
        continue
