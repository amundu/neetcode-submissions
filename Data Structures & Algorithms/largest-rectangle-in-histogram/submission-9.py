class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # i, n
        max_area = 0

        for i, height in enumerate(heights):
            last_idx = i
            while stack and stack[-1][1] > height:
                last_idx, s_h = stack.pop()
                max_area = max(max_area, (i-last_idx) * s_h)
            stack.append((last_idx, height))

        while stack:
            i, s_h = stack.pop()
            max_area = max(max_area, (len(heights)-i) * s_h)
        return max_area
