class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.insert(0, val)

    def pop(self) -> None:
        self.stack = self.stack[1:]

    def top(self) -> int:
        val = self.stack[0]
        return val

    def getMin(self) -> int:
        if self.stack == []:
            return None
        return min(self.stack)
