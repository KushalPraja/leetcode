class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        indices = {} # last index of lowercase char in word
        seen = set([]) # if u have seen the uppercase before no dups
        count = 0

        # find the last index of each lowercase char in word
        for i in range(len(word)):
            if word[i].lower() == word[i]:
                indices[word[i]] = i


        # loop 
        for curr in range(len(word)):
            i = word[curr]

            # if u have seen the uppercase before no dups
            if i in seen:
                continue

            # add new uppercase char to seen
            if i == i.upper():
                seen.add(i.upper())

            # if u have seen the uppercase before no dups
            if i == i.upper() and i.lower() in indices and indices[i.lower()] < curr:
                count += 1

        return count

#time complexity: O(2n) where n is the length of word

        

