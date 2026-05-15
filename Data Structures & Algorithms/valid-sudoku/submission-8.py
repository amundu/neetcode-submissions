class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in rows[i] and board[i][j] not in cols[j] and board[i][j] not in squares[(i//3, j//3)]:
                    rows[i].add(board[i][j])
                    squares[(i//3, j//3)].add(board[i][j])
                    cols[j].add(board[i][j])
                else:
                    return False
        return True