class Solution:
    def processStr(self, s: str, k: int) -> str:
        new_len=0
        n=len(s)
        for i in range(len(s)):
            if "a"<=s[i]<="z":
                new_len+=1

            if s[i]=="#":
                new_len*=2

            if s[i]=="*":
                if new_len>0:
                  new_len-=1


        if k>=new_len:
            return "."          

       

        for i in range(n-1,-1,-1):
            if s[i]=="#":
                new=new_len//2
                if k>=new:
                    k=k-new
                new_len=new


            if "a"<=s[i]<="z":
                new_len-=1


            if s[i]=="%":
                k=new_len-k-1

            if s[i]=="*":
                new_len+=1   
            if k==new_len:
                return s[i]                 
