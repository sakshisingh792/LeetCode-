class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix=1
        suffix=1
        ans=float("-inf")
        n=len(nums)
        for i in range(len(nums)):
            prefix=(prefix or 1)*nums[i]
            suffix=(suffix or 1)*nums[n-i-1]
            ans=max(ans,prefix,suffix)
        return ans    

        