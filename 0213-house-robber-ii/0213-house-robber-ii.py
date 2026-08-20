class Solution:
    #tabulation
    def solve(self,nums,dp,ind):

        prev=nums[0]
        prev2=0
        for i in range(1,len(nums)):
            pick=nums[i]+prev2
            skip=prev
            curr=max(pick,skip)
            prev2=prev
            prev=curr
        return prev    
            


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

                 
        