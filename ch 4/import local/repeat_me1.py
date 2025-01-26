#!/usr/bin/python3
from mysay import print_say
from mysr import voice_to_text

print_say('Welcome Sir, I hope you are well.')
print_say('I am listening now!')

while True:
	print('Python is listening...')
	inp=voice_to_text()
	if inp=="stop listening":
		print_say(f'You just said {inp}, goodbye!!')
		break
	else:
		print_say(f'You just said {inp}')
		continue
