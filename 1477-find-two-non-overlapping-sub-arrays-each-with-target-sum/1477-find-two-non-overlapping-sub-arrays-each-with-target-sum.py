class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n=len(arr)
        left=0

        best = [float('inf')] * n
        ans = float('inf')
        min_length = float('inf')
        currsum=0
        for right in range(n):
            currsum+=arr[right]
            while currsum>target:
                currsum-=arr[left]
                left+=1

            if currsum==target:
                length=right-left+1
                if(left>0 and best[left-1]!=float("inf")):
                    ans=min(ans,length+best[left-1])

                min_length=min(min_length,length)
            best[right]=min_length
        return -1 if ans==float("inf") else ans                

       