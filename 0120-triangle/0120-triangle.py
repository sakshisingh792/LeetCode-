class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #Tabulation  TC-O(N*N),SC-O(N*N)
        
        n=len(triangle)
        dp=[[0]*n for _ in range(n)]
        for j in range(n):
            dp[n-1][j]=triangle[n-1][j]

        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                down=triangle[i][j]+dp[i+1][j]
                dia=triangle[i][j]+dp[i+1][j+1]
                dp[i][j]=min(down,dia)


        return dp[0][0]        
