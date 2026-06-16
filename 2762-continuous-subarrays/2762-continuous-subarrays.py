class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        from collections import deque
        qmin=deque()
        qmax=deque()
        ans=0
        left=0
        for right in range(len(nums)):
            while qmax and nums[qmax[-1]]<nums[right]:
                qmax.pop()
            qmax.append(right)


            while qmin and nums[qmin[-1]]> nums[right]:
                qmin.pop()
            qmin.append(right)

            while nums[qmax[0]]-nums[qmin[0]]>2:
                if qmax[0]==left:
                    qmax.popleft()
                if qmin[0]==left:
                    qmin.popleft()
                left+=1

            ans+=right-left+1
        return ans                        
       