class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                continue

            parts=(nums[i]+nums[i+1]-1)//nums[i+1]
            

            ans+=parts-1
            nums[i]=nums[i]//parts

        return ans            
                