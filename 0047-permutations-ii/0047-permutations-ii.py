class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used=[False]*len(nums)
        res=[]
        nums.sort()
        def per2(path):
            if len(path)==len(nums) :
                res.append(path[:])
                return 


            for i in range(len(nums)):
                if used[i]:
                    continue

                # Skip duplicates
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue    

                used[i]=True
                path.append(nums[i])       
                per2(path)
                path.pop()
                used[i]=False
        per2([])
        return res         

        