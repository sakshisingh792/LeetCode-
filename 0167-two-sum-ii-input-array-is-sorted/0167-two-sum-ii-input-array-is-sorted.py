class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        left=0
        right=n-1
        while left<right:
            summ=nums[left]+nums[right]
            if target==summ:
                return [left+1,right+1]
            elif target<summ:
                right-=1
            else:
                left+=1        
        