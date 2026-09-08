class Solution:
    def countCommas(self, n: int) -> int:
        count=0
        for i in range(1,n+1):
            arr=[]
            num=i
            while num>0:
                lstdig=i%10
                arr.append(lstdig)
                num=num//10
            digits=len(arr)    
            if digits>=3:
                count+=  (digits-1)//3
        return count        
