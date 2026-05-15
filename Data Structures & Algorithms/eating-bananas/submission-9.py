class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        def can_eat_bananas(k: int) -> bool:
            time = 0
            for bananas in piles:
                time += math.ceil(bananas/k)
                if time > h:
                    return False
            return True
        
        prev = high
        while low <= high:
            mid = low + (high-low)//2
            if can_eat_bananas(mid):
                high = mid - 1
                prev = mid
            else:
                low = mid + 1
        return prev

