class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix=0
        freq={}
        freq[0]=1
        ans=0
        for i in range(len(nums)):
            prefix+=nums[i]
            if prefix-goal in freq:
                ans+=freq[prefix-goal]

            if prefix in freq:
                freq[prefix]+=1
            else:
                freq[prefix]=1

        return ans                

