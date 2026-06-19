class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum=0
        maxm=float("-inf")
        for i in range(len(nums)):
            cur_sum+=nums[i]
            maxm=max(maxm,cur_sum)   
            if cur_sum<0:
                cur_sum=0

            
        return maxm     
                     


        