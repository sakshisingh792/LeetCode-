class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        #Memoization
        n=len(matrix)
        dp=[[0]*n for _ in range(n)]

    
        for j in range(n):
            dp[n-1][j]=matrix[n-1][j]

        
        
        for i in range(n-2,-1,-1):
            for j in range(n):

                down=dp[i+1][j]
                if j>0:
                    leftdia=dp[i+1][j-1]
                else:
                    leftdia=float("inf")    

                if j==n-1:
                    rightdia=float("inf")
                else:
                    rightdia=dp[i+1][j+1]        

                dp[i][j]=matrix[i][j]+min(leftdia,rightdia,down)
        return min(dp[0])        



        
            


        