class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=intervals[0]
        ans=[]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=res[1]:
                res[1]=max(intervals[i][1],res[1])
            else:
                ans.append(res)
                res=intervals[i]
        ans.append(res)
        return ans        




        