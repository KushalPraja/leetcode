class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        bottlesDrunk = 0
        emptyBottles = 0

        while numBottles > 0 or emptyBottles > numExchange:
            bottlesDrunk += numBottles
            emptyBottles += numBottles
            numBottles = 0
            while emptyBottles >= numExchange:
                emptyBottles -= numExchange
                numBottles += 1
                numExchange += 1

        return bottlesDrunk