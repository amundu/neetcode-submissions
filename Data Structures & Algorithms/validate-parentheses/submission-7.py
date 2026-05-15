class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_bracket = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            if c not in matching_bracket:
                stack.append(c)
                continue
            if not stack or stack[-1] != matching_bracket[c]:
                return False
            stack.pop()
        return not stack