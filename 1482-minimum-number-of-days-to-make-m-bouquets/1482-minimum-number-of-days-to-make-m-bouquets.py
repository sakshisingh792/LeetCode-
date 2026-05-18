class Solution:
    def minDays(self, bloomDay, m, k):

        n = len(bloomDay)

        if m * k > n:
            return -1

        left=min(bloomDay) 
        right=max(bloomDay)
        while left<right:
            mid=(left+right)//2
            count=0
            bouquet=0
            for bloom in bloomDay:
                if bloom<=mid:
                    count+=1
                else:
                    bouquet+=count//k
                    count=0
            bouquet+=count//k
            
            if bouquet>=m:
                right=mid
            else:
                left=mid+1
        return left                       