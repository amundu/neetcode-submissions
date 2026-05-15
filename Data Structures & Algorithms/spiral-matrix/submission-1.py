class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, COLS
        top, bottom = 0, ROWS
        output = []
        while l < r and top < bottom:
            for i in range(l, r):
                output.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                output.append(matrix[i][r-1])
            r -= 1
            if not(l < r and top < bottom):
                break
            for i in range(r-1, l-1, -1):
                output.append(matrix[bottom-1][i])
            bottom -= 1
            for i in range(bottom-1, top-1, -1):
                output.append(matrix[i][l])
            l += 1
        return output
            