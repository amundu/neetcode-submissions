class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, height in enumerate(heights):
            prev_i = i
            while stack and stack[-1][0] >= height:
                prev_height, prev_i = stack.pop()
                max_area = max(max_area, (i - prev_i)*prev_height)
            stack.append((height, prev_i))
        for h, i in stack:
                max_area = max(max_area, (len(heights) - i)*h)
        return max_area

                