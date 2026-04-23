from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        mapping = {}
        res = [0] * len(nums)

        # build index groups (same as yours)
        for i in range(len(nums)):
            if nums[i] not in mapping:
                mapping[nums[i]] = []
            mapping[nums[i]].append(i)

        # process each group
        for val in mapping:
            arr = mapping[val]
            n = len(arr)

            prefix = [0] * n
            prefix[0] = arr[0]

            for i in range(1, n):
                prefix[i] = prefix[i - 1] + arr[i]

            for i in range(n):
                idx = arr[i]

                left_count = i
                right_count = n - i - 1

                left_sum = prefix[i - 1] if i > 0 else 0
                right_sum = prefix[n - 1] - prefix[i]

                left_cost = idx * left_count - left_sum
                right_cost = right_sum - idx * right_count

                res[idx] = left_cost + right_cost

        return res

