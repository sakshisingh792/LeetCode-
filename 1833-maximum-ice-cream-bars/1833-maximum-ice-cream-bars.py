class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        
        n=len(costs)
        summ=0
        for i in range(n):
            summ+=costs[i]
            if summ>coins:
                break
            count+=1 
        return count          

        