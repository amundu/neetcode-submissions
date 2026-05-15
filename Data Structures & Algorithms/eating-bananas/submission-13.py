class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        min_k = 1

        def can_eat_piles(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours <= h

        while min_k < max_k:
            mid_k = (min_k + max_k) // 2
            if can_eat_piles(mid_k):
                max_k = mid_k
            else:
                min_k = mid_k + 1
        return max_k