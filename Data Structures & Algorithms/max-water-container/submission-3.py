class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0, len(heights)-1
        max_area = 0
        while l < r:
            l_h = heights[l]
            r_h = heights[r]
            curr_area = (r - l) * min(l_h, r_h)
            max_area = max(max_area, curr_area)
            if l_h < r_h:
                l += 1
            else:
                r -= 1
        return max_area
