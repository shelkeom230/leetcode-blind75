# sum of 2 integers without using +
# print even number from 1 to 10 using recursion 
def printSub(arr,sub,idx,n):
	if idx==n:
		print(sub)
		return 

	# take 
	sub.insert(idx,arr[idx])
	printSub(arr,sub,idx+1,n)

	# not take 
	sub.remove(arr[idx])
	printSub(arr,sub,idx+1,n)
	return sub 
arr=[1,2,3]
sub=[]
n=len(arr)
idx=0
printSub(arr,sub,idx,n)

