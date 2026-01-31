import math
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = {}

        for i in points:
            if not self.calculate_euq(i[0],i[1]) in distances:
                distances[self.calculate_euq(i[0],i[1])] = []
            distances[self.calculate_euq(i[0],i[1])].append(i)
        
        distances_array = [values for keys, values in sorted(distances.items(), key= lambda x: x[0])]
        final_array = []
        for i in distances_array:
            for j in i:
                final_array.append(j)

        return final_array[0:k]
        

    def calculate_euq(self, x1, y1, x2 = 0 , y2 = 0):
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
