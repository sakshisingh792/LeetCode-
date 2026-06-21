class Solution:
    def maxDistance(self, nums: str) -> int:
        cor=[0,0]
        wild=0
        for i in range(len(nums)):
            if nums[i]=="L":
                cor[0]-=1
            elif nums[i]=="R":
                cor[0]+=1
            elif nums[i]=="U":
                cor[1]+=1
            elif nums[i]=="D":
                cor[1]-=1
            else:
                wild+=1
        return  abs(cor[0])+abs(cor[1])+wild
                     
