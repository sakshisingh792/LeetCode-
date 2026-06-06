class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left_sum=0
        
        total_sum=sum(nums)
        ans=[0]*n
        for i in range(n):
            right_sum=total_sum-left_sum-nums[i]
            ans[i]=abs(right_sum-left_sum)
            left_sum+=nums[i]
        return ans    