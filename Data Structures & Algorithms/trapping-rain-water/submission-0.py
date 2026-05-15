class Solution:
    def trap(self, height: List[int]) -> int:
        total_area = 0
        max_l, max_r = height[0], height[-1]
        l, r = 0, len(height) - 1

        while l < r:
            if max_l < max_r:
                l += 1
                total_area += max(max_l - height[l], 0)
                max_l = max(max_l, height[l])
            else:
                r -= 1
                total_area += max(max_r - height[r], 0)
                max_r = max(max_r, height[r])

        return total_area
                
        