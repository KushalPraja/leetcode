from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.find_val = k
        self.nums = nums
        
    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[len(self.nums) - self.find_val]
        

