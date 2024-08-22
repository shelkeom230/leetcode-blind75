# sum of first n numbers 
def printSum(i,sum):
	if i<1: 
		print(sum)
		return
	return printSum(i-1,i+sum)

i=int(input("enter a number: "))
printSum(i,0)