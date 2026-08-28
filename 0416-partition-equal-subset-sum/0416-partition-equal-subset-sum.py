class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        #Memoization
        n=len(nums)
        total=sum(nums)
        target=total//2
        if total%2==1:
            return False
        dp= [[-1]*(target+1) for _ in range(n)]  
        def partition(i,target):
            if target==0:
                return True

            if i>n-1:
                return False


            if dp[i][target]!=-1:
                return dp[i][target]   
            pick=False    
            if nums[i]<=target:

                
                pick=partition(i+1,target-nums[i])
                
                
            notpick=partition(i+1,target)

            dp[i][target]= pick or notpick
            return dp[i][target]
            


        return partition(0,target)    
            
        