class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n == 1:
          return nums[0]

        def dfs(start,end):
            dp=[-1]*n

            def solve(i):
                if i>end:
                    return 0


                if dp[i]!=-1:
                    return dp[i]


                rob=nums[i]+solve(i+2)
                skip=solve(i+1)
                dp[i]=max(rob,skip)
                return dp[i]
            return solve(start)
        return max(dfs(0,n-2),dfs(1,n-1))        


       