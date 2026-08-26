class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        i=0
        j=len(s)-1
        lst=list(s)
        while i<j:
            if lst[i]!=lst[j]:
                if lst[i]<lst[j]:
                    lst[j]=lst[i]
                else:
                    lst[i]=lst[j]
            i+=1
            j-=1        
        return "".join(lst)                
        