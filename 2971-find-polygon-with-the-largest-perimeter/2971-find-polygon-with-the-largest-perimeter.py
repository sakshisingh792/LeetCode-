class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        total=sum(nums)
        nums.sort()
        while len(nums)>=3:
            largest=nums[-1]
            if total-largest>largest:
                return total
            total-=nums.pop()   
        return -1     
        