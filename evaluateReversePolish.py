from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack  = []

        for i in tokens:
            print(stack)
            if i in ["+","-","*","/"]:
                first_element = stack[-1]
                stack.pop()
                second_element  = stack[-1]
                stack.pop()

                if i == "+":
                    stack.append((first_element) + (second_element))
                
                if i == "*":
                    stack.append((first_element) * (second_element))
                
                if i == "/":
                    stack.append(int((second_element) / (first_element)))
                   
                if i == "-":
                    stack.append((second_element) - (first_element))
            else:
                stack.append(int(i))
            
        return int(stack[0])
