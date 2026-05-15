class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        def can_eat(k, h):
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile/k)
            return total_hours <= h

        while low <= high:
            mid = ((high-low)//2)+low
            if can_eat(mid, h):
                high = mid - 1
            else:
                low = mid + 1

        return low