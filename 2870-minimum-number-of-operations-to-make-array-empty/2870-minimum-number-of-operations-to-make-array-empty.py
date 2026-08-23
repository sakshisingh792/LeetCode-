class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq={}
        for x in nums:
            freq[x]=freq.get(x,0)+1
        ans=0    
        for y in freq:
            z=freq[y]
            if z==1:
                return -1

            if z%3==0:
                ans+=z//3

            else:
                ans+=(z//3)+1
        return ans                    

