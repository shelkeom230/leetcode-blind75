# sum of first n numbers 
def printSum(nums):
    sum=0
    for i in nums:
        sum+=i 
    return sum 
    

nums=[1,2,3,4]
print(printSum(nums))