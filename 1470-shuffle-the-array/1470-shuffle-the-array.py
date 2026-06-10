class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        m=len(nums)
        ans=[0]*m
        pos1=0
        pos2=1
        for i in range(n):
            ans[pos1]=nums[i]
            ans[pos2]=nums[i+n]
            pos1+=2
            pos2+=2
        return ans    
        