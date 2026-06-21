class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        ans=0
        for i in range(len(nums)):
            summ=0
            for j in range(i,len(nums)):
                summ+=nums[j]
                if int(str(summ)[0])==x and int(str(summ)[-1])==x:
                    ans+=1
                
        return ans            
        
        