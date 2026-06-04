class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans=[]
        index_key=[]
        for i in range(len(nums)):
            if nums[i]==key:
                index_key.append(i)


        for i in range(len(nums)):
            for j in range(len(index_key)):
                if abs(i-index_key[j])<=k:
                    ans.append(i)
                    break
        return ans                                
        