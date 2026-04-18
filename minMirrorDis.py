from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        
        mapping = {}
        dis = float('inf')
        
        for i in range(len(nums)):
            if nums[i] in mapping:
                dis = min(dis, abs(i - mapping[nums[i]]))
        
            rev = int(str(nums[i])[::-1])
            mapping[rev] = i
        
        return dis if dis != float('inf') else -1
            