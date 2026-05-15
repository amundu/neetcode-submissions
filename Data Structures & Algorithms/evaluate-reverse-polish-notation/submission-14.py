class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                x, y = stack.pop(), stack.pop()
                stack.append(x+y)
            elif token == '-':
                y, x = stack.pop(), stack.pop()
                stack.append(x-y)
            elif token == '*':
                x, y = stack.pop(), stack.pop()
                stack.append(x*y)
            elif token == '/':
                y, x = stack.pop(), stack.pop()
                stack.append(int(x/y))
            else:
                stack.append(int(token))
        return stack.pop()