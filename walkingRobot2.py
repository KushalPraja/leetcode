from typing import List

class Robot:

    def __init__(self, width: int, height: int):
        self.pos = 0
        self.height = height - 1
        self.width = width - 1
        self.south = False

    def step(self, num: int) -> None:
        self.pos = (self.pos + num) % (self.width * 2 + self.height * 2)
        self.south = (self.pos == 0 and num > 0)
        
    def getPos(self) -> List[int]:
        if self.pos >= self.width + self.height + self.width:
            temp = self.pos - self.width - self.height - self.width
            return [0, self.height - temp]
        
        elif self.pos >= self.width + self.height:
            temp = self.pos - self.width - self.height
            return [self.width - temp, self.height]
        
        elif self.pos >= self.width:
            temp = self.pos - self.width
            return [self.width, temp]
        
        else:
            return [self.pos, 0]

    def getDir(self) -> str:
        if self.pos > self.height + self.width + self.width or self.south:
            return "South"
        if self.pos > self.width + self.height:
            return "West"
        if self.pos > self.width:
            return "North"
        return "East"
