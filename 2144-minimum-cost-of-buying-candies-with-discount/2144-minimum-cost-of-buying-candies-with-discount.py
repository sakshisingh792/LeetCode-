class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        total=0
        k=0
        for i in range(len(cost)):
            
            if k<2:
                total+=cost[i]  
                k+=1 
            else:
                k=0
                continue
        return total                
        