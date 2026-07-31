class Solution:
    def heightChecker(self, nums: List[int]) -> int:
        expected=sorted(nums)
        ans=0
        for i in range(len(nums)):
            if nums[i]!= expected[i]:
                ans+=1
        return ans        

        