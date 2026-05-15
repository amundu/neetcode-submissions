class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        lowest = high

        def can_eat_bananas(k: int) -> bool:
            return sum([math.ceil(bananas / mid) for bananas in piles]) <= h

        while low <= high:
            mid = low + (high-low)//2
            if can_eat_bananas(mid):
                lowest = mid
                high = mid -1
            else:
                low = mid + 1
        return lowest

            
            