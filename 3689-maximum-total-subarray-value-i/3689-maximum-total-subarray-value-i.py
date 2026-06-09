class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maxm=max(nums)
        minm=min(nums)
        diff=maxm-minm
        return k*diff
        