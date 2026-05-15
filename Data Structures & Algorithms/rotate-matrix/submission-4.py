class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        def print_matrix(m):
            for i in range(len(m)):
                print(m[i])

        for row in range(ROWS//2):
            left = row
            right = COLS-1-row
            top = left
            bottom = right
            for col in range(right-left):
                temp = matrix[top][left+col]
                matrix[top][left+col] = matrix[bottom-col][left]
                matrix[bottom-col][left] = matrix[bottom][right-col]
                matrix[bottom][right-col] = matrix[top+col][right]
                matrix[top+col][right] = temp
            print(top, bottom, left, right)
            print_matrix(matrix)
        
        print("")
        print_matrix([[4,33,13,32,12,2],[24,1,14,33,27,29],[1,20,32,32,9,20],[6,7,27,2,25,26],[32,21,22,28,13,16],[34,7,26,14,21,28]])
