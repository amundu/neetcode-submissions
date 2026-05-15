class Solution:
    def trap(self, height: List[int]) -> int:
        L_max, R_max = 0, 0
        L, R = 0, len(height)-1
        trapped_water = 0
        while L <= R:
            if L_max < R_max:
                L_max = max(L_max, height[L])
                trapped_water += L_max - height[L]
                L += 1
            else:
                R_max = max(R_max, height[R])
                trapped_water += R_max - height[R]
                R -= 1
        return trapped_water