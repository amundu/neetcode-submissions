class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # colum check
        for col in range(len(board[0])):
            prev_nums = set()
            for row in range(len(board)):
                n = board[row][col]
                if n != '.' and n in prev_nums:
                    return False
                prev_nums.add(n)
        # row check
        for row in range(len(board)):
            prev_nums = set()
            for n in board[row]:
                if n  != '.' and n in prev_nums:
                    return False
                prev_nums.add(n)
        # squares check
        nums_quadrant = defaultdict(set) # (qrow,qcol): set()
        # For every elevent in matrix
        for row in range(len(board)):
            for col in range(len(board[0])):
                # check in which quadrant is located using the row and col
                n = board[row][col]
                if n == '.':
                    continue
                q_row, q_col = row // 3, col // 3
                if n in nums_quadrant[(q_row, q_col)]:
                    return False
                nums_quadrant[(q_row, q_col)].add(n)
        return True
                