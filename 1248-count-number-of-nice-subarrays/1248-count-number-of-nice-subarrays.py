class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        freq={}
        freq[0] = 1
        prefix=0
        ans=0
        for i in range(len(nums)):
            if nums[i]%2==1:
                prefix+=1

            if prefix-k in freq:
                ans+=freq[prefix-k]

            if prefix in freq:
                freq[prefix]+=1
            else:
                freq[prefix]=1
        return ans                  
