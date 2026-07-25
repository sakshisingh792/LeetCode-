class Solution:
    def maxProduct(self, n: int) -> int:
        num=[]
        while n>0:
            d=n%10
            num.append(d)
            n=n//10

        num.sort()
        return num[-1]*num[-2]    
        