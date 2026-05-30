class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        freq={}
        freq[0]=-1
        prefix=0
        max_len=0
        for i in range(len(nums)):
            if nums[i]==0:
                prefix+=-1
            else:
                prefix+=1

            if prefix in freq:
                lenn=i-freq[prefix]
                max_len=max(lenn,max_len)
            else:
                freq[prefix]=i

        return max_len                    

        