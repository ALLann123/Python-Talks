#!/usr/bin/python3    #shebang statement

#for a grading system
name=input("Enter Student Name: ")
course="BSc. IT"
reg_no=input("Enter Regisration Number: ")
marks=int(input("Enter STudent Marks: "))

print("===============================================")
print("----------Student Details-----------------")

print(name)
print(course)
print(reg_no)

if marks>=80 and marks<100:
	print("Grade: A")
elif marks>=70:
	print("Grade: B")
elif marks>=60:
	print("Grade: C")
elif marks>=50:
	print("Grade: D")
else:
	print("Fail!!")

print()
print("GoodBye!!")
