class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        freq={}
        n=len(s)
        maxm=0
        for i in range(n):
            ch=s[i]
            freq[ch]=freq.get(ch,0)+1
            
        grp=defaultdict(list)
        for ch,cnt in freq.items():
            if cnt not in grp:
                grp[cnt]=[]
            grp[cnt].append(ch)


        bst_fre=0
        bst_len=0
        for k in grp:
            if  len(grp[k])>bst_len or(len(grp[k])==bst_len and k>bst_fre):
                bst_len=len(grp[k])
                bst_fre=k


        return "".join(grp[bst_fre])             

       



        