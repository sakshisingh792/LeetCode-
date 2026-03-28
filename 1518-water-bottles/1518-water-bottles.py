class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        full = numBottles
        empty = 0
        drunk = 0

        while full > 0:
            drunk += full
            empty += full

            # exchange empty bottles
            full = empty // numExchange
            empty = empty % numExchange

        return drunk