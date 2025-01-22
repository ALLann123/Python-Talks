#!/usr/bin/python3

def calc_sales(sales1,sales2,sales3):
	sales=sales1+sales2+sales3
	return sales

total=calc_sales(1900,2000,2333)

def divide_share(earned):
	result=earned/2
	print(f"Each Investor Earned {result}")

divide_share(total)

