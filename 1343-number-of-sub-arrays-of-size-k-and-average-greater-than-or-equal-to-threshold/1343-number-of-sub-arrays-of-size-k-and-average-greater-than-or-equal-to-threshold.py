class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        ans=0
        left=0
        summ=0
        for right in range(len(nums)):
            summ+=nums[right]
            if right-left+1>k:
                summ-=nums[left]
                left+=1

            if right-left+1==k:
                if summ//k>=threshold:
                    ans+=1    
        return ans            
        