class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n=len(grid)
        m=len(grid[0])

        arr=[]
        for row in grid:
            arr.extend(row)


        total=len(arr)
        k=k %total

        arr=arr[-k:]+arr[:-k]  

        idx=0
        ans=[[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                ans[i][j]=arr[idx]
                idx+=1


        return ans         
        