class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        diff_x=abs(z-x)
        diff_y=abs(z-y)
        if diff_x<diff_y:
            return 1
        elif diff_y<diff_x:
            return 2
        else:
            return 0       
        