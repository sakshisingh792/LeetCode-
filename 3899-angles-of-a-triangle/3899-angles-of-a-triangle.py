import math
class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        a,b,c=sides
        if a+b<=c or a+c<=b or b+c<=a:
            return []
        A=math.degrees(math.acos((b*b+c*c-a*a)/(2*b*c)))
        B=math.degrees(math.acos((a*a+c*c-b*b)/(2*a*c)))
        C=math.degrees(math.acos((a*a+b*b-c*c)/(2*a*b)))  

        return sorted([A,B,C])  
        