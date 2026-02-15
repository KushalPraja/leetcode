
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        carry = 0

        a_list = [int(i) for i in a]
        b_list= [int(i) for i in b]
        output = []

        while a_list or b_list or carry:
            digit_a = a_list.pop() if a else 0
            digit_b = b_list.pop() if b else 0

            new_digit = (digit_a + digit_b + carry) % 2
            carry = (digit_a + digit_b + carry) // 2
            output.insert(0, new_digit)

        return "".join([str(i) for i in output])
