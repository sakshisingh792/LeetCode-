class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]]=t[i]
            else:
                if dict1[s[i]]!=t[i]:
                    return False

            if t[i] in dict2:
                if dict2[t[i]]!=s[i]:
                    return False
            else:
                dict2[t[i]]=s[i]                

        return True            

        