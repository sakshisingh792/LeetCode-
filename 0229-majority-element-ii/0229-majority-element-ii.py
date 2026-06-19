class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        freq={}
        ans=set()
        for i in range(len(nums)):
            ch=nums[i]
            freq[ch]=freq.get(ch,0)+1

            if freq[ch]>n//3:
                ans.add(ch)
        return list(ans)        


        