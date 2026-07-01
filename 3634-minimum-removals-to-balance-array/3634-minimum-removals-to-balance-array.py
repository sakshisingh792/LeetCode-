class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_len=0
        left=0
        n=len(nums)
        for right in range(n):
            while nums[right]> nums[left]*k:
                left+=1

            max_len=max(max_len,right-left+1)

        return  n-max_len        
        