#!/usr/bin/python3
search_ip=input("Enter The Target IP>> ")
print("Learn Continue")            
for n in (1,2,3):
	if n == 2:
		continue
	print(n)

print("==============================================")

print("Learning break")

ip=["192.168.1.1","192.168.1.34","192.168.1.155","192.168.1.100","192.168.1.90","192.168.1.23"]

for i in ip:
	if i==search_ip:
		print(f"Found the target {search_ip}")
		break

print("===============================================")

