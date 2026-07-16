class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        import math
        ans=[]
        maxm=0
        for i in range(len(nums)):
            maxm=max(nums[i],maxm)
            res=math.gcd(maxm,nums[i])
            ans.append(res)


        ans.sort()
        left=0
        right=len(ans)-1

        sum=0
        while left<right:
            gd=math.gcd(ans[left],ans[right])
            sum+=gd
            left+=1
            right-=1

        return sum        
        