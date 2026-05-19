class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        n=len(weights)


        while left<=right:
            mid=(left+right)//2
            days_needed=1
            curr_weight=0
            for w in weights:
                if w+curr_weight>mid:
                    days_needed+=1
                    curr_weight=w
                else:
                    curr_weight+=w
            if days_needed<=days:
                right=mid-1
            else:
                left=mid+1
        return left                        
