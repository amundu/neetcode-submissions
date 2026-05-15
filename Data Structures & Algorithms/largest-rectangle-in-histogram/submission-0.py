class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # (height, index)

        for i, h in enumerate(heights):
            reduced_h = False
            while stack and stack[-1][0] > h:
                reduced_h = True
                prev_h, idx = stack.pop()
                max_area = max(max_area, prev_h * (i - idx))

            if reduced_h:
                stack.append((h, i-1))
            else:
                stack.append((h, i))
    
        while stack:
                prev_h, idx = stack.pop()
                max_area = max(max_area, prev_h * (len(heights) - idx))

        return max_area
        