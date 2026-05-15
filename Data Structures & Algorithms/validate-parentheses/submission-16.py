class Solution:
    def isValid(self, s: str) -> bool:
        closing_brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for c in s:
            if c not in closing_brackets:
                stack.append(c)
                continue
            if not stack or stack[-1] != closing_brackets[c]:
                return False
            stack.pop()
        return not stack