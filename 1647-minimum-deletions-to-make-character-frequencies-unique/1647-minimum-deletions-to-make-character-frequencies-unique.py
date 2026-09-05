class Solution:
    def minDeletions(self, s: str) -> int:
        ch_arr=[0]*26
        for ch in s:
            ind=ord(ch)-ord("a")
            ch_arr[ind]+=1


        res=0
        seen=set()
        for x in range(len(ch_arr)):
            while ch_arr[x]>0 and ch_arr[x] in seen:
                ch_arr[x]-=1
                res+=1
            seen.add(ch_arr[x])
        return res        


        