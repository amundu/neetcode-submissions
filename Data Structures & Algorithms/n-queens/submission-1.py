class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols_set = set()
        diag_up_set = set()
        diag_down_set = set()
        path = []
        output = []

        def block(row, col):
            cols_set.add(col)
            diag_up_set.add(row+col)
            diag_down_set.add(row-col)
        
        def unblock(row, col):
            cols_set.remove(col)
            diag_up_set.remove(row+col)
            diag_down_set.remove(row-col)

        def backtrack(row):
            if row == n:
                output.append(path[:])
                return
            
            for col in range(n):
                if (col in cols_set
                or row-col in diag_down_set
                or row+col in diag_up_set):
                    continue
                curr = ['.']*n
                curr[col] = 'Q'
                path.append("".join(curr))
                block(row, col)
                backtrack(row + 1)
                unblock(row, col)
                path.pop()

        backtrack(0)
        return output