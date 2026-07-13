from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        

        def generate(digits):
            curr = deque([])
            for i in range(digits):
                curr.append(i + 1)
            return curr



        result = []
        
        curr = deque([0])
        
        value = 0
        length = 1

        while (True):

            if value > high:
                break

            if value >= low:
                result.append(value)

            right = curr[-1] + 1
            left = curr.popleft()

            if right >= 10:
                curr = generate(length + 1)
                length += 1

            else:
                curr.append(right)

            value = int("".join(str(num) for num in curr))

           
        return result

