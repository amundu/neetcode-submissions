class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            n = c
            if c == '+':
                b, a = stack.pop(), stack.pop()
                stack.append(a + b)
            elif c == '-':
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif c == '*':
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)
            elif c == '/':
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(c))
        return stack[-1]