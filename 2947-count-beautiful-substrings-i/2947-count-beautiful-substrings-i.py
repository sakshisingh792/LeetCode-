class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n=len(s)
        vowel=["a","e","i","o","u"]
        vow=0
        cons=0
        sub=0
        for i in range(n):
            vow=0
            cons=0
            for j in range(i,n):
                if s[j] in vowel:
                    vow+=1
                else:
                    cons+=1


                if vow==cons and (vow*cons)%k==0:
                    sub+=1

        return sub            

