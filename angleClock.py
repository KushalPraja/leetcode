class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        x = (minutes * 6)- (((hour % 12) * 5 + 5 * (minutes/60)) * 6)
        return min( abs(x), 360 - abs(x))