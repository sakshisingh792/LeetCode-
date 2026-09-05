class Solution:
    def minDeletions(self, s: str) -> int:
        ch_arr=[0]*26
        for ch in s:
            ind=ord(ch)-ord("a")
            ch_arr[ind]+=1


        ch_arr.sort()
        n=len(ch_arr)
        res=0
        for i in range(n-2,-1,-1):
            if ch_arr[i]>=ch_arr[i+1]:
                prev=ch_arr[i]
                ch_arr[i]=max(0,ch_arr[i+1]-1)
                res+=prev-ch_arr[i]
        return res        