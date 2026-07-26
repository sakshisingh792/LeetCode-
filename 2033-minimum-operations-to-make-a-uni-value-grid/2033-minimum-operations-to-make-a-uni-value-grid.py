class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                arr.append(grid[i][j])



        arr.sort()

        rem=arr[0]%x
        for i in range(len(arr)):
            if arr[i]%x!=rem:
                return -1
        mediun=arr[len(arr)//2]
        operations=0
        for i in range(len(arr)):
            operations+=abs(arr[i]-mediun)//x    


        return operations      
        