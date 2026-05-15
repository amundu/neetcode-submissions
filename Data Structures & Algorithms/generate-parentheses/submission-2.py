class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def backtracking(stack: List[int], o: int, c: int) -> None:
            if o == c == n:
                output.append(''.join(stack))
                return
            if o < n:
                stack.append('(')
                backtracking(stack, o + 1, c)
                stack.pop()
            if o > c:
                stack.append(')')
                backtracking(stack, o, c + 1)
                stack.pop()
            

        backtracking([], 0, 0)
        return output