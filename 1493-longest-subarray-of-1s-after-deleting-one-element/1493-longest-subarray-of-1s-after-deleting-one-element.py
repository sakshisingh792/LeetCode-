class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count_zeros=0
        left=0
        maxm=float("-inf")
        for right in range(len(nums)):
            if nums[right]==0:
                count_zeros+=1

            while count_zeros>1:
                if nums[left]==0:
                    count_zeros-=1

                left+=1    

            maxm=max(maxm,right-left)  

           
        return maxm        

        