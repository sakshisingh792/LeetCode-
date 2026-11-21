class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        dp=[[0]*m for _ in range(n)]
        for i in range(m):
            dp[0][i]=matrix[0][i]


        for i in range(1,n):
            for j in range(m):
                up=dp[i-1][j]
                left=float("inf")
                right=float("inf")
                if j>0:
                    left=dp[i-1][j-1]

                if j<n-1:
                    right=dp[i-1][j+1]

                dp[i][j]=matrix[i][j]+min(up,right,left)

        return min(dp[n-1])                    
        