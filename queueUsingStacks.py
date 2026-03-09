class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.size = 0

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.size +=1
        
    def pop(self) -> int:
        for i in range(self.size):
            curr = self.stack1[-1]
            self.stack1.pop()
            self.stack2.append(curr)

        x = self.stack2[-1]
        self.stack2.pop()
        self.size -=1

        for i in range(self.size):
            curr = self.stack2[-1]
            self.stack2.pop()
            self.stack1.append(curr)
        return x

    def peek(self) -> int:

        print(self.stack1)
        for i in range(self.size):
            curr = self.stack1[-1]
            print(curr)
            self.stack1.pop()
            self.stack2.append(curr)

        x = self.stack2[-1]

        for i in range(self.size):
            curr = self.stack2[-1]
            self.stack2.pop()
            self.stack1.append(curr)

        return x

    def empty(self) -> bool:
        return self.size == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()