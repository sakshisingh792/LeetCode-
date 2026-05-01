class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i=0
        j=2
        n=len(s)
        count=0
        while j<n:
            if s[i] != s[i+1] and s[i] != s[i+2] and s[i+1] != s[i+2]:
                count+=1
            i+=1
            j+=1
        return count        

        