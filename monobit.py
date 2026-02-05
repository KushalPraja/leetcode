

class Solution:
    def countMonobit(self, n: int) -> int:
        
        monobits = 0
        
        def isMonobit(i):
            binary = bin(i)
            binary = binary[::-1]
            zeros = 0
            ones = 0
            for i in binary:
                if i == "0":
                    zeros+=1;
                if i== "1":
                    ones +=1;
                if i == "b":
                    break

            return zeros == 0 or ones == 0


        for i in range(0, n + 1):
            if isMonobit(i):
                monobits+=1

        return monobits

print(Solution().countMonobit(4))
