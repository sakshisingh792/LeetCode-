class Solution:
    def partitionString(self, s: str) -> int:
        ans=1
        seen=set()
        for i in range(len(s)):
            ch=s[i]
            if s[i] in seen:
                ans+=1
                seen=set()
            seen.add(ch)
        return ans        