class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        flowers=list(zip(plantTime,growTime))
        flowers.sort(key=lambda x : x[1],reverse=True)
        ans=0
        plant=0
        for p,g in flowers:
            plant+=p
            ans=max(ans,plant+g)
        return ans    
        