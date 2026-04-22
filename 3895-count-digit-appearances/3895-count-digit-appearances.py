class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        n=len(nums)
        count=0
        for i in range(n):
            while nums[i]>0:
                lst=nums[i]%10
                if lst==digit:
                    count+=1
                nums[i]=nums[i]//10
        return count             
            
        