class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lis_mag=[0]*27
        lis_ran=[0]*27
        for ch in ransomNote:
            ascii_val=ord(ch)
            index=ascii_val-97
            lis_ran[index]+=1

        for ch in magazine:
            ascii_val=ord(ch)
            index=ascii_val-97
            lis_mag[index]+=1    

        for i in range(len(lis_ran)):
            if lis_ran[i]>lis_mag[i]:
                return False   
        return True        
            
        