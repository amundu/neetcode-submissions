class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        max_L, max_R = 0, 0
        L, R = 0, len(height)-1

        while L <= R:
            if max_L < max_R:
                max_L = max(max_L, height[L])
                res += max(0, min(max_L, max_R) - height[L])
                L += 1
            else:
                max_R = max(max_R, height[R])
                res += max(0, min(max_L, max_R) - height[R])
                R -= 1
        return res