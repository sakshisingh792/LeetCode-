class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
       
        n=len(nums)
      
        for i in range(len(nums)):
            maxm=max(nums[:i+1])
            minm=min(nums[i:n])
            score=maxm-minm
            if score<=k:
                return i
                
                
        return -1