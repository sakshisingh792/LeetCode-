class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atmost(k):
            n=len(nums)
            freq={}
            count=0
            left=0
            ans=0
            for right in range(n):
                ele=nums[right]
                freq[ele]=freq.get(ele,0)+1

                while len(freq)>k:
                    freq[nums[left]]-=1

                    if freq[nums[left]]==0:
                        del freq[nums[left]]
                    left+=1
                ans+=right-left+1
            return ans
        return atmost(k)-atmost(k-1)           
            


        re            
       