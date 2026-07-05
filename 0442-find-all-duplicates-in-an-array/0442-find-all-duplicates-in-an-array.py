class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1

        ans=[]
        for i in freq:
            if freq[i]==2:
                ans.append(i)

        return ans            
        