class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score=0
        n=len(tokens)
        left=0
        right=n-1
        maxmscore=0
        while left<=right:
            if tokens[left]<=power:
                power-=tokens[left]
                score+=1
                left+=1
                maxmscore=max(score,maxmscore)  

            elif score>=1 :
                power+=tokens[right]
                score-=1
                right-=1
            else:
                break    

            
        return maxmscore      


     