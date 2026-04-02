class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        ans=""
        while i<len(s) and j<len(t):
            if s[i]!=t[j]:
                j+=1
            else:
                ans+=s[i]

                i+=1
                j+=1
        return ans==s
        
        