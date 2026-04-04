class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lis_mag=[0]*26
       
        for i in range(len(magazine)):
            ascii_val=ord(magazine[i])
            index=ascii_val-97
            lis_mag[index]+=1

            

        for i in range(len(ransomNote)):
            ascii_val=ord(ransomNote[i])
            index=ascii_val-97
            lis_mag[index]-=1    
             

        for num in lis_mag:
            if num<0:
                return False

        return True              
            
        