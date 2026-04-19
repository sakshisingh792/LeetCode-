class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev=0
        num=n
        while num>0:
            lst=num%10
            rev=rev*10+lst
            num=num//10

        return abs(n-rev)    
        