class Solution:
    def maxArea(self, nums: List[int]) -> int:
        ans=0
        left=0
        n=len(nums)
        right=n-1
        while left<right:
            height=min(nums[left],nums[right])
            wid=right-left
            ans=max(ans,height*wid)
            if nums[left]<nums[right]:
                left+=1
            else:
                right-=1
        return ans            
        