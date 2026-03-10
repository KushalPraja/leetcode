from collections import deque

# implementing stacks using two queues. 1st one is the main one and the seconds is the helper queue.
class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        self.size = 0

    def push(self, x: int) -> None:
        self.queue1.append(x)
        self.size += 1

    def pop(self) -> int:
        for _ in range(self.size - 1):
            self.queue2.append(self.queue1.popleft())

        x = self.queue1.popleft()

        self.queue1, self.queue2 = self.queue2, self.queue1
        self.size -= 1

        return x

    def top(self) -> int:
        for _ in range(self.size - 1):
            self.queue2.append(self.queue1.popleft())

        x = self.queue1.popleft()
        self.queue2.append(x)

        self.queue1, self.queue2 = self.queue2, self.queue1

        return x

    def empty(self) -> bool:
        return self.size == 0