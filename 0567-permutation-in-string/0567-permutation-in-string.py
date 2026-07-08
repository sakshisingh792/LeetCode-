class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_arr=[0]*26
        s2_arr=[0]*26
        for ch in s1:
            idx=ord(ch)-ord("a")
            s1_arr[idx]+=1


        for ch in s2[:len(s1)]:
            idx=ord(ch)-ord('a')
            s2_arr[idx]+=1

        if s1_arr==s2_arr:
            return True
        
        left=0
        for right in range(len(s1),len(s2)):
            idx=ord(s2[right])-ord('a')
            s2_arr[idx]+=1
            s2_arr[ord(s2[left])-ord('a')]-=1
            left+=1

            if s1_arr==s2_arr:
                return True
        return False        

       