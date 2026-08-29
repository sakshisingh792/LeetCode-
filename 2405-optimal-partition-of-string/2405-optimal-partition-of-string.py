class Solution:
    def partitionString(self, s: str) -> int:
        ans=1
        freq={}
        for i in range(len(s)):
            ch=s[i]
            if s[i] in freq:
                ans+=1
                freq={}
            freq[ch]=freq.get(ch,0)+1
        return ans        