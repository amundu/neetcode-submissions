class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]
        cols = set()
        pos_diagonal = set()
        neg_diagonal = set()

        def dfs(r: int) -> None:
            if r == n:
                res.append(["".join(r) for r in board])
                return
            for c in range(n):
                if c in cols or (r+c) in pos_diagonal or (r-c) in neg_diagonal:
                    continue
                cols.add(c)
                pos_diagonal.add((r+c))
                neg_diagonal.add((r-c))
                board[r][c] = 'Q'

                dfs(r+1)

                cols.remove(c)
                pos_diagonal.remove((r+c))
                neg_diagonal.remove((r-c))
                board[r][c] = '.'
                
        dfs(0)
        return res