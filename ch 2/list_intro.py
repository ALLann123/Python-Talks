#!/usr/bin/python3

ip=["192.168.1.1","192.168.1.34","192.168.1.155","192.168.1.100","192.168.1.90","192.168.1.23"]

for i in range(len(ip)):
	print(f"[+]Starting Attack on {ip[i]}")

print("==========================================")
ip.append("192.168.90.90")
for i in range(len(ip)):
	print(f"[+]Starting Attack on {ip[i]}")
print("Session Job Created")


