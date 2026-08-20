class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def solve(i,j,dp):
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            up=solve(i-1,j,dp)
            left=solve (i,j-1,dp)
            dp[i][j]=left+up  
            return dp[i][j]
        
        dp=[[-1]*m for i in range (n)]
        return solve(n-1,m-1,dp)      