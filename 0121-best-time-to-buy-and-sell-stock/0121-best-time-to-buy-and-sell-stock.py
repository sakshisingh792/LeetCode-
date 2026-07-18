class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        mxm_profit=float("-inf")
        cp=nums[0]
        sp=0
        for i in range(len(nums)):
            if nums[i]<=cp:
                cp=nums[i]

            if nums[i]>=cp:
                sp=nums[i] 

            mxm_profit=max(mxm_profit,sp-cp)


        return mxm_profit           
        