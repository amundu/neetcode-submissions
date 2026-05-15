class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                res[row][col] = res[row-1][col] + res[row][col-1]
        return res[-1][-1]
