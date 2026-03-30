class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total=0
        empty=0
        full=numBottles
        while full>0:
            total+=full
            empty+=full
            full=0
            if empty>=numExchange:
                empty-=numExchange
                full=1
                numExchange+=1
        return total        

        