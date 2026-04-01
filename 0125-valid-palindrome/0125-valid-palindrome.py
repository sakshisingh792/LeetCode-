class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr=[]
        for ch in s:
            ch2=ch.lower()
            if "a"<=ch2<="z" or ch2.isdigit() :
                arr.append(ch2)
        return "".join(arr)=="".join(arr)[::-1]


        