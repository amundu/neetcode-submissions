class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        lowest = high
        while low <= high:
            mid = low + (high-low)//2
            hours = sum([math.ceil(bananas / mid) for bananas in piles])
            if hours > h:
                low = mid + 1
            elif hours <= h:
                lowest = mid
                high = mid -1
        return lowest

            
            