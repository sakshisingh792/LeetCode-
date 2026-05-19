class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left=1
        right=max(nums)
        while left<right:
            mid=(left+right)//2
            summ=0
            for num in nums:
                summ+=ceil(num/mid)

            if summ<=threshold:
                right=mid
            else:
                left=mid+1
        return left            

