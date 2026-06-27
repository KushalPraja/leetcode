class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        
        mapping = {}

        for i in range(len(nums)):
            if nums[i] not in mapping:
                mapping[nums[i]] = 0
            
            mapping[nums[i]] += 1


        max_size = 0
       
        if 1 in mapping and mapping[1] > 0:
            if mapping[1] % 2 == 0 : 
                max_size = max(max_size, mapping[1] - 1)
            else:
                max_size = max(max_size, mapping[1])

        for i in list(set(nums)):


            if i == 1:
                continue
            
            curr = 1
            size = 0

            while i ** curr in mapping and mapping[i**curr] >= 2 and i ** (curr * 2) in mapping:
                curr *= 2
                size += 2

            if i ** curr in mapping and mapping[i**curr] > 0:
                size += 1

            print(i, size)
            max_size = max(max_size, size)

        return max_size

        
