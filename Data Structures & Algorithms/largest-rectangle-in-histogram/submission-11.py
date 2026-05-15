class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        stack = []
        for i, height in enumerate(heights):
            prev_i = i
            while stack and stack[-1][0] >= height:
                prev_height, prev_i = stack.pop()
                max_area = max(max_area, (i - prev_i)*prev_height)
            stack.append((height, prev_i))
        while stack:
                height, i = stack.pop()
                max_area = max(max_area, (n - i)*height)
        return max_area

                