class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.insert(0, val)
        if self.min == []:
            self.min.insert(0, val)
        else:
            self.min.insert(0, val if val < self.min[0] else self.min[0])

    def pop(self) -> None:
        self.stack = self.stack[1:]
        self.min = self.min[1:]

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.min[0]
