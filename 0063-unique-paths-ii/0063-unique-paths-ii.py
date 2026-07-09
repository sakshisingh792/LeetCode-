class Solution:
    def uniquePathsWithObstacles(self, Grid: List[List[int]]) -> int:
        if Grid[0][0]==1:
            return 0

        m=len(Grid)
        n=len(Grid[0])
        dp=[0]*n
        dp[0]=1
        for i in range(m):
            for j in range(n):
                if Grid[i][j]==1:
                    dp[j]=0
                elif j>0:
                    dp[j]=dp[j]+dp[j-1]

        return dp[n-1]                 

        