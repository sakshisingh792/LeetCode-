class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        maxm=0
        count=0
        for right in range(len(nums)):
            count+=1
            if nums[right]==0:
                count=0

            maxm=max(count,maxm)    
        return maxm