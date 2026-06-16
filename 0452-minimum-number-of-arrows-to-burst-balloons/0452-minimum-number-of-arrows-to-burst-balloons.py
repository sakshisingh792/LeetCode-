class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x : x[1])
        arrow=1
        arr_pos=points[0][1]
        for start ,end in points[1:]:
            if start>arr_pos:
                arrow+=1
                arr_pos=end
        return arrow        


        