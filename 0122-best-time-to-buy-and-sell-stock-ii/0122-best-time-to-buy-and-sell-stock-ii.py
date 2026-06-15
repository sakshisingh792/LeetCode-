class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        min_price=float("inf")
        for i in range(len(prices)):
            min_price=min(prices[i],min_price)
            if prices[i]>min_price:
                profit+=prices[i]-min_price
                min_price=prices[i]

        return profit        

        