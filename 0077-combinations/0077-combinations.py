class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def combina(i,path):
            if len(path)==k:
                ans.append(path[:])
                return
            for j in range(i,n+1):  
               
                    path.append(j)
                    combina(j+1,path)
                    path.pop()

                 

        combina(1,[])    
        return ans
        