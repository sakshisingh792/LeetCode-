class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans=[]
        left=0
        right=0
        while left<=right and right<len(nums):
            while right+1<len(nums) and nums[right+1]==nums[right]+1:
                right+=1
            if left!=right:
                strn=str(nums[left])+"->"+str(nums[right])
                ans.append(strn)
            else:
                strn=str(nums[left])
                ans.append(strn)   
            right+=1
            left=right    
        return ans     
                    


            