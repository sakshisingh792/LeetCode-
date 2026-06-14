class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        freq={}
        left=0
        n=len(nums)
        maxm=0
        curr=0
        for right in range(n):
            freq[nums[right]]=freq.get(nums[right],0)+1
            curr+=nums[right]
            while freq[nums[right]]>1:
                
                freq[nums[left]]-=1
                curr-=nums[left]
                left+=1
            maxm=max(curr,maxm)
        return maxm         