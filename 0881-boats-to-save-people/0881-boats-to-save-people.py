class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        
        boats=0
        while left<=right:
            if nums[left]+nums[right]<=limit:
                boats+=1
                left+=1
                right-=1
            else:
                boats+=1
                right-=1

          

        return boats             
                

        