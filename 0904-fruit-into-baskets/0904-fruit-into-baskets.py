class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq={}
        left=0
        ans=0
        n=len(fruits)
        for right in range(n):
            freq[fruits[right]]=freq.get(fruits[right],0)+1
            
            
            
            while len(freq)>2:
                freq[fruits[left]]-=1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                left+=1

            ans=max(right-left+1,ans)   
        return ans     


        