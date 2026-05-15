class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        rows = [set() for _ in range(ROWS)]
        cols = [set() for _ in range(COLS)]
        grids = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                curr = board[r][c]
                if curr == '.':
                    continue
                grid = (r//3, c//3)
                if curr in rows[r] or curr in cols[c] or curr in grids[grid]:
                    return False
                cols[c].add(curr)
                rows[r].add(curr)
                grids[grid].add(curr)
        return True



