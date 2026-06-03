class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        res=[]
        def com(i,ds,rem):

            if i==len(arr):
                if rem==0:
                    res.append(ds[:])
                
                return    


            if arr[i]<=rem:
                ds.append(arr[i])
                
                com(i,ds,rem-arr[i])
                ds.pop()

            
            
            com(i+1,ds,rem)
        com(0,[],target)    
        return res

