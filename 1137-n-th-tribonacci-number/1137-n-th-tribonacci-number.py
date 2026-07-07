class Solution:
    def tribonacci(self, n: int) -> int:
        memo={}
        def dfs(n):
            if n==0:
                return 0
            if n==1:
                return 1
            if n==2:
                return 1


            if n in memo:
                return memo[n]
            res=dfs(n-1)+dfs(n-2)+dfs(n-3)
            memo[n]=res
            return memo[n]
        return dfs(n)    


        