class Solution:
    def trap(self, heights: List[int]) -> int:
        max_L, max_R = 0, 0
        L, R = 0, len(heights)-1
        total = 0
        while L < R:
            if heights[L] <= heights[R]:
                max_L = max(max_L, heights[L])
                total += max_L - heights[L]
                L += 1
            else:
                max_R = max(max_R, heights[R])
                total += max_R - heights[R]
                R -= 1
        return total
