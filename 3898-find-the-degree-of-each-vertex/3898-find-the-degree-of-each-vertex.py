class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n=len(matrix)
        m=len(matrix[0])
        ans=[]
        for i in range(n):
            ver=0
            for j in range(m):
                if matrix[i][j]==1:
                    ver+=1
            ans.append(ver)  
        return ans          

        