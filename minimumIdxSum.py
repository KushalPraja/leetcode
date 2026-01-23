class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        mapping = {}
        for i in range(len(list1)):
            val = list1[i]
            if (val in list2):
                mapping[val] = i + list2.index(val)
                
        results = [(i,j) for i,j in sorted(mapping.items(), key = lambda item: item[1])]
        min_val = results[0][1]
        return [i for i,j in results if j==min_val ]

result = Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"])

print(result)
