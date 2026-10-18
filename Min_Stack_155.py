class MinStack:
    def __init__(self):
        self.stack = []
        self.lowest = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.lowest:
            self.lowest.append(value)
        elif self.lowest[-1] >= value:
            self.lowest.append(value)
        

    def pop(self) -> None:
        if not self.stack or not self.lowest:
            return None
        if self.stack[-1] == self.lowest[-1]:
            self.lowest.pop()
        self.stack.pop()
        

    def top(self) -> int:
        topElement = self.stack[-1] #python syntax accessing last item in a list
        return topElement
        

    def getMin(self) -> int:
        if not self.lowest:
            return None
        return self.lowest[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()