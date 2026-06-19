class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        left=0
        right=n-1
        while left<right:
            total=nums[left]+nums[right]
            if total==target:
                return [left+1,right+1]

            if total<target:
                left+=1
            else:
                right-=1

        