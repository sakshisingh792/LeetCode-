class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        m=len(nums)
        nums=set(nums)
        for i in range(1,m+1):
            if i in nums:
                nums.remove(i)
            else:
                nums.add(i)    
        return list(nums)       

        