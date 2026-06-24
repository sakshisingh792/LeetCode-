class Solution:
    def hIndex(self, nums: List[int]) -> int:
   
        nums.sort()
        n = len(nums)

        for i in range(n):
            h = n - i

            if nums[i] >= h:
                return h

        return 0        
             
              

        