class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def addParenthesis(s: str, o: int, c: int) -> None:
            if o == c == n:
                res.append(s)
                return

            if o < n:
                addParenthesis(s+"(", o+1, c)
            if c < o:
                addParenthesis(s+")", o , c+1)
        addParenthesis("", 0, 0)
        return res

        