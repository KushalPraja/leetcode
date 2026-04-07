from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        obstacles = set(tuple((x, y)) for [x,y] in obstacles)
        furthest = 0
        x = 0
        y = 0 

        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        curr = 0

        for command in commands:
            if command == -1:
                curr = (curr + 1) % 4
            
            elif command == -2:
                curr = (curr - 1) % 4
            else:
                curr_x, curr_y = direction[curr]
                i = 0
               
                while i < command:            
                    if (x + curr_x, y + curr_y) in obstacles:
                        break
                        
                    x += curr_x
                    y += curr_y
                    i += 1

                furthest = max(furthest, x**2 + y**2)
        return furthest