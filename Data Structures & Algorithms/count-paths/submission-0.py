class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            res[i][0] = 1
        for i in range(n):
            res[0][i] = 1

        for row in range(1, m):
            for col in range(1, n):
                res[row][col] = res[row-1][col] + res[row][col-1]
        return res[-1][-1]
