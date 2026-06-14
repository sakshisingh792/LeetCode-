class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        ana_window=Counter(p)
        window=Counter()
        ans=[]
        k=len(p)

        for right in range(len(s)):
            window[s[right]]+=1

            if right>=k:
                left=s[right-k]
                window[left]-=1

                if window[left]==0:
                    del window[left]


            if window==ana_window:
                ans.append(right-k+1)  
        return ans              