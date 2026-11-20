class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[0]*n
        if n==1:
            return nums[0]
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n):
            rob=dp[i-2]+nums[i]
            skip=dp[i-1]
            dp[i]=max(rob,skip)


        return dp[n-1]    

        
                
        