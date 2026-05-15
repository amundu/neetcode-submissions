class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_value = min(self.min_value_stack[-1], val) if self.min_value_stack else val
        self.min_value_stack.append(min_value)

    def pop(self) -> None:
        self.stack.pop()
        self.min_value_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value_stack[-1]
