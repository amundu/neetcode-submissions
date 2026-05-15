class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        chars = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in chars:
                if stack and stack[-1] == chars[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack