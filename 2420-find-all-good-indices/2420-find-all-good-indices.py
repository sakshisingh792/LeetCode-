class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        n=len(nums)
        dec=[1]*n
        inc=[1]*n
        for i in range(1,n):
            if nums[i-1]>=nums[i]:
                dec[i]=dec[i-1]+1


        for i in range(n-2,-1,-1):
            if nums[i+1]>=nums[i]:
                inc[i]=inc[i+1]+1


        for i in range(k,n-k):
            if dec[i-1]>=k and inc[i+1]>=k:
                ans.append(i)
        return ans                        
