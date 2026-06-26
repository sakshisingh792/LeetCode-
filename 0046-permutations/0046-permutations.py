class Solution:
        def permute(self, nums: List[int]) -> List[List[int]]:
            n=len(nums)
            used=[False]*n
            res=[]

            def backtrack(path):
                if len(path)==len(nums):
                    res.append(path[:])
                    return 


                for i in range(n):
                    if used[i]:
                        continue

                    used[i]=True
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    used[i]=False    
            backtrack([])
            return res            