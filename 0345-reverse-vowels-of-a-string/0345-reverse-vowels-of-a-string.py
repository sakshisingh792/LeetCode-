class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=set("aeiouAEIOU")
        i=0
        s=list(s)
        j=len(s)-1
        while i<j:
            if s[i] in vowels and s[j] in vowels:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1

            if s[i] not in vowels:
                i+=1
            if s[j] not in vowels:
                j-=1

        return "".join(s)
        