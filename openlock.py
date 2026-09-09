class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        mapping = {}
        
        if "0000" in deadends:
            return -1

        if target in deadends:
            return -1 

        mapping["0000"] = 0
        queue = deque(["0000"])

        deadends = set(deadends)
        visited = set()
        cnt = 0
        while queue:
            curr = queue.popleft()
            count = mapping[curr]
            old = curr

            if curr == target:
                return count

            for i in range(len(curr)):
                curr = list(curr)
                temp = int(curr[i])
                plus_one = (temp + 1) % 10
                minus_one = (temp - 1) % 10
                curr[i] = str(plus_one)
                curr = "".join(curr)

                if curr not in visited and curr not in deadends:
                    visited.add(curr)
                    queue.append(curr)
                    mapping[curr] = count + 1

                curr = list(curr)
                curr[i] = str(minus_one)
                curr = "".join(curr)

                if curr not in visited and curr not in deadends:
                    visited.add(curr)
                    queue.append(curr)
                    mapping[curr] = count + 1
                curr = list(curr)
                curr[i] = str(temp)

        return -1
