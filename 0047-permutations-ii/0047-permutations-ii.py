class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used=[False]*len(nums)
        res=[]
        def per2(path):
            if len(path)==len(nums) and path not in res:
                res.append(path[:])
                return 


            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i]=True
                path.append(nums[i])       
                per2(path)
                path.pop()
                used[i]=False
        per2([])
        return res         

        