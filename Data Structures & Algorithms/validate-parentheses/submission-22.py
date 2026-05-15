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
            else:
                if stack and stack[-1] == closing_brackets[c]:
                    stack.pop()
                else:
                    return False
        return not stack
