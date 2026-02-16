from collections import deque, defaultdict
from sortedcontainers import SortedList
from typing import List

class Node:
    def __init__(self, source, destination, timestamp):
        self.source = source
        self.destination = destination
        self.timestamp = timestamp

class Router:
    def __init__(self, memoryLimit: int):
        self.capacity = memoryLimit
        self.items = deque()
        self.packet_set = set()
        self.dest_index = defaultdict(SortedList)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet_key = (source, destination, timestamp)
        
        if packet_key in self.packet_set:
            return False
        
        while len(self.items) >= self.capacity:
            removed = self.items.popleft()
            self.packet_set.discard((removed.source, removed.destination, removed.timestamp))
            self.dest_index[removed.destination].remove(removed.timestamp)
        
        node = Node(source, destination, timestamp)
        self.items.append(node)
        self.packet_set.add(packet_key)
        self.dest_index[destination].add(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.items:
            return []
        
        item = self.items.popleft()
        self.packet_set.discard((item.source, item.destination, item.timestamp))
        self.dest_index[item.destination].remove(item.timestamp) 
        return [item.source, item.destination, item.timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_index:
            return 0
        
        timestamps = self.dest_index[destination]
        left_idx = timestamps.bisect_left(startTime)
        right_idx = timestamps.bisect_right(endTime)
        return right_idx - left_idx
        
