def twoSum(nums: list[int], target: int) -> list[int]:
    mappings = {}

    for i in range(len(nums)):
        val = nums[i];
        difference = target - val;
        if difference in mappings:
            return [mappings[difference], i]
        mappings[val] = i;
       
    return []

if __name__ == "__main__":
    print(twoSum([1,2,3,4,5], 6))
