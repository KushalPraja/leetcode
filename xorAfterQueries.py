from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        
        for query in queries:
            for i in range(query[0], query[1] + 1, query[2]):
                nums[i] = (nums[i] * query[3]) % (10**9 + 7)
        
        result = None

        for i in nums:
            if result == None:
                result = i

            else:
                result = result ^ i

        return result