class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum=nums[0]
        i=1
        sum=nums[0]
        while i<len(nums):
            if nums[i]>nums[i-1]:
                sum+=nums[i]
                i+=1
            else:
                sum=nums[i]
                i+=1    
                
            
            max_sum=max(max_sum,sum) 
        return max_sum       

            
        