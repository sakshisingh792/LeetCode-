class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq={}
        ans=1
        for num in nums:
            freq[num]=freq.get(num,0)+1


        if 1 in freq:
            if freq[1]%2==0 :
                ans=max(ans,freq[1]-1)
            else:
                ans=max(ans,freq[1])  


        for x in freq:
            if x==1:
                continue


            curr=x
            length=0
            while curr in freq:
                if freq[curr]>=2:
                    length+=2
                    curr=curr*curr


                else:
                    length+=1
                    break

            if curr not in freq:
                length-=1
            ans=max(ans,length)
        return ans                    
            


        