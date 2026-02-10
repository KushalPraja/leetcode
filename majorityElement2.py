class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        min_element = len(nums) // 3
        mapping = {}

        for i in nums:
            if i not in mapping:
                mapping[i] = 0

            mapping[i] += 1

        return [i for i,j in mapping.items() if j > min_element]