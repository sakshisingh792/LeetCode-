class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        ans=[]
        n=len(nums)
        largest=nums[n-1]
        freq=[0]*(largest+1)
        
        for i in range(len(nums)):
            ch=nums[i]
            if  freq[ch]<k:
                ans.append(ch)
                freq[ch]+=1
                
            else:
                continue   

            

        return ans        


        