class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq={}
        for i in range(len(s)):
            
            freq[s[i]]=i
         

        
        ans=[]
        start=0
        end=0
        for i in range(len(s)):
            end=max(end,freq[s[i]])
            if i==end:
                ans.append(end-start+1)
                start=i+1
        return ans                

            
            

