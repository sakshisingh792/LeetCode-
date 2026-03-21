class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        n=len(strs)
        first=strs[0]
        last=strs[n-1]
        ans=[]
        for i in range(min(len(first),len(last))):
            if first[i]!=last[i]:
                return "".join(ans)
            else:
                ans.append(first[i])
        return "".join(ans) 