class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        ans=0
        for i in range(num1,num2+1):
            valley=0
            peak=0
            num=str(i)
            for j in range(1,len(num)-1):
                if int(num[j])>int(num[j-1]) and int(num[j])>int(num[j+1]):
                    peak+=1
                elif int(num[j])<int(num[j-1]) and int(num[j])<int(num[j+1]):
                    valley+=1

            total=peak+valley
            ans+=total
        return ans        
