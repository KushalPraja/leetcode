class Solution:
    def getHint(self, secret: str, guess: str) -> str:
     
        bull = 0
        cow = 0
        mapping = {}
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bull += 1
            else:
                if guess[i] in mapping:
                    if mapping[guess[i]] > 0:
                        cow += 1
                    mapping[guess[i]] -= 1
                else:
                    mapping[guess[i]] = -1

                if secret[i] in mapping:
                    if mapping[secret[i]] < 0:
                        cow += 1
                    mapping[secret[i]] += 1
                else:
                    mapping[secret[i]] = 1 
                

        return str(bull) + "A" + str(cow) + "B"
