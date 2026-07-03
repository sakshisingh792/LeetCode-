class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total=sum(arr)
        if total%3!=0:
            return False
        
        target=total//3
        curr=0
        count=0

        for i in range(len(arr)):
            curr+=arr[i]
            if curr==target:
                count+=1
                curr=0

                if count==2 and i< len(arr)-1:
                    return True

        return False               

       