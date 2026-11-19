class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            new_s=""
            n=len(s)
            for i in range(0,n,k):
                group=s[i:i+k]
                digitsum=0
                for num in group:
                    digitsum+=int(num)
                new_s+=str(digitsum)
            s=new_s
        return s            
            


        