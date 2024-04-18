# striver playlist codes

# 1. print 0,1,2 using recursion
```python
count=0
def one():
	global count 
	if count==3:
		return 
	print(count)
	count+=1
	one()
one()

```
# 2. print name 5 times
```python
cnt=0
def printName():
	global cnt 
	if cnt==5:
		return 
	print("omkar shelke")
	cnt+=1
	printName()
printName()

#way by striver through recursion
def printName(i,n):
	if i>n:
		return
	print("omkar")
	printName(i+1,n)
printName(0,5)
```
# 3. print from 1 to N
```python
def printFrom(i,n):
	if i>n:
		return
	print(i)
	printFrom(i+1,n)
printFrom(1,5)
```
# 4. print from N to 1 
```python
def printFrom(n):
	if n<1:
		return 
	print(n)
	printFrom(n-1)
printFrom(5)
```
# 5. print even numbers from 0 to n uisng recursion
```python
def printEven(i,n):
	if i>n:
		return 
	print(i)
	printEven(i+2,n)
printEven(0,10)

# way 2
def printEven(i,n):
	if i>=n:
		return
	if i%2==0:
		print(i)
	printEven(i+1,n)
printEven(1,10)
```
# 4. print odd numbers from i to n both given as args 
```python
def printOdd(i,n):
	if i>=n:
		return
	if i%2!=0:
		print(i)
	printOdd(i+1,n)
printOdd(0,10)
```
# 5. print 1 to n using backtracking
```python
def printIncreasing(i,n): 
	#using backtracking
	if i<1:
		return 
	printIncreasing(i-1,n)
	print(i)
printIncreasing(3,3)
```
# 6. print n to 1 using backtracking
```python
def printDecreasing(i,n): 
	#using backtracking
	if i>n:
		return
	printDecreasing(i+1,n)
	print(i)
printDecreasing(1,3)
```
# 7. sum of first n numbers using recursion
```python
def printSum(i,sum):
	# parametarized recursion
	if i<1:
		print(sum)
		return 
	return printSum(i-1,i+sum)
printSum(3,0)

#using functional recursion , here functions itself returns me value	
def printSum(n):
	# functional recursion
	if n==0:
		return 0 
	return n+printSum(n-1)

print(printSum(3))	
```
# 8. print factorial of n 
```python
def printFact(n):
	# functional recursion
	if n==0:
		return 1 
	return n*printFact(n-1)

print(printFact(3))	

# parametarized recursion/way
def printFact(i,fact):
	# parametarized recursion
	if i<1:
		print(fact)
		return	
	return printFact(i-1,fact*i)

printFact(7,1)	
```
# 9. reverse an array using 2 pointer approach
```python
def revArray(arr):
	# using 2 pointer approach
	l,r=0,len(arr)-1

	while l!=r:
		arr[l],arr[r]=arr[r],arr[l]
		l+=1
		r-=1
	return arr 

arr=[1,2,3]
print(revArray(arr))
```
# 10. reverse array using single pointer 
```python
def revArray(i,arr):
	# using 2 pointer approach
	n=len(arr)

	if i>=n//2:
		return
	else:
		arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
		revArray(i+1,arr)
	return arr 
arr=[1,2,3,4]
n=len(arr)
print(revArray(0,arr))
```
# 11. reverse array using two pointer approach (recursion)
```python
def revArray(l,r,arr):
	# using two pointer l and r
	if l>=r: return 
	arr[l],arr[r]=arr[r],arr[l]
	revArray(l+1,r-1,arr)
	return arr 

arr=[1,2,3]
print(revArray(0,len(arr)-1,arr))
```
# 12. check for palindrome string
```python
def checkPalindrome(s,i):
	n=len(s)
	if i>len(s)//2:
		return True
	if s[i]!=s[n-i-1]:
		return False
	return checkPalindrome(s,i+1)

print(checkPalindrome("om",0))
```
# 13. print fib using recursion
```python
def printFib(n):
	if n<=1:
		return n 
	last=printFib(n-1)
	slast=printFib(n-2)
	return last+slast
print(printFib(5))
```
14. print all subsequences of an array arr 
```python
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
```
# 15. print subsequences whose sum is equal to k
```python
def printS(idx,sub,s,target_sum,arr,n):
	# idx reaches end of array
	if idx==n:
		# s becomes equal to target sum
		if s==target_sum:
			print([ele for ele in sub])
		return

	# take
	sub.append(arr[idx])
	s+=arr[idx]
	printS(idx+1,sub,s,target_sum,arr,n)

	# not to take 
	sub.pop()
	s-=arr[idx]
	printS(idx+1,sub,s,target_sum,arr,n)
	return sub
arr=[1,2,1]
n=len(arr)
target_sum=2
sub=[]
printS(0,sub,0,target_sum,arr,n)
```
# 16. print only 1 subsequence which leads to sum k 
```python
def printS(idx,sub,s,target_sum,arr,n):
	if idx==n:
		if s==target_sum:
			for ele in sub:
				print(ele)
			return True 
		return False 

	# take
	sub.append(arr[idx])
	s+=arr[idx]
	if printS(idx+1,sub,s,target_sum,arr,n)==True:
		return True	

	# not to take 
	sub.pop()
	s-=arr[idx]
	if printS(idx+1,sub,s,target_sum,arr,n)==True:
		return True
	return False

arr=[1,2,1]
n=len(arr)
target_sum=2
sub=[]
printS(0,sub,0,target_sum,arr,n)
```
# 17. count subsequences with sum equal to k 
```python
def printS(idx,arr,n,s,sum):
	# only when array contains positive
	if s>sum: return 0
	# when indx reached last
	if idx==n:
		# when s becomes equal to sum 
		if s==sum:
			return 1 
		else:
			return 0

	# take 
	s+=arr[idx]
	l=printS(idx+1,arr,n,s,sum)

	# not to take 
	s-=arr[idx]
	r=printS(idx+1,arr,n,s,sum)

	return l+r
arr=[1,2,1]
n=len(arr)
target_sum=2
print(printS(0,arr,n,0,target_sum))
```
18. merge sort 
```python
```