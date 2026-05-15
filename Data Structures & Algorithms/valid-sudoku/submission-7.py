class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_check = defaultdict(set)
        cols_check = defaultdict(set)
        squares_check = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    continue

                n = board[row][col]
                square = (row//3, col// 3)
                if (n in rows_check[row]
                or n in cols_check[col]
                or n in squares_check[square]):
                    return False

                rows_check[row].add(n)
                cols_check[col].add(n)
                squares_check[square].add(n)
        return True