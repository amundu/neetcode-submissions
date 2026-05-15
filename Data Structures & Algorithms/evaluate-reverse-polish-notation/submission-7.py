class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                x, y = int(stack.pop()), int(stack.pop())
                stack.append(x+y)
            elif token == '-':
                x, y = int(stack.pop()), int(stack.pop())
                stack.append(y-x)
            elif token == '*':
                x, y = int(stack.pop()), int(stack.pop())
                stack.append(y*x)
            elif token == '/':
                x, y = int(stack.pop()), int(stack.pop())
                stack.append(int(y/x))
            else:
                stack.append(token)
        return int(stack.pop())