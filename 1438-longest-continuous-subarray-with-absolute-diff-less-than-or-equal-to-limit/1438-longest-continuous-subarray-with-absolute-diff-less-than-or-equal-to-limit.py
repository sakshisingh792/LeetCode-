class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque
        maxq=deque()
        minq=deque()
        left=0
        maxm=float("-inf")
        for right in range(len(nums)):
            while maxq and nums[right]>maxq[-1]:
                maxq.pop()

            maxq.append(nums[right])
            while minq and nums[right]<minq[-1]:
                minq.pop()
            minq.append(nums[right])

            while maxq[0]-minq[0]>limit:
                if maxq[0]==nums[left]:
                    maxq.popleft()

                if minq[0]==nums[left]:
                    minq.popleft()
                left+=1
            maxm=max(maxm,right-left+1) 
        return maxm               


       
             

        