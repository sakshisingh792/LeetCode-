class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n=len(nums)
        left_sum=0
        total_sum=sum(nums)
        for i in range(n):
            right=total_sum-left_sum-nums[i]
            if left_sum==right:
                return i
            left_sum+=nums[i]  
        return -1      
        