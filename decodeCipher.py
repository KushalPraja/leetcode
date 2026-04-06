class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        
        curr = [[0] * (len(encodedText)//rows) for _ in range(rows)]

        for i in range(rows):
            for j in range(len(encodedText)//rows):
                curr[i][j] = encodedText[i*(len(encodedText)//rows) + j]

        curr_y = 0
        stri = ""
        while curr_y < len(encodedText)//rows:
            prev = curr_y
            for curr_x in range(rows):
                if curr_y < len(encodedText)//rows:
                    stri += curr[curr_x][curr_y]
                curr_y += 1
            curr_y = prev + 1

        return stri.rstrip()