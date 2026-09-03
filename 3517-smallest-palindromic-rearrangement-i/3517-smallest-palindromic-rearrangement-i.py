class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==1:
            return s
        half=n//2
        arrsor=sorted(s[0:half])
        ans=""
        if n%2==0:
            for i in range(len(arrsor)):
                ans+=arrsor[i]
            for i in range(len(arrsor)-1,-1,-1):
                ans+=arrsor[i]
        else:
            for i in range(len(arrsor)):
                ans+=arrsor[i]
            ans+=s[half]
            for i in range(len(arrsor)-1,-1,-1):
                ans+=arrsor[i]

        return ans                
        