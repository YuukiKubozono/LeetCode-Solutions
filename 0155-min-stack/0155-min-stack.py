class MinStack:

    def __init__(self):
        self.d = {}
        self.list = []
        self.id = 0
        self.min = float("inf")
    def push(self, value: int) -> None:
        if value <= self.min:
            self.min = value
            self.d[self.id] = value
            self.id += 1
        self.list.append(value)

    def pop(self) -> None:
        if self.list[-1] == self.min:
            self.id -= 1
            del self.d[self.id]
            if self.id > 0:
                self.min = self.d[self.id - 1]
            else:
                self.min = float("inf")
        self.list.pop()

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()