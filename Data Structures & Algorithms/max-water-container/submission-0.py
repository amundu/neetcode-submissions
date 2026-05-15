class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        r, l = 0, len(heights) - 1

        while r < l:
            r_h, l_h = heights[r], heights[l]
            min_h = min(r_h, l_h)
            max_area = max(max_area, min_h * (l - r))
            if r_h <= l_h:
                r += 1
            else:
                l -= 1 
        return max_area