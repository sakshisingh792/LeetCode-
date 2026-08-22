class Solution:
    def minCost(self, colors: str, time: List[int]) -> int:
        cost=0
        col=list(colors)
        for i in range(1,len(col)):
            if col[i]==col[i-1]:
                cost+=min(time[i],time[i-1])

                time[i]=max(time[i],time[i-1])
        return cost        

