class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_L, max_R = [0] * n, [0] * n

        for i in range(n):
            max_L[i] = height[0] if i == 0 else max(max_L[i-1], height[i])
            max_R[n-1-i] = height[n-1] if i == 0 else max(max_R[n-i], height[n-1-i])
        
        res = 0

        for i, h in enumerate(height):
            res += max(min(max_L[i], max_R[i]) - h, 0)
        return res