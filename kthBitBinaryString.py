class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        

        def dfs(n):
            if n == 1:
                return "0"

            else:
                prev  = dfs(n - 1)
                temp = ""

                for i in prev:
                    if i == "1":
                        temp += "0"
                    else:
                        temp += "1"           
                return prev + "1" + "".join(reversed(temp))

        x = dfs(n + 1)
        return x[k-1]
        

            