class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        dp=[[-1]*n for _ in range(n)]

        def ispalindrome(i,j,s):
            if i>j:
                return True

            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==s[j]:
                dp[i][j]= ispalindrome(i+1,j-1,s)
            else:
                dp[i][j]=False     

            return dp[i][j]   

        count=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if ispalindrome(i,j,s):
                    count+=1
        return  count            

        