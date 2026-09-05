class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        suffix_minm=[0]*n
        suffix_minm[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            suffix_minm[i]=min(nums[i],suffix_minm[i+1])

        maxm=nums[0]
        for i in range(n)   :
            maxm=max(nums[i],maxm)
            if maxm-suffix_minm[i] <=k:
                return i
        return -1        
        