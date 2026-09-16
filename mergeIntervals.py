

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda i:i[0])
        temp = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            curr, end = intervals[i]

            if curr > temp[-1]:
                res.append(temp)
                temp = [curr, end]
                continue
                
            if curr <= temp[-1]:
                temp[0] = min(temp[0], curr)
                temp[1] = max(temp[1], end)

        if temp:
            res.append(temp)
        return res


           
