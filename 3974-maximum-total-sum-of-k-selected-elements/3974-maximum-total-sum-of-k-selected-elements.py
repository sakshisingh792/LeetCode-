class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse=True)
        ans=0
        for i in range(k):
            if mul>0:
                ans+=nums[i]*mul
            else:
                ans+=nums[i]
            mul-=1

        return ans            
        