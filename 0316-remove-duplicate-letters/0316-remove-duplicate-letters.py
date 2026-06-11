class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last=[0]*26
        for i in range(len(s)):
            ch=s[i]
            index=ord(ch)-ord("a")
            last[index]=i

        taken=[False]*26
        res=""
        for i in range(len(s)):
            ch=s[i]
            index=ord(ch)-ord("a")

            if taken[index]:
                continue

            while res and res[-1]>ch and last[ord(res[-1])-ord("a")]  >i:
                taken[ord(res[-1])-ord("a")]=False
                res=res[:-1]

            res+=ch
            taken[ord(ch)-ord("a")]=True 
        return res             