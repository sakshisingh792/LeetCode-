class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        need=[]
        for i in range(len(capacity)):
            need.append(capacity[i]-rocks[i])

        need.sort()
        ans=0

        for x in need:
            if x<=additionalRocks:
                ans+=1
                additionalRocks-=x
            else:
                break
        return ans                
       