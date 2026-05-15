class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        chars = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = deque()
        for c in s:
            if c not in chars:
                stack.append(c)
            else:
                if stack and stack[-1] == chars[c]:
                    stack.pop()
                else:
                    return False
        return not stack
