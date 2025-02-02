# Make sure you put mysr.py in the same folder as this script
from mysr import voice_to_text
import os

def speak(text):
    os.system(f'espeak "{text}"')

speak("Welcome.")

while True:
    print('Python is listening...')
    inp = voice_to_text()
    if inp == "stop listening":
        print(f'You just said {inp}; goodbye!')
        speak(f'You just said {inp}; goodbye!')
        break
    else:
        print(f'You just said {inp}')
        speak(f'You just said {inp}')
