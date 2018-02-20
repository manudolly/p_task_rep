#!/usr/bin/python
def prime_tuple(inp1=50,inp2=200):
        l=[]
        for val in range(inp1,inp2):
                if(val>1):
                        for val1 in range(2,(val/2)+1):
                                if (val%val1==0):
                                        break
                        else:
                                l.append(val)
        return tuple(l)
print prime_tuple()

if __name__=="__main__":
	inp1=input("Enter the starting number :")
	inp2=input("Enter the ending number :")
	print prime_tuple(inp1,inp2)
