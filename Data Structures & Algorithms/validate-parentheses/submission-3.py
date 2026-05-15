class Solution:
    def isValid(self, s: str) -> bool:
        closing_brackets = { 
            ')' : '(', 
            '}' : '{', 
            ']' : '['
        }

        stack = []

        for c in s:
            if c in closing_brackets:
                if not stack or closing_brackets[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        
        return not stack
        