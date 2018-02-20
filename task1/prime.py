#!/usr/bin/python
def prime_num(inp):
	for val in range(2,(inp/2)+1):
		if (inp%val==0):
			print "%d is not a prime number"%inp
			break
	else:
		print "%d is prime number"%inp

if __name__=="__main__":
	inp=input("Enter the input number :")
	prime_num(inp)
