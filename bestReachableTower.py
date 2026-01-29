from typing import List

class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        
        best_tower = []
        for i in towers:
            distance = abs(i[0] - center[0]) + abs(i[1] - center[1])

            if distance <= radius:
                if best_tower and i[2]>=best_tower[2]:
                    if i[2]==best_tower[2]:
                        if i[0] < best_tower[0] or i[0] == best_tower[0] and i[1] < best_tower[1]:
                            best_tower = i
                    else:
                        best_tower = i  
                else:
                    if not best_tower:
                        best_tower = i
        
        if not best_tower:
            return [-1,-1]

        return best_tower[0:2]
