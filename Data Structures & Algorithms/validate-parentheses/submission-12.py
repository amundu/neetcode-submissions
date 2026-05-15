class Solution:
    def isValid(self, s: str) -> bool:
        closing_chars_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for c in s:
            if c not in closing_chars_map:
                stack.append(c)
                continue
            if not stack or stack[-1] != closing_chars_map[c]:
                return False
            stack.pop()
        return not stack