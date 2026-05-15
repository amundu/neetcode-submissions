class Solution:
    def trap(self, height: List[int]) -> int:
        max_L, max_R = 0, 0
        L, R = 0, len(height)-1
        trapped_water = 0
        while L < R:
            if height[L] <= height[R]:
                max_L = max(max_L, height[L])
                trapped_water += max_L - height[L]
                L += 1
            else:
                max_R = max(max_R, height[R])
                trapped_water += max_R - height[R]
                R -= 1
        return trapped_water