class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0 
        l ,r = 0 , len(height)-1
        max_left, max_right = height[l], height[r]
        while l < r:
            trapped_water = 0
            if max_left < max_right:
                l += 1
                trapped_water = max_left - height[l]
                max_left = max(max_left, height[l])
            else:
                r -= 1
                trapped_water = max_right - height[r]
                max_right = max(max_right, height[r])
            total += trapped_water if trapped_water > 0 else 0
                
        return total