class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        curr = []
        res = []
        def backtrack(left, right):
            if left == right == 0:
                res.append("".join(curr))
                return
            if left > 0:
                curr.append('(')
                backtrack(left-1, right)
                curr.pop()
            if right > left:
                curr.append(')')
                backtrack(left, right-1)
                curr.pop()
        backtrack(n, n)
        return res