class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            h = heights[i]
            last_i = i
            while stack and h < stack[-1][1]: 
                last_i, s_h = stack.pop()
                max_area = max((i - last_i) * s_h, max_area)
            stack.append((last_i, h))

        for i, h in stack:
            max_area = max((len(heights) - i) * h, max_area)
        return max_area