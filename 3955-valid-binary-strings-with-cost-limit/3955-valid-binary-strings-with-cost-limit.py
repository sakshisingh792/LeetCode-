class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        ans=[]
        def backtrack(i,path,cost):
            if cost>k:
                return

            if i==n:
                ans.append(path)
                return 
            

            backtrack(i+1,path+"0",cost)

            if not path or path[-1]!="1":
                backtrack(i+1,path+"1",cost+i)
        backtrack(0,"",0)
        return ans