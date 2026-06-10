class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=0
        n=len(nums)
        summ=0
       
        max_avg=float("-inf")
        for right in range(n):
            summ+=nums[right]
            if ((right-left)+1)==k:
                avg=summ/k
                
                max_avg=max(avg,max_avg)
                summ=summ-nums[left]
                left+=1
        return max_avg