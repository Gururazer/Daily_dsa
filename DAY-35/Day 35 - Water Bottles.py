class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        sum = numBottles
        while(numBottles >= numExchange):
            sum += numBottles // numExchange
            numBottles = (numBottles // numExchange) + (numBottles - ((numBottles // numExchange)*numExchange))
        return sum
    
