class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0 
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        for i in range(1, len(height)):
            left_max[i] = max(height[i-1], left_max[i-1])
        
        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(height[i+1], right_max[i+1])
        
        for i in range(len(height)):
            trapped_water = min(left_max[i], right_max[i]) - height[i]
            total += trapped_water if trapped_water > 0 else 0
                
        return total