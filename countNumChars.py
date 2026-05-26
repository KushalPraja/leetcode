class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        x = set([])

        word = set(list(word))

        count = 0
        for i in word:
            if i.lower() == i and i.upper() in x:
                count += 1

            elif i.upper() == i and i.lower() in x:
                count += 1

            else:
                x.add(i)

        return count