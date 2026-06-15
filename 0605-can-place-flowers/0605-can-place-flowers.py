class Solution:
    def canPlaceFlowers(self, nums: List[int], n: int) -> bool:

        if n == 0:
            return True

        for i in range(len(nums)):
            if nums[i]==0:
                left=(i==0 or nums[i-1]==0)
                right=(i==len(nums)-1 or nums[i+1]==0)

                if left and right:
                    n-=1
                    nums[i]=1

                    if n==0:
                        return True
        return False                

                        

        