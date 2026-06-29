class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        def backtrack(start,path,n):
            if len(path)==k:
                if n==0:
                    ans.append(path[:])
                    return


            for i in range(start,10):
                if n>=i:
                    path.append(i)
                    backtrack(i+1,path,n-i)
                    path.pop()

                

        backtrack(1,[],n)   
        return ans         


        