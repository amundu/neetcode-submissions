class Solution:
    def trap(self, heights: List[int]) -> int:
        L, R = 0, len(heights)-1
        max_left, max_right = heights[0], heights[-1]
        total = 0

        while L < R:
            if max_left < max_right:
                L += 1
                max_left = max(max_left, heights[L])
                total += max_left - heights[L]
            else:
                R -= 1
                max_right = max(max_right, heights[R])
                total += max_right - heights[R]
        return total