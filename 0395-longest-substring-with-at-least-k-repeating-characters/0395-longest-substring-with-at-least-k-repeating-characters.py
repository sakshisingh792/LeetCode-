class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        from collections import Counter
        freq=Counter(s)
        if len(s)<k:
            return 0
        for ch in freq:
            if freq[ch]<k:
                parts=s.split(ch)
                ans=0
                for part in parts:
                    ans=max(ans,self.longestSubstring(part,k))

                return ans             
        return len(s)