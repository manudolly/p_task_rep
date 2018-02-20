#!/usr/bin/python
def prime_list(inp1=1,inp2=100):
        l=[]
        for val in range(inp1,inp2):
                if(val>1):
                        for val1 in range(2,(val/2)+1):
                                if (val%val1==0):
                                        break
                        else:
                                l.append(val)
        return l
print prime_list()

if __name__=="__main__":
	inp1=input("Enter the starting number :")
	inp2=input("Enter the ending number :")
	print prime_list(inp1,inp2)
