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
                if len(stack) == 0 or closing_brackets[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0
        