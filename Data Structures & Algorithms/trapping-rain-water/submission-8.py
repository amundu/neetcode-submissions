class Solution:
    def trap(self, heights: List[int]) -> int:
        max_L, max_R = heights[0], heights[-1]
        L, R = 0, len(heights)-1
        total = 0
        while L < R:
            if max_L <= max_R:
                while  L < R and heights[L] <= max_L:
                    total += max_L - heights[L]
                    L += 1
                if L < R:
                    max_L = heights[L]
            else:
                while  L < R and heights[R] <= max_R:
                    total += max_R - heights[R]
                    R -= 1
                if L < R:
                    max_R = heights[R]
        return total
