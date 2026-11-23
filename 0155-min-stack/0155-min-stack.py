class MinStack:

    def __init__(self):
        self.min_list= []
        self.list = []
        
    def push(self, value: int) -> None:
        self.list.append(value)
        if self.min_list:
            self.min_list.append(min(self.min_list[-1], value))
        else:
            self.min_list.append(value)

    def pop(self) -> None:
        self.list.pop()
        self.min_list.pop()
        
    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return self.min_list[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()