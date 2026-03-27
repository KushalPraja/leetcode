class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        nums1 = list(num1[::-1])
        nums2 = list(num2[::-1])
        carry = 0
        i = 0
        final = []
        
        while carry or i < len(nums1) or i < len(nums2):
            val1 = 0
            val2 = 0
            if i >= len(nums1):
                val1 = 0
            else:
                val1 = int(nums1[i])

            if i >= len(nums2):
                val2 = 0
            else:
                val2 = int(nums2[i])

            final.append(str((val1 + val2 + carry) % 10)) 
            carry = (val1 + val2 + carry) // 10
            i += 1

        return "".join(final[::-1])
       