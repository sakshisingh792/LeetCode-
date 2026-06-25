class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        for row in range(1,n):
            for col in range(1,m):
                if matrix[row-1][col-1]!=matrix[row][col]:
                    return False

        return True                       
        