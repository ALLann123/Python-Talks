# Make sure you put mysr.py in the same folder as this script
from mysr import voice_to_text
import os

os.system('gtts-cli --nocheck "Welcome." | mpg123 -q -')

while True:
    print('Python is listening...')
    inp = voice_to_text()
    if inp == "stop listening":
        print(f'You just said {inp}; goodbye!')
        os.system(f'gtts-cli --nocheck "You just said {inp}; goodbye!" | mpg123 -q -')
        break
    else:
        print(f'You just said {inp}')
        os.system(f'gtts-cli --nocheck "You just said {inp}" | mpg123 -q -')
