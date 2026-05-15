class Solution:
    def isValid(self, s: str) -> bool:
        closing_brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for c in s:
            if c in closing_brackets:
                if stack and stack[-1] == closing_brackets[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack