class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target={}
        for i in range(len(t)):
            ch=t[i]
            target[ch]=target.get(ch,0)+1

        have=0
        need=len(target)
        ans=[-1,-1]
        ans_len=float("inf")

        freq={}
        l=0
        for r in range(len(s)):
            ch=s[r]
            freq[ch]=freq.get(ch,0)+1
            if  ch in target and freq[ch]==target[ch]:
                have+=1    

                while have==need:
                    if r-l+1<ans_len:
                        ans=[l,r]
                        ans_len=r-l+1

                    freq[s[l]]-=1
                    if s[l] in target and target[s[l]]>freq[s[l]]:
                        have-=1

                    l+=1
        l,r=ans
        return s[l:r+1] if  ans_len!=float("inf") else   ""       



        