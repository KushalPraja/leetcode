from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        tasks.sort(key = lambda i: i[1] - i[0], reverse = True)


        start = tasks[0][1]
        starting_balance = tasks[0][1]
        loan = 0

        for i in tasks:
            actual, required = i

            if starting_balance < required:
                loan += required - starting_balance
                starting_balance += required - starting_balance

            starting_balance -= actual 
        
        return loan + start

                
