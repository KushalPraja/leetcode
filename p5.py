class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        mapping = {}

        for i in range(len(nums)):
            val = nums[i]
            if val in mapping:
                mapping[val]+=1;
            else:
                mapping[val]=1;
        
        print(mapping)

        vals = {k:v for k,v in sorted(mapping.items(), key=lambda item:item[1], reverse= True)}
        return list(vals)[0:k]


print(Solution().topKFrequent([1,2,2,3,3,3], 2))
        
        
