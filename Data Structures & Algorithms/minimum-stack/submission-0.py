class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimum_stack or val <= self.minimum_stack[-1]:
            self.minimum_stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.minimum_stack[-1]:
            self.minimum_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum_stack[-1]
