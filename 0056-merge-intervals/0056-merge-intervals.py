class Solution:
    def merge(self,intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort( key =lambda x: x[0])
        res=[intervals[0]]
        lst_end=res[-1][1]
        for start,end in intervals[1:]:
            if start<=lst_end:
                lst_end=max(end,lst_end)
                res[-1][1]=lst_end
            else:
                lst_end=end
                  
                res.append([start,end])
            
           
        return res

   
      