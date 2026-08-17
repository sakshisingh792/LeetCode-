class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def solve(i,j,nums):
            if i>j:
                return 0

            if i==j:
                return nums[i]


            take_i=nums[i]+min(solve(i+2,j,nums),solve(i+1,j-1,nums))    
            take_j=nums[j]+min(solve(i,j-2,nums),solve(i+1,j-1,nums))


            return max(take_i,take_j)     

        total=sum(nums)
        n=len(nums)
        player1_sc=solve(0,n-1,nums)
        player2_sc=total-player1_sc

        if player1_sc>=player2_sc:
            return True
        else:
            return False    
       