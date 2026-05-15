class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def add_parenthesis(op: int, cp: int) -> None:
            if op == n and op == cp:
                res.append("".join(stack))
                return
            
            if op < n:
                stack.append('(')
                add_parenthesis(op+1, cp)
                stack.pop()
            if cp < op:
                stack.append(')')
                add_parenthesis(op, cp+1)
                stack.pop()

        add_parenthesis(0, 0)
        return res