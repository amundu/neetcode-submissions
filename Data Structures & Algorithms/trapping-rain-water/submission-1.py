class Solution:
    def trap(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height)-1
        max_l_idx, max_r_idx = l, r

        i = l
        while l < r:
            if height[max_l_idx] < height[l]:
                max_l_idx = l
            if height[max_r_idx] < height[r]:
                max_r_idx = r
            if height[max_l_idx] < height[max_r_idx]:
                max_area += height[max_l_idx] - height[l]
                l += 1
            else:
                max_area += height[max_r_idx] - height[r]
                r -= 1
        return max_area

