class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ans=0
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1


        for num in freq:
            if num+1 in freq:
                ans=max(ans,freq[num]+freq[num+1])

        return ans                