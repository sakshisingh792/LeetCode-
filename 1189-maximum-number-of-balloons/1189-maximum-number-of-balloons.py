class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq={}
        n=len(text)
        for i in range(n):
            ch=text[i]
            freq[ch]=freq.get(ch,0)+1
        return  min(
            freq.get("b",0),
            freq.get("a",0),
            freq.get("l",0)//2,
            freq.get("o",0)//2,
            freq.get("n",0)
        ) 
         
            

        