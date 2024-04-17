# all solutions

## 1 Two sum

```python
def TwoSum(nums,target):
    prevMap={}

    for i,n in enumerate(nums):
        diff=target-n
        if diff in prevMap:
            return [prevMap[diff],i]
        prevMap[n]=i
    return prevMap[n]        
```
# 2 best time to buy and sell stock brother
```python
def BestTime(prices):
    l,r=0,1
    maxP=0

    while r<len(prices):
        if prices[l]<prices[r]:
            profit=prices[r]-prices[l]
            maxP=max(maxP,profit)
        else:
            l=r
        r+=1
    return maxP
```
# 3 contains duplicate
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset=set()

        for ele in nums:
            if ele in hashset:
                return True
            hashset.add(ele)
        return False  
```
# 4. Product of array except self
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        prefix=1

        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        postfix=1

        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res
```
# 5. maximum subarray
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub=nums[0]
        curSum=0

        for ele in nums:
            if curSum<0:
                curSum=0
            curSum+=ele
            maxSub=max(maxSub,curSum)
        return maxSub
```
# 6. maximum product subarray
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curMin,curMax=1,1

        for n in nums:
            if n==0:
                curMin,curMax=1,1
                continue 
            tmp=curMax*n
            curMax=max(n*curMax,n*curMin,n)
            curMin=min(tmp,n*curMin,n)
            res=max(res,curMax)
        return res
```

## 7. find minimum  in a sorted rotated array 
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res=nums[0]
        l,r=0,len(nums)-1

        while l<=r:
            if nums[l]<nums[r]:
                res=min(res,nums[l])
                break 
            else:
                m=(l+r)//2
                res=min(res,nums[m])
                if nums[m]>=nums[l]:
                    l=m+1
                else:
                    r=m-1
        return res           
```        

## 8. search in a rotated sorted array
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1

        while l<=r:
            mid=(l+r)//2

            if nums[mid]==target:
                return mid 

            # search left sorted portion 
            if nums[l]<=nums[mid]:
                if target>nums[mid] or target<nums[l]:
                    l=mid+1
                else:
                    r=mid-1

            # search for right sorted portion 
            else:
                if target<nums[mid] or target>nums[r]:
                    r=mid-1
                else:
                    l=mid+1
        return -1                 
```
# 9. three sum 
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue 
            
            l,r=i+1,len(nums)-1
            while l<r:
                threeSum=a+nums[l]+nums[r]
                if threeSum>0:
                    r-=1
                elif threeSum<0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res
```
# 10. container with max water 
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # res=0

        # for l in range(len(height)):
        #     for r in range(l+1,len(height)):
        #         area=(r-l)*min(height[l],height[r])
        #         res=max(res,area)
        # return res

        res=0

        l,r=0,len(height)-1

        while l<r:
            area=(r-l)*min(height[l],height[r])
            res=max(res,area)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res
```
# 11. sum of 2 integers
```cpp
class Solution {
public:
    int getSum(int a, int b) {
        uint32_t carry=a&b;
        int swc=a^b;
        int acc=carry<<1;

        while(carry!=0){
            carry=swc&acc;
            swc=swc^acc;
            acc=carry<<1;
        }
        return swc;
        
    }
};
```
# 12. count no. of 1's in a decimal number
```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        binary=bin(n)[2:]
        binary=binary.zfill(3)

        count=0
        for ele in binary:
            if ele=='1':
                count+=1
        return count                
```        
# 13. return number of set bits as an array 
```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]*(n+1)

        for i in range(1,n+1):
            ans[i]=ans[i>>1]+(i&1)
        return ans

# answer 2 by neetcode 
    def countBits(self, n: int) -> List[int]:
        dp=[0]*(n+1)
        offset=1

        for i in range(1,n+1):
            if offset*2==i:
                offset=i
            dp[i]=1+dp[i-offset]
        return dp        
```
# 14. find missing number from an array 
```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        arithsum=(n*(n+1))//2
        arrsum=sum(nums)
        return arithsum-arrsum
```
# 15. return the decimal number for 32 bit unsigned binary number brother
```python
class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for i in range(32,0,-1):
            rightbit=n&1
            res=(res<<1)|rightbit
            n=n>>1
        return res
```        
# 16. climbing stairs 1 or 2 dp
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        one,two=1,1
        for i in range(n-1):
            temp=one
            one=one+two
            two=temp
        return one              
```
# 17. coin change
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)

        dp[0]=0
        for a in range(1,amount+1):
            for coin in coins:
                if a-coin>=0:
                    dp[a]=min(dp[a],1+dp[a-coin])
        return dp[amount] if dp[amount]!=amount+1 else -1                    
```    
# 18. longest increasing subsequence DP 
```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS=[1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    LIS[i]=max(LIS[i],1+LIS[j])
        return max(LIS)                    
```
# 19. longest common subsequence dp 
```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i]==text2[j]:
                    dp[i][j]=1+dp[i+1][j+1] #diagonal
                else:
                    dp[i][j]=max(dp[i][j+1],dp[i+1][j]) #right and bottom
        return dp[0][0]
```
# 20. word break dp 
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        dp[len(s)]=True

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:    
                if (i+len(w))<=len(s) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]                                       
```
# 21. combination sum 4
```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp={0:1}
        total=0
        for total in range(1,target+1):
            dp[total]=0
            for n in nums:
                dp[total]+=dp.get(total-n,0)
        return dp[target]                
```
# 22. house roober 
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2=0,0

        #[rob1,rob2,n,n+1,n+2,...]

        for n in nums:
            temp=max(n+rob1,rob2)
            rob1=rob2
            rob2=temp
        return rob2
```
# 23. house robber 3
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))

    def helper(self,nums):
        rob1,rob2=0,0

        for n in nums:
            newRob=max(n+rob1,rob2)
            rob1=rob2
            rob2=newRob
        return rob2
```
# 24. decode ways 
```python
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0
            res = dfs(i + 1)
            if (i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            dp[i] = res
            return res
        
        return dfs(0)
```
# 25. moving robot
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row=[1]*n

        for i in range(m-1):
            newRow=[1]*n
            for j in range(n-2,-1,-1):
                newRow[j]=newRow[j+1]+row[j]
            row=newRow
        return row[0]
```
# 26. jump game
```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # start from last
        goal=len(nums)-1

        for i in range(len(nums)-1,-1,-1):
            #if the index plus value at index can reach the goal or beyond that
            if i+nums[i]>=goal:
                #update the goal index
                goal=i
                #goal reached then true otherwise false
        return True if goal==0 else False
```