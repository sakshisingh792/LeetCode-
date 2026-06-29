class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def subset(i,path):
            if i==len(nums):
                ans.append(path[:])
                return
            

            path.append(nums[i])
            subset(i+1,path)
            path.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1


            subset(i+1,path)

        subset(0,[])
        return ans        