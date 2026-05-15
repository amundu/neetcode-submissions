class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, rows*cols-1

        while l <= r:
            m = (l+r)//2
            m_r, m_c = m//cols, m%cols
            print(l, r, m, m_r, m_c)

            if matrix[m_r][m_c] > target:
                r = m - 1
            elif matrix[m_r][m_c] < target:
                l = m + 1
            else:
                return True
        return False

