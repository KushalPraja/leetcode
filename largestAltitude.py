from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        start = 0
        max_altitude = 0

        for i in range(len(gain)):
            start += gain[i]
            max_altitude = max(start, max_altitude)

        return max_altitude