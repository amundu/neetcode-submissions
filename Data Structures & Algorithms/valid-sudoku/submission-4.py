class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set) # key = (r // 3, c // 3)

        n = len(board)
        for r in range(n):
            for c in range(n):
                digit = board[r][c]
                if digit == ".":
                    continue
                if digit in rows[r] or digit in cols[c] or digit in squares[(r//3, c//3)]:
                    return False

                rows[r].add(digit)
                cols[c].add(digit)
                squares[(r//3, c//3)].add(digit)
        
        return True

        
                

        