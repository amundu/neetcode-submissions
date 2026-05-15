class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)):
            h = heights[i]
            last_i = i
            while stack and h < stack[-1][1]: 
                s_i, s_h = stack.pop()
                last_i = s_i
                curr_area = (i - s_i) * s_h
                max_area = max(curr_area, max_area)
            
            stack.append((last_i, h))
        print(stack)
        while stack:
            s_i, s_h = stack.pop()
            curr_area = (len(heights) - s_i) * s_h
            max_area = max(curr_area, max_area)
        return max_area