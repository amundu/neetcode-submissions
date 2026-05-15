class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # (height, index)

        for i, h in enumerate(heights):
            start_i = i
            while stack and stack[-1][0] > h:
                prev_h, idx = stack.pop()
                max_area = max(max_area, prev_h * (i - idx))
                start_i = idx

            stack.append((h, start_i))
    
        while stack:
                prev_h, idx = stack.pop()
                max_area = max(max_area, prev_h * (len(heights) - idx))

        return max_area
        