class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        list = []
        for i in nums:
            if i in list:
                return True # contains duplicate
            list.append(i);
        return False

if __name__ == "__main__":
    print(Solution().hasDuplicate([1, 2, 3, 3]))
