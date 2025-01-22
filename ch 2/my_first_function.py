#!/usr/bin/python3
from time import sleep
def msg(name):
        print(f"To {name}, Hey You are welcome to the event this coming week")

'''msg('allan')
msg('karis')'''

#get user inputs to send to the message
num_sends=int(input("How many people to send to the message? "))

person=[]
for i in range(num_sends):
        i=input("Enter Recepient Name: ")
        person.append(i)
print("---------------------------------------")
print("[+]Sending Message Wait")
sleep(2)
for name in person:
        msg(name)
print()
print("[+]Done")