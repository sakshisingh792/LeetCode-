class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        runn_sum=[0]*n
        summ=0
        for i in range(n):
            summ+=nums[i]
            runn_sum[i]=summ

        return runn_sum    
        