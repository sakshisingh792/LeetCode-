class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        ans=min(
            nums[n-1]-nums[2], # change nums[0],nums[1] two smallest value
            nums[n-3]-nums[0],# change nums[n-1],nums[n-2] two largest value
            nums[n-2]-nums[1] # change nums[n-1],nums[0] one smallest and one largest
        )
        return ans

        