class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        chars = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c not in chars:
                stack.append(c)
                continue
            if not stack or stack[-1] != chars[c]:
                return False
            stack.pop()
        return not stack