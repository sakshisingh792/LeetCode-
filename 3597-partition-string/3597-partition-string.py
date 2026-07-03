class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen=set()
        ans=[]
        i=0
        curr=""
        for i in range(len(s)):
            curr+=s[i]
            if curr not in seen:
                seen.add(curr)
                ans.append(curr)
                curr=""
        return ans        

                



        