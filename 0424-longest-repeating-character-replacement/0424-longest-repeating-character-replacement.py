class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        left=0
        max_fre=0
        maxm=0
        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0)+1
            max_fre=max(max_fre,count[s[right]])
           
            while  (right-left+1)-max_fre>k:
                count[s[left]]-=1
                left+=1
            maxm=max(maxm,right-left+1) 
        return maxm       

            