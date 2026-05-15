class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_bracket = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            if c in matching_bracket:
                if stack and stack[-1] == matching_bracket[c]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(c)
        return len(stack) == 0