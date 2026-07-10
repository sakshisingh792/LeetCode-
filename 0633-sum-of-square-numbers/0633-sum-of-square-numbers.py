class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left=0
        right=int(c**0.5)
        while left<=right:
            sqr=left**2+right**2
            if sqr==c:
                return True
            elif sqr>c:
                right-=1
            else:
                left+=1
        return False                
        