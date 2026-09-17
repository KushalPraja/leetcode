from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        init = [float('inf')] * len(arr)
        prefix = [arr[0]]
        
        for i in range(1, len(arr)):
            prefix.append(arr[i] + prefix[i - 1])

        temp_set = {0: -1}

        for i in range(len(prefix)):
            diff = prefix[i] - target
            if diff in temp_set:
                init[i] = i - temp_set[diff]
            temp_set[prefix[i]] = i

        min_so_far = float('inf')
        prefix_arr = []
        for i in range(len(prefix)):
            prefix_arr.append(min_so_far)
            min_so_far = min(min_so_far, init[i])


        temp = [float('inf')] * len(prefix)

        for i in range(len(temp)):
            if init[i] != float('inf'):
                start = i - init[i] + 1
                temp[start] = min(temp[start], init[i])

        suffix = [float('inf')] * len(prefix)
        min_so_far = float('inf')
        for i in range(len(suffix) - 1, -1, -1):
            min_so_far = min(min_so_far, temp[i])
            suffix[i] = min_so_far

        min_result = float('inf')
        for i in range(len(prefix_arr)):
            if prefix_arr[i] == float('inf') or suffix[i] == float('inf'):
                continue
            else:
                min_result = min(min_result, prefix_arr[i] + suffix[i])
        
        if min_result == float('inf'):
            return -1
        return  min_result

            
