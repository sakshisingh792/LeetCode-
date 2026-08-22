class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        arr=list(palindrome)
        
        n=len(arr)
        if n==1:
            return ""
        for i in range(len(palindrome)//2):
            if arr[i]>"a":
                arr[i]="a"
                
                return "".join(arr)

                
        arr[-1]="b"

        return "".join(arr)                

