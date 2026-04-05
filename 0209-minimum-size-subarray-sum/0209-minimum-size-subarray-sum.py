class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minm = float("inf")
        left=0
        sum=0
        for right in range(len(nums)):
            sum+=nums[right]
            while sum>=target:
                minm=min(minm,right-left+1)
                
                sum-=nums[left]
                left+=1
     
        
        if minm == float("inf"):
            return 0
        return minm            

                

        