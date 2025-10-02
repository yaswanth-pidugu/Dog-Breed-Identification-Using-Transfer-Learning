class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            numBottles -= numExchange
            numExchange+=1
            numBottles+=1
            res+=1
        return res