class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans=0
        n=len(nums)
        for i in range(len(nums)):
            count=0
            for j in range(i,n)  :
                if nums[j]==target:
                    count+=1
                else:
                    count-=1

                if count>0:
                    ans+=1
        return ans                             