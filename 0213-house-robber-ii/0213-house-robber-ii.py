class Solution:

    def solve(self,nums,dp,ind):
        if ind==0:
            return nums[0]

        if dp[ind]!=-1:
            return dp[ind]

        if ind>1:
          pick=nums[ind]+self.solve(nums,dp,ind-2)
        else:
            pick=nums[ind]   
        skip=self.solve(nums,dp,ind-1)

        dp[ind]=max(pick,skip)

        return dp[ind]        
    def rob(self, nums: List[int]) -> int:
        n=len(nums)

        if n==1:
            return nums[0]

        arr1=nums[0:n-1]
        dp1=[-1]*len(arr1) 

        arr2=nums[1:n]
        dp2=[-1]*len(arr2)

        ans1=self.solve(arr1,dp1,len(arr1)-1)   
        ans2=self.solve(arr2,dp2,len(arr2)-1)

    

        return max(ans1,ans2)

                 
        