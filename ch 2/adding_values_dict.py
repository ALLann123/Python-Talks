#!/usr/bin/python3
from time import sleep
#create empty dictionary
students=[]

num_stud_add=int(input("Enter the number of students  to add>> "))

#lets add students to the list
for i in range(num_stud_add):
	student={}
	student['name']=input("Enter Students Name: ")
	student['age']=int(input("Enter Students Age: "))
	student['course']=input("Course of study(BSc.): ")
	students.append(student)
	print()

print("=========================================================")
print("\n[+] Displaying student Records")
sleep(2)
for student in students:
	for key, value in student.items():
		print(f"  '{key}': '{value}',")
	print("--------------------------------------------------")

print()
print("Good Bye!!")
